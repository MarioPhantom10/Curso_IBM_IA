# Autor: Mario Santander
"""Registro de temperaturas
Solicitar la tempertura de 5 dias consecutivos
mostrar la temperatura maxima, minima y promedio semanal
contar cuantos dias tuvieron temperaturas mayor a 25 grados
mostrar un resumen completo de los datos registrados"""

temp_dias = []
#Se crea una lista vacía llamada temp_dias.
#Se guardarán todas las temperaturas que ingrese el usuario

for i in range(5): #se repite 5 veces (para 5 días).
    temp = float(input(f"Ingrese la temperatura del dia {i+1}: ")) #pide al usuario que ingrese una temperatura. float convierte el valor ingresado en número decimal. 
    temp_dias.append(temp) #la temperatura ingresada se agrega a la lista temp_dias. append() añade un elemento al final de la lista.
temp_max = max(temp_dias) #se calcula la temperatura máxima usando la función max() aplicada a la lista temp_dias.
temp_min = min(temp_dias) #se calcula la temperatura mínima usando la función min() aplicada a la lista temp_dias.
temp_prom = sum(temp_dias) / len(temp_dias) #se calcula la temperatura promedio sumando todas las temperaturas (sum(temp_dias)) y dividiéndola por la cantidad de días (len(temp_dias)).
dias_mayores_25 = sum(1 for temp in temp_dias if temp > 25) #se cuenta cuántos días tuvieron temperaturas mayores a 25 grados. Se usa una expresión generadora que suma 1 por cada temperatura en temp_dias que sea mayor a 25. Esto es un generador que recorre cada temp de la lista.
print("\nResumen de temperaturas registradas:")
print(f"Temperatura maxima: {temp_max}°C") #se imprimen los resultados.
print(f"Temperatura minima: {temp_min}°C")
print(f"Temperatura promedio: {temp_prom:.2f}°C") #:.2f formatea el número para que tenga dos decimales. promedio semanal
print(f"Dias con temperatura mayor a 25°C: {dias_mayores_25} dias")

# mostrar un resumen completo de los datos registrados
print("Temperaturas registradas por dia:")
for i, temp in enumerate(temp_dias, start=1): #se usa enumerate para obtener tanto el índice (i) como la temperatura (temp) de cada día en la lista temp_dias. start=1 hace que el conteo comience en 1 en lugar de 0.
    print(f"Día {i}: {temp}°C")


