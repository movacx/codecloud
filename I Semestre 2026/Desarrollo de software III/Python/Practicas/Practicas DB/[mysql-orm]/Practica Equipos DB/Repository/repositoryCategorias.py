from Entity.categoriasORM import CategoriasORM
from Config.database_conexion import SessionLocal

class RepositoryCategorias:
    def __init__(self):
        self.db = SessionLocal()

    def save(self, nombre):
        categoria = CategoriasORM(nombre = nombre)
        self.db.add(categoria)
        self.db.commit()
        return categoria
    
    def list(self):
        return self.db.query(CategoriasORM).all()
    
    def list_id(self, id):
        return self.db.query(CategoriasORM).filter_by(id=id).first()
    
    def update(self, id, nombre):
        categoria = self.list_id(id)
        if categoria:
            categoria.nombre = nombre
            self.db.commit()
        return categoria
    
    def delete(self, id):
        categoria = self.list_id(id)
        if categoria:
            self.db.delete(categoria)
            self.db.commit()
        return categoria
    