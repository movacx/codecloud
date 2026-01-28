from Model.reservaModel import Reserva
import View.reservaView as vista

<<<<<<< HEAD
import Data.baseHabitacion as baseHabitacion
import Data.huespedData as baseHuesped 

import View.reservaView as vista

=======
import Data.baseReserva as baseReserva
import Data.baseHabitacion as baseHabitacion
import Data.huespedData as baseHuesped 

>>>>>>> bca83c171393135ff296d7e046c268738d8e5d5e
class ReservasController:

    def __init__(self):
        pass
#--------------------------------------------------------------------------------------------------#
    def crear_reserva(self, numero_habitacion, id_huesped, fecha_entrada, fecha_salida):
<<<<<<< HEAD
=======
        #Validar Habitacion
>>>>>>> bca83c171393135ff296d7e046c268738d8e5d5e
        habitacion = baseHabitacion.buscarHabitacionId(numero_habitacion)
        if not habitacion:
            vista.mostrarMensaje("Error: La habitación no existe.")
            return
<<<<<<< HEAD

=======
#--------------------------------------------------------------------------------------------------#
        #Validar Disponibilidad
>>>>>>> bca83c171393135ff296d7e046c268738d8e5d5e
        datosHab = habitacion[0]
        if datosHab[4].strip() == "Ocupada":
            vista.mostrarMensaje("Error: Habitación OCUPADA.")
            return
<<<<<<< HEAD

=======
        
>>>>>>> bca83c171393135ff296d7e046c268738d8e5d5e
        if not baseHuesped.searchId(id_huesped):
             vista.mostrarMensaje("Error: El huésped no existe.")
             return

        nuevaReserva = Reserva(0, numero_habitacion, id_huesped, fecha_entrada, fecha_salida)
        baseReserva.registrarReserva(nuevaReserva)

        baseHabitacion.modificar(numero_habitacion, "Ocupada")
        vista.mostrarMensaje("Reserva creada y Habitación ocupada.")
#--------------------------------------------------------------------------------------------------#
    def listar_reservas(self):
        lista = baseReserva.listarReservas()
        
        if not lista:
            vista.fileNoFound()
            return
<<<<<<< HEAD

=======
>>>>>>> bca83c171393135ff296d7e046c268738d8e5d5e
        vista.mostrarListados(lista)
#--------------------------------------------------------------------------------------------------#
    def eliminar_reserva(self, id_reserva):
<<<<<<< HEAD

=======
>>>>>>> bca83c171393135ff296d7e046c268738d8e5d5e
        datos = baseReserva.buscarReservaPorId(id_reserva)
        if not datos:
            vista.fileNoFound()
            return
            
        num_hab = datos[1]
<<<<<<< HEAD

=======
>>>>>>> bca83c171393135ff296d7e046c268738d8e5d5e
        if baseReserva.eliminarReserva(id_reserva):
            baseHabitacion.modificar(num_hab, "Disponible")
            vista.mostrarMensaje(f"Reserva eliminada. Habitación {num_hab} liberada.")
        else:
            vista.mostrarMensaje("Error al eliminar.")
#--------------------------------------------------------------------------------------------------#