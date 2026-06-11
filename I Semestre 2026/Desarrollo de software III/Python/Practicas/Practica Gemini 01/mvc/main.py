from Controller.controlador import Controlador
from View.vista import Vista
from service.juego_service import JuegoService
from Repository.juego_repository import JuegoRepository

def main():
    repo = JuegoRepository()
    servicio = JuegoService(repo)
    controlador = Controlador(servicio)


    while True:
        opcion = Vista.menu()

        if opcion == 1:
            datos = Vista.pedir_juego()
            try:
                controlador.agregar(*datos)
                Vista.mostrar_mensaje('Juego guardado exitosamente!')
            except ValueError as error:
                Vista.mostrar_mensaje(f'Error: {error}')

        elif opcion == 2:
            Vista.mostrar_mensaje('\nJuegos disponibles')
            Vista.mostrar_juegos(controlador.consultar())

        elif opcion == 3:
            termino = Vista.pedir_busqueda()
            try:
                resultados = controlador.buscar_titulo(termino)
                Vista.mostrar_juegos(resultados)
            except ValueError as e:
                Vista.mostrar_mensaje(f'Error: {e}')

        elif opcion == 0:
            Vista.mostrar_mensaje('Saliendo del sistema..')
            break

if __name__ == '__main__':
    main()
