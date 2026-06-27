from Config.database_conexion import SessionLocal
from Entity.biblioteca import AutorORM

class AutorRepository:
    def __init__(self):
        self.db = SessionLocal()
    
    def create(self, nombre,nacionalidad):
        autor = AutorORM(nombre=nombre, nacionalidad=nacionalidad)
        self.db.add(autor)
        self.db.commit()
        return autor
    
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#

    def get(self, id):
        return self.db.query(AutorORM).filter_by(id=id).first()
    
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#

    def get_all(self):
        return self.db.query(AutorORM).all()
    
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#

    def update(self, id, nombre, nacionalidad):
        autor = self.get(id)
        if autor:
            autor.nombre = nombre
            autor.nacionalidad = nacionalidad
            self.db.commit()
        return autor
    
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#

    def delete(self, id):
        autor = self.get(id)
        if autor:
            self.db.delete(autor)
            self.db.commit()
        return autor
    
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def get_por_nombre(self, nombre):
        return self.db.query(AutorORM).filter(AutorORM.nombre == nombre).first()
    
    def get_nacionalidad(self, nacionalidad):
        return self.db.query(AutorORM).filter(AutorORM.nacionalidad == nacionalidad).first()
