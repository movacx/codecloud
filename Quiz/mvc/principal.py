from Controller.estudianteController import EstudianteController
from Controller.profesorController import ProfesorController
from Controller.cursosController import CursosController
nuevoEstudiante = EstudianteController()
nuevoProfesor = ProfesorController()
nuevoCurso = CursosController()


nuevoCurso.agregarCurso("Info", "d", "d")
variableTres = nuevoCurso.mostrarDatos()

nuevoEstudiante.agregarEstudiante("Fabian",19,"sexto","XD")
variable = nuevoEstudiante.mostrarDatos()

nuevoProfesor.agregarProfesor("Irwin", "Profesor", 894785, "iw@fsfas")
variableDos = nuevoProfesor.mostrarDatos()
print(variable)
print(variableDos)
print(variableTres)









def gestionEstudiante():
      while True:
            opcion = int(input("""
            1. Registrar estudiante
            2. Listar estudiantes
            3. Buscar estudiante
            4. Actualizar estudiante
            5. Eliminar estudiante
            6. Volver
            input: """))
            
            if opcion == 1:
                  continue
            elif opcion == 2:
                  continue
            elif opcion == 3:
                  continue
            elif opcion == 4:
                  continue
            elif opcion == 5:
                  continue
            elif opcion == 6:
                  break
            else:
                  print("Opcion Invalida [1-4]")
                  
      return " "


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
                  break
            else:
                  print("Opcion Invalida [1-4]")
                  
      return " "
            
print(main())
