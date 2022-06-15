#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.4

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.4"

def ej1():
    # Ejercicios de práctica numérica
    numero_1 = 5
    numero_2 = 7

    # Realizar la suma de las dos variables
    # numero_1 y numero_2
    # Almacenar el valor de la suma en una variable
    # ej:
    # operacion = .....

    # Imprimir en pantalla el resultado de la suma
    # print(....)
    suma = numero_1 + numero_2
    print('El resultado de la suma es', suma)

    # Repita el procedimiento para realizar la resta
    resta = numero_1 - numero_2
    print('El resultado de la resta es', resta)


def ej2():
    # Ejercicios de práctica numérica

    # Operadores con números decimales
    # Ahora los valores a operar deben ser ingresados por
    # consola con la función "input" como se ve a continuación
    numero_3 = 3.0
    print('El primer numero decimal a operar es', numero_3)
    
    numero_4 = 10.5
    print('El segundo numero decimal a operar es', numero_4)
    

    # Alumno: Imprima en pantalla los dos números decimales solicitados
    # print(....)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_1, numero_2
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    # Suma
    suma = numero_3 + numero_4
    print('El resultado de la suma es', suma)
    # Resta
    resta = numero_3 + numero_4
    print('El resultado de la resta es', resta)
    # División
    division = numero_3 / numero_4
    print('El resultado de la division es', division)
    # Multiplicación


def ej3():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    
    nombre = 'Beatriz'
    apellido = 'Garrido'
    suma = nombre + apellido
    print('El resultado de la suma es', suma)

    # Imprima su nombre completo

    # Almacenar su nombre completo en una variable
    # nombre_completo = .....

    # Imprimir la cantidad de letras que posee su nombre completo


def ej4():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('Ingrese palabra_1')
    palabra_1 = str(input())

    print('Ingrese palabra_2')
    palabra_2 = str(input())

    print('Ingrese palabra_3')
    palabra_3 = str(input())

    # De cada palabra debe tomar la primera letra y armar el acrónimo
    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla


def ej5():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    # Formar una nueva palabra con los recortes solicitados
    # Imprima en pantalla los resultados


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    # ej2()
    # ej3()
    # ej4()
    # ej5()
