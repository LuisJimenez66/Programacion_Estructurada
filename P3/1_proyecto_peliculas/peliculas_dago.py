#1.- Funcion que no recibe parametros y no regresa valor
import os
import mysql.connector
from mysql.connector import Error
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
  import os  
  os.system("cls")

def esperarTecla():
  print(" 🕒 Oprima cualquier tecla para continuar 🕒 ...")
  input()  

def conectar():
  try:
    conexion=mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="",
      database="bd_peliculas"
    )
    return conexion
  except Error as e:
    print(f"El error que sucedio es: {e}")
    return None


def CrearPeliculas():
    conexionBD=conectar()
    if conexionBD!=None:
        limpiar()
        print("\t\t\n\U0001F4DD Alta de peliculas \U0001F4DD")
        pelicula.update({"nombre": input("\t\U0001F4DD Agrege el nombre: ").upper().strip()})
        pelicula.update({"categoria": input("\t\U0001F4DD Agrege la categoria: ").upper().strip()})
        pelicula.update({"clasificacion": input("\t\U0001F4DD Agrege la clasificacion: ").upper().strip()})
        pelicula.update({"genero": input("\t\U0001F4DD Agrege el genero: ").upper().strip()})
        pelicula.update({"idioma": input("\t\U0001F4DD Agrege el idioma:").upper().strip()})

        ###AGREGAR PELICULA A LA BASE DE DATOS
        try:
            cursor = conexionBD.cursor()
            cursor.execute("INSERT INTO peliculas (id, nombre, categoria, clasificacion, genero, idioma) VALUES (NULL, %s, %s, %s, %s, %s)"
            , (pelicula ["nombre"], pelicula["categoria"], pelicula["clasificacion"], pelicula["genero"], pelicula["idioma"]))
            conexionBD.commit()
            print("\t\t.:: ✅ Operacion realizada con exito ✅ ::.")
        except Error as e:
           print("Error al intentar guardar registro en Base de Datos")    
        
   


    

      

    
