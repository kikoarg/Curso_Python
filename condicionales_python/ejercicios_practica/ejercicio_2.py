# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
if texto_1 == texto_2:
    print(f'Las dos palabras son iguales')
elif texto_1 > texto_2:
    print(f'La primer palabra es mayor')
else:
    print(f'La segunda palabra es mayor')
# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
print(f'--------------')
if len(texto_1) == len(texto_2):
    print(f'Las dos palabras contienen misma cantidad de letras')
elif len(texto_1) > len(texto_2):
    print(f'la primer palabra contiene mayor cantidad de letras')
else:
    print(f'la segunda palabra contiene mayor cantidad de letras')
# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda
print(f'--------------')
if (texto_1[0]) == (texto_2[0]):
    print(f'Las dos palabras contienen la primer letra iguales')
elif (texto_1[0]) > (texto_2[0]):
    print(f'la primera letra de la palabra "{texto_1}" es MAYOR a la segunda palabra "{texto_2}"')
else:
    print(f'la primera letra de la palabra "{texto_1}" es MENOR a la segunda palabra "{texto_2}"')


# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda
print(f'--------------')
copia_texto_1 = texto_1  # Copia de la variable texto_1
if copia_texto_1 == texto_1:
    print(f'{copia_texto_1} es igual a {texto_1}')

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
print(f'--------------')
if copia_texto_1 != texto_2:
    # mejoria de codigo deberia verificar primero si son iguales
    print(f'{copia_texto_1} es distinta a {texto_2}')
