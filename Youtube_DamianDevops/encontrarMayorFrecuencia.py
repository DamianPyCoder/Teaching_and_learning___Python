from collections import Counter
import time
import random

def encontrar_mas_frecuente_con_counter(lista):
    inicio = time.time()  # Tiempo de inicio de la función
    contador = Counter(lista)
    numero_mas_frecuente = contador.most_common(1)[0][0]
    fin = time.time()  # Tiempo de finalización de la función
    tiempo_ejecucion = fin - inicio  # Calcula el tiempo de ejecución
    return numero_mas_frecuente, tiempo_ejecucion

def encontrar_mas_frecuente_con_diccionario(lista):
    inicio = time.time()  # Tiempo de inicio de la función
    frecuencia_numeros = {}
    for num in lista:
        if num in frecuencia_numeros:
            frecuencia_numeros[num] += 1
        else:
            frecuencia_numeros[num] = 1
    numero_mas_frecuente = max(frecuencia_numeros, key=frecuencia_numeros.get)
    fin = time.time()  # Tiempo de finalización de la función
    tiempo_ejecucion = fin - inicio  # Calcula el tiempo de ejecución
    return numero_mas_frecuente, tiempo_ejecucion

# Generar una lista con mil números aleatorios
lista = [random.randint(1, 100) for _ in range(1000)]

# Ejemplo de uso con Counter
numero_mas_frecuente_counter, tiempo_counter = encontrar_mas_frecuente_con_counter(lista)
print("Número más frecuente con Counter:", numero_mas_frecuente_counter)
print("")
print("Tiempo de ejecución con Counter:", "{:.10f}".format(tiempo_counter), "segundos")
# Ejemplo de uso con diccionario
numero_mas_frecuente_diccionario, tiempo_diccionario = encontrar_mas_frecuente_con_diccionario(lista)
# print("Número más frecuente con diccionario:", numero_mas_frecuente_diccionario)
print("Tiempo de ejecución con diccionario:", "{:.10f}".format(tiempo_diccionario), "segundos")
