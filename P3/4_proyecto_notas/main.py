

import funciones
import conexionBD

def main():
   respuesta=True
   while True:
        funciones.borrarPantalla()
        opcion=funciones.menu_Principal()

        if opcion=="1" or opcion=="REGISTRO":
            print("Registro")
        elif opcion=="2" or opcion=="LOGIN":
            print("Login")
        elif opcion=="3" or opcion=="SALIR":
            print("Saldra")  
            funciones.esperarTecla()
            respuesta=False
        else:
            print("Opcion invalida") 
            funciones.esperarTecla()         

if __name__=="__main__":
    main()




