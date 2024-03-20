import sqlite3
from termcolor import colored

# crear conexión bbdd
conn = sqlite3.connect('datos.db')
cursor = conn.cursor()

# crear tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, edad INTEGER NOT NULL, email TEXT NOT NULL)''')
conn.commit()

#Funciones de control
def validar_edad(edad):
    try:
        edad = int(edad)
        if 1 <= edad <= 99:
            return True
        else:
            return False
    except ValueError:
        return False

def validar_email(email):
    if email.count('@') == 1 and email.count('.') == 1:
        return True
    else:
        return False

def validar_nombre(nombre):
    if not any(char.isdigit() for char in nombre):
        return True
    else:
        return False
    
# Funciones CRUD
def crear_usuario(nombre, edad, email):
    if validar_nombre(nombre) and validar_edad(edad) and validar_email(email):
        cursor.execute('''INSERT INTO usuarios (nombre, edad, email) VALUES (?,?,?)''', (nombre, edad, email))
        conn.commit()
        print(colored("Usuario creado correctamente", "green"))
    else:
        print(colored("Error: Por favor compruebe los datos ingresados.","red"))

def mostrar_usuarios():
    cursor.execute('''SELECT * FROM usuarios''')
    usuarios = cursor.fetchall()
    if not usuarios:
        print(colored("No hay usuarios registrados en la base de datos","yellow"))
    else:
        for usuario in usuarios:
            print(usuario)
def actualizar_usuario(id, nombre, edad, email):
    if validar_nombre(nombre) and validar_edad(edad) and validar_email(email):
        cursor.execute('''UPDATE usuarios SET nombre=?, edad=?, email=? WHERE id=?''', (nombre, edad, email, id))
        conn.commit()
        print(colored("Usuario creado exitosamente","green"))
    else:
        print(colored("Error al introducir los datos", "red"))

def eliminar_usuario(id):
    cursor.execute('''DELETE FROM usuarios WHERE id=?''', (id,))
    conn.commit()
    print(colored("Usuario eliminado exitosamente","green"))

def borrar_todos_los_usuarios():
    cursor.execute('''DELETE FROM usuarios''')
    conn.commit()
    print(colored("Todos los usuarios han sido eliminados","green"))

#Menu
def menu():
    while True:
        print(colored("\n--- MENU ---","cyan"))
        print("1. Crear usuario")
        print("2. Mostrar usuario")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Borrar todos los usuarios")
        print("6. Salir")

        opcion = input(colored("Selecciona una opción","cyan"))

        if opcion == '1':
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            email = input("Email: ")
            crear_usuario(nombre, edad, email)
        elif opcion == '2':
            mostrar_usuarios()
        elif opcion =='3':
            id = int(input("ID del usuario a actualizar: "))
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            email = input("Email: ")
            actualizar_usuario(id,nombre,edad,email)
        elif opcion =='4':
            id = int(input("ID del usuario a eliminar: "))
            eliminar_usuario(id)
        elif opcion =='5':
            borrar_todos_los_usuarios()
        elif opcion =='6':
            print(colored("Saliendo!!","yellow"))
            break
        else:
            print(colored("Opción no valida","red"))

#Ejecutar programa y cerrar conexión
if __name__ == '__main__':
    menu()

conn.close()


