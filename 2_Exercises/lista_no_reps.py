def borraDuplicados(data):
    result = []
    for item in data:
        if item not in result:
            result.append(item)
    return result

valores1 = input("Entra una lista de valores separados por comas: ")
lista1 = valores1.split(',')

valores2 = input("Entre una lista de valores separados por comas: ")
lista2 = valores2.split(',')

lista3 = borraDuplicados(lista1 + lista2)

print("Llista sense duplicats:",lista3)

lista4 = lista3.copy()
lista4.sort()
print("Llista ordenada:",lista4)
lista4.reverse()
print("Llista invertida:",lista4)