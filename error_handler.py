# error_handler.py

import config  # Importar la configuración

def check_for_errors(label_addresses, text_instructions, instruction_codes):
    """
    Verifica la existencia de errores en el código ensamblador.

    Args:
        label_addresses (dict): Diccionario de direcciones de etiquetas.
        text_instructions (list): Lista de instrucciones de texto con sus contadores.
        instruction_codes (dict): Diccionario de códigos de instrucción.

    Returns:
        list: Lista de errores encontrados.
    """
    errors = []

    for instruction_counter, line in text_instructions:
        parts = line.split()
        instruction = parts[0]

        if instruction not in instruction_codes:
            errors.append(f"Error: Instrucción desconocida '{instruction}' en la línea {instruction_counter + 1}.")
            continue

        if instruction == "HLT":
            if len(parts) > 1:
                errors.append(f"Error: La instrucción 'HLT' no debe tener operandos en la línea {instruction_counter + 1}.")
            continue

        if len(parts) == 1:
            errors.append(f"Error: Instrucción '{instruction}' en la línea {instruction_counter + 1} requiere un operando.")
            continue

        operand = parts[1]

        if instruction in ['ADD', 'SUB', 'LDA', 'STA']:
            if operand.startswith('[') and operand.endswith(']'):
                operand = operand[1:-1]  # Eliminar corchetes
            else:
                errors.append(f"Error: Operando '{operand}' para la instrucción '{instruction}' debe estar entre corchetes en la línea {instruction_counter + 1}.")
                continue

        if not operand.isdigit() and operand not in label_addresses:
            errors.append(f"Error: Operando desconocido '{operand}' en la línea {instruction_counter + 1}.")

    return errors
