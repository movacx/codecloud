#Participantes: 
#Herlin Fabian Chavarria Beita C5E187
#Joseph Campos C4D660
#David Mora Gomez C5H441

from Controller.estudianteController import EstudianteController
from Controller.profesorController import ProfesorController
from Controller.cursosController import CursosController



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
                  continue   
            elif opcion == 2:
                 continue
            elif opcion == 3:
                 continue
            elif opcion == 4:
                  print("Saliendo del sistema")
                  break
            else:
                  print("Opcion Invalida [1-4]")
                  
      return " "
            
print(main())