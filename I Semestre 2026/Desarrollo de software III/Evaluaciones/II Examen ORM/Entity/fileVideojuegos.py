from Config.database_conexion import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class VideoJuegoORM(Base):
    __tablename__ = 'videojuegos'
    codigo = Column(String(20), primary_key=True)
    titulo = Column(String(100), nullable=False)
    desarrollador = Column(String(100), nullable=False)
    categoria = Column(String(50), nullable=False)
    licencias_disponibles = Column(Integer, nullable=False, default=0)

