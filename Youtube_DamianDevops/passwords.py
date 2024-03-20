import random
import string
import pyperclip
import colorama
from colorama import Fore, Style
colorama.init()

def generate_password(length):
    while True:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        # verificamos que la contraseña cumple requisitos mínimos
        if any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password):
            return password

length = int(input("Indique la longitud de la contraseña: "))
password = generate_password(length)

print(f"La contraseña generada es: {Fore.GREEN}{password}{Style.RESET_ALL}")

copy_to_clipboard = input("Desea copiar la contraseña en el portapapeles? (s/n)")
if copy_to_clipboard.lower() == "s":
    pyperclip.copy(password)
    print(f"{Fore.GREEN}La contraseña se ha copiado correctamente.{Style.RESET_ALL}")
    print()