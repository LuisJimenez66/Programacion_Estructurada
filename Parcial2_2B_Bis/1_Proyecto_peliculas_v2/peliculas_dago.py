#1.- Funcion que no recibe parametros y no regresa valor
import os

#Utilizar dict para almacenar los atributos de las peliculas [nombre, Categoria, Clasificacion, Genero, Idioma]
'''
pelicula={
    "nombre": [],
    "categoria": [],
    "clasificacion": [],
    "genero": [],
    "idioma": []

}
'''
pelicula={}
def limpiar():
    os.system("cls")

def esperarTecla():
    input("\n\tTeclee una tecla para continuar")


def CrearPeliculas():

    limpiar()
    print("\t\n\U0001F4DD Alta de peliculas \U0001F4DD")
    pelicula.update({"nombre": input("\U0001F4DD Agrege el nombre:\n").upper().strip()})
    pelicula.update({"categoria": input("\U0001F4DD Agrege la categoria:\n").upper().strip()})
    pelicula.update({"clasificacion": input("\U0001F4DD Agrege la clasificacion:\n").upper().strip()})
    pelicula.update({"genero": input("\U0001F4DD Agrege el genero:\n").upper().strip()})
    pelicula.update({"idioma": input("\U0001F4DD Agrege el idioma:\n").upper().strip()})
    input("\t\n\u2705 La operacion se realizo con exito \u2705")
    esperarTecla()
    
def MostrarPeliculas():
    limpiar()
    print("\n\t\U0001F50DMostrar peliculas \U0001F50D")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"\n\t{i}: {pelicula[i]}")
    else:
        print("\n\t\u26A0 No hay peliculas en el sistema \u26A0")
    esperarTecla()

def BorrarPeliculas():
    limpiar()
    print("\n\t\U0001F4DB Borrar peliculas \U0001F4DB")
    resp=input("\n\tDeseas borrar todas las peliculas del sistema? SI/NO\n").upper()
    if resp=="SI":
        pelicula.clear()
        input("\t\n\u2705 La operacion se realizo con exito \u2705")
    else:
        print("\n\tOk")
    esperarTecla()    

def AgregarCaracteristicasPeliculas():
    limpiar()
    print("\n\t\U0001F4DD Agregar caracteristicas a las peliculas \U0001F4DD")
    if len(pelicula)>0:
        atributo=input("\n\t\U0001F4DD Ingrese la caracteristica que desea agregar: ").lower().strip()
        valor=input(f"\n\t \U0001F4DD Ingrese el valor de la caracteristica: ").upper().strip()
        pelicula.update({atributo: valor})
        input("\t\n\u2705 La operacion se realizo con exito \u2705")
    else:
        print("\n\t\u26A0 No hay peliculas en el sistema \u26A0")
    esperarTecla()

def BorrarCaracteristicasPeliculas():
    limpiar()
    print("\n\t\U0001F4DB Borrar caracteristicas de las peliculas \U0001F4DB")
    if len(pelicula) > 0:
        print("\n\tValores actuales: ")
        for i in pelicula:
            print(f"\n\t{i}: {pelicula[i]}")
        respuesta = input("\n\tDesea borrar una caracteristica? SI/NO\n").upper().strip()
        if respuesta == "SI":    
            atributo = input("\n\t\U0001F4DD Ingrese la caracteristica que desea borrar: ").upper().strip()
        if atributo in pelicula:
            pelicula.pop(atributo)
            input("\t\n\u2705 La operacion se realizo con exito \u2705")
        else:
            print("\n\t\u26A0 La caracteristica no existe \u26A0")
    else:
        print("\n\t\u26A0 No hay peliculas en el sistema \u26A0")

def ModificarCaracteristicasPeliculas():
    limpiar()
    print("\n\t\U0001F501 Modificar caracteristicas de las peliculas \U0001F501")
    if len(pelicula) > 0:
        print("\n\tValores actuales: ")
        for i in pelicula:
            print(f"\n\t{i}: {pelicula[i]}")
            respuesta = input(f"\n\tDesea cambiar el valor de {i}? SI/NO\n").upper().strip()
            if respuesta == "SI":
                pelicula.update({f"{i}": input(f"\n\t\U0001F4DD Ingrese el nuevo valor: ").upper().strip()})
        input("\t\n\u2705 La operacion se realizo con exito \u2705")
        esperarTecla()
        limpiar()
    else:
        print("\n\\u26A0 tNo hay peliculas en el sistema \u26A0")
'''
def ModificarCaracteristicasPeliculas():
    limpiar()
    print("\n\tModificar caracteristicas de las peliculas")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"\n\t{i}: {pelicula[i]}")
        caracteristica=input("\n\tIngrese la caracteristica que desea modificar: ").upper().strip()
        if caracteristica in pelicula:
            valor=input(f"\n\tIngrese el nuevo valor de la caracteristica {caracteristica}: ").upper().strip()
            pelicula.update({caracteristica: valor})
            input("\t\nLa operacion se realizo con exito")
        else:
            print("\n\tLa caracteristica no existe")
    else:
        print("\n\tNo hay peliculas en el sistema")
    esperarTecla()

def BorrarCaracteristicasPeliculas():
    limpiar()
    print("\n\tBorrar caracteristicas de las peliculas")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"\n\t{i}: {pelicula[i]}")
        atributo=input("\n\tIngrese la caracteristica que desea borrar: ").upper().strip()
        if atributo in pelicula:
            pelicula.pop(atributo)
            input("\t\nLa operacion se realizo con exito")
        else:
            print("\n\tLa caracteristica no existe")
    else:
        print("\n\tNo hay peliculas en el sistema")
    esperarTecla()            
'''

