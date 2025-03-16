from src.database import db_manager

import os
import pandas as pd

def ver_usuarios():
    from src.registro import registrar_usuario
    from src.menu import mostrar_menu, salir
    
    os.system('cls' if os.name == 'nt' else 'clear')

    tabla = {'ID':[],
             'username':[],
             'password':[],
             'email':[],
             'edad':[]}

    usuarios = db_manager.mostrar_personas()

    for usuario in usuarios:
        i = 0
        for clave in tabla.keys():
            tabla[clave].append(usuario[i])
            i += 1

    menu = {'1':registrar_usuario,'2':mostrar_menu,'3':salir}
    tabla_usuarios = pd.DataFrame(tabla)
    print("LISTA DE USUARIOS REGISTRADOS")
    print(tabla_usuarios)

    print("\n1. Registrar nuevo usuario\n2. Menú\n3. Salir")
    op = input("\nSeleccione una opción: ")

    accion = menu.get(op)

    if accion:
        accion()
    else:
        print("Opción no válida")