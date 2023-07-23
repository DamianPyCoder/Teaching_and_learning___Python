import random

def adivinar_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("Estoy pensando en un número del 1 al 100. Cual crees que puede ser?")

    while True:
        intento = int(input("Introduce tu número: "))
        intentos += 1

        if intento < numero_secreto:
            print("El número es más alto. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("El número es más bajo. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

if __name__ == "__main__":
    adivinar_el_numero()
