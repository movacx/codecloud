from View.vistaPlatillos import Vista


class ControllerPlatillo:
    def __init__(self, service):
        self.service = service

    def registrar_platillo(self, nombre, precio, categoria):
        self.service.registrar(nombre,precio,categoria)
        return Vista.mostrar_mensaje('Agregado con exito!')

    def mostrar_platillos(self):
        return Vista.imprimir_datos(self.service.imprimir_dato())

    def buscar_platillo(self, nombre):
        return Vista.imprimir_datos(self.service.buscar_por_nombre(nombre))
