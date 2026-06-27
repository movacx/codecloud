from Repository.videojuego_repository import VideoJuegoRepository
class VideoJuegoService:
    def __init__(self):
        self.repo = VideoJuegoRepository()

    def agregar(self,codigo,titulo,desarrollador,categoria,licencias_disponibles):
        if not codigo.strip() or not titulo.strip() or not desarrollador.strip() or not categoria.strip():
            raise ValueError('Debe de completar los campos.')
        if self.repo.list_id(codigo):
            raise ValueError('Ya existe un videoJuego con el mismo codigo de registro.')
        if licencias_disponibles <= 0:
            raise ValueError('Las licencias no pueden ser negativas o iguales a cero.')
        return self.repo.save(codigo,titulo,desarrollador,categoria,licencias_disponibles)
    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def mostrar(self):
        dato_encontrado = self.repo.list()
        if dato_encontrado is None:
            raise ValueError('No se encontraron datos a mostrar.')
        return dato_encontrado
    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def buscar(self, codigo):
        dato_encontrado =  self.repo.list_id(codigo)
        if dato_encontrado is None:
            raise ValueError(f'No se encontro ningun videoJuego asociado al siguiente Codigo: {codigo}')
        return dato_encontrado
    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def filtrar_categoria(self, categoria):
        dato_encontrado = self.repo.list_categoria(categoria)
        if dato_encontrado is None:
            raise ValueError(f'No se encontro ninguna categoria: {categoria}')
        return dato_encontrado
    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#