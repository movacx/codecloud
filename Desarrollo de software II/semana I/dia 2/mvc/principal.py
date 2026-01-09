#Es el encargado de llamar los archivos view

#Comento hacer un calculadora
#datoa, datob, resultado

from controller.calculadoraController import calculadoraController
from controller.personaController import personaController

def principal():

    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    genero = input("Ingrese su genero: ")


    datoa = int(input("Ingresa el datoa: "))
    datob = int(input("Ingresa el datob: "))

    _personaController = personaController()
    modelo_personaModel = _personaController.crearPersona(nombre, edad, genero)
    

    _calculadoraController = calculadoraController()
    modelo_calculadoraModell = _calculadoraController.agregardatos(datoa, datob)
    print("\n=== Operaciones en MVC===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcion = int(input("Seleccione una operacion (1-4): "))
    _calculadoraController.operaciones(modelo_calculadoraModell, opcion)
    _calculadoraController.presntardatos(modelo_calculadoraModell)

    _personaController.mostrarDatos(modelo_personaModel)

principal()