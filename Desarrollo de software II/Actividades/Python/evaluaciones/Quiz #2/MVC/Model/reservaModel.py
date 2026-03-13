
class Reserva: 
    def __init__(self, id, numeroHabitacion, idHuesped, fechaEntrada, fechaSalida):
        self.id = id
        self.numeroHabitacion = numeroHabitacion
        self.idHuesped = idHuesped 
        self.fechaEntrada = fechaEntrada
        self.fechaSalida = fechaSalida

    def importarToCsv(self):
        return ([self.id, self.numeroHabitacion, self.idHuesped, self.fechaEntrada, self.fechaSalida])