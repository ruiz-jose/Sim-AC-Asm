# Sim-AC - Simulador y Ensamblador para Simulador de Arquitectura de Computadoras

## Descripción
Sim-AC es una herramienta que proporciona un simulador y ensamblador para la arquitectura de computadoras Sim-AC. Este proyecto permite escribir programas en lenguaje ensamblador Sim-AC y ejecutarlos en un simulador para comprender y experimentar con el funcionamiento interno de esta arquitectura de computadoras.

## Uso
Para utilizar Sim-AC, sigue los pasos siguientes:

1. **Instalación de dependencias:** Asegúrate de tener instaladas las siguientes dependencias:
   - Python 3.x
   - Colorama (puedes instalarlo con `pip install colorama`)

2. **Ejecución del programa:**
   - Abre una terminal en la carpeta raíz del proyecto.
   - Ejecuta el siguiente comando para ensamblar y simular un programa en lenguaje ensamblador Sim-AC:
     ```
     python main.py archivo.ac
     ```
     Reemplaza `archivo.ac` con el nombre del archivo que contiene el programa en lenguaje ensamblador Sim-AC.

3. **Interpretación de resultados:**
   - El programa mostrará la salida correspondiente al ensamblaje y ejecución del programa, incluyendo mensajes de error si los hubiera.

## Partes Principales del Proyecto

### 1. `main.py`
Este archivo contiene el punto de entrada del programa. Coordina la ejecución del ensamblaje y la simulación del programa en lenguaje ensamblador Sim-AC.

### 2. `file_reader.py`
Este módulo se encarga de leer el archivo que contiene el programa en lenguaje ensamblador Sim-AC y devolver sus líneas para su procesamiento.

### 3. `instruction_processor.py`
Este módulo realiza el procesamiento del programa en lenguaje ensamblador Sim-AC, dividiéndolo en secciones de datos y texto, identificando etiquetas, reemplazando operandos y manejando las instrucciones.

### 4. `error_handler.py`
Este módulo se encarga de manejar los errores que pueden surgir durante el ensamblaje y la ejecución del programa en lenguaje ensamblador Sim-AC.

### 5. `instruction_code_generator.py`
Este módulo genera los códigos de instrucción correspondientes a partir del programa ensamblado en lenguaje ensamblador Sim-AC.

### 6. `config.py`
Este archivo contiene constantes y patrones de expresiones regulares utilizados en todo el proyecto.

## Contribución
¡Las contribuciones son bienvenidas! Si encuentras algún error o tienes alguna mejora que sugerir, por favor, crea un "issue" o envía una "pull request" en el repositorio del proyecto.

## Licencia
Este proyecto está bajo la Licencia GNU. Consulta el archivo `LICENSE` para obtener más detalles.

