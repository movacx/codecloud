from Config.database_conexion import SessionLocal
from Entity.estudiantesORM import EstudianteORM
class EstudianteRepository:
    def __init__(self):
        self.db = SessionLocal()
        

    def save(self,  nombre, correo, carrera):
        estudiante = EstudianteORM(nombre=nombre, correo = correo, carrera=carrera)
        self.db.add(estudiante)
        self.db.commit()
        return estudiante
    
    def list(self):
        return self.db.query(EstudianteORM).all()
    
    def list_id(self, id):
        return self.db.query(EstudianteORM).filter_by(id=id).first()
    def update(self, id, nombre, correo, carrera):
        estudiante_encontrado = self.list_id(id)
        if estudiante_encontrado:
            estudiante_encontrado.nombre = nombre
            estudiante_encontrado.correo = correo
            estudiante_encontrado.carrera = carrera
            self.db.commit()
        return estudiante_encontrado
    
    def delete(self, id):
        estudiante_encontrado = self.list_id(id)
        if estudiante_encontrado:
            self.db.delete(estudiante_encontrado)
            self.db.commit()
        return estudiante_encontrado
    