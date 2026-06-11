from Model.videojuego import Videojuego

class JuegoService:
    def __init__(self, repo):
        #Guardamos la referencia al repositorio para usarlo luego
        self.repo = repo

    def registrar_juego(self, titulo, genero, precio):
        if not titulo.strip():
            raise ValueError('El Titulo no puede estar vacio')
        if not genero.strip():
            raise ValueError('El Genero es obligatorio')
        if precio <= 0:
            raise ValueError('El precio debe ser mayor a cero')

        nuevo_juego = Videojuego(titulo,genero,precio)
        self.repo.agregar(nuevo_juego)

    def obtener_todos(self):
        return self.repo.get_all()

    def buscar_juegos_por_titulo(self, titulo):
        if not titulo.strip():
            raise ValueError('Tiene que ingresar un nombre valido para buscar.')
        return self.repo.buscar(titulo)
