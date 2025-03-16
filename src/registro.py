from src.database import db_manager

import os
import re

def validar_username(username):
    conexion = db_manager.conectar()
    cursor = conexion.cursor()

    # Consulta para verificar si el username existe
    cursor.execute("SELECT EXISTS(SELECT 1 FROM usuarios WHERE username = ?)", (username,))
    existe = cursor.fetchone()[0]

    if existe:
        return True
    else:
        return False
    
def validar_password(password):
    if len(password) < 6:
        return True
    else:
        return False

def validar_email(email):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(patron, email):
        return False
    else:
        return True

def registrar_usuario():
    os.system('cls' if os.name == 'nt' else 'clear')
    db_manager.crear_tabla()
    print("REGISTRO DE USUARIOS")
    username = str(input("Nombre de usuario: "))
    while validar_username(username) == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("REGISTRO DE USUARIOS")
        print(f"El usuario {username} ya esta registrado\ningrese otro nombre de usuario")
        username = str(input("Nombre de usuario: "))

    os.system('cls' if os.name == 'nt' else 'clear')
    print("REGISTRO DE USUARIOS")
    password = str(input("Contraseña: "))
    while validar_password(password) == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("REGISTRO DE USUARIOS")
        print(f"La contraseña debe tener almenos 6 caracteres\ningrese una contraseña válida")
        password = str(input("Contraseña: "))

    os.system('cls' if os.name == 'nt' else 'clear')
    print("REGISTRO DE USUARIOS")
    email = str(input("Email: "))
    while validar_email(email) == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("REGISTRO DE USUARIOS")
        print(f"El correo ({email}) no es válido.\nVerifique que tenga la forma (correo@dominio.com)")
        email = str(input("Email: "))

    os.system('cls' if os.name == 'nt' else 'clear')
    print("REGISTRO DE USUARIOS")
    edad = int(input("Edad: "))
    while edad < 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("REGISTRO DE USUARIOS")
        print(f"La edad {edad} no es válidad\nVerifica que sea un número positivo")
        edad = int(input("Edad: "))
    
    db_manager.registrar_persona(username,password,email,edad)