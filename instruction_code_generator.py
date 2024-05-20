# instruction_code_generator.py

import config  # Importar la configuración

def extract_data_values_hex(data_values):
    return ' '.join(f'{value:02X}' for value in data_values.values())

def generate_instruction_code(text_instructions, instruction_codes):
    """
    Genera los códigos de instrucción a partir de las instrucciones de texto.

    Args:
        text_instructions (list): Lista de instrucciones de texto con sus contadores.
        instruction_codes (dict): Diccionario de códigos de instrucción.

    Returns:
        list: Lista de tuplas con códigos de instrucción en binario y hexadecimal.
    """
    instruction_code_list = []
    for instruction_counter, instruction_line in text_instructions:
        parts = instruction_line.split()
        instruction = parts[0]
        operand = parts[1].strip('[]') if len(parts) > 1 else None

        if instruction == "HLT":
            instruction = "JMP"
            operand = instruction_counter  # Pseudo instrucción HLT usa JMP a sí mismo

        instruction_code = instruction_codes[instruction] << 5
        if operand is not None:
            if str(operand).isdigit():
                instruction_code |= int(operand)
            else:
                instruction_code |= int(operand)

        instruction_code_bin = f'{instruction_code:08b}'
        instruction_code_hex = f'{instruction_code:02X}'
        instruction_code_list.append((instruction_code_bin, instruction_code_hex))

    return instruction_code_list
