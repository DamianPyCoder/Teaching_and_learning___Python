def es_matricula_valida(matricula):

    if len(matricula) != 7:
        return False

    numeros = matricula[:4]
    lletres = matricula[4:]

    if not numeros.isdigit():
        return False

    for lletra in lletres:
        if lletra not in 'BCDFGHJKLMNPRSTVXYZ':
            return False
        
    return True

matricula = input('Introdueix la matricula: ')

if es_matricula_valida(matricula):
    print('La matrícula és vàlida')
else:
    print('La matrícula no és vàlida')
