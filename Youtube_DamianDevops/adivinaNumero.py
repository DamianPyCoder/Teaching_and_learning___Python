import random

def adivinar_el_numero():
    numero_secreto = random.randint(1,100)
    intentos = 0

    print("Estoy pensando en un número del 1 al 100, cual crees que podría ser?")

    while True:
        intento = int(input("Introduce tu número: "))
        intentos +=1

        if intento < numero_secreto:
            print("El número es más ALTO, sigue intentándolo.")
        elif intento > numero_secreto:
            print("El número es más BAJO, sigue intentándolo.")
        else:
            print(f"Felicidades, adivinaste el número en {intentos} intentos.")
            break

if __name__ == "__main__":
    adivinar_el_numero()
