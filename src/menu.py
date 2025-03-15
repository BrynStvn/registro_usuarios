from src.registro import registrar_usuario
from src.data import ver_usuarios

import os

def mostrar_menu():
    menu = {'1':registrar_usuario,'2':ver_usuarios,'3':salir}

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("MENÚ")
        print("\n1. Registrar nuevo usuario\n2. Ver usuarios registrados\n3. Salir")
        
        op = input("\nSeleccione una opción: ")

        accion = menu.get(op)

        if accion:
            accion()
        else:
            print("Opción no válida")

def salir():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("¡Hasta luego!")
    exit()