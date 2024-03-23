import numpy as np
import os

# BROADCASTING
array1 = np.array([[1,2,3],[4,5,6]])
array2 = np.array([22,16,10])
# print("Broadcasting de arrays: ",array1+array2)

# RESIZING
# resized_array= np.resize(array2, (3,2))
# print("Array redimensionado: ")
# print(resized_array)

# DIVISIONES DE ARRAYS
# array3 = np.array([[3,2,5],[4,1,7],[8,2,9]])
# split_arrays = np.split(array3,3, axis=1)
# print("Arrays divididos: ")
# for arr in split_arrays:
#     print(arr)

# INDEXACIÓN DE ARRAYS DE ÍNDICES
# array = np.array([4,5,6,8,0,1,2,3,4,5,6,7,8])    
# indices = np.array([0,2,4])
# selected_elements = array[indices]
# print("Elementos seleccionados por índices: ", selected_elements)



# ARCHIVOS
# Cargar datos desde un archivo de texto
# Obtener y mostrar el directorio de trabajo actual
print("Directorio de trabajo actual:", os.getcwd())
# Intentar cargar el archivo
try:
    data = np.loadtxt('palabras.txt')
    print("Datos cargados:")
    print(data)
except FileNotFoundError:
    print("No se encontró el archivo 'palabras.txt'.")

# Guardar datos en un archivo
np.savetxt('datos_guardados.txt', data)
print("Datos guardados en el archivo: 'datos_guardados.txt'")

# Guardar datos en un archivo binario
np.save('datos_guardados.npy', data)
print("Datos guardados en 'datos_guardados.npy'")

# Cargar datos desde un archivo binario
loaded_data = np.load('datos_guardados.npy')
print("Datos cargados desde 'datos_guardados.npy':")
print(loaded_data)
