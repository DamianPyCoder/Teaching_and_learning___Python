import numpy as np

# BROADCASTING
# array1 = np.array([[1,2,3],[4,5,6]])
# array2 = np.array([22,16,10])
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
array = np.array([4,5,6,8,0,1,2,3,4,5,6,7,8])    
indices = np.array([0,2,4])
selected_elements = array[indices]
print("Elementos seleccionados por índices: ", selected_elements)