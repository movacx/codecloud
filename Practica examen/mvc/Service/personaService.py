from Model.personaBeneficiariaModel import Beneficiaria

class PersonaService:
    def __init__(self, repository):
        self.repository = repository



    def registrar(self, id, nombre, comunidad, cantidadIntegrantes, prioridadSocial):
        if not id.strip():
            raise ValueError('El id es obligatorio')
        if not nombre.strip():
            raise ValueError('El nombre es obligatorio')
        if not comunidad.strip():
            raise ValueError('La comunidad es obligatoria')
        if not cantidadIntegrantes.strip():
            raise ValueError('La cantidad de integrantes es necesaria')
        if not prioridadSocial.strip():
            raise ValueError('El campo de prioridad social es necesaria')

        nueva_persona = Beneficiaria(id, nombre, comunidad, cantidadIntegrantes, prioridadSocial)

        exito = self.repository.agregar(nueva_persona)
        if exito:
            return True
        else:
            return False

    def mostrar_beneficiarios(self):
        return self.repository.listar()



