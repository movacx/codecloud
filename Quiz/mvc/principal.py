from Controller.estudianteController import EstudianteController


def main():
      nuevoControler = EstudianteController()
      nuevoControler.agregarEstudiante("Fabian",22,"Sexto Grado", "FabianBeita31@gmail.com")
      nuevoControler.agregarEstudiante("David",19,"Materno", "David@gmail.com")
      
      
      #nuevoControler.eliminarEstudiante("Fabian")
      print(nuevoControler.mostrarDatos())
      
      nuevoControler.modificarEstudiante("Fabian","Joseph",3)
      print(nuevoControler.mostrarDatos())
      
      
print(main())