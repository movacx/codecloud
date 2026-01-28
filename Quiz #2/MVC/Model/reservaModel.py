from Model.huespedModel import HuespedModel
class Reserva(HuespedModel):
    contador_id = 1
    def __init__(self,id,numeroHabitacion,idHuesped, fechaEntrada, fechaSalida):
        super().__init__(idHuesped)
        self.id = id
        self.numeroHabitacion = numeroHabitacion
        self.fechaEntrada = fechaEntrada
        self.fechaSalida = fechaSalida


    def importarToCsv(self):
	    return ([self.id, self.numeroHabitacion, super().self.idHuesped, self.fechaEntrada, self.fechaSalida])
    
    def mostrarInfo(self):
        return f"Id reservacion: {self.id} Reservacion numero: {self.numeroHabitacion} Huesped Id: {self.idHuesped} Fecha de entrada: {self.fechaEntrada} Fecha de salida:  {self.fechaSalida}"
