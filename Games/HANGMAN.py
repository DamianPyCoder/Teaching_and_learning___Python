import random

# Lista de palabras
frutas = ["manzana", "banana", "naranja", "sandía", "uva", "kiwi", "mango", "piña", "fresa", "frambuesa"]

while True:
    # Elige una palabra al azar
    palabra = random.choice(frutas)

    # Crea una variable para las letras adivinadas
    adivinado = []

    # Crea una lista para adivinanzas fallidas
    fallidos = []

    # Define el número máximo de intentos permitidos
    intentos_max = 6

    # Mientras el jugador no haya adivinado la palabra y no haya agotado los intentos
    while len(fallidos) < intentos_max and set(palabra) - set(adivinado):

        # Muestra la palabra con las letras adivinadas
        for letra in palabra:
            if letra in adivinado:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        print("\n")

        # Muestra la cantidad de intentos restantes
        print(f"Te quedan {intentos_max - len(fallidos)} intentos.")

        # Pide al jugador que adivine una letra
        letra = input("Adivina una letra: ").lower()

        # Verifica si la letra adivinada es válida y si está en la palabra
        if len(letra) == 1 and letra.isalpha():
            if letra in palabra:
                adivinado.append(letra)
            else:
                fallidos.append(letra)
        else:
            print("Ingresa una letra válida")

        # Muestra las letras adivinadas incorrectamente
        print("Fallidos: ", fallidos)

    # Si el jugador adivina la palabra, muestra un mensaje de victoria. Si no, muestra un mensaje de derrota.
    if set(palabra) <= set(adivinado):
        print("¡Ganaste! La palabra era", palabra)
    else:
        print("¡Perdiste! La palabra era", palabra)

    # Pregunta si el jugador quiere jugar otra vez
    jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ").lower()

    # Si el jugador no quiere jugar de nuevo, sale del bucle while
    if jugar_nuevamente != "s":
        break
