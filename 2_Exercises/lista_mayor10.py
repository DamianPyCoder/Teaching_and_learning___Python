valores = input("Entra una lista de valores separados por comas: ")

lista = valores.split(',')

lista2 = []
lista3 = []
for x in lista:
    if int(x) > 10:
        lista3.append(x)
    else:
       lista2.append(x)

print("Lista sin mayores de 10: ", lista2)
print("Lista con mayores de 10: ", lista3)