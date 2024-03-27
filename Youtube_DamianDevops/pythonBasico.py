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

# EXPRESIÓN TERNARIA
# edad = 12
# if edad >= 18:
#     print("Es mayor de edad")
# else:
#     print("Es menor de edad")

# mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
# print(mensaje)


# PASS, CONTINUE y BREAK
# x = 100

# if x > 66:
#     pass
# else:
#     print("X es menor o igual que 66!")
# print("")

# for i in range(10):
#     print(i)
# else:
#     print("Bucle completado")

# for i in range(10):
#     if i == 4:
#         continue
#     if i == 9:
#         break
#     print(i)


# ZIP()
# nombres = ['Damian','Maria','Luis']
# edades = [25,28,32] 
# for nombre, edad in zip(nombres, edades):
#     print(f"{nombre} tiene {edad} años, ya eres un poco viejo")   


# STRINGS REPASO
# saludo = "hola, Damian"
# saludoConEspacios = "      Hola, Damián    "
# saludosPalabras = ["Hola", "Damian"]

# print(saludo.split(","))
# print(saludoConEspacios.strip())
# print("-".join(saludosPalabras))
# print(saludo.startswith("Hola"))
# print(saludo.endswith("Hola"))

# print(saludo.upper())
# print(saludo.lower())
# print(saludo.capitalize())
# print(saludo.count("a"))
# print(saludo.find("Damian"))
# print(saludo.replace("Damian","amigo"))
# print(saludo.isalnum())
# print(saludo.isalpha())



# COMPARAR NÚMEROS / STRINGS

# numero1 = 10
# numero2 = 10
# igualQue = numero1 == numero2
# diferenteQue = numero1 != numero2

# string1 = "rojo"
# string2 = "azul"
# igualQue = string1 == string2
# diferenteQue = string1 != string2

# print(string1 > string2)
# print(string1 < string2)




# # POO
# class Vehiculo:
#     def __init__(self, nombreMarca, ruedas, puertas, consumogasolina):
#         self.nombreMarca = nombreMarca
#         self.ruedas = ruedas
#         self.puertas = puertas
#         self.consumogasolina = consumogasolina
#     def acelerar(self):
#         print("Acelera el vehículo")


# class Coche(Vehiculo):
#     def __init__(self, nombreMarca, ruedas, puertas, consumogasolina, aforo):
#         super().__init__(nombreMarca, ruedas, puertas, consumogasolina)
#         self.aforo = aforo
#     def acelerar(self):
#         print("El coche está acelerando")


# class Moto(Vehiculo):
#     def __init__(self, nombreMarca, ruedas, puertas, consumogasolina):
#         super().__init__(nombreMarca, ruedas, puertas, consumogasolina)
#     # def acelerar(self):
#     #     print("La moto está acelerando")


# # instancias
# miCoche = Coche("Ferrari", 4, True, 2.5, 2)
# miMoto = Moto("Suzuki", 2, False, 1.2)

# # print(miCoche.acelerar())
# # print(miMoto.acelerar())

# # atributos de las instancias
# print("Coche:")
# print("Nombre/Marca:", miCoche.nombreMarca)
# print("Ruedas:", miCoche.ruedas)
# print("Puertas:", miCoche.puertas)
# print("Consumo de Gasolina:", miCoche.consumogasolina)
# print("Aforo:", miCoche.aforo)

# print("\nMoto:")
# print("Nombre/Marca:", miMoto.nombreMarca)
# print("Ruedas:", miMoto.ruedas)
# print("Puertas:", miMoto.puertas)
# print("Consumo de Gasolina:", miMoto.consumogasolina)


# EXCEPCIONES
# number = 2

# try:
#     resultado = 10 / number
#     print(resultado)
# except ZeroDivisionError:
#     print("Error: división por cero es imposible")
# finally:
#     print("Intento de división completado")

# # resultado = 10 / number
# # print(resultado)

# print("Hola")



# ARCHIVOS
# try:
#     archivo = open("palabra.txt","r")
#     contenido = archivo.read()
#     print(contenido)
# except FileNotFoundError:
#     print("Error: archivo no encontrado")
# finally:
#     try:
#         archivo.close()
#     except:
#         pass


# # try:
# #     with open("palabra.txt","w")  as archivo:
# #         archivo.write("casa, ")
# #         archivo.write("dormitorio")
# # except IOError:
# #     print("Error al escribir en el documento")


# try:
#     with open("palabra.txt","a")  as archivo:
#         archivo.write(", salón, ")
#         archivo.write("cocina")
# except IOError:
#     print("Error al escribir en el documento")


# try:
#     archivo = open("palabra.txt","r")
#     contenido = archivo.read()
#     print(contenido)
# except FileNotFoundError:
#     print("Error: archivo no encontrado")
# finally:
#     try:
#         archivo.close()
#     except:
#         pass