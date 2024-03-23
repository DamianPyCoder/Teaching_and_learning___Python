import numpy as np

# Array unidimensional
# array_1d = np.array([1,2,3])
# print("array unidimensional: ",array_1d)
# print("")

# Array multidimensional
# array_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print("array multidimensional:")
# print(array_2d)
# print("")

# Propiedades
# print("Propiedades:")
# print("Forma del array array_2d: ", array_2d.shape)
# print("Tamaño del array array_2d: ", array_2d.size)
# print("Tipo de dato del array_2d: ",array_2d.dtype)

# Acceso a elementos dentro del array
# print("Primer elemento en array_1d: ", array_1d[0])
# print("Elemento de la primera fila y la tercera columna de array_2d: ", array_2d[0,2])

# Modificación de elementos en el array
# array_1d[0] = 7
# print(array_1d)
# print("")
# array_2d[0,0] = 7
# print(array_2d)



# array1 = np.array([2,4,6,8,10])
# array2 = np.array([1,3,5,7,9])

# # operaciones sencillas
# suma_resultado=array1 + array2
# print("Suma: ",suma_resultado)

# resta_resultado=array1 - array2
# print("Resta: ",resta_resultado)

# multiplic_resultado = array1 * array2
# print("Multiplicación: ", multiplic_resultado)

# division_resultado = array2 / array1
# print("División: ", division_resultado)

# sqrt_resultado = np.sqrt(array1)
# print("Raiz cuadrada: ", sqrt_resultado)

# exponencial_resultado = np.exp(array1)
# print("Exponencial: ",exponencial_resultado)

# seno_resultado = np.sin(array1)
# print("Seno: ",seno_resultado)

# coseno_resultado = np.cos(array1)
# print("Coseno: ",coseno_resultado)



# array = np.array([0,1,2,3,4,5,6,7,8,9,10])
# print("Obtener quinto elemento del array: ", array[4])
# print("Obtener los resultados desde el elemento 3 hasta el 7: ",array[2:6])
# print("Obtener los elementos pares: ",array[::2])

# array = np.array([1,2,3,4,5,6])
# cambiar forma del array a una matriz 2x3
# reshaped_array = array.reshape(2,3)
# print("Array modificada: ")
# print(reshaped_array)

# Propiedades 2
#print("Dimensión del array: ",array.ndim)

# Cambiar tipos de datos
# float_array = array.astype(float)
# print("Array casteado a float:")
# print(float_array)

# Tamaño en bytes de cada elemento
# print("Tamaño de cada elemento: ",array.itemsize)

# Mínimos y máximos
# print("Valor mínimo: ",array.min()," y valor máximo: ",array.max())

# Suma y productos de los elementos del array
# print("Suma de todos los elementos: ", array.sum(), " y multiplicación de los elementos: ", array.prod())



array = np.array([1,2,3,4,5,6])

# Máscara booleana
# mask = array > 2
# selected_elements = array[mask]
# print("Elementos mayores que dos: ",selected_elements)

# Operaciones estadísticas
# print("Media: ",array.mean())
# print("Mediana: ",np.median(array))
# print("Desviación estandar: ",array.std())
# print("Varianza: ",array.var())

# Ordenar elementos
# array.sort()
# print("Array ordenado: ", array)

# Arrays especiales
# zeros_array = np.zeros((2,3))
# print("Array de ceros: ")
# print(zeros_array)
# ones_array = np.ones((3,2))
# print("Arrays de unos: ")
# print(ones_array)


array1 = np.array([1,2,3,4,5,6])
array2 = np.array([4,5,2,1,8,7])

# Concatenación de arrays
# verticalmente
# concatenated_array = np.vstack((array1, array2))
# print("Arrays concatenados: ")
# print(concatenated_array)
# horizontalmente
# concatenated_array = np.hstack((array1, array2))
# print(concatenated_array)

# # Encontrar el índice con valores máximos y mínimos
# print("Índice con valor máximo: ",array2.argmax())
# print("Índice con valor mínimo: ",array2.argmin())

# Crear secuencia de 0 a 9, con paso de 2
# sequence = np.arange(0, 10, 2)
# print("Secuencia númerica equiespaciada: ",sequence)

# sequence = np.linspace(0,1,5)
# print("Secuencia numérica de valores espaciados uniformemente: ", sequence)

# Funciones álgebra lineal
# dot_product = np.dot(array1, array2)
# print("Producto punto entre los dos arrays: ",dot_product)

# Calcular determinante de una matriz
# matrix = np.array([[1,2],[3,4]])
# determinant = np.linalg.det(matrix)
# print("Determinante de la matriz:")
# print(determinant)

# Invertir array
# reversed_array = array1[::-1]
# print("Array invertido: ",reversed_array)