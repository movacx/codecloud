from sqlalchemy import Integer, Column, ForeignKey, String
from Config.database_conexion import Base
class MascotasORM(Base):
    __tablename__ = 'mascotas'
    codigo = Column(String(100), primary_key=True)
    nombre = Column(String(100), nullable=True)
    especie = Column(String(50))
    edad = Column(Integer)
    dueno_id = Column(Integer, ForeignKey('duenos.id'))

    def __repr__(self):
        return f'\n{self.codigo} - {self.nombre} - {self.especie} - {self.edad} - {self.dueno_id} \n'