''' 
Crear un proyecto que permita gestionar (Administrar) peliculas, colocar un menu de opciones para agregar,
eliminar, modificar y consultar peliculas.
Notas: 
1.-Utilizar funciones y mandarlas llamar desde otro archivo
2.-Utilizar listas para almacenar los nombres de las peliculas 
3.-
'''
import peliculas_dago
import os

peliculas_dago.limpiar()
pelicula=[]
opcion=True
while opcion:
    print(f"\n\t\t\t Selecciona una opcion: \n\t\t1)Agregar una pelicula\n\t\t2)Eliminar una pelicula"
                 "\n\t\t3)Modificar una pelicula\n\t\t4)Consultar las peliculas\n\t\t5)Buscar pelicula\n\t\t6)Borrar todo\n\t\t7)Salir\n ")
    opcion=input("Selecciona una opcion: ")

    match opcion:
        case "1":
            peliculas_dago.agregarPeliculas()
            peliculas_dago.esperarTecla()
        case "2":
            
            peliculas_dago.eliminarPeliculas()
            peliculas_dago.esperarTecla()
        case "3":
            peliculas_dago.actualizarPeliculas()
            peliculas_dago.esperarTecla()
        
        case "4":
            peliculas_dago.consultarPeliculas()
            peliculas_dago.esperarTecla()
        case "5":
             peliculas_dago.buscarPeliculas()
             peliculas_dago.esperarTecla()
        case "6": 
            peliculas_dago.vaciarPeliculas()
            peliculas_dago.esperarTecla()
        case "7":
            peliculas_dago.limpiar() 
            print("\t\tSaldra")
            peliculas_dago.esperarTecla()
                
            opcion=False
        case _:
            print("Error")              

