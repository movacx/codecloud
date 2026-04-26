class Recurso:
    def __init__(self, codigoRecurso:str, nombre:str, categoria:str, cantidadDisponible:int, costoUnitario:int) -> None:
        self.codigoRecurso = codigoRecurso
        self.nombre = nombre
        self.categoria = categoria
        self.cantidadDisponible = cantidadDisponible
        self.costoUnitario = costoUnitario

    def __str__(self) -> str:
        return self.codigoRecurso, self.nombre, self.categoria, self.cantidadDisponible, self.costoUnitario

    def to_dict(self) -> dict:
        return {
            'Codigo':self.codigoRecurso,
            'Nombre':self.nombre,
            'Categoria':self.categoria,
            'Cantidad disponible':self.cantidadDisponible,
            'Costo Unitario':self.costoUnitario
        }
