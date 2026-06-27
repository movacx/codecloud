
from sqlalchemy import Column, Integer, String
from Config.database_conexion import Base
class JugadoresORM(Base):
    __tablename__ = 'jugadores'
    identificacion = Column(String(20), primary_key=True)
    nombre_completo = Column(String(100), nullable=False)
    correo_electronico = Column(String(100), nullable=False)
    pais = Column(String, nullable=False)

    def __repr__(self):
        return f'\n{self.identificacion} - {self.nombre_completo} - {self.correo_electronico} - {self.pais}'

