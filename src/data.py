import os
import pandas as pd

usuarios = {'username':[],
            'password':[],
            'email':[],
            'edad':[]}

def ver_usuarios():
    from src.registro import registrar_usuario
    from src.menu import mostrar_menu, salir
    
    os.system('cls' if os.name == 'nt' else 'clear')
    menu = {'1':registrar_usuario,'2':mostrar_menu,'3':salir}
    tabla_usuarios = pd.DataFrame(usuarios)
    print("LISTA DE USUARIOS REGISTRADOS")
    print(tabla_usuarios)

    print("\n1. Registrar nuevo usuario\n2. Menú\n3. Salir")
    op = input("\nSeleccione una opción: ")

    accion = menu.get(op)

    if accion:
        accion()
    else:
        print("Opción no válida")