from Controller.estudianteController import EstudianteController


def main():
      nuevoControler = EstudianteController()
      nuevoControler.agregarEstudiante("Fabian",22,"Sexto Grado", "FabianBeita31@gmail.com")
      print(nuevoControler)

print(main())