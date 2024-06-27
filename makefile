.PHONY: all clean compile

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

# Nombre del ejemplo a compilar (opcional)
ej ?=

# Regla all para compilar el ejemplo especificado o todos si no se especifica ninguno
all:
ifeq ($(ej),)
	$(MAKE) compile AC_NAMES="$(AC_NAMES)"
else
	$(MAKE) compile AC_NAMES="$(ej)"
endif

# Regla para compilar los ejemplos
compile: $(AC_NAMES)
	@echo "Compilación completada."

# Regla para procesar cada archivo .ac
$(AC_NAMES):
	@mkdir -p $(BIN_DIR)
	python3 $(MAIN_PY) $(EXAMPLES_DIR)/$@.ac

# Regla clean para limpiar la carpeta bin
clean:
	@rm -rf $(BIN_DIR)
	@echo "Carpeta 'bin' limpiada."