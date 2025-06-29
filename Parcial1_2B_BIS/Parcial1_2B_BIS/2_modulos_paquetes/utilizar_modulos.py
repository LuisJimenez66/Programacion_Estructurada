
import modulos
modulos.borrar()
#Primer forma de utilizar modulos
nombre=input("Ingresa tu nombre: \n")
print(modulos.saludar(nombre))
modulos.esperar()
#Segunda forma de utilizar modulos
from modulos import saludar,borrar,esperar,datos4
borrar()
nombre=input("Ingresa tu nombre: \n")
print(saludar(nombre))
esperar()
borrar()
nombre2=input("Ingresa tu nombre: \n")
Telefono=input("Ingresa tu telefono: \n")
nom,tel=datos4(nombre2,Telefono)

print(f"\tnombre: {nom}\n \ttelefono: {tel}")