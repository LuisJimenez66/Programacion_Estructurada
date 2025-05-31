'''Un modulo es simplemente un archivo con extension py que contiene codigo de python(funciones, clases, 
variables, etc.).

    Un paquete es una carpeta que contiene varios modulos (archivos py) y un archivo especial 
    llamado __init__.py que le indica a Python que esa carpeta debe tratarse como un paquete
'''
import os
def borrar():
    os.system("cls")

def esperar():
    input("..::Oprima cualquier tecla para continuar::..")

def saludar(nombre):
    nombre=nombre
    saludo=f"Hola {nombre}"
    return saludo

#1.- Funcion que no recibe parametros y no regresa valor
def datos1():
    nombre=input("Ingresa el nombre  ");
    telefono=input("Ingresa el telefono  ");
    print(f"La 1.- El nombre es{nombre} y el telefono {telefono}");

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

