from sqlalchemy import Column, String, Integer, ForeignKey
from Config.database_conexion import Base



class AutorORM(Base):
    __tablename__ = 'autores'

    id = Column(Integer, autoincrement=True, primary_key=True)
    nombre = Column(String(100), nullable=False)
    nacionalidad = Column(String(50))

    def __repr__(self):
        return f'{self.id} - {self.nombre} - {self.nacionalidad}'
    
    

class LibroORM(Base):
    __tablename__ = 'libros'

    codigo = Column(String(20), primary_key=True)
    titulo = Column(String(100), nullable=False)
    categoria = Column(String(50))
    anio_publicacion = Column(Integer)
    autor_id = Column(Integer, ForeignKey('autores.id'))

    def __repr__(self):
        return f'{self.codigo} - {self.titulo} - {self.categoria} - {self.anio_publicacion} - {self.autor_id}'

