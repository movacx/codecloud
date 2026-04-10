from View.consola import VistaConsola
from Controller.gestor_notificaciones import GestorNotificaciones
from Model.mensaje import Mensaje

def main():
    vista = VistaConsola()
    controlador = GestorNotificaciones()

    while True:
        opcion = vista.mostrar_menu()

        if opcion == "0":
            vista.mostrar_resultado("Saliendo del sistema")
            break

        try:
            texto = vista.solicitar_mensaje()
            mensaje_obj = Mensaje(texto)
            
            resultado = controlador.ejecutar_envio(opcion, mensaje_obj)
            vista.mostrar_resultado(resultado)
            
        except ValueError as error:
            vista.mostrar_error(str(errr))

if __name__ == "__main__":
    main()