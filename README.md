# Laboratorio 2: Sistema de Tipos con ANTLR

Este repositorio contiene el laboratorio 2 del curso “Construcción de Compiladores” en UVG. El objetivo es:

* Generar un *lexer* y *parser* con ANTLR en Python
* Implementar un sistema de chequeo de tipos tanto con *Visitor* como con *Listener*
* Analizar casos de prueba que pasan y que fallan
* Extender la gramática con dos nuevas operaciones
* Ampliar el sistema de tipos para detectar al menos tres nuevos conflictos
* Documentar la solución en un video de YouTube (no listado) y publicar el código en GitHub

## Contenido

* **`SimpleLang.g4`**: Gramática ANTLR para SimpleLang (expr, literales, paréntesis)
* **`Driver.py`**: Driver Python que recorre el árbol con un *Visitor*
* **`type_check_visitor.py`**: Implementación del chequeo de tipos con *Visitor*
* **`DriverListener.py`**: Driver Python que recorre el árbol con un *Listener*
* **`type_check_listener.py`**: Implementación del chequeo de tipos con *Listener*
* **`custom_types.py`**: Definición de las clases `IntType`, `FloatType`, `StringType`, `BoolType`
* **`program_test_pass.txt`**: Ejemplos válidos que deben pasar sin errores
* **`program_test_no_pass.txt`**: Ejemplos con errores de tipos que deben detectarse
* **`README.md`**: Este documento

## Requisitos Previos

* Docker (Windows, macOS o Linux).
* Conexión a internet para descargar imágenes y paquetes.

## Construcción de la Imagen Docker

Desde la raíz de este repositorio:

```bash
docker build --rm -t lab2-image .
```

## Ejecución del Contenedor

Para montar la carpeta `program` y abrir un shell interactivo:

```bash
docker run --rm -it -v "${PWD}/program:/program" lab2-image bash
```

> En PowerShell se utiliza `${PWD}`; en CMD se puede usar `%cd%`.

## Generación del Parser

Dentro del contenedor, en `/program`:

 ```bash
antlr -Dlanguage=Python3 -visitor SimpleLang.g4			*** Para generar archivos para Visitor ***
antlr -Dlanguage=Python3 -listener SimpleLang.g4		*** Para generar archivos para Listener ***
```

## Ejecución del Driver

Para el archivo de prueba **sin errores**
```bash
python3 Driver.py program_test_pass.txt               *** Ejecutar con Visitor ***
python3 DriverListener.py program_test_pass.txt       *** Ejecutar con Listener ***
```

Para el archivo de prueba que **contiene errores**
```bash
python3 Driver.py program_test_pass.txt               *** Ejecutar con Visitor ***
python3 DriverListener.py program_test_pass.txt       *** Ejecutar con Listener ***
```

* **Sin errores**: la sintaxis y las operaciones entre tipos del programa son válidas.
* **Con errores**: Se mostrarán mensajes que describen el error.

## Video de Demostración

Video con la explicación:

[https://youtu.be/WrOVtlEXm6E](https://youtu.be/WrOVtlEXm6E)

