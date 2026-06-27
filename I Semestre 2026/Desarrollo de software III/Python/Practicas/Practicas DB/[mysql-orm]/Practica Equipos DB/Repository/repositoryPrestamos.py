from Config.database_conexion import SessionLocal
from Entity.prestamosORM import PrestamosORM

class RepositoryPrestamos:
    def __init__(self):
        self.db = SessionLocal()

    def save(self, estudiante_id, equipo_codigo, fecha_prestamo, fecha_devolucion, estado):
        prestamo = PrestamosORM(estudiante_id=estudiante_id, equipo_codigo = equipo_codigo, fecha_prestamo = fecha_prestamo, fecha_devolucion = fecha_devolucion, estado=estado)
        self.db.add(prestamo)
        self.db.commit()
        return prestamo
    
    def list(self):
        return self.db.query(PrestamosORM).all()
    
    def list_id(self, id):
        return self.db.query(PrestamosORM).filter_by(id=id).first()
    
    def update(self, id, estado):
        prestamo = self.list_id(id)
        if prestamo:
            prestamo.estado = estado
            self.db.commit()
        return prestamo

    def delete(self, id):
        prestamo = self.list_id(id)
        if prestamo:
            self.db.delete(prestamo)
            self.db.commit()
        return prestamo
    