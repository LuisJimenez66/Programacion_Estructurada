import os
import platform

def borrarPantalla(): 
   sistema_operativo = platform.system()
   if sistema_operativo == "Windows":
      os.system('cls')
   else:
      os.system('clear')

def esperarTecla():
  input("\n\t\t ... ⚠️ Oprima enter para continuar ⚠️ ...")

def menu_usurios():
   borrarPantalla()
   print("\n \t..::☕ Bienvenido a cafetería ☕::..\n\t\t1.-  Registro  \n\t\t2.-  Login \n\t\t3.- Salir ")
   opcion=input("\t\t Elige una opción: ").upper().strip() 
   return opcion

def menu_admin():
   borrarPantalla()
   print("\n \t .::  ADMIN ::. \n\t1.- Administrar Comida \n\t2.- Administrar Bebidas\n\t3.- Administrar usuarios\n\t4.- Administrar ordenes\n\t5.- Salir """)
   opcion = int(input("\t\t Elige una opción: "))
   return opcion   

def menu_clientes():
   borrarPantalla()
   print("\n \t .::  Pedir orden ::. \n\t1.- Ordenar Comida \n\t2.- Ordenar Bebidas \n\t3.- Realizar pedido \n\t4.- Salir")
   opcion = int(input("\t\t Elige una opción: "))
   return opcion   

