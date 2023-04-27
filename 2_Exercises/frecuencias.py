def obtenerFrecuencias(frase):

    palabras = frase.split(' ')

    frecuencias = []  
      
    for palabra in palabras:

        palabraEncontrada = False
        for f in frecuencias:
            if f['palabra'] == palabra:
                f['frecuencia'] += 1
                palabraEncontrada = True
                break

        if not palabraEncontrada:
            frecuencias.append({'palabra': palabra, 'frecuencia': 1})

    return frecuencias

def obtenerPalabraMasRepetida(frecuencias):

    palabraMasRepetida = frecuencias[0]
    
    for frecuencia in frecuencias:
        if frecuencia['frecuencia'] > palabraMasRepetida['frecuencia']:
            palabraMasRepetida = frecuencia

    return palabraMasRepetida

frase = input('Introdueix una frase: ')
frecuencias = obtenerFrecuencias(frase)
print('Frecuencias =',frecuencias)
palabraMasRepetida = obtenerPalabraMasRepetida(frecuencias)
print('Palabra mas repetida =',palabraMasRepetida)
