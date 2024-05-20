import sys
import os.path
import re
from colorama import Fore, Style
import config
from file_reader import read_file
from instruction_processor import read_and_split_sections, process_line, handle_data_section, handle_text_section, replace_operands
from error_handler import check_for_errors
from instruction_code_generator import generate_instruction_code, extract_data_values_hex  # Corregimos el módulo

def validate_file_extension(file_path):
    """Valida que la extensión del archivo sea '.ac'"""
    _, file_extension = os.path.splitext(file_path)
    if file_extension != '.ac':
        print("Error: El archivo debe tener la extensión '.ac'.")
        sys.exit(1)

def main(file_path):
    validate_file_extension(file_path)
    lines = read_file(file_path)
    section_data, section_text, text_instructions, data_values, label_addresses = read_and_split_sections(lines)
    
    errors = check_for_errors(label_addresses, text_instructions, config.INSTRUCTION_CODES)
    if errors:
        for error in errors:
            print(error)
        return

    # Calcular la longitud de la etiqueta más larga en la sección .DATA
    max_data_label_length = max(len(label) for label, _ in section_data) if section_data else 0

    print("Valores de la sección .DATA:")
    for index, (label, value) in enumerate(section_data):
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
    instruction_code_list = generate_instruction_code(text_instructions, config.INSTRUCTION_CODES)
    print("\nCódigos de instrucción:")
    for instruction_code_bin, instruction_code_hex in instruction_code_list:
        colored_bits = Fore.BLUE + instruction_code_bin[:3] + Style.RESET_ALL + instruction_code_bin[3:]
        print(f"Binario: {colored_bits} | Hexadecimal: {instruction_code_hex}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python main.py archivo.ac")
        sys.exit(1)
    main(sys.argv[1])
