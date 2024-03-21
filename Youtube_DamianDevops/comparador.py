import time
from array import array

def test_speed(data_structure, operation):
    start_time = time.time()
    if operation == "create":
        if isinstance(data_structure, tuple):
            data_structure = tuple(range(1000000))
        elif isinstance(data_structure, list):
            data_structure = list(range(1000000))
        elif isinstance(data_structure, dict):
            data_structure = dict.fromkeys(range(1000000))
        elif isinstance(data_structure, array):
            data_structure.extend(range(1000000))
    elif operation == "insert":
        for i in range(1000000):
            data_structure.append(i)
    elif operation == "search":
        for i in range(100):
            _ = i in data_structure
    elif operation == "delete":
        if isinstance(data_structure, list):
            data_structure.clear()
        elif isinstance(data_structure, array):
            for i in range(1000000):
                data_structure.remove(i)
    end_time = time.time()
    return end_time - start_time

# Test de creación
print("Tiempo de creación:")
print("Tupla:", test_speed(tuple(), "create"))
print("Lista:", test_speed([], "create"))
print("Diccionario:", test_speed({}, "create"))
print("Array:", test_speed(array('i'), "create"))

# Test de inserción
print("\nTiempo de inserción:")
print("Lista:", test_speed([], "insert"))
print("Array:", test_speed(array('i'), "insert"))

# Test de búsqueda
print("\nTiempo de búsqueda:")
print("Tupla:", test_speed(tuple(range(1000000)), "search"))
print("Lista:", test_speed(list(range(1000000)), "search"))
print("Diccionario:", test_speed(dict.fromkeys(range(1000000)), "search"))
print("Array:", test_speed(array('i', range(1000000)), "search"))

# Test de eliminación
print("\nTiempo de eliminación:")
print("Lista:", test_speed(list(range(1000000)), "delete"))
print("Array:", test_speed(array('i', range(1000000)), "delete"))
