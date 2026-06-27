from Config.database_conexion import SessionLocal
from Entity.mascotasORM import MascotasORM

class RepositoryMascota:
    def __init__(self):
        self.db = SessionLocal()
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def save(self, codigo,nombre,especie,edad,dueno_id):
        mascota = MascotasORM(codigo=codigo, nombre=nombre, especie=especie, edad=edad, dueno_id=dueno_id)
        self.db.add(mascota)
        self.db.commit()
        return mascota
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def list(self):
        return self.db.query(MascotasORM).all()
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def get_list(self, codigo):
        return self.db.query(MascotasORM).filter_by(codigo=codigo).first()
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def update(self, codigo,nombre,especie,edad,dueno_id):
        autor = self.db.get(codigo)
        if autor:
            autor.nombre = nombre
            autor.especie = especie
            autor.edad = edad
            autor.dueno_id = dueno_id
            self.db.commit()
        return autor
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def delete(self, codigo):
        autor = self.db.get(codigo)
        if autor:
            self.db.delete()
            self.db.commit()
        return autor
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#
    def existe_dueno_con_mascota(self, id):
        return self.db.query(MascotasORM).filter_by(dueno_id = id).first() is not None
    
    #=-=--=-==--==--=-==-=-=-=--==-=--==-=-=-=-=-=--=-=-=-==-=-=-=-=--=-=-=-=#