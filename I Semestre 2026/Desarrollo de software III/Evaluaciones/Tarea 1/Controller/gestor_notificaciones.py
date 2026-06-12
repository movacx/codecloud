from Model.notificador import Notificador, NotificadorEmail, NotificadorSMS, NotificadorWhatsApp

class GestorNotificaciones:
    '''Controlador Pro aplicando buenas practicas de solid creo'''
    
    def crear_notificador(self, opcion: str) -> Notificador:

        if opcion == '1':
            return NotificadorEmail()
        elif opcion == '2':
            return NotificadorSMS()
        elif opcion == '3':
            return NotificadorWhatsApp()
        raise ValueError('Opcion invalida. Elija del 1 al 3')

    def ejecutar_envio(self, opcion: str, mensaje_obj) -> str:
        canal = self.crear_notificador(opcion)
        return canal.enviar(mensaje_obj)