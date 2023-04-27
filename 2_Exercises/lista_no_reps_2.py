valores1 = input("Entra una lista de valores separados por comas: ")
lista1 = valores1.split(',')

valores2 = input("Entre una lista de valores separados por comas: ")
lista2 = valores2.split(',')

for x in lista1:
    if x not in lista2:
        lista2.append(x)

print("Llista sense duplicats:",lista2)

lista2.sort()
print("Llista ordenada:",lista2)
lista2.reverse()
print("Llista invertida:",lista2)