#1 alumno es profesor
#1 alumno es asistente
#(A) pedir la edad de los compañeros que vinieron hoy a clases y ordenar los datos de menor a mayor
#(B) El mayor de la clase es el profesor y el menor es el asistente: ¿Quien es quien?
 

alumnos = list([])
contador_de_edad = 0
contador = 0
    
while contador < 10:
    contador_de_edad = edad_de_alumnos = int(input("Ingrese su edad: "))
    alumnos.append(contador_de_edad)
    if contador_de_edad == 0:
        break

print(alumnos)    

    