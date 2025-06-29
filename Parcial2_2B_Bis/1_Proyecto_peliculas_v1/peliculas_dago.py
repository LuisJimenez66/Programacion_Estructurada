#1.- Funcion que no recibe parametros y no regresa valor
import os
peliculas=[]

def limpiar():
    os.system("cls")

def esperarTecla():
    input("\n\tTeclee una tecla para continuar")

def consultarPeliculas ():
    limpiar()
    print("\n\tConsultar o mostrar peliculas")
    if len(peliculas)>0:
        for i in range (0,len(peliculas)):
            print(f"\n\t{i+1}: {peliculas[i]}")
    else:
        print("\n\tNo hay peliculas en el sistema")        

def agregarPeliculas():

    limpiar()
    print("\t\nAlta de peliculas")
    peliculas.append(input("Agrege una pelicula:\n").upper().strip())
    input("\t\nLa operacion se realizo con exito")
    
def vaciarPeliculas():
    limpiar()
    print("\n\tBorrar todas las peliculas")
    resp=input("\n\tDeseas borrar todas las peliculas del sistema? SI/NO\n").upper()
    if resp=="SI":
        peliculas.clear()
        input("\t\nLa operacion se realizo con exito")
    else:
        print("\n\tOk")    
    
def buscarPeliculas():
    limpiar()
    print("\t\nBusqueda de peliculas")
    pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar\n").upper().strip()
    encontro=0
    if not(pelicula_buscar in peliculas):
        print("\n\tNo se encuntra la pelicula a buscar ")
    else:
        for i in range(0,len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                print(f"\n\tLa pelicula {pelicula_buscar} si la tenemos y esta en la casilla: {i+1}")
                encontro+=1
        if encontro>0:
            print(f"\n\tTenemos {encontro} peliculas(s) con este titulo")
            input("\t\nLa operacion se realizo con exito")        


'''
def eliminarPeliculas ():
    limpiar()
    print("\t\nEliminar peliculas")
    pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar\n").upper().strip()
    encontro=0
    borro=0
    if not(pelicula_buscar in peliculas):
        print("\n\tNo se encuntra la pelicula a buscar ")
    else:
        for i in range(0,len(peliculas)):
            if pelicula_buscar in peliculas:
                borrar=input("Desea borrar la pelicula? SI/NO").upper()
                if borrar == "SI":
                    peliculas.remove(pelicula_buscar)
                    print(f"\n\tLa pelicula que se borro es: {pelicula_buscar} y estaba en la casilla: {i+1}")
                    encontro+=1
                    borro+=1
                    if encontro>1:
                        for j in range (0,encontro):
                            borrar=input("Desea borrar la pelicula? SI/NO").upper()
                            if borrar == "SI":
                                peliculas.remove(pelicula_buscar)
                                print(f"\n\tLa pelicula que se borro es: {pelicula_buscar} y estaba en la casilla: {i+1}")
                                borro+=1
                            else:
                                print("ok")
                                break         
                else:
                    print("ok")
                    break
        print(f"la pelicula se borro {borro} veces")                   
'''
def eliminarPeliculas():
    limpiar()
    print("\n\tEliminar películas")
    pelicula_buscar = input("Ingrese el nombre de la película a buscar:\n").strip().upper()

    borro = 0
    while i < len(peliculas):
        if peliculas[i].upper() == pelicula_buscar:
            respuesta = input(f"¿Desea eliminar la película '{peliculas[i]}' en la posición {i + 1}? (SI/NO): ").strip().upper()
            if respuesta == "SI":
                print(f"\n\tLa película '{peliculas[i]}' fue eliminada de la posición {i + 1}.")
                peliculas.pop(i)
                borro += 1
                # No aumentamos i porque la lista se ha reducido
                continue
        i += 1

    if borro == 0:
        print("\n\tNo se eliminó ninguna película.")
    else:
        print(f"\n\tSe eliminaron {borro} película(s) llamada(s) '{pelicula_buscar}'.")

        


respuesta2 = ""
def actualizarPeliculas():
    limpiar()
    print("\n\tModificar películas")
    pelicula_buscar = input("Ingrese el nombre de la película a modificar:\n").strip().upper()
    while i < len(peliculas):
        if peliculas[i] == pelicula_buscar:
            respuesta = input(f"¿Desea modificar la película '{peliculas[i]}' en la posición {i + 1}? (SI/NO): ").strip().upper()
            if respuesta == "SI":
                respuesta2 = input(f"Ingresa la nueva pelicula ").strip().upper()
                peliculas[i] = respuesta2
                print(f"\n\tLa película '{peliculas[i]}' fue modificada en la posición {i + 1}.")
                peliculas.pop(i)
                borro += 1
                continue
        i += 1

    if borro == 0:
        print("\n\tNo se eliminó ninguna película.")
    else:
        print(f"\n\tSe eliminaron {borro} película(s) llamada(s) '{pelicula_buscar}'.")



