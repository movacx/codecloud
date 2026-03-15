from Model.reservaModel import Reserva
import View.reservaView as vista

import Data.baseReserva as baseReserva
import Data.baseHabitacion as baseHabitacion 
import Data.huespedData as baseHuesped 

class ReservasController:

    def __init__(self):
        pass
#--------------------------------------------------------------------------------------------------#
    def crear_reserva(self, numero_habitacion, id_huesped, fecha_entrada, fecha_salida):
        #Validar Habitacion
        habitacion = baseHabitacion.buscarHabitacionId(numero_habitacion)
        if not habitacion:
            vista.mostrarMensaje("Error: La habitación no existe.")
            return
#--------------------------------------------------------------------------------------------------#
        #Validar Disponibilidad
        datosHab = habitacion[0]
        if datosHab[4].strip() == "Ocupada":
            vista.mostrarMensaje("Error: Habitación OCUPADA.")
            return
        
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
        vista.mostrarListados(lista)
#--------------------------------------------------------------------------------------------------#
    def eliminar_reserva(self, id_reserva):
        datos = baseReserva.buscarReservaPorId(id_reserva)
        if not datos:
            vista.fileNoFound()
            return
            
        num_hab = datos[1]
        if baseReserva.eliminarReserva(id_reserva):
            baseHabitacion.modificar(num_hab, "Disponible")
            vista.mostrarMensaje(f"Reserva eliminada. Habitación {num_hab} liberada.")
        else:
            vista.mostrarMensaje("Error al eliminar.")
#--------------------------------------------------------------------------------------------------#
    def buscar_reserva(self, id_reserva):
        dato = baseReserva.buscarReservaPorId(id_reserva)
        
        if not dato:
            vista.fileNoFound()
            return

        vista.mostrarListados([dato])

    def modificar_reserva(self, id_reserva, habitacion, huesped, entrada, salida):
       
        if not baseReserva.buscarReservaPorId(id_reserva):
            vista.mostrarMensaje("Error: La reserva no existe.")
            return

        exito = baseReserva.modificarReserva(id_reserva, habitacion, huesped, entrada, salida)
        
        if exito:
            vista.mostrarMensaje("Reserva modificada correctamente.")
        else:
            vista.mostrarMensaje("Error al modificar.")
