# Participantes: 
# Herlin Fabian Chavarria Beita C5E187
# Joseph Campos C4D660
# David Mora Gomez C5H441

from controller.estudianteController import EstudianteController
from controller.profesorController import ProfesorController
from controller.cursosController import CursosController

import view.estudianteView
import view.profesorView
import view.cursosView

# Instancias
nuevoEstudiante = EstudianteController()
nuevoProfesor = ProfesorController()
nuevoCurso = CursosController()

def main():
    while True:
        print("\n===============================")
        print("   SISTEMA DE GESTIÓN ESCOLAR")
        print("===============================")
        print("1. Gestión de Estudiantes")
        print("2. Gestión de Profesores")
        print("3. Gestión de Cursos")
        print("4. Salir")
        
        opcionMenuPrincipal = int(input("Ingrese una opción: "))
        
        # =========================================================
        # GESTIÓN DE ESTUDIANTES
        # =========================================================
        if opcionMenuPrincipal == 1:
            while True:
                view.estudianteView.gestionEstudiante()
                opcionEstudiantes = int(input("input: "))
                
                if opcionEstudiantes == 1:
                    print("\n--- REGISTRO DE ESTUDIANTE ---")
                    # Pedimos los datos uno por uno con variables claras
                    nombreEstudiante = input("Nombre: ")
                    apellidosEstudiante = input("Apellidos: ")
                    edadEstudiante = int(input("Edad: "))
                    telefonoEstudiante = int(input("Teléfono: "))
                    direccionEstudiante = input("Dirección: ")
                    fechaNacimientoEst = input("Fecha Nacimiento (DD/MM/AAAA): ")
                    gradoEstudiante = input("Grado: ")
                    correoEstudiante = input("Correo: ")
                    
                    # Llamamos al controlador con todos los datos
                    nuevoEstudiante.agregarEstudiante(nombreEstudiante, apellidosEstudiante, edadEstudiante, telefonoEstudiante, direccionEstudiante, fechaNacimientoEst, gradoEstudiante, correoEstudiante)
                
                elif opcionEstudiantes == 2:
                    nuevoEstudiante.mostrarDatos()
                    
                elif opcionEstudiantes == 3:
                    buscarEst = input("Ingrese el nombre a buscar: ")
                    nuevoEstudiante.buscarEstudiante(buscarEst)
                    
                elif opcionEstudiantes == 4:
                    modificarEst = input("Ingrese el nombre del estudiante a modificar: ")
                    view.estudianteView.MenuModificacion()
                    seleccionModificar = int(input("Input: "))
                    
                    if seleccionModificar != 0:
                        nuevoDato = input("Ingrese el nuevo dato: ")
                        nuevoEstudiante.modificarEstudiante(modificarEst, nuevoDato, seleccionModificar)
                        
                elif opcionEstudiantes == 5:
                    eliminarEst = input("Ingrese el nombre del estudiante a eliminar: ")
                    nuevoEstudiante.eliminarEstudiante(eliminarEst)
                    
                elif opcionEstudiantes == 6:
                    break # Salir del while de estudiantes
                else:
                    print("Opción inválida")

        # =========================================================
        # GESTIÓN DE PROFESORES
        # =========================================================
        elif opcionMenuPrincipal == 2:
            while True:
                view.profesorView.gestionProfesor()
                opcionProfesores = int(input("input: "))
                
                if opcionProfesores == 1:
                    print("\n--- REGISTRO DE PROFESOR ---")
                    nombreProfesor = input("Nombre: ")
                    apellidosProfesor = input("Apellidos: ")
                    especialidadProfesor = input("Especialidad: ")
                    telefonoProfesor = int(input("Teléfono: "))
                    direccionProfesor = input("Dirección: ")
                    fechaNacimientoProf = input("Fecha Nacimiento: ")
                    correoProfesor = input("Correo: ")
                    
                    nuevoProfesor.agregarProfesor(nombreProfesor, apellidosProfesor, especialidadProfesor, telefonoProfesor, direccionProfesor, fechaNacimientoProf, correoProfesor)

                elif opcionProfesores == 2:
                    nuevoProfesor.mostrarDatos()

                elif opcionProfesores == 3:
                    modificarProfe = input("Ingrese el nombre del profesor a modificar: ")
                    view.profesorView.MenuModificacion()
                    seleccionModificar = int(input("Input: "))
                    
                    if seleccionModificar != 0:
                        nuevoDato = input("Ingrese el nuevo dato: ")
                        nuevoProfesor.modificarProfesor(modificarProfe, nuevoDato, seleccionModificar)

                elif opcionProfesores == 4:
                    eliminarProfe = input("Ingrese el nombre del profesor a eliminar: ")
                    nuevoProfesor.eliminarProfesor(eliminarProfe)
                    
                elif opcionProfesores == 5:
                    break
                else:
                    print("Opción inválida")

        # =========================================================
        # GESTIÓN DE CURSOS
        # =========================================================
        elif opcionMenuPrincipal == 3:
            while True:
                view.cursosView.gestionCursos()
                opcionCursos = int(input("input: "))
                
                if opcionCursos == 1:
                    print("\n--- NUEVO CURSO ---")
                    nombreCurso = input("Nombre del Curso: ")
                    codigoCurso = int(input("Código del Curso: "))
                    profesorAsignado = input("Nombre del Profesor Asignado: ")
                    
                    nuevoCurso.agregarCurso(nombreCurso, codigoCurso, profesorAsignado)
                    
                elif opcionCursos == 2:
                    nuevoCurso.mostrarDatos()

                elif opcionCursos == 3:
                    modificarCurso = input("Ingrese el nombre del curso a modificar: ")
                    view.cursosView.MenuModificacion()
                    seleccionModificar = int(input("Input: "))
                    
                    if seleccionModificar != 0:
                        nuevoDato = input("Ingrese el nuevo dato: ")
                        nuevoCurso.modificarCursos(modificarCurso, nuevoDato, seleccionModificar)

                elif opcionCursos == 4:
                    eliminarCurso = input("Ingrese el nombre del curso a eliminar: ")
                    nuevoCurso.eliminarCursos(eliminarCurso)
                    
                elif opcionCursos == 5:
                    break
                else:
                    print("Opción inválida")

        # =========================================================
        # SALIR
        # =========================================================
        elif opcionMenuPrincipal == 4:
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción Inválida")

if __name__ == "__main__":
    main()