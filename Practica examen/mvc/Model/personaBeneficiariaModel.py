class Beneficiaria:
    def __init__(self, id:str, nombre:str, comunidad:str, cantidadIntegrantes:int, prioridadSocial:str) -> None:
        self.id = id
        self.nombre = nombre
        self.comunidad = comunidad
        self.cantidadIntegrantes = cantidadIntegrantes
        self.prioridadSocial = prioridadSocial

    def __str__(self) -> str:
        return self.id, self.nombre, self.comunidad, self.cantidadIntegrantes, self.prioridadSocial

    def to_dict(self) -> dict:
        return {
            'Cedula':self.id,
            'Nombre':self.nombre,
            'Comunidad':self.comunidad,
            'Cantidad Integrantes':self.cantidadIntegrantes,
            'Prioridad Social':self.prioridadSocial
        }

