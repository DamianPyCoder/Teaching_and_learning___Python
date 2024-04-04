lista = [5, 6, 2, 9, 0, 1, 4, 7, 3, 8]
n = len(lista)

for i in range(n):
    for j in range(0, n-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1]=lista[j+1],lista[j]

print("Lista ordenada: ", lista)