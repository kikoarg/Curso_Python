# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))
print(f'--------------')
# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda
if numero_1 == numero_2:
    print(f'Los dos numeros son iguales')
elif numero_1 > numero_2:
    print(f'El primer numero {numero_1} es mayor que {numero_2}')
else:
    print(f'El segundo numero {numero_2} es mayor que {numero_1}')

# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso
print(f'--------------')
if numero_1 > 0:
    print(f'{numero_1} es positivo')
elif numero_1 < 0:
    print(f'{numero_1} es negativo')
else:
    print(f'El numero ingresado es cero')
# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición
print(f'--------------')
if numero_1 > 0 and numero_1 < 100:
    print(f'El numero ingresado cumple con la condicion')
else:
    print(f'El numero no cumple con la condicion')


# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición
print(f'--------------')
if numero_1 < 10 and numero_2 > -2:
    print(f'Cumple con la condicion {numero_1} es menor a 10 y {numero_2} es mayor a -2')
else:
    print(f'No cumple con la condicion')