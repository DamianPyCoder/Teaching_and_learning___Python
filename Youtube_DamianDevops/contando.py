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

def encontrar_mas_frecuente_array(lista):
    inicio = time.time()
    frecuencia_numeros = [0] * (max(lista) + 1)
    for num in lista:
        frecuencia_numeros[num] += 1
    numero_mas_frecuente = frecuencia_numeros.index(max(frecuencia_numeros))
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    return numero_mas_frecuente, tiempo_ejecucion

def imprimir_resultado(nombre, tiempo, es_menor, es_mayor):
    if es_menor:
        print("{}\t({})".format(nombre, Fore.GREEN + "{:.10f} segundos".format(tiempo) + Fore.RESET))
    elif es_mayor:
        print("{}\t({})".format(nombre, Fore.RED + "{:.10f} segundos".format(tiempo) + Fore.RESET))
    else:
        print("{}\t({:.10f} segundos)".format(nombre, tiempo))

def formato_miles(numero):
    return "{:,}".format(numero).replace(",", ".")

def generar_lista_larga(tamanio):
    return [random.randint(1, 100) for _ in range(tamanio)]

# Lista de ejemplo
medida_lista = 1000000
lista_larga = generar_lista_larga(medida_lista)

# Utilizando Counter
resultado_counter, tiempo_counter = encontrar_mas_frecuente_counter(lista_larga)

# Utilizando diccionario
resultado_diccionario, tiempo_diccionario = encontrar_mas_frecuente_diccionario(lista_larga)

# Utilizando array
resultado_array, tiempo_array = encontrar_mas_frecuente_array(lista_larga)

# Determinar el menor y el mayor
tiempos = [tiempo_counter, tiempo_diccionario, tiempo_array]
indice_menor = tiempos.index(min(tiempos))
indice_mayor = tiempos.index(max(tiempos))

# Imprimir resultados
print("------------------------------------------------------------------")
print("El número más repetido es:", resultado_counter)
print("Se ha buscado entre un número total de", formato_miles(medida_lista), "elementos.")
print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -")
imprimir_resultado("Utilizando Counter:", tiempo_counter, indice_menor == 0, indice_mayor == 0)
imprimir_resultado("Utilizando Diccion:", tiempo_diccionario, indice_menor == 1, indice_mayor == 1)
imprimir_resultado("Utilizando Array:", tiempo_array, indice_menor == 2, indice_mayor == 2)
print("------------------------------------------------------------------")
