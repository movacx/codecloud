from sqlalchemy import Integer, String, Column, ForeignKey

class CategoriasORM:
    __tablename__ = 'categorias'
    id = Column(Integer, autoincrement=True, primary_key=True)
    nombre = Column(String(100))

    def __repr__(self):
        return f'{self.id} - {self.nombre}'
    
    

