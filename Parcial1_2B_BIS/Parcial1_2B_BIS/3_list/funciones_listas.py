'''
List (Array)
Son colleciones o conjuntos de datos/valores bajo un mismo nombre
para acceder a los valores que hace con un indice numerico

Nota: Sus valores si son modificables

La lista es una collecion ordenada y modificable.
Permite miebros duplicados
'''
#Funciones mas comunes con listas.
paises=["Mexico", "Brasil","España","Canada"]
numeros=[23,12,100,34]
#ordenar ascendentemente
print(numeros)
numeros.sort()
print(numeros)
print(paises)
paises.sort()
print(paises)
#Añadir o ingresar o insertar elementos a una lista
#Primer forma
paises.append("Honduras")
print(paises)
#Segunda forma
paises.insert(1,"Honduras")
print(paises)
#Eliminar o borrar elementos a una lista
#Primer forma
paises.pop(1)
print(paises)
#Segunda forma
paises.remove("Honduras")
print(paises)
#Buscar elemento dentro de la lista
#Primer Forma
resp="Brasil" in paises
if resp==True:
    print("Si se encontro el pais")
else:
    print ("No se encontro el pais")    
#Segunda forma
pais_buscar=input("Dame el pais a buscar")
for i in range(0,len(paises)):
    if paises[i]==pais_buscar:
        print("Si se encontro el pais")
    else:
        print ("No se encontro el pais")  

#Cuantas veces aparece un numero dentro de la lista
#numeros=[23,12,100,34]
numeros=[23,12,100,34]
print(f"Este numero 12 aparece: {numeros.count(12)} vez o veces")

numeros.append(12)
print(f"Este numero 12 aparece: {numeros.count(12)} vez o veces")

numeros.append(12)
#identificar o conocer el indice de un valor
indice=paises.index("España")
print(indice)
paises.pop(indice)
print(paises)
#Recorrer los valores de la lista
for i in paises:
    print(i)
#Segunda forma 
for i in range(0, len(paises)):
    print(f"El valor {i} es: {paises[i]}")   

#Unir contenido de listas
print(paises)
print(numeros)
paises.extend(numeros)
print(paises)