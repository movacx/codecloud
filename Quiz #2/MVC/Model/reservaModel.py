class Reserva:
    contador_id = 1

    def __init__(self, numero_habitacion, id_huesped, fecha_entrada, fecha_salida, id_reserva=False):
        if id_reserva is False:
            self.id_reserva = Reserva.contador_id
            Reserva.contador_id += 1
        else:
            self.id_reserva = int(id_reserva)
            if self.id_reserva >= Reserva.contador_id:
                Reserva.contador_id = self.id_reserva + 1

        self.numero_habitacion = numero_habitacion
        self.id_huesped = id_huesped
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida

    def mostrar_info(self):
        return f"Reservacion numero{self.id_reserva} Habitacion: {self.numero_habitacion} Huesped Id: {self.id_huesped} {self.fecha_entrada}  {self.fecha_salida}"
