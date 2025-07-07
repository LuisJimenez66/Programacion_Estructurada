#1.- Funcion que no recibe parametros y no regresa valor
import os
pelicula=["Iron Man","Roma","Toy Story"]
def consultar ():
    print(pelicula)
    return pelicula

def agregar ():
    agregar=input("Agrege una pelicula:\n")
    pelicula.append(agregar)

def eliminar ():
    eliminar=int(input("Inserte el numero de la pelicula que desea elminiar\n"))
    pelicula.pop(eliminar)
    return pelicula

def buscar():
    pelicula_buscar=input("Dame la pelicula a buscar")
    for i in range(0,len(pelicula)):
        if pelicula[i]==pelicula_buscar:
            print(f"Si se encontro la pelicula en: {i}")
        else:
            print ("No se encontro la pelicula")
    return         


def limpiar():
    os.system("cls")
        

#3.- Funcion que recibe parametros y no regresa valor
def datos3(nombre,telefono):
    nombre=nombre;
    telefono=telefono;
    print(f"La 3.- El nombre es{nombre} y el telefono {telefono}");

#2.- Funcion que no recibe parametros y regresa valor
def datos2():
    nombre=input("Ingresa el nombre  ");
    telefono=input("Ingresa el telefono  ");
    return nombre, telefono

#4.- Funcion que recibe parametros y regresa valor
def datos4(nombre,telefono):
    nombre=nombre;
    telefono=telefono;
    return nombre, telefono