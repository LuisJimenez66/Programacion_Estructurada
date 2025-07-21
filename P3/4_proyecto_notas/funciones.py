def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t\t ..:: Oprima Cualquier tecla para continuar::..")   

def menu_Principal():
    print("\n\t\t\tSISTEMA DE GESTION DE NOTAS")
    print(f"\n\t\t\t\U0001F50D Selecciona una opcion: \n\t\t1\ufe0f\u20e3  Registro\n\t\t2\ufe0f\u20e3  Login"
                 "\n\t\t3\ufe0f\u20e3  Salir\n ")
    opcion=input("Selecciona una opcion: ") .upper()
    return opcion
