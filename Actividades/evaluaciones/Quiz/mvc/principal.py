#Participantes: 
#Herlin Fabian Chavarria Beita C5E187
#Joseph Campos C4D660
#David Mora Gomez C5H441

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
                  while True:
                        View.estudianteView.gestionEstudiante()
                        opcionEstudiantes = int(input("input: "))
                        if opcionEstudiantes == 1:
                              nuevoEstudiante.agregarEstudiante("Herlin",22,"Septimo","Herlin.chavarria@gmail.com")
                              nuevoEstudiante.agregarEstudiante("David",19,"Octavo","David.Mora@ucr.ac.cr")
                              nuevoEstudiante.agregarEstudiante("Joseph",30,"Noveno","Joseph.Campos")
                              continue
                        
                        elif opcionEstudiantes == 2:
                              nuevoEstudiante.mostrarDatos()
                              continue
                        elif opcionEstudiantes == 3:
                              buscarEstudiante = input("Ingrese el nombre a buscar: ")
                              nuevoEstudiante.buscarEstudiante(buscarEstudiante)
                              continue
                        
                        elif opcionEstudiantes == 4:
                              buscarEst = input("Ingrese el nombre del estudiante a encontrar: ")
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
                              eliminarEstudiante = input("Ingrese el nombre del estudiante a eliminar: ")
                              nuevoEstudiante.eliminarEstudiante(eliminarEstudiante)
                              continue
                        elif opcionEstudiantes == 6:
                              break
                        else:
                              print("Opcion invalida")
                        
                        
            elif opcion == 2:
                 while True:
                        View.profesorView.gestionProfesor()
                        opcionProfesor = int(input("Input: "))
                        if opcionProfesor == 1:
                              nuevoProfesor.agregarProfesor("Marcos","ProfeHumanidades",64580060,"marcos123@gmail.com")
                              nuevoProfesor.agregarProfesor("Irwin","ProfeIngles",4545334,"irwin456@gmail.com")
                              nuevoProfesor.agregarProfesor("Matt","ProfeProgra",989180,"matt056@gmail.com")

                        elif opcionProfesor == 2:
                              nuevoProfesor.mostrarDatos()

                        elif opcionProfesor == 3:
                              buscarProfesor = input("Digitie el profesor que desea modificar: ")
                              View.estudianteView.MenuModificacion()
                              seleccion = int(input("Input: "))

                              if seleccion == 1: 
                                    nuevoDato = input("Ingrese el nuevo dato a registrar: ")
                                    nuevoProfesor.modificarProfesor(buscarProfesor,nuevoDato,seleccion)
                                    continue
                              elif seleccion == 2: 
                                    nuevoDato = input("Ingrese el nuevo dato a registrar: ")
                                    nuevoProfesor.modificarProfesor(buscarProfesor,nuevoDato,seleccion)
                                    continue
                              elif seleccion == 3:
                                    nuevoDato = input("Ingrese el nuevo dato a registrar: ")
                                    nuevoProfesor.modificarProfesor(buscarProfesor,nuevoDato,seleccion)
                                    continue
                              elif seleccion == 4: 
                                    nuevoDato = input("Ingrese el nuevo dato a modificar")
                                    nuevoProfesor.modificarProfesor(buscarProfesor,nuevoDato,seleccion)
                                    continue

                        elif opcionProfesor == 4:
                              nuevoProfesor.eliminarProfesor("Irwin")
                        elif opcionProfesor == 5:
                              break
                        else:
                              print("Opcion invalida")

            elif opcion == 3:
                  while True:
                        View.cursosView.gestionCursos()
                        opcionCursos= int(input("Input:"))
                        if opcionCursos == 1:
                              nuevoCurso.agregarCurso("Mates",1111,"Fabri")
                              nuevoCurso.agregarCurso("Desa",1211,"Mario")
                              nuevoCurso.agregarCurso("Bases",1311,"Uma")
                              continue
                        elif opcionCursos == 2:
                              nuevoCurso.mostrarDatos()
                              continue

                        elif opcionCursos == 3:
                              cursoModificar = input("Ingrese el curso que desea modificar: ")
                              View.cursosView.MenuModificacion()
                              opcionModificar = int(input("Input: "))
                              if opcionModificar ==1:
                                    nuevoDato = input("Ingrese un nuevo dato: ")
                                    nuevoCurso.modificarCursos(cursoModificar,nuevoDato,opcionModificar)
                                    
                              elif opcionModificar == 2:
                                    nuevoDato = input("Ingrese un nuevo Codigo: ")
                                    nuevoCurso.modificarCursos(cursoModificar,nuevoDato,opcionModificar)
                              
                              elif opcionModificar == 3:
                                    nuevoDato = input("Ingrese un nuevo Profe: ")
                                    nuevoCurso.modificarCursos(cursoModificar,nuevoDato,opcionModificar)
                                    
                              else:
                                    print("Opcion invalida...")

                        elif opcionCursos == 4:
                              cursoEliminar=input("Que curso desea borrar: ")
                              nuevoCurso.eliminarCursos(cursoEliminar)
                              continue
                        elif opcionCursos == 5:

                              break
                        else:
                              print("Opcion invalida")
            

            elif opcion == 4:
                  print("Saliendo del sistema")
                  break


            else:
                  print("Opcion Invalida [1-4]")
                  
      return " "
            
print(main())