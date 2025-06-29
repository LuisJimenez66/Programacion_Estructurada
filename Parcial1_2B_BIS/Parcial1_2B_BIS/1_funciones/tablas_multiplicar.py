'''Crear un programa que calucle e imprima la tabla de multiplicar del 2
    Requisitos:
     1.- Sin estructuras de control
     2.- Sin funciones

     print (f" 2X1= {2*1} \n 2X2= {2*2} \n 2X3= {2*3}\n 2X4= {2*4}\n 2X5= {2*5}\n 2X6= {2*6}\n 2X7= {2*7}\n 2X8= {2*8}\n 2X9= {2*9}\n 2X10= {2*10}")
'''

num=int(input("Ingresa un numero: "))
#Version 1::
multi=num*1
print (f"{num} X1 = {multi}")
multi=num*num
print (f"{num} X2 = {multi}")
multi=num*3
print (f"{num} X3 = {multi}")
multi=num*4
print (f"{num} X4 = {multi}")
multi=num*5
print (f"{num} X5 = {multi}")
multi=num*6
print (f"{num} X6 = {multi}")
multi=num*7
print (f"{num} X7 = {multi}")
multi=num*8
print (f"{num} X8 = {multi}")
multi=num*9
print (f"{num} X9 = {multi}")
multi=num*10
print (f"{num} X10 = {multi}")
'''
'''
#VERSION 2
for i in range(1,10+1,1):
    multi=num*i
    print(f"{num}X{i}={multi} ")
print("While:\n")
j=1
while j<11:
    multi=num*j
    print(f"{num}X{j}={multi} ")
    j=j+1

#VERSION 3
def tabla(num):
    num=num
    tabla1=""
    for i in range(1, 10+1,1):
        multi=num*i;
        tabla1+=f"{num} * {i} = {multi}\n"
    return tabla1
    
print(tabla(num))

