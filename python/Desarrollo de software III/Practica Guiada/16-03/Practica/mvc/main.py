from View.vista import Vista
from Controller.controlador import Controlador
def main():
    vista = Vista()
    manejo = Controlador()


    while True:
        opcion = vista.mostrar_menu()
        if opcion == 1:
            carnet = input('Ingrese el carnet: ')
            nombre = input('Ingrese el nombre: ')
            carrera = input('Ingrese la carrera: ')
            manejo.agregar_estudiantes(carnet, nombre, carrera)
            pass
        elif opcion == 2:
            sigla = input('Ingrese la sigla del curso: ')
            nombreCurso = input('Ingrese el nombre del curso')
            creditos = input('Ingrese los creditos: ')
            manejo.agregar_curso(sigla, nombreCurso, creditos)
            pass
        elif opcion == 3:
            sigla = input('Ingrese la sigla del curso a matricular: ')
            carnet = input('Ingrese el carnet del estudiante a matricular: ')
            manejo.registrar_matricula(sigla, carnet)

            pass
        elif opcion == 4:
            manejo.consultar_estudiantes()
            pass
        elif opcion == 5:
            manejo.consultar_cursos()
            pass
        elif opcion == 6:
            manejo.consultar_matriculas()
            pass
        elif opcion == 7:
            carnet = input('Ingrese el carnet: ')
            manejo.buscarEstudiante(carnet)
        elif opcion == 0:
            vista.mostrar_mensaje("Saliendo del sistema")
            SystemExit(0)


if __name__ == "__main__":
    main()