# No heredamos de HuespedModel, son cosas distintas
class Reserva: 
    def __init__(self, id, numeroHabitacion, idHuesped, fechaEntrada, fechaSalida):
        self.id = id
        self.numeroHabitacion = numeroHabitacion
        self.idHuesped = idHuesped # Guardamos el ID como una variable normal
        self.fechaEntrada = fechaEntrada
        self.fechaSalida = fechaSalida

    def importarToCsv(self):
        # Es mucho mas simple
        return ([self.id, self.numeroHabitacion, self.idHuesped, self.fechaEntrada, self.fechaSalida])