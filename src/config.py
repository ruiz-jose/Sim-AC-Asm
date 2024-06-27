# config.py

# Constantes para patrones de expresiones regulares
DATA_SECTION_PATTERN = r'^SECTION\s*\.DATA\s*$'
TEXT_SECTION_PATTERN = r'^SECTION\s*\.TEXT\s*$'
DATA_ENTRY_PATTERN = r'^([a-zA-Z]\w*)(?::)?\s+DB\s+(\d+)\s*$'
LABEL_PATTERN = r'^([a-zA-Z]\w*):'
INSTRUCTION_PATTERN = r'^([A-Z]{3})\s+\[(\w+)\]$'

# Instrucciones y sus códigos de operación
INSTRUCTION_CODES = {
    "ADD": 0,
    "SUB": 1,
    "LDA": 2,
    "STA": 3,
    "JMP": 4,
    "JZ": 5,
    "JC": 6,
    "LDI": 7  # Cambiado a 7
}
