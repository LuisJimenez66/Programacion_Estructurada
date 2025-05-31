'''
Es un tipo de dato para una coleccion de valores pero no tinen ni indice ni orde
Set es una coleccion desordenada, inmutable y no indexada. No ha miembros duplicados.


'''
import os
os.system("cls")
personas={"Ramiro","Choche","Lupe"}
print(personas)
personas.add("Choche")
print(personas)
'''personas.discard("Choche")
print(personas)
personas.clear()
print(personas)'''

varios={3.12,3,True,"hola"}
print(varios)
#Ejemplo Crear un programa que solicite los e mail de los alumnos de la 
# UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados
os.system("cls")
opc="SI"
emails=[]
while opc=="SI":
    emails.append(input("Dame el email:  "))
    opc=input("Deseas solicitar otro email? ").upper()
#Imprimir los email sin duplicados

print(emails)

