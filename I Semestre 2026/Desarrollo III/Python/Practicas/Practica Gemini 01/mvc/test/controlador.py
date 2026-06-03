class Controlador:
    def __init__(self, servicio):
        self.servicio = servicio

    def agregar(self, servicio):
        #Guardamos el servicio que ya trae el repositorio inyectado
        self.servicio = servicio

    def agregar(self, titulo, genero, precio):
        self.servicio.registrar_juego(titulo,genero,precio)

    def consultar(self):
        return self.servicio.repo.get_all()