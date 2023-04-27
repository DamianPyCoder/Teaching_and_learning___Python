def contador_vocales(texto):
    contador = 0

    for caracter in texto:
        if caracter in 'aeiouAEIOUáéíóúüÁÉÍÓÚÜ':
            contador += 1
            
    return contador

texto = input('Introduce un texto: ')
print('El texto introducido contiene ' + str(contador_vocales(texto)) + ' vocales')
