texto = input('Introduce un texto: ')
vocal = input('Introduce una vocal: ')

texto_modificado = ''
for x in texto:
    if x == vocal:
        x = x.upper() 
    texto_modificado += x

print(texto_modificado)
