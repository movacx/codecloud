from Config.database_conexion import LocalSession
from Entity.fileVideojuegos import VideoJuegoORM

class VideoJuegoRepository:
    def __init__(self):
        self.db = LocalSession()

    #=-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def save(self, codigo,titulo,desarrollador,categoria,licencias_disponibles):
        videojuego = VideoJuegoORM(codigo=codigo, titulo=titulo, desarrollador=desarrollador, categoria=categoria,licencias_disponibles=licencias_disponibles)
        self.db.add(videojuego)
        self.db.commit()
        return videojuego
    #=-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def list(self):
        return self.db.query(VideoJuegoORM).all()
    #=-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def list_id(self, codigo):
        return self.db.query(VideoJuegoORM).filter_by(codigo=codigo).first()
    #=-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def list_categoria(self, categoria):
        return self.db.query(VideoJuegoORM).filter_by(categoria=categoria).first()
    #=-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#




