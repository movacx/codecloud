from Entity.equiposORM import EquiposORM
from Config.database_conexion import SessionLocal


class RepositoryEquipos:
    def __init__(self):
        self.db = SessionLocal()

    def save(self, nombre, marca, estado, categoria_id):
        equipo = EquiposORM(nombre = nombre, marca = marca, estado = estado, categoria_id = categoria_id)
        self.db.add(equipo)
        self.db.commit()
        return equipo
    
    def list(self):
        return self.db.query(EquiposORM).all()
    
    def list_id(self, codigo):
        return self.db.query(EquiposORM).filter_by(codigo=codigo).first()
    
    def update(self, codigo, nombre, marca, estado, categoria_id):
        equipo = self.list_id(codigo)
        if equipo:
            equipo.nombre = nombre
            equipo.marca = marca
            equipo.estado = estado
            equipo.categoria_id = categoria_id
            self.db.commit()
        return equipo
    
    def delete(self, codigo):
        equipo = self.list_id(codigo)
        if equipo:
            self.db.delete(equipo)
            self.db.commit()
        return equipo
    