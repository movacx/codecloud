from sqlalchemy import Integer, ForeignKey, String, Column, Date

class PrestamosORM:
    __tablename__ = 'prestamos'
    id = Column(Integer, autoincrement=True, primary_key=True)
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id'))
    equipo_codigo = Column(Integer, ForeignKey('equipos.codigo'))
    fecha_prestamo = Column(Date)
    fecha_devolucion = Column(Date)
    estado = Column(String(30))


    def __repr__(self):
        return f'{self.id} - {self.estudiante_id} - {self.equipo_codigo} - {self.fecha_prestamo} - {self.fecha_devolucion} - {self.estado}'