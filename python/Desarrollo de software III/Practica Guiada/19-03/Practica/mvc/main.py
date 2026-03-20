from Controller.controller import Controller
from View.vista import Vista

def main():
    controlador = Controller()
    vista = Vista()

    while True:
        opcion = vista.mostrar_menu()

        if opcion == 1:
            carnet = input("Carnet del estudiante: ")
            nombre = input("Nombre del estudiante: ")
            carrera = input("Carrera del estudiante: ")
            controlador.registrar_estudiante(carnet, nombre, carrera)
            pass
        elif opcion == 2:
            codigoLibro = input('Ingrese el codigo del libro: ')
            titulo = input('Ingrese el titulo del libro: ')
            autor = input('Ingrese el autor del libro: ')
            categoria = input('Ingrese la categoria: ')
            controlador.registrar_libro(codigoLibro, titulo, autor, categoria)
            pass
        elif opcion == 3:
            codigoPrestamo = input('Ingrese el codigo del prestamo: ')
            carnet = input("Carnet del estudiante: ")
            codigoLibro = input("Ingrese el codigo del Libro: ")
            fecha = input("Fecha del registro: ")

            controlador.registrar_prestamo(codigoPrestamo, carnet, codigoLibro, fecha)
            pass
        elif opcion == 4:
            controlador.consultar_estudiante()
            pass
        elif opcion == 5:
            controlador.consultar_libros()
        elif opcion == 6:
            controlador.consultar_prestamos()
        elif opcion == 7:
            controlador.consultar_categorias()
        elif opcion == 0:
            vista.mostrar_mensaje("Saliendo del sistema...")
            break

#Participantes:
#Herlin Fabian Chavarria Beita C5E187
#MALCOLM ARIEL MENDEZ VARGA

if __name__ == '__main__':
    main()