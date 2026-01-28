from Controller.habitacionesController import HabitacionesController
from Controller.huespedesController import HuespedesController
from Controller.reservasController import ReservasController

from View.habitacionesView import HabitacionesView
from View.huespedesView import HuespedesView
from View.reservaView import ReservaView


def main():
    # Inicializar controladores
    habitacionesController = HabitacionesController()
    huespedesController = HuespedesController()
    reservasController = ReservasController(habitacionesController, huespedesController)

    # Inicializar vistas
    habitacionView = HabitacionesView()
    huespedView = HuespedesView()
    reservaView = ReservaView()

    print("=== PRUEBA DEL MÓDULO DE RESERVAS ===\n")

    
    print("Registrando habitación...")
    habitacionesController.registrar_habitacion("101", "Sencilla", 45000)
    habitacionView.mostrar_habitaciones(habitacionesController.listar_habitaciones())

    
    print("\nRegistrando huésped...")
    huespedesController.registrar_huesped("Juan Pérez", "8888-9999")
    huespedView.mostrar_huespedes(huespedesController.listar_huespedes())

    
    print("\nCreando reserva...")
    mensaje = reservasController.crear_reserva(
        numero_habitacion="101",
        id_huesped=1,
        fecha_entrada="2026-02-01",
        fecha_salida="2026-02-05"
    )
    reservaView.mostrar_mensaje(mensaje)

    
    print("\nReservas registradas:")
    reservaView.mostrar_reservas(reservasController.listar_reservas())

    
    print("\nEstado de habitaciones después de reservar:")
    habitacionView.mostrar_habitaciones(habitacionesController.listar_habitaciones())

    
    print("\nEliminando reserva...")
    mensaje = reservasController.eliminar_reserva(1)
    reservaView.mostrar_mensaje(mensaje)

    
    print("\nEstado de habitaciones después de eliminar la reserva:")
    habitacionView.mostrar_habitaciones(habitacionesController.listar_habitaciones())


if __name__ == "__main__":
    main()
