# instruction_processor.py

import re
import config  # Importar la configuración

def process_line(line):
    """Elimina espacios en blanco y comentarios de la línea"""
    line = line.strip()
    line = re.sub(r';.*', '', line)
    return line if line else None

def handle_data_section(line, section_data, data_values):
    """Procesa una línea de la sección de datos"""
    match = re.match(config.DATA_ENTRY_PATTERN, line)
    if match:
        identifier = match.group(1)
        value = int(match.group(2))
        data_values[identifier] = value
        section_data.append((identifier, value))  # Asegúrate de agregar la tupla a section_data

def handle_text_section(line, section_text, instruction_counter, label_addresses, text_instructions):
    """Procesa una línea de la sección de texto"""
    match_label = re.match(config.LABEL_PATTERN, line)
    if match_label:
        label_name = match_label.group(1)
        label_addresses[label_name] = instruction_counter
    else:
        text_instructions.append((instruction_counter, line.strip()))
        instruction_counter += 1
        section_text.append(line)
    return instruction_counter

def replace_operands(text_instructions, label_addresses, section_data):
    """Reemplaza los operandos de las instrucciones con los valores correctos"""
    for i, (instruction_counter, line) in enumerate(text_instructions):
        instruction_parts = line.strip().split()
        if len(instruction_parts) > 1:
            if instruction_parts[0] in ['JMP', 'JZ', 'JC'] and instruction_parts[1] in label_addresses:
                label_address = label_addresses[instruction_parts[1]]
                instruction_parts[1] = str(label_address)
                text_instructions[i] = (instruction_counter, ' '.join(instruction_parts))
            elif instruction_parts[0] in ['ADD', 'SUB', 'LDA', 'STA']:
                operand = instruction_parts[1].strip('[]')
                for index, (identifier, value) in enumerate(section_data):  # Verifica la iteración sobre section_data
                    if operand == identifier:
                        instruction_parts[1] = f'[{index}]'
                        text_instructions[i] = (instruction_counter, ' '.join(instruction_parts))
                        break
    return text_instructions


def read_and_split_sections(lines):
    section_data = []
    section_text = []
    data_values = {}
    instruction_counter = 0
    text_instructions = []
    label_addresses = {}
    current_section = None

    for line in lines:
        line = process_line(line)
        if not line:
            continue
        if re.match(config.DATA_SECTION_PATTERN, line, re.IGNORECASE):
            current_section = section_data
            continue
        elif re.match(config.TEXT_SECTION_PATTERN, line, re.IGNORECASE):
            current_section = section_text
            continue

        if current_section is section_data:
            handle_data_section(line, section_data, data_values)
        elif current_section is section_text:
            instruction_counter = handle_text_section(line, section_text, instruction_counter, label_addresses, text_instructions)

    text_instructions = replace_operands(text_instructions, label_addresses, section_data)
    return section_data, section_text, text_instructions, data_values, label_addresses
