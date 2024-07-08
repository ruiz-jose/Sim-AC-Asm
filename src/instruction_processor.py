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

def replace_operands_harvard(text_instructions_harvad, label_addresses, section_data):
    """Reemplaza los operandos de las instrucciones con los valores correctos para Harvard"""
   
    for i, (instruction_counter, line) in enumerate(text_instructions_harvad):
        instruction_parts = line.strip().split()
        # Implementación específica para Harvard
        if len(instruction_parts) > 1:
            instruction = instruction_parts[0]
            operand = instruction_parts[1]
            # Para instrucciones de salto, se reemplaza el operando por la dirección de la etiqueta
            if instruction in ['JMP', 'JZ', 'JC'] and operand in label_addresses:
                label_address = label_addresses[operand]
                instruction_parts[1] = str(label_address)
            # Para instrucciones de operación, se reemplaza el operando por su posición en la memoria de datos
            elif instruction in ['ADD', 'SUB', 'LDA', 'STA']:
                for index, (identifier, value) in enumerate(section_data):
                    if operand.strip('[]') == identifier:
                        # La dirección de memoria se calcula como el índice en la memoria de datos
                        instruction_parts[1] = f'[{index}]'
                        break
            text_instructions_harvad[i] = (instruction_counter, ' '.join(instruction_parts))
    return text_instructions_harvad

def replace_operands_neumann(text_instructions_neumann, label_addresses, section_data):
    """Reemplaza los operandos de las instrucciones con los valores correctos para Neumann, ajustando por el tamaño de la sección .text"""
    size_of_text_section = len(text_instructions_neumann)  # Cálculo del tamaño de la sección .text
   
    for i, (instruction_counter, line) in enumerate(text_instructions_neumann):
        instruction_parts = line.strip().split()
        if len(instruction_parts) > 1:
            instruction = instruction_parts[0]
            operand = instruction_parts[1]
            # Para instrucciones de salto, se reemplaza el operando por la dirección de la etiqueta
            if instruction in ['JMP', 'JZ', 'JC'] and operand in label_addresses:
                label_address = label_addresses[operand]
                instruction_parts[1] = str(label_address)
            # Para instrucciones de operación, se ajusta el operando por el tamaño de la sección .text
            elif instruction in ['ADD', 'SUB', 'LDA', 'STA']:
                for index, (identifier, value) in enumerate(section_data):
                    if operand.strip('[]') == identifier:
                        # La dirección de memoria ajustada se calcula como el tamaño de la sección .text más el índice
                        adjusted_memory_address = size_of_text_section + index
                        instruction_parts[1] = f'[{adjusted_memory_address}]'
                        break
            text_instructions_neumann[i] = (instruction_counter, ' '.join(instruction_parts))
    return text_instructions_neumann

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

    text_instructions_neumann = text_instructions.copy()
    text_instructions_harvard = replace_operands_harvard(text_instructions, label_addresses, section_data)
    text_instructions_neumann = replace_operands_neumann( text_instructions_neumann, label_addresses, section_data)

   
    return section_data, section_text, text_instructions_harvard, text_instructions_neumann, data_values, label_addresses
