from conexionBD import *
import funciones
import datetime
from usuarios import usuario
from comidas import comida
from bebidas import bebida
descripcion=[]
total=0
opc=0
def pedir_comida(pedido):
    try:
        global descripcion, total
        cursor.execute("Select * from  comida where id=%s",(pedido,))
        registros= cursor.fetchall()
        if registros:
            funciones.borrarPantalla()
            print("\n\tComida seleccionada: \n")
            print(f"{"ID":<10}{"Nombre":<30}{"Precio":<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<30}{fila[2]:<15}")
            print(f"-"*80)   
            seguro=input("Seguro de ordenar esto? (si/no) ").lower().strip()
            if seguro=="si":
                fila = registros[0]
                descripcion.append((fila[1], fila[2]))
                total += fila[2]
                input("Pedido añadido corectamente")
                return True
            else:    
                print("No ordeno nada")
                return False
        else:  
            print("\u26A0 No existe este producto \u26A0")
            return False  
    except:
        return False 
    
def pedir_bebida(pedido):
    try:
        global descripcion, total
        cursor.execute("Select * from  bebidas where id=%s",(pedido,))
        registros= cursor.fetchall()
        if registros:
            funciones.borrarPantalla()
            print("\n\tBebida seleccionada: \n")
            print(f"{"ID":<10}{"Nombre":<30}{"Precio":<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<30}{fila[2]:<15}")
            print(f"-"*80)   
            seguro=input("Seguro de ordenar esto? (si/no) ").lower().strip()
            if seguro=="si":
                fila = registros[0]
                descripcion.append((fila[1], fila[2]))  # nombre, precio
                total += fila[2]
                input("Pedido añadido corectamente")
                return True
            else:    
                print("No ordeno nada")
                return False
        else:  
            print("\u26A0 No existe este producto \u26A0")
            return False  
    except:
        return False     
    
def realizar(user_id):
    try:
        global descripcion, total
        if not descripcion:
            print("No hay productos en el pedido.")
            return False

        # Mostrar ticket
        print("\n" + "=" * 40)
        print("\tRESUMEN DEL PEDIDO")
        print("=" * 40)
        print(f'{"Producto":<25}{"Precio":>10}')
        print("-" * 40)

        for producto, precio in descripcion:
            print(f'{producto:<25}{precio:>10.2f}')

        print("-" * 40)
        print(f'{"TOTAL":<25}{total:>10.2f}')
        print("=" * 40)

        seguro = input("Seguro de realizar tu pedido? (si/no): ").lower().strip()

        if seguro == "si":
            # Convertir la lista de tuplas a solo nombres para guardar en la BD
            descripcion2 = ", ".join([p[0] for p in descripcion])
            cursor.execute(
                "INSERT INTO pedidos (id_usuario, descripcion, precio) VALUES (%s, %s, %s)",
                (user_id, descripcion2, total)
            )
            conexion.commit()
            descripcion = []
            total = 0
            print("Pedido registrado correctamente.")
            return True
        else:
            print("No realizó su pedido")
            return False
    except Exception as e:

        print("Error:", e)
        return False    
    


def mostrar ():
    try:
        cursor.execute("Select * from  pedidos")
        return cursor.fetchall()
    except:
        return False    

def buscar(buscar):
    try:
        cursor.execute("Select * from  pedidos where id=%s",(buscar,))
        return cursor.fetchall()
    except:
        return False 
