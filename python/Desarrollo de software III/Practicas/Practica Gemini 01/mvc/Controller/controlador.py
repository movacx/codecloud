

class Controlador:
    def __init__(self, servicio):
        self.servicio = servicio

    def agregar(self, titulo, genero, precio):
        self.servicio.registrar_juego(titulo,genero,precio)

    def consultar(self):
        return self.servicio.obtener_todos()

    def buscar_titulo(self, titulo):
        return self.servicio.buscar_juegos_por_titulo(titulo)