def MostrarPeliculas():
    conexionBD=conectar()
    if conexionBD!=None:
        limpiar()
        print("\n\t\t.:: 🔍 Mostrar o consultar la pelicula 🔍 ::.\n ")
        cursor=conexionBD.cursor()
        cursor.execute(
            "select * from peliculas"
        )
        registros=cursor.fetchall()
        if registros:
            print("\n\tTabla de peliculas: \U0001F4BE\n")
            print(f"{"ID":<10}{"Nombre":<15}{"Categoria":<15}{"Clasificacion":<15}{"Genero":<15}{"Idioma":<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
            print(f"-"*80)    
        else:
            print("\t .:: ⚠ No hay peliculas en el sistema ⚠::.")

def BorrarPeliculas():
    conexionBD=conectar()
    if conexionBD!=None:
        limpiar()
        print("\n\t\t.:: \U0001F4DB Borrar peliculas \U0001F4DB ::.\n ")
        cursor=conexionBD.cursor()
        buscar=int(input("\t\U0001F4DDIngresa el Id de la pelicula a buscar: "))
        cursor.execute(
            "Select * from peliculas where id=%s",(buscar,)
        )
        registros=cursor.fetchall()
        if registros:
            print("\n\tTabla de peliculas: \U0001F4BE\n")
            print(f"{"ID":<10}{"Nombre":<15}{"Categoria":<15}{"Clasificacion":<15}{"Genero":<15}{"Idioma":<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
            print(f"-"*80)
            borrar=input("DESEA BORRAR ESTA PELICULA? (si/no) ").lower()
            if borrar=="si":
                cursor.execute(
                "delete from peliculas where id=%s",(buscar,)
                )
                conexionBD.commit()
                print("\tPelicula borrada correctamente \U0001F4DB")
            else:
                print("No borro nada")    
           
        else:
            print("\t .:: ⚠ No esta esa pelicula en el sistema ⚠::.")


def ModificarPeliculas():
    conexionBD=conectar()
    if conexionBD!=None:
        limpiar()
        print("\n\t\t.:: 🔄 Modificar peliculas 🔄 ::.\n ")
        cursor=conexionBD.cursor()
        buscar=input("\t\U0001F4DDIngresa el nombre de la pelicula a buscar: ")
        cursor.execute(
            "Select * from peliculas where nombre=%s",(buscar,)
        )
        registros=cursor.fetchall()
        if registros:
            print("\n\tTabla de peliculas: \U0001F4BE\n")
            print(f"{"ID":<10}{"Nombre":<15}{"Categoria":<15}{"Clasificacion":<15}{"Genero":<15}{"Idioma":<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
            print(f"-"*80)
            Modificar=input("DESEA Modificar ESTA PELICULA? (si/no) ").lower()
            if Modificar=="si":
                pelicula.update({"nombre": input("\t\U0001F4DD Agrege el nombre: ").upper().strip()})
                pelicula.update({"categoria": input("\t\U0001F4DD Agrege la categoria: ").upper().strip()})
                pelicula.update({"clasificacion": input("\t\U0001F4DD Agrege la clasificacion: ").upper().strip()})
                pelicula.update({"genero": input("\t\U0001F4DD Agrege el genero: ").upper().strip()})
                pelicula.update({"idioma": input("\t\U0001F4DD Agrege el idioma:").upper().strip()})

                ###AGREGAR PELICULA A LA BASE DE DATOS
                try:
                    cursor = conexionBD.cursor()
                    cursor.execute("update peliculas set nombre=%s, categoria=%s, clasificacion=%s, genero=%s, idioma=%s where nombre=%s"
                    , (pelicula ["nombre"], pelicula["categoria"], pelicula["clasificacion"], pelicula["genero"], pelicula["idioma"],buscar,))
                    conexionBD.commit()
                    print("\t\t.:: ✅ Operacion realizada con exito ✅ ::.")
                except Error as e:
                    print("Error al intentar guardar registro en Base de Datos")
                    print("\tPelicula Modificada correctamente 🔄")
            else:
                print("No modifico nada")    
           
        else:
            print("\t .:: ⚠ No esta esa pelicula en el sistema ⚠::.")




def BuscarPeliculas():
    conexionBD=conectar()
    if conexionBD!=None:
        limpiar()
        print("\n\t\t.:: 🔍 Mostrar o consultar la pelicula 🔍 ::.\n ")
        cursor=conexionBD.cursor()
        buscar=input("\t\U0001F4DDIngresa el nombre de la pelicula a buscar: ")
        cursor.execute(
            "select * from peliculas where nombre=%s",(buscar,)
        )
        registros=cursor.fetchall()
        if registros:
            print("\n\tTabla de peliculas: \U0001F4BE\n")
            print(f"{"ID":<10}{"Nombre":<15}{"Categoria":<15}{"Clasificacion":<15}{"Genero":<15}{"Idioma":<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
            print(f"-"*80)    
        else:
            print("\t .:: ⚠ No esta esa pelicula en el sistema ⚠::.")
        

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

def ModificarPeliculas():
    limpiar()
    print("\n\t.:: 🔄 Modificar pelicula 🔄 ::.\n ")
    conexion=conectar()
    cursor=conexion.cursor()
    cursor.execute(
        "select id, nombre from peliculas"
    )
    registros=cursor.fetchall()
    if registros:
        for i in registros:
          print(f"{i[0]} {i[1]}")
    else:
      print(" ⚠ No hay registros ⚠ ")
    if conexion:
        id=int(input("Teclea el id de la pelicula que quieras modificar: "))
        nombre = input("Nuevo nombre: ").upper().strip()
        categoria = input("Nueva categoría: ").upper().strip()
        clasificacion = input("Nueva clasificación: ").upper().strip()
        genero = input("Nuevo género: ").upper().strip()
        idioma = input("Nuevo idioma: ").upper().strip()
        cursor.execute(
        "update peliculas set nombre=%s, categoria=%s, clasificacion=%s, genero=%s, idioma=%s where id=%s",(nombre,categoria,clasificacion,genero,idioma,id)
        )
        conexion.commit()
    else:
        print("⚠ No se pudo conectar con la base de datos ⚠")
'''
