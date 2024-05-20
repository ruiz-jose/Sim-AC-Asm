# file_reader.py

def read_file(file_path):
    """
    Lee el archivo y devuelve las líneas.

    Args:
        file_path (str): La ruta al archivo de código ensamblador.

    Returns:
        list: Una lista de líneas del archivo.
    """
    with open(file_path, 'r') as file:
        return file.readlines()
