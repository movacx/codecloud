from Model.asignacionesModel import Asignaciones

class AsignacionService:
    def __init__(self, repository):
        self.repo = repository

    def agregar(self, codigoAsignacion, beneficiario, recurso, cantidadEntregada, fecha, responsableEntrega):
        if not codigoAsignacion.strip():
            raise ValueError('El codigo es necesario, favor de ingresarlo!')
        if not beneficiario.strip():
            raise ValueError('El campo beneficiario es obligatorio')
        if not recurso.strip():
            raise ValueError('El campo recurso es obligatorio')
        if cantidadEntregada <=0:
            raise ValueError('La cantidad entregada no puede ser menor o igual a 0.')
        if not fecha.strip():
            raise ValueError('Ingrese la fecha para continuar.')
        if not responsableEntrega.strip():
            raise ValueError('El campo en blanco es necesario favor de rellenarlo.')
        
        nueva_asignacion = Asignaciones(codigoAsignacion, beneficiario, recurso, cantidadEntregada, fecha, responsableEntrega)

        exito = self.repo.agregar(nueva_asignacion)
        if exito:
            return True
        else:
            return False
        
    def listarAsignaciones(self):
        return self.repo.listar()