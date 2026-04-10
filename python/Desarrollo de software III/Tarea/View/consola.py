class VistaConsola:
    @staticmethod
    def mostrar_menu() -> str:
        return input('''
===== SISTEMA DE NOTIFICACIONES =====
1. Enviar Email
2. Enviar SMS
3. Enviar WhatsApp
0. Salir
Input: ''')

    @staticmethod
    def solicitar_mensaje() -> str:
        return input('Ingrese el mensaje: ')

    @staticmethod
    def mostrar_resultado(mensaje: str) -> None:
        print(f'\n Resultado: {mensaje}')

    @staticmethod
    def mostrar_error(error: str) -> None:
        print(f'\n Error: {error}')