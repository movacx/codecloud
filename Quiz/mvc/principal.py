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
                  View.estudianteView.gestionEstudiante()
                  opcionEstudiantes = int(input("input: "))
                  if opcionEstudiantes == 1:
                        nuevoEstudiante.agregarEstudiante("Fabian",22,"Septimo","Herlin.chavarria@gmail.com")
                        nuevoEstudiante.agregarEstudiante("David",19,"Octavo","David.Mora@ucr.ac.cr")
                        nuevoEstudiante.agregarEstudiante("Joseph",30,"Noveno","Joseph.Campos")
                        continue
                  
                  elif opcionEstudiantes == 2:
                        nuevoEstudiante.mostrarDatos()
                        continue
                  elif opcionEstudiantes == 3:
                        nuevoEstudiante.buscarEstudiante("Fabian")
                        continue
                  
                  elif opcionEstudiantes == 4:
                        buscarEst = input("Ingrese el nombre del estudiante a encontrar: ")
                        nuevoEstudiante.buscarEstudiante(buscarEst)
                        View.estudianteView.MenuModificacion()
                        seleccion = int(input("Input: "))
                        if seleccion == 1:
                              nuevoDato = input("Ingrese el nuevo dato a registrar: ") 
                              nuevoEstudiante.modificarEstudiante(buscarEst,nuevoDato,seleccion)
                              continue
                        elif seleccion == 2:
                              nuevoDato = input("Ingrese el nuevo dato a registrar: ") 
                              nuevoEstudiante.modificarEstudiante(buscarEst,nuevoDato,seleccion)
                              continue
                        elif seleccion == 3:
                              nuevoDato = input("Ingrese el nuevo dato a registrar: ")
                              nuevoEstudiante.modificarEstudiante(buscarEst,nuevoDato,seleccion)
                              continue
                        elif seleccion == 4:
                              nuevoDato = input("Ingrese el nuevo dato a registrar: ")
                              nuevoEstudiante.modificarEstudiante(buscarEst,nuevoDato,seleccion)
                              continue
                        elif seleccion == 0:
                              continue
                        else:
                              print("Opcion invalida [Valores dentro de 1-4]")
                        
                  elif opcionEstudiantes == 5:
                        eliminarEstudiante = input("Ingrese el nombre del estudiante a encontrar: ")
                        nuevoEstudiante.eliminarEstudiante(eliminarEstudiante)
                        continue
                  elif opcionEstudiantes == 6:
                        continue
                  else:
                        print("Opcion invalida")
                  
                  continue
            elif opcion == 2:
                  
                  View.profesorView.gestionProfesor()
                  opcionProfesor = int(input("Input: "))
                  if opcionProfesor == 1:
                        nuevoProfesor.agregarProfesor("Marcos",64580060,"marcos123@gmail.com")
                        nuevoProfesor.agregarProfesor("Irwin",4545334, "irwin456@gmail.com")
                        nuevoProfesor.agregarProfesor("Matt",989180, "matt056@gmail.com")

                  elif opcionProfesor == 2:
                        nuevoProfesor.mostrarDatos()

                  elif opcionProfesor == 3:
                        nuevoProfesor.buscarProfesor("Marcos")

                  elif opcionProfesor == 4:
                        
                        nuevoProfesor.eliminarProfesor(nuevoProfesor)


                  continue
            elif opcion == 3:
                  
                  continue
            elif opcion == 4:
                  break


            else:
                  print("Opcion Invalida [1-4]")
                  
      return " "
            
print(main())
