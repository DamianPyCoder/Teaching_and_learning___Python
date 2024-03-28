def contador_vocales(texto):
    contador = 0
    texto = texto.lower()
    for caracter in texto:
        if caracter in 'aeiouáéíóúü':
            contador +=1

    return contador

print("Introduce un texto:")
texto = input("")
print('El texto introducido contiene '+str(contador_vocales(texto)) + ' vocales')