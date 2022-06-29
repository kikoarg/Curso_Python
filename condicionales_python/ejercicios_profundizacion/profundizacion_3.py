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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
numero_1 = float(input('Ingrese temperatura #1:'))
numero_2 = float(input('Ingrese temperatura #2:'))
numero_3 = float(input('Ingrese temperatura #3:'))

temp_a = 0
temp_b = 0
temp_p = (numero_1+numero_2+numero_3) / 3 

if numero_1 > numero_2 and numero_1 > numero_3:
    temp_a = numero_1
elif numero_2 > numero_1 and numero_2 > numero_3:
    temp_a = numero_2
else:
    temp_a = numero_3

if numero_1 < numero_2 and numero_1 < numero_3:
    temp_b = numero_1
elif numero_2 < numero_1 and numero_2 < numero_3:
    temp_b = numero_2
else:
    temp_b = numero_3

print(f"La temperatura mas alta es {temp_a} °C")
print(f"La temperatura mas baja es {temp_b} °C")
print(f"La temperatura prromedio es de {temp_p} °C")