'''

def cambiar(id):
    try:
        
        cursor.execute("SELECT * FROM pedidos WHERE id=%s", (id,))
        fila = cursor.fetchone()
        
        if fila:
            funciones.borrarPantalla()
            print("\n\tOrden a modificar: \n")
            print(f"{'ID':<10}{'ID Usuario':<15}{'Orden':<50}{'Total':<10}")
            print("-" * 100)
            print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<50}{fila[3]:<10}")
            print("-" * 100)
            
            seguro = input("¿Seguro que deseas modificar este registro? (si/no): ").lower().strip()
            if seguro == "si":
                global descripcion, total
                descripcion = []
                total = 0
                repetir_id=True
                while repetir_id:
                    user_id=input("Ingresa el id del usuario")
                    respuesta=usuario.buscar(user_id)
                    if respuesta:
                        seguro_id=input("Seguro de utilizar este usuario? (si/no): ")
                        if seguro_id=="si":
                            repetir_id=False
                            while True:
                                opc=funciones.menu_clientes()
                                if opc==1:
                                    funciones.borrarPantalla()
                                    menu_comida = comida.mostrar()
                                    if len(menu_comida) > 0:
                                        print("\n\tMenu de comida: \U0001F4BE\n")
                                        print(f"{'ID':<10}{'Nombre':<30}{'Precio':<15}")
                                        print("-" * 60)
                                        for fila in menu_comida:
                                            print(f"{fila[0]:<10}{fila[1]:<30}{fila[2]:<15}")
                                        print("-" * 60)
                                        pedir_comida=input("Ingresa el id de lo que deseas ordenar: ")  
                                        producto = comida.buscar(pedir_comida)
                                        if producto:
                                            descripcion.append((producto[1], producto[2]))
                                            total += producto[2]
                
                                elif opc==2:
                                    funciones.borrarPantalla()
                                    menu_bebidas = bebida.mostrar()
                                    if len(menu_bebidas) > 0:
                                        print("\n\tMenu de bebidas: \U0001F4BE\n")
                                        print(f"{'ID':<10}{'Nombre':<30}{'Precio':<15}")
                                        print("-" * 60)
                                        for fila in menu_bebidas:
                                            print(f"{fila[0]:<10}{fila[1]:<30}{fila[2]:<15}")
                                        print("-" * 60)
                                        pedir_bebida=input("Ingresa el id de lo que deseas ordenar: ")  
                                        producto=pedir_bebida(pedir_bebida)
                                        if producto:
                                            descripcion.append((producto[1], producto[2]))
                                            total += producto[2]

                                elif opc==3:        
                                    if not descripcion:
                                        print("No hay productos en el pedido.")
                                        return False

                                    # Mostrar ticket
                                    print("\n" + "=" * 40)
                                    print("\tRESUMEN DEL PEDIDO")
                                    print("=" * 40)
                                    print(f'{"Producto":<25}{"Precio":>10}')
                                    print("-" * 40)

                                    for producto, precio in descripcion:
                                        print(f'{producto:<25}{precio:>10.2f}')

                                    print("-" * 40)
                                    print(f'{"TOTAL":<25}{total:>10.2f}')
                                    print("=" * 40)

                                    seguro = input("Seguro de realizar tu pedido? (si/no): ").lower().strip()

                                    if seguro == "si":
                                        # Convertir la lista de tuplas a solo nombres para guardar en la BD
                                        descripcion2 = ", ".join([p[0] for p in descripcion])
                                        cursor.execute(
                                            "UPDATE pedidos SET usuario_id=%s, descripcion=%s, precio=%s WHERE id=%s",
                                            (user_id,descripcion2, total, id )
                                        )
                                    conexion.commit()
                                    descripcion = []
                                    total = 0
                                    print("Pedido modificado correctamente.")
                                    return True   
                    else:
                        print("No se encontro el usuario")
                        return                
            else:
                print("No modifico nada")
                return False
        else:
            print("\u26A0 No existe. \u26A0")
            return False

    except Exception as e:
        print("\u26A0 Error al modificar:", e)
        return False
'''
def cambiar(id):
    try:
        global descripcion, total
        cursor.execute("SELECT * FROM pedidos WHERE id=%s", (id,))
        fila = cursor.fetchone()

        if not fila:
            print("\u26A0 No existe. \u26A0")
            return False

        funciones.borrarPantalla()
        print("\n\tOrden a modificar: \n")
        print(f"{'ID':<10}{'ID Usuario':<15}{'Orden':<50}{'Total':<10}")
        print("-" * 100)
        print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<50}{fila[3]:<10}")
        print("-" * 100)

        seguro = input("¿Seguro que deseas modificar este registro? (si/no): ").lower().strip()
        if seguro != "si":
            input("No se modificó nada.")
            return False

        descripcion = []
        total = 0

        # Selección de usuario
        while True:
            user_id = input("Ingresa el id del usuario: ")
            respuesta = usuario.buscar2(user_id)
            if not respuesta:
                input("No se encontró el usuario.")
                return False

            seguro_id = input("¿Seguro de utilizar este usuario? (si/no): ").lower().strip()
            if seguro_id == "si":
                break

        # Menú de selección
        while True:
            opc = funciones.menu_clientes()

            if opc == 1:
                funciones.borrarPantalla()
                menu_comida = comida.mostrar()
                if menu_comida:
                    print("\n\tMenu de comida:\n")
                    print(f"{'ID':<10}{'Nombre':<30}{'Precio':<15}")
                    print("-" * 60)
                    for item in menu_comida:
                        print(f"{item[0]:<10}{item[1]:<30}{item[2]:<15}")
                    print("-" * 60)
                    comida_id = input("Ingresa el id de lo que deseas ordenar: ")
                    producto = pedir_comida(comida_id)
                    if producto:
                        funciones.esperarTecla()
                    else:
                        print("Producto no encontrado.") 
                        funciones.esperarTecla()

            elif opc == 2:
                funciones.borrarPantalla()
                menu_bebidas = bebida.mostrar()
                if menu_bebidas:
                    print("\n\tMenu de bebidas:\n")
                    print(f"{'ID':<10}{'Nombre':<30}{'Precio':<15}")
                    print("-" * 60)
                    for item in menu_bebidas:
                        print(f"{item[0]:<10}{item[1]:<30}{item[2]:<15}")
                    print("-" * 60)
                    bebida_id = input("Ingresa el id de lo que deseas ordenar: ")
                    producto = pedir_bebida(bebida_id)
                    if producto:
                        funciones.esperarTecla()
                    else:
                        print("Producto no encontrado.") 
                        funciones.esperarTecla()    

            elif opc == 3:
                if not descripcion:
                    print("No hay productos en el pedido.")
                    return False

                # Mostrar resumen
                print("\n" + "=" * 40)
                print("\tRESUMEN DEL PEDIDO")
                print("=" * 40)
                print(f'{"Producto":<25}{"Precio":>10}')
                print("-" * 40)
                for producto, precio in descripcion:
                    print(f'{producto:<25}{precio:>10.2f}')
                print("-" * 40)
                print(f'{"TOTAL":<25}{total:>10.2f}')
                print("=" * 40)

                seguro_final = input("¿Seguro de realizar tu pedido? (si/no): ").lower().strip()
                if seguro_final == "si":
                    descripcion_texto = ", ".join([p[0] for p in descripcion])
                    cursor.execute(
                        "UPDATE pedidos SET id_usuario=%s, descripcion=%s, precio=%s WHERE id=%s",
                        (user_id, descripcion_texto, total, id)
                    )
                    conexion.commit()
                    print("Pedido modificado correctamente.")
                return True

    except Exception as e:
        print("\u26A0 Error al modificar:", e)
        return False

def borrar (id,):
    try:
        cursor.execute("Select * from pedidos where id=%s",(id,))
        registros=cursor.fetchall()
        if registros:
            funciones.borrarPantalla()
            print("\n\t\U0001F4DB Pedido a eliminar: \n")
            print(f"{'ID':<10}{'ID Usuario':<15}{'Orden':<50}{'Total':<10}")
            print("-" * 100)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<50}{fila[3]:<10}")
            print("-" * 100) 
            seguro=input("Seguro de borrar este registro? (si/no) ").lower().strip()
            if seguro=="si":
                cursor.execute("delete from pedidos where id=%s",(id,))
                conexion.commit()
                return True
            else:    
                print("No borro nada")
                return False
        else:  
            print("\u26A0 No existe este pedido \u26A0")
            return False  
    except:
        print("\u26A0 Error al ingresar a base de datos \u26A0")
        return False


