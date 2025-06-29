'''Una funcion es un conjunto de istrucciones agrupadas bajo un nombre en particular como un programa 
que cumple una funcion especifica. La funcion se puede realizar con el simple hecho de invocarla es 
decir andarla a llamar

Sintaxis:
    def nombredeMifuncion (parametros):
        bloque o conjunto de instrucciones

    nombredeMifuncion(parametros)

    Las funciones pueden ser de 4 tipos:

    Funciones de tipo "Procedimiento"
    1.- Funcion que no recibe parametros y no regresa valor
    3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
    2.- Funcion que no recibe parametros y regresa valor
    4.- Funcion que recibe parametros y regresa valor
    

'''
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

#Convocar las funciones

datos1()

nombre=input("Ingresa el nombre  ");
telefono=input("Ingresa el telefono  ");
datos3(nombre,telefono)

nombre,telefono=datos2()
print(f"El nombre es{nombre} y el telefono {telefono}");



nombre, telefono=datos4(nombre,telefono)
print(f"El nombre es{nombre} y el telefono {telefono}");

