import re
from colorama import Fore, Style

# Definir los códigos de instrucción
instruction_codes = {
    "ADD": 0,
    "SUB": 1,
    "LDA": 2,
    "STA": 3,
    "JMP": 4,
    "JZ": 5,
    "JC": 6,
    "HLT": 7,
    "LDI": 8
}

def read_file(file_path):
    """Lee el archivo y devuelve las líneas"""
    with open(file_path, 'r') as file:
        return file.readlines()

def process_line(line):
    """Elimina espacios en blanco y comentarios de la línea"""
    line = line.strip()
    line = re.sub(r';.*', '', line)
    return line if line else None

def handle_data_section(line, section_data, data_values):
    """Procesa una línea de la sección de datos"""
    match = re.match(r'^([a-zA-Z]\w*)(?::)?\s+DB\s+(\d+)\s*$', line)
    if match:
        identifier = match.group(1)
        value = int(match.group(2))
        data_values[identifier] = value
        section_data.append((identifier, value))

def handle_text_section(line, section_text, instruction_counter, label_addresses, text_instructions):
    """Procesa una línea de la sección de texto"""
    match_label = re.match(r'^([a-zA-Z]\w*):', line)
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
                for index, (identifier, value) in enumerate(section_data):
                    if operand == identifier:
                        instruction_parts[1] = f'[{index}]'
                        text_instructions[i] = (instruction_counter, ' '.join(instruction_parts))
                        break
    return text_instructions

def read_and_split_sections(file_path):
    lines = read_file(file_path)
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
        if re.match(r'^SECTION\s*\.DATA\s*$', line, re.IGNORECASE):
            current_section = section_data
            continue
        elif re.match(r'^SECTION\s*\.TEXT\s*$', line, re.IGNORECASE):
            current_section = section_text
            continue

        if current_section is section_data:
            handle_data_section(line, section_data, data_values)
        elif current_section is section_text:
            instruction_counter = handle_text_section(line, section_text, instruction_counter, label_addresses, text_instructions)

    text_instructions = replace_operands(text_instructions, label_addresses, section_data)
    return section_data, section_text, text_instructions, data_values, label_addresses

def extract_data_values(data_values):
    return [value for key, value in data_values.items()]

def extract_data_values_hex(data_values):
    return ' '.join(f'{value:02X}' for value in data_values.values())

def generate_instruction_code(text_instructions, instruction_codes):
    instruction_code_list = []
    for instruction_counter, instruction_line in text_instructions:
        parts = instruction_line.split()
        instruction = parts[0]
        operand = parts[1].strip('[]')
        instruction_code = instruction_codes[instruction] << 5
        if operand.isdigit():
            instruction_code |= int(operand)
        instruction_code_bin = f'{instruction_code:08b}'
        instruction_code_hex = f'{instruction_code:02X}'
        instruction_code_list.append((instruction_code_bin, instruction_code_hex))
    return instruction_code_list

# Ejemplo de uso
data, text, text_instructions, data_values, label_addresses = read_and_split_sections('lda.ac')

# Calcular la longitud de la etiqueta más larga en la sección .DATA
max_data_label_length = max(len(label) for label, _ in data) if data else 0

print("Valores de la sección .DATA:")
for index, (label, value) in enumerate(data):
    print(f"{label.ljust(max_data_label_length)} | {index}: {value}")

# Calcular la longitud de la etiqueta más larga en la sección .TEXT
max_text_label_length = max(len(label) for label in label_addresses.keys()) if label_addresses else 0

print("\nInstrucciones de la sección .TEXT:")
for instruction_counter, instruction in text_instructions:
    # Buscar si hay alguna etiqueta para esta instrucción
    label = next((lbl for lbl, addr in label_addresses.items() if addr == instruction_counter), "")
    # Imprimir con formato ajustado
    print(f"{label.ljust(max_text_label_length)} | {instruction_counter}: {instruction}")

if label_addresses:
    print("\nDirecciones de etiquetas:")
    for label, address in label_addresses.items():
        print(f"{label}: {address}")

# Mostrar valores en hexadecimal
print("\nValores de la sección .DATA en hexadecimal:")
hex_values = extract_data_values_hex(data_values)
print(hex_values)

# Generar y mostrar códigos de instrucción
instruction_code_list = generate_instruction_code(text_instructions, instruction_codes)
print("\nCódigos de instrucción:")
for instruction_code_bin, instruction_code_hex in instruction_code_list:
    colored_bits = Fore.BLUE + instruction_code_bin[:3] + Style.RESET_ALL + instruction_code_bin[3:]
    print(f"Binario: {colored_bits} | Hexadecimal: {instruction_code_hex}")

