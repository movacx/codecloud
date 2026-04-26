from Controller.periferico_controller import Controller
from Repository.periferico_repository import Repositorio
from Services.periferico_service import PerifericoService
from View.perifericos_view import Vista


def main():
    repo = Repositorio()
    services = PerifericoService(repo)
    controlador = Controller(services)

    while True:
        try:
            opcion = Vista.mostrar_menu()

            if opcion == 1:
                datos = Vista.pedir_datos()
                try:
                    controlador.registrar_periferico(*datos)
                    Vista.mostrar_mensaje(f'Guardado con exito!')
                except ValueError as error:
                    Vista.mostrar_mensaje(f'Error: {error}')
            elif opcion == 2:
                controlador.imprimir_datos()
                pass
            elif opcion == 3:
                pass
            elif opcion == 0:
                break

        except Exception as e:
            Vista.mostrar_mensaje(f'Error: {e}')



if __name__ == '__main__':
    main()