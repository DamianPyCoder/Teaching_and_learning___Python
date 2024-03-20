import os
import random
from colorama import init, Fore

# Inicializar colorama para permitir el coloreado del texto
init(autoreset=True)

def seleccionar_palabra():
    with open("palabras.txt", "r") as f:
        palabras = f.readlines()
    return random.choice(palabras).strip().lower()

def mostrar_palabra_oculta(palabra, letras_adivinadas):
    oculto = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            oculto += letra + " "
        else:
            oculto += "_ "
    return oculto

def mostrar_estado_juego(palabra, letras_adivinadas, vidas, letras_usadas):
    palabra_oculta = mostrar_palabra_oculta(palabra, letras_adivinadas)
    print("Palabra: " + palabra_oculta)
    print("Vidas: " + str(vidas))

    print("Letras usadas:", end=" ")
    for letra in "abcdefghijklmnopqrstuvwxyz":
        if letra in letras_usadas:
            if letra in palabra:
                print(Fore.GREEN + letra, end=" ")
            else:
                print(Fore.RED + letra, end=" ")
        else:
            print(letra, end=" ")
    print()

def jugar():
    palabra = seleccionar_palabra()
    letras_adivinadas = set()
    vidas = 7
    letras_usadas = set()

    print("¡Bienvenido al juego del ahorcado!")
    while True:
        mostrar_estado_juego(palabra, letras_adivinadas, vidas, letras_usadas)
        if "_" not in mostrar_palabra_oculta(palabra, letras_adivinadas):
            print("¡Felicidades, has ganado!")
            break
        if vidas == 0:
            print("¡Has perdido! La palabra era:", palabra)
            break

        letra = input("Introduce una letra: ").lower()
        letras_usadas.add(letra)
        if letra in palabra:
            letras_adivinadas.add(letra)
        else:
            vidas -= 1
        
        # Limpiar la pantalla después de que el usuario introduzca una letra
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    jugar()
