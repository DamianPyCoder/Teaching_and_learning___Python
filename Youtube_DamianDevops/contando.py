from collections import Counter
import time
import random
from colorama import init, Fore

init(autoreset=True)  # Inicializar Colorama

def encontrar_mas_frecuente_counter(lista):
    inicio = time.time()
    contador = Counter(lista)
    numero_mas_frecuente = contador.most_common(1)[0][0]
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    return numero_mas_frecuente, tiempo_ejecucion

def encontrar_mas_frecuente_diccionario(lista):
    inicio = time.time()
    frecuencia_numeros = {}
    for num in lista:
        if num in frecuencia_numeros:
            frecuencia_numeros[num] += 1
        else:
            frecuencia_numeros[num] = 1
    numero_mas_frecuente = max(frecuencia_numeros, key=frecuencia_numeros.get)
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    return numero_mas_frecuente, tiempo_ejecucion

def imprimir_resultado(nombre, tiempo):
    print(f"{nombre} ({Fore.GREEN if tiempo == min(tiempo_counter, tiempo_diccionario) else ''}{tiempo:.10f} segundos{Fore.RESET})")

def generar_lista_larga(tamanio):
    return [random.randint(1, 100) for _ in range(tamanio)]

# Lista de ejemplo
medida_lista = 1000000
lista_larga = generar_lista_larga(medida_lista)

# Utilizando Counter
resultado_counter, tiempo_counter = encontrar_mas_frecuente_counter(lista_larga)

# Utilizando diccionario
resultado_diccionario, tiempo_diccionario = encontrar_mas_frecuente_diccionario(lista_larga)

# Imprimir resultados
print("El número más repetido es:", resultado_counter)
print("Se ha buscado entre un número total de", medida_lista, "elementos.")
imprimir_resultado("Utilizando Counter necesitó", tiempo_counter)
imprimir_resultado("Utilizando diccionario necesitó", tiempo_diccionario)
