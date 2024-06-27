.PHONY: all clean

# Directorio de los archivos fuente y de los ejemplos
SRC_DIR := src
EXAMPLES_DIR := examples
BIN_DIR := bin

# Archivo principal de Python
MAIN_PY := $(SRC_DIR)/main.py

# Encuentra todos los archivos .ac en el directorio de ejemplos
AC_FILES := $(wildcard $(EXAMPLES_DIR)/*.ac)

# Nombres de los archivos sin la ruta y la extensión
AC_NAMES := $(notdir $(basename $(AC_FILES)))

# Regla all para procesar todos los archivos .ac
all: $(AC_NAMES)

# Regla para procesar cada archivo .ac
$(AC_NAMES):
	@mkdir -p $(BIN_DIR)
	python3 $(MAIN_PY) $(EXAMPLES_DIR)/$@.ac

# Regla clean para limpiar la carpeta bin
clean:
	@rm -rf $(BIN_DIR)
	@echo "Carpeta 'bin' limpiada."