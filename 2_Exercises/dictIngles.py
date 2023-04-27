#en:in,un:a,de:of,la:the,lugar:place 

def traducir_palabra(palabra, dict):
    palabra_traducida = ''
    for entrada in dict:
        if entrada['sp'] == palabra:
            palabra_traducida = entrada['en']
            break
    
    if palabra_traducida == '':
        palabra_traducida = palabra
    
    return palabra_traducida

def traducir(frase, dict):
    traduccion = ''
    palabras = frase.split(' ')
    for p in palabras:
        palabra_traducida = traducir_palabra(p.lower(), dict)
        if palabra_traducida != '':
            if p[0].isupper():
                palabra_traducida = palabra_traducida.capitalize()
            traduccion += palabra_traducida + ' '
        else:
            traduccion += p + ' '
    return traduccion

dict_text = input('Intoduiu les paraules del diccionari: ')
dict_list = dict_text.split(',')
dict_trad = []

for p in dict_list:
    tokens = p.split(':')
    dict_trad.append({'sp': tokens[0], 'en': tokens[1]})

frase = input('Introduiu la frase a traduir: ')

print('Frase traducida:',traducir(frase, dict_trad))
