from Config.database_conexion import SessionLocal
from Entity.duenosORM import DuenosOrm

class RepositoryDuenos:
    def __init__(self):
        self.db = SessionLocal()

    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def save(self, tupla_recibida):
        dueno = DuenosOrm(*tupla_recibida)
        self.db.add(dueno)
        self.db.commit()
        return dueno
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def get_all(self):
        return self.db.query(DuenosOrm).all()
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    #1
    def search_id(self, id):
        return self.db.query(DuenosOrm).filter_by(id=id).first()
    #2
    def search_name(self, nombre):
        return self.db.query(DuenosOrm).filter_by(nombre=nombre).first()
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def update(self, id,nombre,telefono,email):
        dueno = self.search_id(id)
        if dueno:
            dueno.nombre = nombre
            dueno.telefono = telefono
            dueno.email = email
            self.db.commit()
        return dueno
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def delete(self, id):
        dueno = self.search_id(id)
        if dueno:
            self.db.delete(dueno)
            self.db.commit()
        return dueno
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#

    # def validar_mascotas(self, id):
    #     return self.db.query(DuenosOrm)