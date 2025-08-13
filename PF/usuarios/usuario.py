import datetime
from conexionBD import *
import hashlib
import funciones
import getpass

def registrar (usuario, password):
    try:
        password=hashlib.sha256(password.encode()).hexdigest()
        cursor.execute(
            "INSERT INTO usuarios (usuario, contrasena) VALUES (%s, %s)", (usuario, password)
        )
        conexion.commit()
        return True
    except:
        print("Error") 
        return False
    
def iniciar_sesion(usuario,password):
    try:
        password=hashlib.sha256(password.encode()).hexdigest()
        cursor.execute(
            "select * from usuarios where usuario=%s and contrasena=%s", (usuario, password)
        )
        registros=cursor.fetchone()
        if registros:
            input("Sesion iniciada correctamente")
            return registros
        else:
            return None
    except:
        print("Error")
        return None    
    
def modificar(buscar):
    try:
        
        cursor.execute("Select * from usuarios where id=%s",(buscar,))
        registros=cursor.fetchall()
        if registros:
            funciones.borrarPantalla()
            print("\n\tUsuario: \n")
            print(f"{"ID":<10}{"Nombre":<15}")
            print(f"-"*40)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<30}")
            print(f"-"*40)   
            seguro=input("Seguro de modificar este registro? (si/no) ").lower().strip()
            if seguro=="si":
                user=input("\t\U0001F464 Ingresa tu usuario: ").upper().strip()
                password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
                password=hashlib.sha256(password.encode()).hexdigest()
                cursor.execute(
                    "UPDATE usuarios SET usuario=%s, contrasena=%s WHERE id=%s",
                    (user, password, buscar)
                )
                conexion.commit()
                return True
            else:    
                print("No Modifico nada")
                return False
        else:  
            print("\u26A0 No existe esta usuario \u26A0")
            return False
    except:
        print("Error") 
        return False
    

def mostrar ():
    try:
        cursor.execute("Select * from usuarios")
        return cursor.fetchall()
    except:
        return False    

def buscar(buscar):
    try:
        cursor.execute("Select * from  usuarios where usuario=%s",(buscar,))
        return cursor.fetchall()
    except:
        return False 
    
def buscar2(buscar):
    try:
        cursor.execute("Select * from  usuarios where usuario=%s",(buscar,))
        return True
    except:
        return False     
def borrar (buscar,):
    try:
        cursor.execute("Select * from usuarios where id=%s",(buscar,))
        registros=cursor.fetchall()
        if registros:
            funciones.borrarPantalla()
            print("\n\t\U0001F4DB Usuario: \n")
            print(f"{"ID":<10}{"Nombre":<15}")
            print(f"-"*40)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<30}")
            print(f"-"*40)   
            seguro=input("Seguro de borrar este registro? (si/no) ").lower().strip()
            if seguro=="si":
                cursor.execute("delete from usuarios where id=%s",(buscar,))
                conexion.commit()
                return True
            else:    
                print("No borro nada")
                return False
        else:  
            print("\u26A0 No existe esta usuario \u26A0")
            return False  
    except:
        print("\u26A0 Error al ingresar a base de datos \u26A0")
        return False    
    
def pedir_id(user):
    try:
        cursor.execute("Select id from usuarios where usuario=%s",(user,))
        fila = cursor.fetchone()
        if fila:
            return fila[0]
        else:
            return None
    except:
        return False 
