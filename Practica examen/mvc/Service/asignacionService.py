from Model.asignacionesModel import Asignaciones



class AsignacionService:
    def __init__(self, repPersona,repRecurso,repAsignacion)->None:
        self.repo_asignacion = repAsignacion
        self.repo_recurso = repRecurso
        self.repo_persona = repPersona


    def agregar(self, codigoAsignacion, beneficiario, recurso, cantidadEntregada, fecha, responsableEntrega)->bool:
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
        
        #=-=-=-=-=-=-=-=- Validaciones de existencia =-=-=-=-=-=-=-=-buscarBeneficiario buscar_recurso
        if not self.repo_persona.buscarBeneficiario(beneficiario):
            raise ValueError('No se encontro ningun beneficiario registrado')
        if not self.repo_recurso.buscar_recurso(recurso):
            raise ValueError('No se encontro ningun recurso con ese id')


        
        nueva_asignacion = Asignaciones(codigoAsignacion, beneficiario, recurso, cantidadEntregada, fecha, responsableEntrega)


        exito = self.repo_asignacion.guardar(nueva_asignacion)
        if exito:
            return True
        else:
            return False
        
    def listarAsignaciones(self)->list[Asignaciones]:
        return self.repo_asignacion.listar()