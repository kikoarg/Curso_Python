# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese tres palabras y arme un acrónimo con ellas
# Si desea puede modificar el código para ingresar más palabras
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

print('Ingrese palabra 3:')
palabra_3 = str(input())

# Printeamos las palabras elegidas
print(f'Las palabras son: {palabra_1}, {palabra_2} y {palabra_3}')

# De cada palabra debe tomar la primera letra y armar el acrónimo
# Ejemplo: Alumbrado, barrido y limpieza --> ABL

# Realizamos el acronimo con las dos primeras letras de cada palabra
resul1 = palabra_1[:2] + palabra_2[:2] + palabra_3[:2]

# Imprimir el resultado en pantalla
print(resul1)