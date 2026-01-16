import Controller.estudianteController

almacen = Controller.estudianteController.agregarEstudiante("Fabian",22,"Quinto Grado", "Fabianfsf@gmail.com")
print(almacen)
almacenDos = Controller.estudianteController.agregarEstudiante("David",19,"Sexto Grado", "Davod@gmail.com")
print(almacenDos)


Controller.estudianteController.mostrarDatos()

buscarEstudiante = input("Ingrese el nombre del estudiante a modificar: ")
print("""Modificar MenuTest
      1. Modificar Nombre
      2. Modificar Edad
      3. Modificar Grado
      4. Modificar Correo""")
opcion = int(input("input: "))
nuevoDato = input("Ingrese el nuevo dato: ")

modificar = Controller.estudianteController.modificarEstudiante(buscarEstudiante,nuevoDato,opcion)
print(modificar)


Controller.estudianteController.mostrarDatos()