from Controller.controlador import Controlador
from View.vista import Vista
def main():
    controlador = Controlador()
    vista = Vista()

    while True:
        opcion = vista.menu()

        if opcion == 1:
            datos = vista.pedir_cliente()
            controlador.agregar(*datos)
            pass
        elif opcion == 2:
            datos = vista.pedir_flete()
            controlador.agregar_flete(*datos)
            pass
        elif opcion == 3:
            print('\n Clientes disponibles')
            vista.mostrar_cliente(controlador.consultar_clientes())
            pass
        elif opcion == 4:
            print('\n Fletes disponibles')
            vista.mostrar_fletes(controlador.consultar_fletes())
            pass
        elif opcion == 0:
            vista.mostrar_Messaje("Saliendo del sistema...")
            break


if __name__ == '__main__':
    main()