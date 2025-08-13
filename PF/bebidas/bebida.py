from conexionBD import *
import funciones
import datetime

def crear (bebida,precio):
    try:
        fecha=datetime.datetime.now()
        cursor.execute("INSERT INTO bebidas (nombre, precio) VALUES (%s, %s)",
                       (bebida, precio))
        conexion.commit()
        return True
    except:
        return False    
    
def mostrar ():
    try:
        cursor.execute("Select * from  bebidas")
        return cursor.fetchall()
    except:
        return False    


def buscar(buscar):
    try:
        cursor.execute("Select * from  bebidas where nombre=%s",(buscar,))
        return cursor.fetchall()
    except:
        return False 
    
def cambiar(id):
    try:
        
        cursor.execute("SELECT * FROM bebidas WHERE id=%s", (id,))
        fila = cursor.fetchone()
        
        if fila:
            funciones.borrarPantalla()
            print("\n\t\U0001F501 Bebida a modificar del menu: \n")
            print(f"{'ID':<10}{'Nombre':<30}{'Precio':<15}")
            print("-" * 80)
            print(f"{fila[0]:<10}{fila[1]:<30}{fila[2]:<15}")
            print("-" * 80)
            
            seguro = input("¿Seguro que deseas modificar este registro? (si/no): ").lower().strip()
            if seguro == "si":
                nombre = input("\t Ingresa el nombre: ")
                precio = input("\t Ingresa el precio: ")
                cursor.execute(
                    "UPDATE bebidas SET nombre=%s, precio=%s WHERE id=%s",
                    (nombre, precio, id )
                )
                conexion.commit()
                return True
            else:
                print("No modifico nada")
                return False
        else:
            print("\u26A0 No existe esta bebida en el menu. \u26A0")
            return False

    except Exception as e:
        print("\u26A0 Error al modificar:", e)
        return False
"""def cambiar (id, titulo, descripcion):
    try:
        cursor.execute("Select * from  notas where id=%s",(id,))
        registros=cursor.fetchone()
        if registros:
            print("\n\tTabla de notas: \U0001F4BE\n")
            print(f"{"ID":<10}{"ID de usuario":<15}{"Titulo":<15}{"Descripcion":<15}{"Fecha":<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]}")
            print(f"-"*80)   
            seguro=input("Seguro de modificar este registro? ")
            if seguro=="si":
                cursor.execute("Update notas set titulo=%s, descripcion=%s, fecha=NOW() where id=%s",(titulo,descripcion,id))
                conexion.commit()
                return True
            else:
                return False
        else:
            print("No existe esta nota")
            return False    
    except:
        return False
"""       
    
def borrar (id,):
    try:
        cursor.execute("Select * from bebidas where id=%s",(id,))
        registros=cursor.fetchall()
        if registros:
            funciones.borrarPantalla()
            print("\n\t\U0001F4DB Bebida a eliminar del menu: \n")
            print(f"{"ID":<10}{"Nombre":<30}{"Precio":<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<30}{fila[2]:<15}")
            print(f"-"*80)   
            seguro=input("Seguro de borrar este registro? (si/no) ").lower().strip()
            if seguro=="si":
                cursor.execute("delete from bebidas where id=%s",(id,))
                conexion.commit()
                return True
            else:    
                print("No borro nada")
                return False
        else:  
            print("\u26A0 No existe esta bebida \u26A0")
            return False  
    except:
        print("\u26A0 Error al ingresar a base de datos \u26A0")
        return False    