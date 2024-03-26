import math
import cmath
import random

# nombre = "Damian"
# x = 10
# y = 5

# OPERACIONES

# suma = x + y
# resta = x - y
# multiplicacion = x * y
# division = x / y

# print("La suma es ", suma)
# print("La resta es ", resta)
# print("La multiplicación es ", multiplicacion)
# print("La división es ", division)

# mayor = 10 > 5
# menor = 5 < 10
# igualdad = 10 == x
# diferencia = x != x

# print(mayor, menor, igualdad, diferencia)


# CONDICIONALES
# nota = 6
# if nota == 5:
#     print("Has aprobado")
# elif nota == 6:
#     print("Has sacado un bien")
# elif nota > 6:
#     print("Ohh genial, buena nota")
# else:
#     print("Suspendiste")
# print("Final del programa")


# BUCLES
# colores = ["rojo","verde","azul"]
# for i in colores:
#     print("Mi color favorito es:")
#     print(i)

# num = 0
# while num < 11:
#     print(num)
#     #num = num + 1
#     num += 1
    

# LISTAS
# miLista = [1,2,3]
# primerElemento = miLista[0]
# print(primerElemento)
# miLista.append(4) # agregar elemento al final de la lista
# miLista.insert(0,7) #modificar primer elemento con un siete
# miLista[1]=9
# print(miLista)

# TUPLAS
# miTupla = (1,2,3)
# elementoTercero = miTupla[2]
# print(elementoTercero)

# DICCIONARIOS
# miDiccionario = {"nombre":"Damian","edad":25}
# miDiccionario["pais"] = "Japón"
# miDiccionario["nombre"] = "Marcos"
# print(miDiccionario)

# CONJUNTOS
# miConjunto = {1,2,3}
# miSegundoConj = {1,2,4}
# miConjunto.add(4)
# miConjunto.remove(3) #genera un error si no existe
# miConjunto.discard(2)
# miConjunto.intersection(miSegundoConj) #encontramos elementos comunes en los conjuntos
# miConjunto.difference(miSegundoConj) #encontramos diferencias entre conjuntos
# unionConjuntos = miConjunto.union(miSegundoConj) #unimos dos conjuntos


# FUNCIONES
# def decirHola():
#     return "Hola"
# def decirHolaConNombre(nombre):
#     return "Hola "+nombre
# print(decirHola())
# print(decirHolaConNombre("Damian"))

# cuadrado = lambda x: x **2
# resultado = cuadrado(5)
# print(resultado)

# def factorial(x):
#     if x == 0:
#         return 1
#     else:
#         return x * factorial(x-1)
# resultado = factorial(5)
# print(resultado)



# # STRINGS
# mensaje = "Hola usuario, eres un buen programador"

# #split
# comas = mensaje.split(",")
# espacios = mensaje.split()

# #strip 
# texto  = "       Hola, usuario!     "
# limpiarEspacios = texto.strip()

# #Join
# palabrasJoin = ["Hola", "usuario", "eres","genial"]
# mensajeJoin = "-".join(palabrasJoin)

# #startswith()
# #endswith()
# print(mensajeJoin.startswith("Hola")) 
# print(mensajeJoin.endswith("Hola")) 

# #CASTEO
# # #String -> otros tipos de datos
# # numeroEntero = int("1")
# # numeroFlotante = float("1.5")

# # #entero a otros tipos de datos
# # numero = str(1)
# # numeroFlot = float(1)

# # #float a otros tipos de datos
# # numeroFlotant = str(12.5)
# # numerEnter = int(12.5)

# # EJEMPLOS CASTEO
# #String a float
# # cadena = "123.5"
# # numero = float(cadena)

# # #Float a int
# # numeroFlot = 123.5
# # numeroEnter = int(numeroFlot)

# # #String en float
# # cadena = "123.5"
# # numero = float(cadena)

# # #Float a int
# # numeroFloat = 123.5
# # numeroEnter = int(numeroFloat)

# # #Int a float
# # numeroEnter = 123
# # numeroFloat = float(numeroEnter)

# # #Float a string
# # numeroFloat = 123.5
# # cadena = str(numeroFloat)

# # #int a string
# # numeroEnter = 123
# # cadena = str(numeroEnter)


# # NUMEROS avanzado
# potencia = 2 ** 5
# divisionEntera = 10 // 3
# modulo = 10 % 3

# valorAbsoluto = abs(-5)
# redondeo = round(3.1416, 3)
# potencia = pow(2,5)
# valorMax = max(3,6,1)
# valorMin = min(4,7,2)

# raizCuadrada = math.sqrt(21)
# factorial = math.factorial(5)
# seno = math.sin(math.pi/2)
# logaritmo = math.log(10,4)

# #números complejos
# complejo = 2 +4j
# conjugar = cmath.conjugate(complejo)
# fase = cmath.phase(complejo)

# numerosAleatorios = random.random()
# enteroAlatorio = random.radint(1,10)
# listaAleatoria = random.sample(range(1,10),2)



