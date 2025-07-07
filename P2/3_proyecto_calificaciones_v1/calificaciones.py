def limpiarPantalla():
    import os
    os.system('cls')

def esperarTecla():
    input("\n\t\u270BPresione una tecla para continuar\u270B  ")    

def AgregarCalificaciones(lista):
    limpiarPantalla()
    print("\n\t\t\t\U0001F4BE ..::Agregar Calificaciones::.. \U0001F4BE\n")
    nombre = input("\U0001F4DD Nombre del alumno:  ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        continua=True
        while continua:
            try:
                cal=float(input(f"\U0001F4DD Calificacion {i}: "))
                if cal>=0 and cal<10.1:
                    calificaciones.append(cal)
                    continua=False
                else:
                    input("\u26A0 Ingresa un numero valido \u26A0  ")    
            except ValueError:
                input("\u26A0 Ingrese un valor numerico \u26A0  ")
    lista.append([nombre]+calificaciones)
    input("\U0001F389 Accion realizada con exito \U0001F389")                     
   

def ConsultarCalificaciones(lista):
    limpiarPantalla()
    print("\n\t\t\t\U0001F50D ..::Consultar calificaciones::.. \U0001F50D")
    if len(lista)>0:
        print(f"\n\t{'Nombre':<15}{'Calf. 1':<10}{'Calf. 2':<10}{'Calf. 3':<10}")
        print(f"\t {'-'*40}")
        for fila in lista:
            print(f"\t{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
        print(f"\t {'-'*40}")
        cuantos=len(lista)
        print(f"\n\tSon: {cuantos} alumnos\U0001F4C2")
    else:
        print("\n\t\u26A0 No hay calificaciones en el sistema \u26A0")



def CalcularPromedio(lista):
    limpiarPantalla()
    print("\n\t\t\t\U0001F9EE ..::PROMEDIOS::.. \U0001F9EE")
    if len(lista) > 0:
        print(f"\n\t{'Nombre':<15}{'Promedio':<10}")
        print(f"\t {'-'*30}")
        promedioTot=0
        promedio=0
        for fila in lista:
            promedio = (sum(fila[1:])) / 3
            print(f"\t{fila[0]:<15}{promedio:<10.2f}")
            promedioTot+=promedio
        promedioTot= promedioTot/(len(lista))
        print(f"\t {'-'*30}")
        print(f"\n\t\U0001F389 El promedio de los alumnos es: {promedioTot:.2f} \U0001F389")
        print(f"\t {'-'*30}")
    else:
        print("\n\t\u26A0 No hay calificaciones en el sistema \u26A0")    
          

def CalcularPromedio2(lista):
    print("\t\t\U0001F552 PROMEDIOS \U0001F552")
    if len(lista) > 0:
        print(f"\n\t{'Nombre':<15}{'Promedio':<10}")
        print(f"\t {'-'*30}")
        promedioTot=0
        promedio=0
        suma=0
        i=1
        for fila in lista:
            print(f"\t{fila[0]:<15}{promedio:<10.2f}")
            while i < 4:
                suma += fila[i]
                i += 1
            promedio = suma / 3
            promedioTot += promedio
            print(f"\t{fila[0]:<15}{promedio:<10.2}")   
        promedioTot= promedioTot/(len(lista))
        print(f"\t {'-'*30}")
        print(f"\n\t\U0001F389 El promedio de los alumnos es: {promedioTot:.2f} \U0001F389")
        print(f"\t {'-'*30}")
    else:
        print("\n\t\u26A0 No hay calificaciones en el sistema \u26A0")    
              
def menuPrincipal():
    print(f"\n\t\t\t\U0001F4DD..::Sistema de Gestion De Calificaciones::..\U0001F4DD \n\t\t1\ufe0f\u20e3  Agregar calificaciones\n\t\t2\ufe0f\u20e3  Consultar calificaciones"
                 "\n\t\t3\ufe0f\u20e3  Calcular promedio\n\t\t4\ufe0f\u20e3  Buscar\n\n\t\t5\ufe0f\u20e3  Salir\n ")
    opcion=input("\n\t\t\U0001F449  Selecciona una opcion: (1-5): ")
    return opcion

def Buscar(datos):
    limpiarPantalla()
    print("\n\t\t\t\U0001F50D ..::Buscar Calificaciones::.. \U0001F50D")
    if len(datos) > 0:
        nombre = input("\U0001F4DD Nombre del alumno a buscar: ").upper().strip()
        encontrado = False
        for fila in datos:
            if fila[0] == nombre:
                print(f"\n\t{'Nombre':<15}{'Calf. 1':<10}{'Calf. 2':<10}{'Calf. 3':<10}")
                print(f"\t {'-'*40}")
                print(f"\t{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
                print(f"\t {'-'*40}")
                encontrado = True
                break
        if not encontrado:
            print(f"\n\t\u26A0 El alumno {nombre} no se encuentra en el sistema \u26A0")
    else:
        print("\n\t\u26A0 No hay calificaciones en el sistema \u26A0")

'''
def main():
    datos=[]
    opcion=True
    while opcion:
        calificaciones.limpiarPantalla()
        opcion = calificaciones.menuPrincipal()

        match opcion:
            case "1":
                calificaciones.AgregarCalificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                
                calificaciones.ConsultarCalificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.CalcularPromedio(datos)
                calificaciones.esperarTecla()
            case "4":
                calificaciones.limpiarPantalla() 
                print("\t\tSaldra")
                print("\t\tTermino la ejecucion del SW")
                calificaciones.esperarTecla()
                
                opcion=False
            case _:
                print("\u26A0 Opcion no valida, oprima cualquier tecla para continuar")              
'''

