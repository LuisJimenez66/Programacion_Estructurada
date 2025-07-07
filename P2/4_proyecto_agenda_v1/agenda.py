def menu_principal():
        print("\t\t\n  1️⃣  Agregar contacto \t\t\n  2️⃣  Mostrar todos los contactos \t\t\n  3️⃣ Bucar contacto por nombre\t\t\n  4\ufe0f\u20e3. Eliminar contacto \t\t\n  5\ufe0f\u20e3. Modificar contacto \t\t\n  6\ufe0f\u20e3. Salir")
        opcion=input("\n\t\tIngrese una opción: (1-4):  ")
        return opcion.strip()

      
def limpiar_pantalla():
    import os
    os.system("cls")

def espere_tecla():
    input("\n\t\tPresione Enter para continuar...")       

def agregar_contacto(agenda):
    print("\n\t\t..::Agregar contacto::.. \U0001F4DD")
    nombre= input("\n\t\t\U0001F4DD Ingrese el nombre del contacto: ").upper().strip()
   
    if nombre in agenda:
        print("\n\t\tEl contacto ya existe.")
        espere_tecla()
    else:
        telefono = input("\n\t\t\U0001F4DD Ingrese el número de teléfono: ").strip()
        email = input("\n\t\t\U0001F4DD Ingrese el correo electrónico: ").lower().strip()
        #Agregar el atributo nombre al diccionario con los valores de tel y email en una lista
        agenda[nombre] = [telefono, email]
        input("\n\t\t\U0001F389 Contacto agregado correctamente. Presione Enter para continuar... \U0001F389")

def mostrar_contactos(agenda):
    print("\n\t\tMostrar todos los contactos")
    if not agenda:
        print("\n\t\t\u26A0 No hay contactos en la agenda. \u26A0")
        espere_tecla()
    else:
        for nombre,datos in agenda.items():
            print(f"\n\t{'Nombre:'+nombre}\n\t{'Telefono: '+datos[0]}\n\t{'E-mail: '+datos[1]}")
    espere_tecla()        

def buscar_contacto(agenda):
    print("\n\t\tBuscar contacto por nombre")
    if not agenda:
        print("\n\t\t\u26A0 No hay contactos en la agenda. \u26A0")
        espere_tecla()
    else:
        buscar=input("\n\t\t\U0001F50D Ingrese el nomber que desea buscar: ").upper().strip()
        for nombre,datos in agenda.items():
            if buscar in nombre:
                print(f"\n\t{'Nombre:'+nombre}\n\t{'Telefono: '+datos[0]}\n\t{'E-mail: '+datos[1]}")
                espere_tecla()
            else:
                print("\n\t\tEl contacto no existe. \u26A0")
                espere_tecla()    
            

def eliminar_contacto(agenda):
    print("\n\t\tEliminar contacto \U0001F4DB")
    if not agenda:
        print("\n\t\t\u26A0 No hay contactos en la agenda. \u26A0")
        espere_tecla()
    else:
        nombre = input("\n\t\t\U0001F50D Ingrese el nombre del contacto a eliminar: ").upper().strip()
        if nombre in agenda:
            del agenda[nombre]
            print("\n\t\tContacto eliminado correctamente. \U0001F389")
        else:
            print("\n\t\tEl contacto no existe. \u26A0")
        espere_tecla()

def modificar_contacto(agenda):
    print("\n\t\tModificar contacto \U0001F4BE")
    if not agenda:
        print("\n\t\t\u26A0 No hay contactos en la agenda. \u26A0")
        espere_tecla()
    else:
        nombre = input("\n\t\t\U0001F4BE Ingrese el nombre del contacto a modificar: ").upper().strip()
        if nombre in agenda:
            telefono = input("\n\t\t\U0001F4DD Ingrese el nuevo número de teléfono: ").strip()
            email = input("\n\t\t\U0001F4DD Ingrese el nuevo correo electrónico: ").lower().strip()
            agenda[nombre] = [telefono, email]
            print("\n\t\tContacto modificado correctamente. \U0001F389")
        else:
            print("\n\t\tEl contacto no existe. \u26A0")
        espere_tecla()


