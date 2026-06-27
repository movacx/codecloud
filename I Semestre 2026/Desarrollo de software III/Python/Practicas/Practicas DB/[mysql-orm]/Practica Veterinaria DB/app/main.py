

import View.view as vista
from Controller.controller_duenos import ControllerDueños
from Controller.controller_mascotas import ControllerMascota


def main():
    controlador_duenos = ControllerDueños()
    controlador_mascostas = ControllerMascota()
    

    while True:
        try:
            opcion = vista.menu_principal()

            if opcion == 1:
                menu_dueno(controlador_duenos)
            elif opcion == 2:
                menu_mascota(controlador_mascostas)
            else:
                vista.mostrar_mensajes('Opcion invalida')

        except ValueError:
            vista.mostrar_mensajes('Debe de ingresar un entero')
        except Exception as error:
            vista.mostrar_mensajes(f'Error: {error}')

#-=-=-==-=--==--==-=-=-=-=-=--==-=-=--==-=-=--=-=-=-==-=--==-=-=-=-=-=-=-=-#

def menu_dueno(controller):

    while True:
        try:
            opcion = vista.menu_duenos()

            if opcion == 1:
                nombre = input('Ingrese el fockin nombre: ')
                telefono = input('Ingrese el telefono: ')
                email =  input('Ingrese el email: ')
                controller.registrar_dueno(nombre,telefono,email)

            elif opcion == 2:
                controller.mostrar_duenos()
            
            elif opcion == 3:
                nombre = input('Ingrese el fockin nombre: ')
                controller.filtrar_duenos(nombre)

            elif opcion == 4:
                id = input('Ingrese el id: ')
                nombre = input('Ingrese el fockin nombre: ')
                telefono = input('Ingrese el telefono: ')
                email =  input('Ingrese el email: ')
                controller.actualizar_datos(id,nombre,telefono,email)

            elif opcion == 5:
                id = input('Ingrese el id: ')
                controller.eliminar_dato(id)

            elif opcion == 0:
                break
            else:
                vista.mostrar_mensajes('Opcion invalida')
                    
        except ValueError:
            vista.mostrar_mensajes('Debe de ingresar un entero')
        except Exception as error:
            vista.mostrar_mensajes(f'Error: {error}')

#-=-=-==-=--==--==-=-=-=-=-=--==-=-=--==-=-=--=-=-=-==-=--==-=-=-=-=-=-=-=-#

def menu_mascota(controller):

    while True:
        try:
            opcion = vista.menu_mascostas()

            if opcion == 1:
                codigo=input('Codigo: ')
                nombre=input('Nombre: ')
                especie=input('Especie: ')
                edad=int(input('Edad: '))
                dueno_id=int(input('Id del dueño asociar: '))

                controller.registrar_mascota(codigo,nombre,especie,edad,dueno_id)
            elif opcion == 2:
                controller.mostrar_mascotas()

            elif opcion == 3:
                codigo=input('Codigo: ')
                controller.buscar_mascostas(codigo)

            elif opcion == 4:
                codigo=input('Codigo: ')
                nombre=input('Nombre: ')
                especie=input('Especie: ')
                edad=int(input('Edad: '))
                dueno_id=int(input('Id del dueño asociar: '))

                controller.actualizar_datos(codigo,nombre,especie,edad,dueno_id)

            elif opcion == 5:
                codigo=input('Codigo: ')
                controller.eliminar_mascota(codigo)

            elif opcion == 0:
                break
            else:
                vista.mostrar_mensajes('Opcion invalida')
                
        except ValueError:
            vista.mostrar_mensajes('Debe de ingresar un entero')
        except Exception as error:
            vista.mostrar_mensajes(f'Error: {error}')


#-=-=-==-=--==--==-=-=-=-=-=--==-=-=--==-=-=--=-=-=-==-=--==-=-=-=-=-=-=-=-#

if __name__ == '__main__':
    main()
