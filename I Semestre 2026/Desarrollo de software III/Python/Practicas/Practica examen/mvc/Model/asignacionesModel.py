class Asignaciones:
    def __init__(self, codigoAsignacion:str, beneficiario:str, recurso:str, cantidadEntregada:int, fecha:str, responsableEntrega:str) -> None:
        self.codigoAsignacion = codigoAsignacion
        self.beneficiario = beneficiario
        self.recurso = recurso
        self.cantidadEntregada = cantidadEntregada
        self.fecha = fecha
        self.responsableEntrega = responsableEntrega

    def __str__(self) -> str:
        return self.codigoAsignacion, self.beneficiario, self.recurso, self.cantidadEntregada, self.fecha, self.responsableEntrega

    def to_dict(self) -> dict:
        return {
            'Codigo':self.codigoAsignacion,
            'Beneficiario':self.beneficiario,
            'Recurso':self.recurso,
            'Cantidad entregada':self.cantidadEntregada,
            'Fecha':self.fecha,
            'Responsable entrega':self.responsableEntrega
        }