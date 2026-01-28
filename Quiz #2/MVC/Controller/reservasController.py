from Data.baseReserva import guardar_reservas, cargar_reservas
from Model.reservaModel import Reserva

class ReservasController:

    def __init__(self, habitacionesController, huespedesController):
        self.reservas = cargar_reservas()
        self.habitacionesController = habitacionesController
        self.huespedesController = huespedesController

    def crear_reserva(self, id_habitacion, id_huesped, fecha_entrada, fecha_salida):

        habitacion = self.habitacionesController.buscarHabitacionId(id_habitacion)
        if habitacion is None:
            return "Habitacion no existe"

        if habitacion.estado != "Disponible":
            return "Habitacion no disponible"

        huesped = self.huespedesController.buscar_huesped_por_id(id_huesped)
        if huesped is None:
            return "Huésped no existe"
        nueva = Reserva(id_habitacion, id_huesped, fecha_entrada, fecha_salida)
        self.reservas.append(nueva)

        self.habitacionesController.cambiarEstado(id_habitacion, "Ocupada")

        guardar_reservas(self.reservas)
        return "Reserva creada correctamente"

    def listar_reservas(self):
        return self.reservas

    def eliminar_reserva(self, id_reserva):
        for rows in self.reservas:
            if rows.id_reserva == id_reserva:
                self.habitacionesController.cambiarEstado(
                    rows.numero_habitacion, "Disponible"
                )
                self.reservas.remove(rows)
                guardar_reservas(self.reservas)
                return "Reserva eliminada"

        return "Reserva no encontrada"