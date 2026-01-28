from Model.reservaModel import Reserva
import Data.baseReserva as baseReserva

# Imports para validaciones
import Data.baseHabitacion as baseHabitacion
import Data.huespedData as baseHuesped 

# Importamos la vista ajustada
import View.reservaView as vista

class ReservasController:

    def __init__(self):
        pass

    def crear_reserva(self, numero_habitacion, id_huesped, fecha_entrada, fecha_salida):
        # 1. Validar Habitacion
        habitacion = baseHabitacion.buscarHabitacionId(numero_habitacion)
        if not habitacion:
            vista.mostrarMensaje("Error: La habitación no existe.")
            return

        # 2. Validar Disponibilidad
        datosHab = habitacion[0]
        if datosHab[4].strip() == "Ocupada":
            vista.mostrarMensaje("Error: Habitación OCUPADA.")
            return

        # 3. Validar Huesped (Si existe huespedData)
        if not baseHuesped.searchId(id_huesped): # Asegurate que searchId exista en huespedData
             vista.mostrarMensaje("Error: El huésped no existe.")
             return

        # 4. Crear Reserva (ID 0 porque se autocalcula)
        nuevaReserva = Reserva(0, numero_habitacion, id_huesped, fecha_entrada, fecha_salida)
        baseReserva.registrarReserva(nuevaReserva)

        # 5. Ocupar Habitacion
        baseHabitacion.modificar(numero_habitacion, "Ocupada")

        vista.mostrarMensaje("Reserva creada y Habitación ocupada.")

    def listar_reservas(self):
        lista = baseReserva.listarReservas()
        
        if not lista:
            vista.fileNoFound()
            return

        # Llamamos a la vista que imprime las 5 columnas
        vista.mostrarListados(lista)

    def eliminar_reserva(self, id_reserva):
        # 1. Buscar para saber que habitacion liberar
        datos = baseReserva.buscarReservaPorId(id_reserva)
        if not datos:
            vista.fileNoFound()
            return
            
        num_hab = datos[1]

        # 2. Eliminar
        if baseReserva.eliminarReserva(id_reserva):
            # 3. Liberar
            baseHabitacion.modificar(num_hab, "Disponible")
            vista.mostrarMensaje(f"Reserva eliminada. Habitación {num_hab} liberada.")
        else:
            vista.mostrarMensaje("Error al eliminar.")