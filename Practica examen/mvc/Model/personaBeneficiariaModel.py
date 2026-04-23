class Beneficiaria:
    def __init__(self, id, nombre, comunidad, cantidadIntegrantes, prioridadSocial):
        self.id = id
        self.nombre = nombre
        self.comunidad = comunidad
        self.cantidadIntegrantes = cantidadIntegrantes
        self.prioridadSocial = prioridadSocial

    def __str__(self):
        return self.id, self.nombre, self.comunidad, self.cantidadIntegrantes, self.prioridadSocial

    def to_dict(self):
        return {
            'Cedula':self.id,
            'Nombre':self.nombre,
            'Comunidad':self.comunidad,
            'Cantidad Integrantes':self.cantidadIntegrantes,
            'Prioridad Social':self.prioridadSocial
        }

