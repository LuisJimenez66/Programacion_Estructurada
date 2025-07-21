''' 
Crear un proyecto que permita gestionar (Administrar) peliculas, colocar un menu de opciones para agregar,
eliminar, modificar y consultar peliculas.
Notas: 
1.-Utilizar funciones y mandarlas llamar desde otro archivo
2.-Utilizar dict para almacenar los atributos de las peliculas [nombre, Categoria, Clasificacion, Genero, Idioma]
3.-Utilizar e implementar una base de datos para gestionar las peliculas
'''
import peliculas_dago
import os

peliculas_dago.limpiar()
pelicula=[]
opcion=True
while opcion:
    print(f"\n\t\t\t\U0001F50D Selecciona una opcion: \n\t\t1\ufe0f\u20e3  Crear\n\t\t2\ufe0f\u20e3  Borrar"
                 "\n\t\t3\ufe0f\u20e3  Mostrar\n\t\t4\ufe0f\u20e3  Modificar caracteristicas\n\t\t5\ufe0f\u20e3  Buscar\n\t\t6\ufe0f\u20e3  Salir\n ")
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
            peliculas_dago.ModificarPeliculas()
            peliculas_dago.esperarTecla()
        case "5":
            peliculas_dago.BuscarPeliculas()
            peliculas_dago.esperarTecla()    
        case "6":
            peliculas_dago.limpiar() 
            print("\t\tSaldra")
            peliculas_dago.esperarTecla()
                
            opcion=False
        case _:
            print("Error")              

