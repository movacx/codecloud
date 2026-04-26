from Model.recursoModel import Recurso

class RecursoService:
    def __init__(self, repository):
        self.repo = repository

    def registrarRecurso(self, codigoRecurso, nombre, categoria, cantidadDisponible, costoUnitario):
        if not codigoRecurso.strip():
            raise ValueError('El codigo recurso es obligatorio')
        if not nombre.strip():
            raise ValueError('El nombre es obligatorio')
        if not categoria.strip():
            raise ValueError('El campo categoria es obligatorio')
        if cantidadDisponible <= 0:
            raise ValueError('La cantidad no puede ser igual o menor a cero')
        if costoUnitario <=0:
            raise ValueError('El costo unitario no puede ser igual o menor a cero')
        
        nuevo_recurso = Recurso(codigoRecurso, nombre, categoria, cantidadDisponible, costoUnitario)
        exito = self.repo.guardar(nuevo_recurso)
        if exito:
            return True
        else:
            return False
        
    def listarRecursos(self):
        return self.repo.listar()
    
     
