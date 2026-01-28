from Controller.habitacionesController import HabitacionesController
from Controller.huespedesController import HuespedesController
from Controller.reservasController import ReservasController

import View.habitacionesView as vistaHabitacion
import View.huespedesView as vistaHuesped
import View.reservaView as vistaReserva


def main():
    manejoHabitaciones = HabitacionesController()
    manejoHuespedes = HuespedesController()
    manejoReservas = ReservasController(manejoHabitaciones, manejoHuespedes)

    print("=== PRUEBA MÓDULO RESERVAS ===")

    manejoHabitaciones.registrarHabitacion(1, "Sencilla", 45000, "Disponible")

    manejoHuespedes.registrarHuesped("Juan Perez", 88889999)

    mensaje = manejoReservas.crear_reserva(
        id_habitacion=1,
        id_huesped=1,
        fecha_entrada="2026-02-01",
        fecha_salida="2026-02-05"
    )
    vistaReserva.mostrarMensaje(mensaje)

    manejoReservas.listar_reservas()

    mensaje = manejoReservas.eliminar_reserva(1)
    vistaReserva.mostrarMensaje(mensaje)


if __name__ == "__main__":
    main()

