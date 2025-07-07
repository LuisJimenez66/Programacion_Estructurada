''' 
Crear un proyecto que permita gestionar (Administrar) peliculas, colocar un menu de opciones para agregar,
eliminar, modificar y consultar peliculas.
Notas: 
1.-Utilizar funciones y mandarlas llamar desde otro archivo
2.-Utilizar dict para almacenar los atributos de las peliculas [nombre, Categoria, Clasificacion, Genero, Idioma]
3.-
'''
import peliculas_dago
import os

peliculas_dago.limpiar()
pelicula=[]
opcion=True
while opcion:
    print(f"\n\t\t\t Selecciona una opcion: \n\t\t1)Crear\n\t\t2)Borrar"
                 "\n\t\t3)Mostrar\n\t\t4)Agregar caracteristicas\n\t\t5)Modificar caracteristicas\n\t\t6)Borrar caracteristicas\n\t\t7)Salir\n ")
    opcion=input("Selecciona una opcion: ")

    match opcion:
        case "1":
            peliculas_dago.CrearPeliculas()
            peliculas_dago.esperarTecla()
        case "2":
            
            peliculas_dago.BorrarPeliculas()
            peliculas_dago.esperarTecla()
        case "3":
            peliculas_dago.MostrarPeliculas()
            peliculas_dago.esperarTecla()
        
        case "4":
            peliculas_dago.AgregarCaracteristicasPeliculas()
            peliculas_dago.esperarTecla()
        case "5":
             peliculas_dago.ModificarCaracteristicasPeliculas()
             peliculas_dago.esperarTecla()
        case "6": 
            peliculas_dago.BorrarCaracteristicasPeliculas()
            peliculas_dago.esperarTecla()
        case "7":
            peliculas_dago.limpiar() 
            print("\t\tSaldra")
            peliculas_dago.esperarTecla()
                
            opcion=False
        case _:
            print("Error")              

