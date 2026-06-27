from sqlalchemy import Column, String, Integer, ForeignKey
from Config.database_conexion import Base
class DuenosOrm(Base):
    __tablename__ = 'duenos'
    id = Column(Integer, autoincrement=True, primary_key=True)
    nombre = Column(String(100), nullable=True)
    telefono = Column(String(20))
    email = Column(String(100))

    def __repr__(self):
        return f'\n{self.id} - {self.nombre} - {self.telefono} - {self.email}\n'
    