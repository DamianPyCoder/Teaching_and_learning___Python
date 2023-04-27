def listConvert2float(list):
    list_float = []
    for x in lista:
        list_float.append(float(x))
    return list_float

def calculaMedia(lista):
    
    suma = 0.0
    for i in range(len(lista)):
        suma += lista[i]
    
    return round(suma / len(lista), 2)


valores = input("Entra una llista d'alçades separades por comas: ")

lista = valores.split(',')

lista_float = listConvert2float(lista)

print("Llista d'alçades:",lista_float)

media = calculaMedia(lista_float)

contador_altos = 0
contador_bajos = 0
for x in lista_float:
    if x >= media:
        contador_altos += 1
    else:
        contador_bajos += 1

print("Mitja =",media)
print("Persones més altes que la mitja:",contador_altos)
print("Persones més baixes que la mitja:",contador_bajos)

