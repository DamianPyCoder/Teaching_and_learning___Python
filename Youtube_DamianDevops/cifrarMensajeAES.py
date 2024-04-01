from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def cifrar_mensaje(mensaje, clave):
    cipher = AES.new(clave, AES.MODE_CBC)
    mensaje_cifrado = cipher.encrypt(pad(mensaje.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + mensaje_cifrado)

def descifrar_mensaje(mensaje_cifrado, clave):
    mensaje_cifrado = base64.b64decode(mensaje_cifrado)
    iv = mensaje_cifrado[:AES.block_size]
    cipher = AES.new(clave, AES.MODE_CBC, iv=iv)
    mensaje = unpad(cipher.decrypt(mensaje_cifrado[AES.block_size:]), AES.block_size)
    return mensaje.decode()

def main():
    opcion = input("¿Quieres cifrar o descifrar un mensaje? (cifrar/descifrar): ").lower()

    if opcion == 'cifrar':
        mensaje = input("Introduce el mensaje a cifrar: ")
        clave = get_random_bytes(16)  # Clave de 128 bits (16 bytes)
        mensaje_cifrado = cifrar_mensaje(mensaje, clave)
        print("Mensaje cifrado:", mensaje_cifrado)
        print("Clave utilizada:", clave.hex())
    elif opcion == 'descifrar':
        mensaje_cifrado = input("Introduce el mensaje cifrado: ")
        clave_hex = input("Introduce la clave en formato hexadecimal: ")
        clave = bytes.fromhex(clave_hex)
        mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, clave)
        print("Mensaje descifrado:", mensaje_descifrado)
    else:
        print("Opción no válida. Por favor, elige 'cifrar' o 'descifrar'.")

if __name__ == "__main__":
    main()
