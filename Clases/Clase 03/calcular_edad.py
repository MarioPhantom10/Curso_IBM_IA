# Autor: Mario Santander
"""Comenzando con el ejercicio de la clase 03
Autor: Mario Santander

Crea un programa interactivo que calcule la edad basándose en el año de nacimiento.
1- Solicita al usuario su nombre y año de nacimiento
2- Calcula la edad basandose en el año actual y muestra qué tipo de dato es
3- Convierte la entrada del usuario para poder hacer cálculos
4- Determina si la persona es mayor de edad y guarda esa información
5- Muestra un saludo personalizado con el nombre y la edad calculada"""


name = input("Acontinuacion indica tu nombre por favor: ")
print ("Tu nombre es: " + (name))
birth_year = input("Indica tu año de nacimiento por favor: ")
print ("Tu año de nacimiento es: " + (birth_year))

current_year = 2025
age = current_year - int(birth_year)
print ("El tipo de dato de la edad es: " + str(type(age)))

is_adult = age >= 18


print ("Hola " + name + ", tu edad es de " + str(age) + " años.")

#el ejercicio no pide mostrar si es mayor o menor de edad, pero se prodria agregar para verificar que funciona
#if is_adult: (en este caso if, si se cumple la condicion de ser adulto, dara el mensaje de abajo)
#    print("Eres mayor de edad.")
#else: (en este caso else, si no se cumple la condicion de ser adulto, dara el mensaje de abajo)
#    print("No eres mayor de edad.")

#if is_adult:
#    print("Eres mayor de edad.")
#else:
#    print("No eres mayor de edad.")

