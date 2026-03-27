'''Archivo principal del sistema
Respondabilidad:
    -iniciar aplicacion
    -crear la vista y el controlador
    -mantener el ciclo principal del menu

Relacion SOLID
SRP: Este archivo solamente iniciay controla el ciclo general del programa
No tiene logica de negocio'''

from View.vista import VistaConsola
from Controller.controller import Procesador_pago



def main() -> None:
    '''
    Funcion principal del sistema
    ejecuta el men en bucle has que el usuario decida salir
    return
    '''
    controlador = Procesador_pago()
    vista = VistaConsola()

    opcion = vista.mostrar_menu()
    

    if opcion == '0':
        vista.mostrar_resultado('Saliendo')
        

    monto = vista.solicitar_monto()
    resultado = controlador.procesar_pago(opcion)

if __name__ == '__main__':
    main()