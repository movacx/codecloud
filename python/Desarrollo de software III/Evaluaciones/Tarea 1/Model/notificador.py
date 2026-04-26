from abc import ABC, abstractmethod

class Notificador(ABC):

    @abstractmethod
    def enviar(self, mensaje_obj):
        pass

class NotificadorEmail(Notificador):
    def enviar(self, mensaje_obj) -> str:
        return f"Email enviado: {mensaje_obj.texto}"

class NotificadorSMS(Notificador):
    def enviar(self, mensaje_obj) -> str:
        return f"SMS enviado: {mensaje_obj.texto}"

class NotificadorWhatsApp(Notificador):
    def enviar(self, mensaje_obj) -> str:
        return f"WhatsApp enviado: {mensaje_obj.texto}"