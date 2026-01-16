from Controller.estudianteController import EstudianteController
from Controller.profesorController import ProfesorController
from Controller.cursosController import CursosController

import View.cursosView
import View.estudianteView
import View.profesorView

nuevoEstudiante = EstudianteController()
nuevoProfesor = ProfesorController()
nuevoCurso = CursosController()







def main():
      while True:
            opcion = int(input("""
1. Gestión de Estudiantes
2. Gestión de Profesores
3. Gestión de Cursos
4. Salir 
input: """))
            
            if opcion == 1:
                  View.cursosView.gestionEstudiante()
                  opcionEstudiantes = int(input("input: "))
                  
                  continue
            elif opcion == 2:
                  continue
            elif opcion == 3:
                  continue
            elif opcion == 4:
                  break
            else:
                  print("Opcion Invalida [1-4]")
                  
      return " "
            
print(main())
