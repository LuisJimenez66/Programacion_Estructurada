''' 
Crear un proyecto que permita gestionar (Administrar) peliculas, colocar un menu de opciones para agregar,
eliminar, modificar y consultar peliculas.
Notas: 
1.-Utilizar funciones y mandarlas llamar desde otro archivo
2.-Utilizar listas para almacenar los nombres de las peliculas 
3.-
'''
import peliculas
import os

peliculas.limpiar()
pelicula=["Iron Man","Roma","Toy Story"]
volver=True
while volver:
    opcion=int(input(f"\t\t Selecciona una opcion: \n\t1)Agregar una pelicula\n\t2)Eliminar una pelicula"
                 "\n\t3)Modificar una pelicula\n\t4)Consultar las peliculas\n\t5)Buscar pelicula\n\t6)Borrar todo\n\t7)Salir\n "))


    if opcion < 1 or opcion>7:
        print("Opcion no valida")

    match opcion:
        case 1:
            peliculas.limpiar()
            print("\t\tAgregara una pelicula")
            peliculas.agregar()
        case 2:
            print("\t\tEliminara una pelicula")
            peliculas.eliminar()
        case 3:
            print("\t\tModificara una pelicula")
            
        case 4:
            print("\t\tConsultara las pelicula")
            peliculas.consultar()
        case 5:
             print("\t\tEncontrara una pelicula")
             peliculas.buscar()
        case 6: 
            print("Borrara toda la lista de peliculas")
            pelicula.clear()
        case 7:
            print("\t\tSaldra")      
            volver=False          

