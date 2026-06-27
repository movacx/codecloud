from Config.database_conexion import LocalSession
from Entity.fileJugadores import JugadoresORM
class JugadorRepository:
    def __init__(self):
        self.db = LocalSession()

    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def save(self, identificacion,nombre_completo,correo_electronico,pais):
        jugador = JugadoresORM(identificacion=identificacion, nombre_completo=nombre_completo, correo_electronico=correo_electronico, pais=pais)
        self.db.add(jugador)
        self.db.commit()
        return jugador
    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def list(self):
        return self.db.query(JugadoresORM).all()
    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def list_id(self, identificacion):
        return self.db.query(JugadoresORM).filter_by(identificacion=identificacion).first()
    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def list_categoria(self, categoria):
        return self.db.query(JugadoresORM).filter_by(categoria=categoria).first()
    # =-=-=-=-=-=-==-=--=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=--==--==-=--==--==-=-=-=-=-=--=-=-=-=-==--=-=-=-=-=-=-=-==--=-=-=-=-=-==--=-=#
    def list_country(self, pais):
        return self.db.query(JugadoresORM).filter_by(pais=pais).first()
