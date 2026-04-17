from View.perifericos_view import Vista
class Controller:
    def __init__(self, services):
        self.service = services

    def registrar_periferico(self, modelo, tipo, precio):
        return self.service.agregar(modelo,tipo,precio)

    def imprimir_datos(self):
        Vista.imprimir_datos(self.service.mostrar_datos())
