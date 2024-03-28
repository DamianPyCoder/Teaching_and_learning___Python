def obtenerFrecuencias(frase):
    palabras = frase.split(' ')
    frecuencias = []

    for palabra in palabras:
        palabraEncontrada = False
        for f in frecuencias:
            if f['palabra'] == palabra:
                f['frecuencia'] +=1
                palabraEncontrada = True
                break
        if not palabraEncontrada:
            frecuencias.append({'palabra':palabra, 'frecuencia':1})
        
    frecuencias.sort(key=lambda x: x['frecuencia'], reverse=True)

    return frecuencias

def obtenerPalbrasMasRepetidas(freciencias):
    max_freciencia = max(frecuencia['frecuencia'] for frecuencia in frecuencias)
    palabras_mas_repetidas = [frecuencia['palabra'] for frecuencia in freciencias if frecuencia['frecuencia'] == max_freciencia]
    return palabras_mas_repetidas

frase = input('Introduce una frase:')
frecuencias = obtenerFrecuencias(frase)
print('Frecuencias:')
for item in frecuencias:
    print(item['palabra'], '-', item['frecuencia'])
palabras_mas_repetidas = obtenerPalbrasMasRepetidas(frecuencias)
print('Palabra más repetidas:',', '.join(palabras_mas_repetidas))