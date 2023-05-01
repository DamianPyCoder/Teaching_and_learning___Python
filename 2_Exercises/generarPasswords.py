#    La función generate_password toma un argumento length que indica la longitud deseada de la contraseña.

#    En el ciclo while, se genera una cadena aleatoria de caracteres alfanuméricos de longitud length utilizando la función random.choices.

#    La condición if verifica si la contraseña generada contiene al menos una letra mayúscula, una letra minúscula y un número. Si es así, la contraseña se devuelve como resultado. De lo contrario, se generará una nueva contraseña hasta que se cumpla la condición.

#    En el programa principal, se pide al usuario que ingrese la longitud deseada de la contraseña y se llama a la función generate_password para generar una contraseña aleatoria que se muestra en la pantalla.

#    Se pregunta al usuario si desea copiar la contraseña al portapapeles. Si la respuesta es "s", la contraseña se copia al portapapeles utilizando pyperclip.copy() y se muestra un mensaje en la pantalla indicando que la contraseña se ha copiado.
#    En caso de no estar instalado hacerlo con el comando pip install pyperclip



import random
import string
import pyperclip
import colorama
from colorama import Fore, Style

colorama.init()

def generate_password(length):
    while True:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password):
            return password

length = int(input(" ¿Cuántos caracteres debe tener la contraseña? "))
password = generate_password(length)
print(f" La contraseña aleatoria generada es: {Fore.GREEN}{password}{Style.RESET_ALL}")
print()
copy_to_clipboard = input(" ¿Desea copiar la contraseña al portapapeles? (s/n): ")
if copy_to_clipboard.lower() == "s":
    pyperclip.copy(password)
    print(f"{Fore.GREEN} La contraseña se ha copiado al portapapeles.{Style.RESET_ALL}")
    print()
