#Crear una lista de numeros e imprimir el contenido.
import os
lista=[1,2,3,4,5,6,7,8,9]
#Primer forma
print(lista)

#Segunda forma
for i in lista:
    print(i)

#Tercer forma
for i in range(0,len(lista)):
    print(lista[i])
os.system("cls")
#Crear una lista de palabras y posteriormente buscar las coincidencias de una palabra
palabras=["hola","adios","salud","carlos","hola"]
palabra_buscar=input("Dame la palabra a buscar: ")
#Primer forma
if palabra_buscar in palabras:
    print("Si se encontro la palabra")
    
else:
    print ("No se encontro la palabra")   
veces=palabras.count(palabra_buscar)
print(f"Se encontro la palabra {veces} veces")
#Segunda forma

encontro=False
for j in palabras:
    if j==palabra_buscar:
        encontro=True
if encontro:

    print("Si se encontro la palabra")
else:
    print("No se encontro la palabra")        
#Tercer forma
posi=0
si=0

for i in range(0,len(palabras)):
    if palabras[i]==palabra_buscar:
        encontro=True
        si=si+1
        i=posi

if encontro:
    print("Si se encontro la palabra")
    print(f"Un total de {si} veces")
else:
    print("No se encontro la palabra")   

input("Oprime una tecla para continuar")  
#Añadir elementos a la lista
os.system("cls")
numeros=[]
opc=True
while opc:
    numero=float(input("Dame un numero "))
    numeros.append(numero)
    desicion=input("Desea agreagar otro numero? ").upper()
    if desicion=="SI":
        opc=True
    else:
        opc=False

print(numeros)

input("Oprime una tecla para continuar")  
#Crear una lista multidimensional que sea una agenda
agenda=[
    ["Carlos","6182345678"],
    ["Alvaro","6667575439"],
    ["Martin","6189345678"]
    ]
print(agenda)
for i in agenda:
    print (i)

for i in range(0,3):
    for j in range(0,2):
        print(agenda [i][j])    

cadena=""
for i in range(0,3):
    for j in range(0,2):
        cadena+=f"{agenda [i] [j]}, "
    cadena+="\n"
print(cadena)
                