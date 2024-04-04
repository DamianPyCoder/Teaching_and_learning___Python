from collections import Counter
import time 
import random

def encontrar_mas_frecuente_con_counter(lista):
    inicio = time.time()
    contador = Counter(lista)
    numero_mas_frecuente = contador.most_common(1)[0][0]
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    return numero_mas_frecuente, tiempo_ejecucion


def encontrar_mas_frecuente_con_diccionario(lista):
    inicio = time.time()
    frecuencia_numeros = {}
    # suma_repetidos = {}
    for num in lista:
        if num in frecuencia_numeros:
            frecuencia_numeros[num] +=1
            # suma_repetidos[num] += num
        else:
            frecuencia_numeros[num] = 1
            # suma_repetidos[num] = num
    numero_mas_frecuente = max(frecuencia_numeros, key=frecuencia_numeros.get)
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    return numero_mas_frecuente, tiempo_ejecucion

lista = [random.randint(1,100) for _ in range(1000)]

# Ejemplo 2
numero_mas_frecuente_counter, tiempo_counter = encontrar_mas_frecuente_con_counter(lista)
print("Número más frecuente con Counter:",numero_mas_frecuente_counter)
print("Tiempo de ejecución con Counter:","{:.10f}".format(tiempo_counter), "segundos")
numero_mas_frecuente_diccionario, tiempo_diccionario = encontrar_mas_frecuente_con_diccionario(lista)
print("Número más frecuente con Diccionario:",numero_mas_frecuente_diccionario)
print("Tiempo de ejecución con Diccionario:","{:.10f}".format(tiempo_diccionario), "segundos")





# Ejemplo
# lista = [1,3,5,6,2,7,5,8,2,4,5,5,1,5]
# numero_mas_frecuente, suma_mas_frecuente = encontrar_mas_frecuente_con_suma(lista)
# print("Número más frecuente:",numero_mas_frecuente)
# print("Suma de elementos repetidos:",suma_mas_frecuente)