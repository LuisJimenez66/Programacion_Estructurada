'''
dict:
Es un tipo de dato que se utiliza para almacenar datos de diferente tipo de datos para 
en lugar de tener mono las listas indices numericos tine alphanumericos es decir 
que es algo parecido como los objetos

Tambien se conoce como un arreglo asosiativo u objeto JSON

El diccionario es una coleccion ordenada y modificable. No hay miembros duplicados
'''
import os
os.system("cls")

paises_mx={"Nombre":"Mexico",
           "Capital":"CDMX",
           "Poblacion":126000000,
           "idioma":"Espagnol",
           "status":True
           }

pais_br={"Nombre":"Brasil",
           "Capital":"Brasilia",
           "Poblacion":213000000,
           "idioma":"Portugues",
           "status":True
           }

pais_canada={"Nombre":"Canada",
             "Capital":"Ottawa",
             "Poblacion":38000000,
             "Idioma":("Ingles","Frances"),
             "status":True
             }

alumno1={"Nombre":"Daniel",
         "Apellido1":"Hernandez",
         "Apellido2":"Gonzalez",
         "Carrera": "TI",
         "Matricula": "3141240113",
         "area":"Software multiplataforma",
         "modalidad":"Bilingue",
         "Semestre": 2,
         }
#Mostrar el diccionario
print(alumno1)
for i in alumno1:
    print(f"{i}={alumno1[i]}")

#Agregar un campo o atributo
alumno1["telefono"]="6182345678"
for i in alumno1:
    print(f"{i}={alumno1[i]}")