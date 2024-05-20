# Sim-AC - Simulador y Ensamblador para Simulador de Arquitectura de Computadoras

## Descripción
Sim-AC es una herramienta que proporciona un simulador y ensamblador para la arquitectura de computadoras Sim-AC. Este proyecto permite escribir programas en lenguaje ensamblador Sim-AC y ejecutarlos en un simulador para comprender y experimentar con el funcionamiento interno de esta arquitectura de computadoras.
El objetivo principal de este proyecto es permitir a los usuarios escribir, ensamblar y ejecutar programas en el lenguaje ensamblador Sim-AC, facilitando la comprensión del funcionamiento interno de una arquitectura de computadoras.

El ensamblador Sim-AC traduce el código escrito en lenguaje ensamblador Sim-AC a su correspondiente código numérico, que puede ser ejecutado en el simulador. El proyecto está estructurado en varios módulos para mejorar la modularidad, legibilidad y mantenibilidad del código. Entre los principales módulos se incluyen:

- `main.py`: Punto de entrada del programa, coordina el ensamblaje y simulación.
- `file_reader.py`: Lee el archivo del programa ensamblador.
- `instruction_processor.py`: Procesa las instrucciones del programa, divide en secciones de datos y texto, y maneja etiquetas y operandos.
- `error_handler.py`: Maneja errores durante el ensamblaje y ejecución.
- `instruction_code_generator.py`: Genera códigos de instrucción a partir del programa ensamblado.
- `config.py`: Contiene constantes y patrones de expresiones regulares usados en todo el proyecto.

Sim-AC ayuda a los estudiantes y entusiastas de la informática a experimentar y entender cómo se ejecutan las instrucciones a nivel de máquina, proporcionando una plataforma práctica para aprender ensamblador y arquitectura de computadoras.

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
   - Se generarán dos archivos: uno para la sección `.data` y otro para la sección `.text` en formato hexadecimal. Los archivos se nombrarán como `archivo.data.mem` y `archivo.text.mem` respectivamente.

## Partes Principales del Proyecto

### 1. `main.py`
Este archivo contiene el punto de entrada del programa. Coordina la ejecución del ensamblaje y la simulación.

### 2. `file_reader.py`
Este módulo se encarga de leer el archivo que contiene el programa en lenguaje ensamblador Sim-AC y devolver sus líneas para su procesamiento.

### 3. `instruction_processor.py`
Este módulo realiza el procesamiento del programa en lenguaje ensamblador Sim-AC, dividiéndolo en secciones de datos y texto, identificando etiquetas, reemplazando operandos y manejando las instrucciones.

### 4. `error_handler.py`
Este módulo se encarga de manejar los errores que pueden surgir durante el ensamblaje y la ejecución del programa en lenguaje ensamblador Sim-AC.

### 5. `instruction_code_generator.py`
Este módulo genera los códigos de instrucción correspondientes a partir del programa ensamblado en lenguaje ensamblador Sim-AC.

### 6. `hex_file_generator.py`
Este módulo genera los archivos en formato hexadecimal para las secciones `.data` y `.text` del programa ensamblado.

### 7. `config.py`
Este archivo contiene constantes y patrones de expresiones regulares utilizados en todo el proyecto.

## Contribución
¡Las contribuciones son bienvenidas! Si encuentras algún error o tienes alguna mejora que sugerir, por favor, crea un "issue" o envía una "pull request" en el repositorio del proyecto.

## Licencia
Este proyecto está bajo la Licencia GNU. Consulta el archivo `LICENSE` para obtener más detalles.
