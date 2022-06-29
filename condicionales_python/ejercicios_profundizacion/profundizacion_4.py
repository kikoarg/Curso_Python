# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
texto_1 = str(input('Ingrese palabra #1:'))
texto_2 = str(input('Ingrese palabra #2:'))
texto_3 = str(input('Ingrese palabra #3:'))

condicion = int(input('Ingrese el numero (1) para ordenar alfabeticamente // ingrese (2) para ordenar por cantidad de letras: '))

if condicion == 1:
    if texto_1[0] < texto_2[0] and texto_1[0] < texto_3[0]:
        if texto_2[0] < texto_3[0]:
            print(f'{texto_1}, {texto_2}, {texto_3}')
        else:
            print(f'{texto_1}, {texto_3}, {texto_2}')
    elif texto_2[0] < texto_1[0] and texto_2[0] < texto_3[0]:
        if texto_1[0] < texto_3[0]:
            print(f'{texto_2}, {texto_1}, {texto_3}')
        else:
            print(f'{texto_2}, {texto_3}, {texto_1}')
    elif texto_3[0] < texto_1[0] and texto_3[0] < texto_2[0]:
        if texto_1[0] < texto_2[0]:
            print(f'{texto_3}, {texto_1}, {texto_2}')
        else:
            print(f'{texto_3}, {texto_2}, {texto_1}')
        
if condicion == 2: # a terminar