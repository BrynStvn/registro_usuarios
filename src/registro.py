from src.data import usuarios, ver_usuarios

import os
import re

def validar_username(username):
    if username in usuarios['username']:
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
    
    usuarios['username'].append(username)
    usuarios['password'].append(password)
    usuarios['email'].append(email)
    usuarios['edad'].append(edad)