#Un alumno es profesor
#Un alumno es asistente
#(A) pedir la edad de los compañeros que vinieron hoy a clases y ordenar los datos de menor a mayor
#(B) El mayor de la clase es el profesor y el menor es el asistente: ¿Quien es quien?
 
lista_nombres = list([])
lista_edad = list([])

def agregarEstudiante(nombre,edad):
    lista_nombres.append(nombre)
    lista_edad.append(edad)

def ver_mayor_menor(lista_edad):
    maximo = lista_edad[0]
    minimo = lista_edad[0]
    
    nombreMax = lista_nombres[0] 
    nombreMin = lista_nombres[0]
    
    for indice in range(len(lista_edad)):
        if lista_edad[indice] > maximo:
            maximo = lista_edad[indice]
            nombreMax = lista_nombres[indice]
            
        elif lista_edad[indice] < minimo:
            minimo = lista_edad[indice]
            nombreMin = lista_nombres[indice]
    return maximo, minimo, nombreMax, nombreMin

contadoro = 0
while contadoro < 10:
    print("\n1. Registrar estudiante", 
        "\n2. Ver estudiante con la edad mas alta",
        "\n3. Ver el estudiante con menor edad",
        "\n4. Resumen ¿Quien es el profesor y el asistente?"
        "\n0. Salir")
    opcion = int(input("Seleccione una opcion: "))
    
    if opcion == 1:
        nombreEstudiante = input("Ingrese el nombre del estudiante: ")
        edadEstudiante = input("Ingrese la edad: ")
        agregarEstudiante(nombreEstudiante,edadEstudiante)
    
    elif opcion == 2:
        maximo,minimo,nombreMax,nombreMin = ver_mayor_menor(lista_edad)
        print(nombreMax,maximo)
            
    elif opcion == 3:
        maximo,minimo,nombreMax,nombreMin = ver_mayor_menor(lista_edad)
        print(nombreMin,minimo)      
        
    elif opcion == 4:
        maximo,minimo,nombreMax,nombreMin = ver_mayor_menor(lista_edad)
        print(f"El profesor es {nombreMax} con {maximo} años, y el asistente es {nombreMin} con {minimo} años")
    elif opcion == 0:
        print("Saliendo del sistema")
        print(lista_nombres)
        print(lista_edad)
        exit(0)
    else:
        print("opcion invalida")
    
















    