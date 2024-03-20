def calcular_letra_dni(numero):
    letras="TRWAGMYFPDXBNJZSQVHLCKE"
    indice_letra = numero % 23
    letra_dni = letras[indice_letra]
    return letra_dni

def main():
    numero_dni = int(input("Introduce los 8 dígitos del DNI sin la letra: "))
    letra_dni=calcular_letra_dni(numero_dni)
    print("La letra del DNI es: ",letra_dni)

if __name__=="__main__":
    main()