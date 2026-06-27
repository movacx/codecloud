import View.view as vista
from Controller.controller_autor import ControllerAutor
from Controller.controller_libro import ControllerLibro
from Service.service_autor import ServiceAutor
from Service.service_libro import ServiceLibro


def main():
    controlador_autor = ControllerAutor(ServiceAutor)
    controlador_libro = ControllerLibro(ServiceLibro)

    while True:
        try:
            opcion = vista.menu_principal()

            if opcion == 1:
                menu_autor(controlador_autor)
            elif opcion == 2:
                menu_libro(controlador_libro)
            elif opcion == 3:
                menu_reportes(controlador_libro, controlador_autor)
            elif opcion == 0:
                print('Hasta luego.')
                break
            else:
                vista.mostrar_mensaje('Opcion invalida')

        except ValueError:
            vista.mostrar_mensaje('Debe de ingresar un entero')
        except Exception as error:
            vista.mostrar_mensaje(f'Error: {error}')


# =-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
def menu_autor(controller):
    while True:
        try:
            opcion = vista.menu_autor()

            if opcion == 1:
                nombre = input('Nombre: ')
                nacionalidad = input('Nacionalidad: ')
                print(controller.registrar_autor(nombre, nacionalidad))

            elif opcion == 2:
                print(controller.listar_autores())

            elif opcion == 3:
                id = input('ID del autor: ')
                print(controller.buscar_autor(id))

            elif opcion == 4:
                id = input('ID del autor: ')
                nombre = input('Nuevo nombre: ')
                nacionalidad = input('Nueva nacionalidad: ')
                print(controller.modificar_autor(id, nombre, nacionalidad))

            elif opcion == 5:
                id = input('ID del autor: ')
                print(controller.eliminar_autor(id))

            elif opcion == 0:
                break
            else:
                vista.mostrar_mensaje('Opcion invalida')

        except ValueError:
            vista.mostrar_mensaje('Debe de ingresar un entero')
        except Exception as error:
            vista.mostrar_mensaje(f'Error: {error}')


# =-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
def menu_libro(controller):
    while True:
        try:
            opcion = vista.menu_libro()

            if opcion == 1:
                codigo = input('Codigo: ')
                titulo = input('Titulo: ')
                categoria = input('Categoria: ')
                anio = input('Año de publicacion: ')
                autor_id = input('ID del autor: ')
                print(controller.registrar_libro(codigo, titulo, categoria, anio, autor_id))

            elif opcion == 2:
                print(controller.mostrar_libros())

            elif opcion == 3:
                codigo = input('Codigo: ')
                print(controller.buscar_libro(codigo))

            elif opcion == 4:
                codigo = input('Codigo: ')
                titulo = input('Nuevo titulo: ')
                categoria = input('Nueva categoria: ')
                anio = input('Nuevo año: ')
                autor_id = input('Nuevo ID del autor: ')
                print(controller.modificar_libro(codigo, titulo, categoria, anio, autor_id))

            elif opcion == 5:
                codigo = input('Codigo: ')
                print(controller.eliminar_libro(codigo))

            elif opcion == 0:
                break
            else:
                vista.mostrar_mensaje('Opcion invalida')

        except ValueError:
            vista.mostrar_mensaje('Debe de ingresar un entero')
        except Exception as error:
            vista.mostrar_mensaje(f'Error: {error}')


# =-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
def menu_reportes(controller_libro, controller_autor):
    while True:
        try:
            opcion = vista.menu_reportes()

            if opcion == 1:
                print(controller_libro.ordenar_libros())

            elif opcion == 2:
                categoria = input('Categoria: ')
                print(controller_libro.filtrar_Categoria(categoria))

            elif opcion == 3:
                nombre_autor = input('Nombre del autor: ')
                print(controller_libro.filtrar_autores_por_libro(nombre_autor))

            elif opcion == 4:
                nacionalidad = input('Nacionalidad: ')
                print(controller_autor.filtrar_autor_por_nacionalidad(nacionalidad))

            elif opcion == 0:
                break
            else:
                vista.mostrar_mensaje('Opcion invalida')

        except ValueError:
            vista.mostrar_mensaje('Debe de ingresar un entero')
        except Exception as error:
            vista.mostrar_mensaje(f'Error: {error}')


if __name__ == '__main__':
    main()