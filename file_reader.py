# file_reader.py

import sys

def read_file(file_path):
    """Lee el archivo y devuelve las líneas"""
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no existe.")
        sys.exit(1)
