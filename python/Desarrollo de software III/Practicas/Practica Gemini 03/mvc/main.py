from Repository.platilloRepository import Repository
from Service.platilloService import PlatilloService
from Controller.platilloController import ControllerPlatillo
from View.vistaPlatillos import Vista
def main():
    repo = Repository()
    service = PlatilloService(repo)
    controlador = ControllerPlatillo(service)

    while True:
        try:
            opcion = Vista.mostrar_menu()

            if opcion == 1:
                datos = Vista.pedir_datos()
                try:
                    controlador.registrar_platillo(*datos)
                    Vista.mostrar_mensaje(f'Guardado con exito!')
                except ValueError as error:
                    Vista.mostrar_mensaje(f'Error: {error}')
            elif opcion == 2:
                controlador.mostrar_platillos()
                pass
            elif opcion == 3:
                nombre = Vista.pedir_nombre()
                controlador.buscar_platillo(nombre)
                pass
            elif opcion == 0:
                break

        except Exception as e:
            Vista.mostrar_mensaje(f'Error: {e}')



if __name__ == '__main__':
    main()