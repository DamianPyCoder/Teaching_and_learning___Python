from collections import Counter
import time 
import random
from colorama import init, Fore
init(autoreset=True)

def encontrarMasFrecuenteCounter(lista):
    inicio = time.time()
    contador = Counter(lista)
    numeroMasFrecuente = contador.most_common(1)[0][0]
    fin = time.time()
    tiempoEjecucion = fin - inicio
    return numeroMasFrecuente, tiempoEjecucion

def encontrarMasFrecuenteDiccionario(lista):
    inicio = time.time()
    frecuenciaNumeros = {}
    for num in lista:
        if num in frecuenciaNumeros:
            frecuenciaNumeros[num] +=1
        else: 
            frecuenciaNumeros[num]=1
    numeroMasFrecuente = max(frecuenciaNumeros, key=frecuenciaNumeros.get)
    fin = time.time()
    tiempoEjecucion = fin -inicio
    return numeroMasFrecuente, tiempoEjecucion

def encontrarMasFrecuenteArray(lista):
    inicio = time.time()
    frecuenciaNumeros =[0] * (max(lista)+1)
    for num in lista:
        frecuenciaNumeros[num] +=1
    numeroMasFrecuente = frecuenciaNumeros.index(max(frecuenciaNumeros))
    fin = time.time()
    tiempoEjecucion = fin -inicio
    return numeroMasFrecuente, tiempoEjecucion

def imprimirResultado(nombre,tiempo,esMenor,esMayor):
    if esMenor:
        print("{}\t({})".format(nombre, Fore.GREEN + "{:.10f} segundos".format(tiempo) + Fore.RESET))
    elif esMayor:
        print("{}\t({})".format(nombre, Fore.RED + "{:.10f} segundos".format(tiempo) + Fore.RESET))
    else:
        print("{}\t({:.10f} segundos)".format(nombre,tiempo))

# Formateamos separador miles 
def formatoMiles(numero):
    return "{:,}".format(numero).replace(",",".")

# Generar lista
def generarListaLarga(tamanio):
    return [random.randint(1,100) for _ in range(tamanio)]
medidaLista= 100000
listaLarga = generarListaLarga(medidaLista)

# Utilización métodos counter, diccionario, array
resultadoCounter, tiempoCounter = encontrarMasFrecuenteCounter(listaLarga)
resultadoDiccionario, tiempoDiccionario = encontrarMasFrecuenteDiccionario(listaLarga)
resultadoArray, tiempoArray = encontrarMasFrecuenteArray(listaLarga)

# Determinamos mayor y menor tiempo ejecución
tiempos = [tiempoCounter, tiempoDiccionario, tiempoArray]
indiceMenor = tiempos.index(min(tiempos))
indiceMayor = tiempos.index(max(tiempos))

# Imprimir resultados
print("-----------------------------------------------------------")
print("El número más repetido es: ", resultadoCounter)
print("Se ha buscado entre un número total de ",formatoMiles(medidaLista),"elementos.")
print("-----------------------------------------------------------")
imprimirResultado("Utilizando Counter:",tiempoCounter,indiceMenor==0,indiceMayor==0)
imprimirResultado("Utilizando Diccion:",tiempoDiccionario,indiceMenor==1,indiceMayor==1)
imprimirResultado("Utilizando Array:",tiempoArray,indiceMenor==2,indiceMayor==2)
print("-----------------------------------------------------------")
