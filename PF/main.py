import funciones
from funciones import *
import conexionBD
from usuarios import usuario
from comidas import comida
from bebidas import bebida
from pedidos import pedido
import getpass
import pymysql
import openpyxl

mensajes = {
    "agregado": "Se agregó correctamente",
    "error": "No fue posible realizar la acción",
    "no_encontrado": "No se encontró"
}
def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro de usuarios ::..")
            user=input("\t\U0001F464 Ingresa tu usuario: ").upper().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            resultado=usuario.registrar(user,password)
            if resultado:
                print(f"\n\t{user} ",mensajes["agregado"])
            else:
                print(mensajes["error"])    
                print("Por favro intente de nuevo")
                esperarTecla()

              
            funciones.esperarTecla()
        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            user=input("\t\U0001F464 Ingresa tu usuario: ").upper().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo 
            registro=usuario.iniciar_sesion(user,password)
            if registro:
                funciones.esperarTecla() 
                menu_cafe(registro[0],registro[1])
            else:
                print(f"\n\tusuario o contraseña incorrectas")
                print("\n\tIntentelo de nuevo")    
            funciones.esperarTecla()    
              
        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_cafe(usuario_id,user):
    if usuario_id==1:
            funciones.borrarPantalla()
            print(f"\tBienvenido {user}")
            while True:
                opc=menu_admin()
                if opc==1:
                    while True:
                        borrarPantalla()
                        print("Administrar Comida")
                        opcion = int(input(
                            "Ingresa una opcion: \n"
                            "\t1️⃣  Añadir\n"
                            "\t2️⃣  Buscar\n"
                            "\t3️⃣  Modificar\n"
                            "\t4️⃣  Ver\n"
                            "\t5️⃣  Borrar\n"
                            "\t6️⃣  Salir\n\t"
                            "\tIngresa un numero (1-6): "
                        ))

                        if opcion == 1:
                            borrarPantalla()
                            print("Añadir comida al menu")
                            nombre = input("\tIngresa la comida: ")
                            precio = int(input("\tIngresa el precio: "))
                            respuesta = comida.crear(nombre, precio)
                            if respuesta:
                                print(f"Se agregó {nombre} de manera correcta")
                            else:
                                print("No fue posible agregar la comida al menú")
                            esperarTecla()

                        elif opcion == 2:
                            borrarPantalla()
                            print("Buscar comida del menu") 
                            buscar = input("\tIngresa el nombre de la comida a buscar: ")
                            menu_comida = comida.buscar(buscar)
                            if len(menu_comida) > 0:
                                print("\n\tMenu de comida: \U0001F4BE\n")
                                print(f"{'ID':<10}{'Nombre':<30}{'Precio':<15}")
                                print("-" * 80)
                                for fila in menu_comida:
                                    print(f"{fila[0]:<10}{fila[1]:<30}{fila[2]:<15}")
                                print("-" * 60)
                            else:
                                print("No se encontró esa comida en el menú")
                            esperarTecla()

                        elif opcion == 3:
                            borrarPantalla()
                            print("Modificar el menú de comida")
                            menu_comida = comida.mostrar()
                            if len(menu_comida) > 0:
                                print("\n\tMenu de comida: \U0001F4BE\n")
                                print(f"{'ID':<10}{'Nombre':<30}{'Precio':<15}")
                                print("-" * 80)
                                for fila in menu_comida:
                                    print(f"{fila[0]:<10}{fila[1]:<30}{fila[2]:<15}")
                                print("-" * 60)
                        
                                id_comida = input("Ingresa el ID de la comida a modificar: ")
                                respuesta = comida.cambiar(id_comida)
                                if respuesta:
                                    print("Se modificó de manera correcta el menú")
                                else:
                                    print("No fue posible modificar el menú")
                            else:
                                print("No hay datos a modificar")        
                            esperarTecla()

                        elif opcion == 4:
                            borrarPantalla()
                            print("Ver el menú de comida")
                            menu_comida = comida.mostrar()
                            if len(menu_comida) > 0:
                                print("\n\tMenu de comida: \U0001F4BE\n")
                                print(f"{'ID':<10}{'Nombre':<30}{'Precio':<15}")
                                print("-" * 80)
                                for fila in menu_comida:
                                    print(f"{fila[0]:<10}{fila[1]:<30}{fila[2]:<15}")
                                print("-" * 60)
                            else:
                                print("No se pudo mostrar el menú de la comida")
                            esperarTecla()

                        elif opcion == 5:
                            borrarPantalla()
                            print("Borrar comida del menú")
                            menu_comida = comida.mostrar()
                            if len(menu_comida) > 0:
                                print("\n\tMenu de comida: \U0001F4BE\n")
                                print(f"{'ID':<10}{'Nombre':<30}{'Precio':<15}")
                                print("-" * 80)
                                for fila in menu_comida:
                                    print(f"{fila[0]:<10}{fila[1]:<30}{fila[2]:<15}")
                                print("-" * 60)
                            else:
                                print("No se pudo mostrar el menú de la comida")
                            
                            id_comida = input("Ingresa el ID de la comida a eliminar del menú: ")
                            respuesta = comida.borrar(id_comida)
                            if respuesta:
                                print("Se eliminó de manera correcta la comida del menú")
                            else:
                                print("No fue posible eliminar la comida del menú")
                            esperarTecla()

                        elif opcion == 6:
                            borrarPantalla()
                            print("Salir")
                            esperarTecla()
                            break

                        else:
                            borrarPantalla()
                            print("Valor inválido")
                            esperarTecla() 
                elif opc==2:
                    while True:
                        borrarPantalla()
                        print("Administrar Bebidas")
                        opcion = int(input(
                            "Ingresa una opcion: \n"
                            "\t1️⃣  Añadir\n"
                            "\t2️⃣  Buscar\n"
                            "\t3️⃣  Modificar\n"
                            "\t4️⃣  Ver\n"
                            "\t5️⃣  Borrar\n"
                            "\t6️⃣  Exportar tabla a excel\n"
                            "\t7️⃣  Salir\n"
                            "\tIngresa un numero (1-7): "
                        ))

                        if opcion == 1:
                            borrarPantalla()
                            print("Añadir Bebidas al menu")
                            nombre = input("\tIngresa la comida: ")
                            precio = int(input("\tIngresa el precio: "))
                            respuesta = bebida.crear(nombre, precio)
                            if respuesta:
                                print(f"Se agregó {nombre} de manera correcta")
                            else:
                                print("No fue posible agregar la comida al menú")
                            esperarTecla()

                        elif opcion == 2:
                            borrarPantalla()
                            print("Buscar bebidas del menu") 
                            buscar = input("\tIngresa el nombre de la bebidas a buscar: ")
                            menu_bebidas = bebida.buscar(buscar)
                            if len(menu_bebidas) > 0:
                                print("\n\tMenu de bebidas: \U0001F4BE\n")
                                print(f"{'ID':<10}{'Nombre':<30}{'Precio':<15}")
                                print("-" * 80)
                                for fila in menu_bebidas:
                                    print(f"{fila[0]:<10}{fila[1]:<30}{fila[2]:<15}")
                                print("-" * 60)
                            else:
                                print("No se encontró esa bebida en el menú")
                            esperarTecla()

                        elif opcion == 3:
                            borrarPantalla()
                            print("Modificar el menú de bebidas")
                            menu_bebidas = bebida.mostrar()
                            if len(menu_bebidas) > 0:
                                print("\n\tMenu de bebidas: \U0001F4BE\n")
                                print(f"{'ID':<10}{'Nombre':<30}{'Precio':<15}")
                                print("-" * 80)
                                for fila in menu_bebidas:
                                    print(f"{fila[0]:<10}{fila[1]:<30}{fila[2]:<15}")
                                print("-" * 60)

                                id_bebida = input("Ingresa el ID de la bebida a modificar: ")
                                respuesta = bebida.cambiar(id_bebida)
                                if respuesta:
                                    print("Se modificó de manera correcta el menú")
                                else:
                                    print("No fue posible modificar el menú")
                            else:
                                print("No hay datos a modificar")
                            esperarTecla()
                                

                        elif opcion == 4:
                            borrarPantalla()
                            print("Ver el menú de bebidas")
                            menu_bebidas = bebida.mostrar()
                            if len(menu_bebidas) > 0:
                                print("\n\tMenu de bebidas: \U0001F4BE\n")
                                print(f"{'ID':<10}{'Nombre':<30}{'Precio':<15}")
                                print("-" * 80)
                                for fila in menu_bebidas:
                                    print(f"{fila[0]:<10}{fila[1]:<30}{fila[2]:<15}")
                                print("-" * 60)
                            else:
                                print("No se pudo mostrar el menú de bebidas")
                            esperarTecla()

                        elif opcion == 5:
                            borrarPantalla()
                            print("Borrar bebidas del menú")
                            menu_bebidas = bebida.mostrar()
                            if len(menu_bebidas) > 0:
                                print("\n\tMenu de bebidas: \U0001F4BE\n")
                                print(f"{'ID':<10}{'Nombre':<30}{'Precio':<15}")
                                print("-" * 80)
                                for fila in menu_bebidas:
                                    print(f"{fila[0]:<10}{fila[1]:<30}{fila[2]:<15}")
                                print("-" * 60)
                                id_bebida = input("Ingresa el ID de la bebida a eliminar del menú: ")
                                respuesta = bebida.borrar(id_bebida)
                                if respuesta:
                                    print("Se eliminó de manera correcta la bebida del menú")
                                else:
                                    print("No fue posible eliminar la bebida del menú")
                            else:
                                print("No hay datos a borrar")
                            esperarTecla()

                        elif opcion == 6:
                            borrarPantalla()
                            print("Exportando tabla a excel...")
                            esperarTecla()

                            def get_connection():
                                try:
                                    return pymysql.connect(
                                        host='127.0.0.1',
                                        user='root',
                                        passwd='',
                                        db='bd_cafe'
                                    )
                                except Exception as e:
                                    print(f"Exception: {e}")
                            
                            class CafeService():
                                @classmethod
                                def get_cafe(cls):
                                    try:
                                        connection = get_connection()
                                        cafe = []
                                        with connection.cursor() as cursor:
                                            cursor.execute(
                                                'SELECT id, nombre, precio FROM bebidas;')
                                            resultset = cursor.fetchall()
                                            for row in resultset:
                                                cafe.append(row)
                                        connection.close()
                                        return cafe
                                    except Exception as e:
                                        print(f"Exception: {e}")

                            try:
                                cafe = CafeService.get_cafe()

                                excel_book = openpyxl.Workbook()
                                sheet = excel_book.active

                                sheet['A1'] = "id"
                                sheet['B1'] = "nombre"
                                sheet['C1'] = "precio"


                                for i, row in enumerate(cafe):
                                    sheet[f'A{i + 2}'] = row[0]
                                    sheet[f'B{i + 2}'] = row[1]
                                    sheet[f'C{i + 2}'] = row[2]

                                excel_book.save("my_excel_file.xlsx")
                                input("✅ Se ha exportado la tabla correctamente ✅")
                                
                            except Exception as e:
                                print(f"Exception: {e}")
                        elif opcion == 7:
                            borrarPantalla()
                            print("Salir")
                            esperarTecla()
                            break

                        else:
                            borrarPantalla()
                            print("Valor inválido")
                            esperarTecla() 
                elif opc==3:
                    while True:
                        borrarPantalla()
                        print("Administrar Usuarios")
                        opcion = int(input(
                            "Ingresa una opcion: \n"
                            "\t1️⃣  Añadir\n"
                            "\t2️⃣  Buscar\n"
                            "\t3️⃣  Modificar\n"
                            "\t4️⃣  Ver\n"
                            "\t5️⃣  Borrar\n"
                            "\t6️⃣  Salir\n\t"
                            "\tIngresa un numero (1-6): "
                        ))

                        if opcion == 1:
                            borrarPantalla()
                            print("\n \t ..:: Registro de usuarios ::..")
                            user=input("\t\U0001F464 Ingresa el usuario: ").upper().strip()
                            password=getpass.getpass("\t Ingresa la contraseña: ").strip()
                            #Agregar codigo
                            resultado=usuario.registrar(user,password)
                            if resultado:
                                print(f"\n\t{user} se registro correctamente")
                                esperarTecla()
                            else:
                                print("No fue posible ingresar el registro")    
                                print("Por favro intente de nuevo")
                                esperarTecla()

                        elif opcion == 2:
                            borrarPantalla()
                            print("Buscar usuarios") 
                            buscar = input("\tIngresa el nombre del usuario a buscar: ").upper().strip()
                            tabla_usuarios = usuario.buscar(buscar)
                            if len(tabla_usuarios) > 0:
                                print("\n\tUsuarios: \U0001F4BE\n")
                                print(f"{'ID':<10}{'Usuario':<20}")
                                print("-" * 40)
                                for fila in tabla_usuarios:
                                    print(f"{fila[0]:<10}{fila[1]:<20}")
                                print("-" * 40)
                            else:
                                print("No se encontró este usuario")
                            esperarTecla()

                        elif opcion == 3:
                            borrarPantalla()
                            print("Modificar usuarios")
                            tabla_usuarios = usuario.mostrar()
                            if len(tabla_usuarios) > 0:
                                print("\n\tUsuarios: \U0001F4BE\n")
                                print(f"{'ID':<10}{'Usuario':<20}")
                                print("-" * 40)
                                for fila in tabla_usuarios:
                                    print(f"{fila[0]:<10}{fila[1]:<20}")
                                print("-" * 40)

                                id_usuario = input("Ingresa el ID del usuario a modificar: ")
                                respuesta = usuario.modificar(id_usuario)
                                if respuesta:
                                    print("Se modificó de manera correcta el usuario")
                                else:
                                    print("No fue posible modificar el usuario")
                            else:
                                print("No hay datos a modificar")
                            esperarTecla()
                                

                        elif opcion == 4:
                            borrarPantalla()
                            print("\t\U0001F464 Usuarios:")
                            tabla_usuarios = usuario.mostrar()
                            if len(tabla_usuarios) > 0:
                                print("\n\tUsuarios: \U0001F4BE\n")
                                print(f"{'ID':<10}{'Usuario':<20}")
                                print("-" * 40)
                                for fila in tabla_usuarios:
                                    print(f"{fila[0]:<10}{fila[1]:<20}")
                                print("-" * 40)
                            else:
                                print("No se logro encontrar usuarios")
                            esperarTecla()

                        elif opcion == 5:
                            borrarPantalla()
                            print("Borrar Usuarios")
                            tabla_usuarios = usuario.mostrar()
                            if len(tabla_usuarios) > 0:
                                print("\n\tUsuarios: \U0001F4BE\n")
                                print(f"{'ID':<10}{'Usuario':<20}")
                                print("-" * 40)
                                for fila in tabla_usuarios:
                                    print(f"{fila[0]:<10}{fila[1]:<30}")
                                print("-" * 40)
                                id_usuario = input("Ingresa el ID del usuario a eliminar: ")
                                respuesta = usuario.borrar(id_usuario)
                                if respuesta:
                                    print("Se eliminó de manera correcta")
                                else:
                                    print("No fue posible eliminar el usuario")
                            else:
                                print("No hay datos a borrar")
                            esperarTecla()


                        elif opcion == 6:
                            borrarPantalla()
                            print("Salir")
                            esperarTecla()
                            break

                        else:
                            borrarPantalla()
                            print("Valor inválido")
                            esperarTecla() 
                elif opc==4:
                    while True:
                        borrarPantalla()
                        print("Administrar pedidos")
                        opcion = int(input(
                            "Ingresa una opcion: \n"
                            "\t1️⃣  Buscar\n"
                            "\t2️⃣  Modificar\n"
                            "\t3️⃣  Ver\n"
                            "\t4️⃣  Borrar\n"
                            "\t5️⃣  Salir\n"
                            "\tIngresa un numero (1-5): "
                        ))


                        if opcion == 1:
                            borrarPantalla()
                            print("Buscar Pedidos") 
                            buscar = input("\tIngresa el id del pedido a buscar: ")
                            tabla_pedidos = pedido.buscar(buscar)
                            if len(tabla_pedidos) > 0:
                                print("\n\tPedidos: \U0001F4BE\n")
                                print(f"{'ID':<10}{'ID Usuario':<15}{'Orden':<50}{'Total':<10}")
                                print("-" * 100)
                                for fila in tabla_pedidos:
                                    print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<50}{fila[3]:<10}")
                                print("-" * 100)
                            else:
                                print("No se encontró este pedido")
                            esperarTecla()

                        elif opcion == 2:
                            borrarPantalla()
                            print("Modificar pedidos")
                            tabla_pedidos = pedido.mostrar()
                            if len(tabla_pedidos) > 0:
                                print("\n\tPedidos: \U0001F4BE\n")
                                print(f"{'ID':<10}{'ID Usuario':<15}{'Orden':<50}{'Total':<10}")
                                print("-" * 100)
                                for fila in tabla_pedidos:
                                    print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<50}{fila[3]:<10}")
                                print("-" * 100)
                                id_pedido = input("Ingresa el ID del pedido a modificar: ")
                                respuesta = pedido.cambiar(id_pedido)
                                if respuesta:
                                    print("Se modificó de manera correcta el pedido")
                                else:
                                    print("No fue posible modificar el pedido")
                            else:
                                print("No hay datos a modificar")
                            esperarTecla()
                                

                        elif opcion == 3:
                            borrarPantalla()
                            print("Ver Pedidos")
                            tabla_pedidos = pedido.mostrar()
                            if len(tabla_pedidos) > 0:
                                print("\n\tPedidos: \U0001F4BE\n")
                                print(f"{'ID':<10}{'ID Usuario':<15}{'Orden':<50}{'Total':<10}")
                                print("-" * 100)
                                for fila in tabla_pedidos:
                                    print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<50}{fila[3]:<10}")
                                print("-" * 100)
                            else:
                                print("No se pudo mostrar el menú de bebidas")
                            esperarTecla()

                        elif opcion == 4:
                            borrarPantalla()
                            print("Borrar pedidos")
                            tabla_pedidos = pedido.mostrar()
                            if len(tabla_pedidos) > 0:
                                print("\n\tPedidos: \U0001F4BE\n")
                                print(f"{'ID':<10}{'ID Usuario':<15}{'Orden':<50}{'Total':<10}")
                                print("-" * 100)
                                for fila in tabla_pedidos:
                                    print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<50}{fila[3]:<10}")
                                print("-" * 100)
                                id_pedido = input("Ingresa el ID del pedido a borrar: ")
                                respuesta = pedido.borrar(id_pedido)
                                if respuesta:
                                    print("Se borro de manera correcta el pedido")
                                else:
                                    print("No fue posible borrar el pedido")
                            else:
                                print("No hay datos a borrar")
                            esperarTecla()


                        elif opcion == 5:
                            borrarPantalla()
                            print("Salir")
                            esperarTecla()
                            break

                        else:
                            borrarPantalla()
                            print("Valor inválido")
                            esperarTecla()
                    
                elif opc==5:
                    print("Salir")
                    break
                else:
                    print("Valor invalido")
                    esperarTecla()
    else:
            funciones.borrarPantalla()
            print(f"\tBienvenido {user}")
            while True:
                opc=menu_clientes()
                if opc==1:
                    borrarPantalla()
                    menu_comida = comida.mostrar()
                    if len(menu_comida) > 0:
                        print("\n\tMenu de comida: \U0001F4BE\n")
                        print(f"{'ID':<10}{'Nombre':<30}{'Precio':<15}")
                        print("-" * 60)
                        for fila in menu_comida:
                            print(f"{fila[0]:<10}{fila[1]:<30}{fila[2]:<15}")
                        print("-" * 60)
                        pedir_comida=input("Ingresa el id de lo que deseas ordenar: ")  
                        respuesta=pedido.pedir_comida(pedir_comida)      
                        


                elif opc==2:
                    borrarPantalla()
                    menu_bebidas = bebida.mostrar()
                    if len(menu_bebidas) > 0:
                        print("\n\tMenu de bebidas: \U0001F4BE\n")
                        print(f"{'ID':<10}{'Nombre':<30}{'Precio':<15}")
                        print("-" * 60)
                        for fila in menu_bebidas:
                            print(f"{fila[0]:<10}{fila[1]:<30}{fila[2]:<15}")
                        print("-" * 60)
                        pedir_bebida=input("Ingresa el id de lo que deseas ordenar: ")  
                        respuesta=pedido.pedir_bebida(pedir_bebida)  

                elif opc==3:
                    user_id=usuario.pedir_id(user)   
                    respuesta = pedido.realizar(user_id)
                    if respuesta:
                        print(f"Se realizo el pedido")    
                    esperarTecla()




                elif opc==4:
                    print("Salir")
                    break
                else:
                    print("Valor invalido")
                    esperarTecla()
     



if __name__ == "__main__":
    main()    