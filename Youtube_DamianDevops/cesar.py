def cifrar(texto, clave):
    resultado =''
    for letra in texto:
        if letra.isalpha():
            if letra.isupper():
                resultado += chr((ord(letra) + clave - 65) % 26 + 65)
            else:
                resultado += chr((ord(letra) + clave - 97) % 26 + 97)
        else:
            resultado += letra
    return resultado

def descifrar(texto, clave):
    return cifrar(texto, -clave)

def main():
    opcion = input("Quieres codificar o descodificar (c/d): ").lower()

    if opcion == 'c':
        texto = input("Introduce un texto para codificar: ")
        clave = int(input("Introduce la clave de cifrado: "))
        texto_codificado = cifrar(texto, clave)
        print("Texto codificado: ", texto_codificado)
    elif opcion == 'd':
        texto = input("Introduce un texto para descodificar: ")
        clave = int(input("Introduce la clave de cifrado: "))
        texto_descodificado = descifrar(texto, clave)
        print("Texto descodificado: ", texto_descodificado)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()