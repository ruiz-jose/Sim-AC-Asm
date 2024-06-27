import sys
import os.path
import re
from colorama import Fore, Style
import config
from file_reader import read_file
from instruction_processor import read_and_split_sections, process_line, handle_data_section, handle_text_section, replace_operands
from error_handler import check_for_errors
from instruction_code_generator import generate_instruction_code, extract_data_values_hex
from hex_file_generator import generate_hex_files  # Agregamos esta línea
import glob

def main():
    # Obtener el nombre del archivo desde los argumentos de la línea de comandos
    filename = sys.argv[1]
    process_file(filename)
    # Verificar si el archivo existe en el directorio actual
    if not os.path.isfile(filename):
        # Construir la ruta del archivo dentro de la carpeta 'examples'
        filename = os.path.join('examples', filename)
        process_file(filename)
        # Verificar si el archivo existe en la carpeta 'examples'
        if not os.path.isfile(filename):
            print(f"Error: El archivo '{filename}' no existe.")
            sys.exit(1)
        
        



def process_file(file_path):
    lines = read_file(file_path)
    
    if len(sys.argv) != 2:
        print("Uso: python main.py archivo.ac")
        sys.exit(1)

    file_path = sys.argv[1]

    if not file_path.endswith('.ac'):
        print("Error: El archivo debe tener la extensión .ac")
        sys.exit(1)

    lines = read_file(file_path)

    data, text, text_instructions, data_values, label_addresses = read_and_split_sections(lines)

    # Verificar errores
    errors = check_for_errors(label_addresses, text_instructions, config.INSTRUCTION_CODES)
    if errors:
        for error in errors:
            print(error)
        sys.exit(1)

    # Mostrar valores de la sección .DATA
    max_data_label_length = max(len(label) for label, _ in data) if data else 0
    print("Valores de la sección .DATA:")
    for index, (label, value) in enumerate(data):
        print(f"{label.ljust(max_data_label_length)} | {index}: {value}")

    # Mostrar instrucciones de la sección .TEXT
    max_text_label_length = max(len(label) for label in label_addresses.keys()) if label_addresses else 0
    print("\nInstrucciones de la sección .TEXT:")
    for instruction_counter, instruction in text_instructions:
        label = next((lbl for lbl, addr in label_addresses.items() if addr == instruction_counter), "")
        print(f"{label.ljust(max_text_label_length)} | {instruction_counter}: {instruction}")

    if label_addresses:
        print("\nDirecciones de etiquetas:")
        for label, address in label_addresses.items():
            print(f"{label}: {address}")

    # Mostrar valores de la sección .DATA en hexadecimal
    hex_values = extract_data_values_hex(data_values)
    print("\nValores de la sección .DATA en hexadecimal:")
    print(hex_values)

    # Generar y mostrar códigos de instrucción
    instruction_code_list = generate_instruction_code(text_instructions, config.INSTRUCTION_CODES)
    print("\nValores de la sección .TEXT en binario(Códigos de instrucción y operando) y hexadecimal:")
    for instruction_code_bin, instruction_code_hex in instruction_code_list:
        colored_bits = Fore.BLUE + instruction_code_bin[:3] + Style.RESET_ALL + instruction_code_bin[3:]
        print(f"Binario: {colored_bits} | Hexadecimal: {instruction_code_hex}")

    # Generar archivos en hexadecimal
    generate_hex_files(file_path, list(data_values.values()), instruction_code_list)

if __name__ == "__main__":
    main()
