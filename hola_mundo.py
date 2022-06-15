# Hola Mundo! [Python]
# ---------------------------
# Autor: Inove Coding School
# Version: 2.0

# Descripcion:
# Programa creado para ensayar el correcto funcionamiento
# del entorno de instalación Python
import os

name = input("Introduce tu nombre: ")
print(f"Hola, {name} este es tu primer script!")

content = '/home/python/Documents/GitHub/hola_mundo_python/'
print("Listando archivos en la carpeta: ")
with os.scandir(content) as ficheros:
    for fichero in ficheros:
        print(fichero.name)