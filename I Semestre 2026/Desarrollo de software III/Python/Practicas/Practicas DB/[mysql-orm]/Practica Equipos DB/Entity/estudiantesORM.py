from sqlalchemy import Integer, ForeignKey, String, Column
class EstudianteORM:
    __tablename__ = 'estudiantes'
    id = Column(Integer, autoincrement=True, primary_key=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100))
    carrera = Column(String(100))


    def __repr__(self):
        return f'{self.id} - {self.nombre} - {self.correo} - {self.carrera}'
    
    def __str__(self):
        return 
    