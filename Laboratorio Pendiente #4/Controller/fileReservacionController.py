import Data.baseReserva as dataReserva
import Data.baseHabitacion as dataHabitacion
import Data.huespedData as dataHuesped
from Model.reservaModel import Reserva
from View.fileReservasGUI import ReservaGUI

class ReservaController:
    def __init__(self, root):
        self.ventanaPrincipal = root
        self.vista = ReservaGUI(root, self)

    def crearReserva(self):
        try:
            numeroHabitacion = self.vista.numeroHabitacion.get()
            idHuesped = self.vista.idHuesped.get()
            fechaEntrada = self.vista.fechaEntrada.get()
            fechaSalida = self.vista.fechaSalida.get()

            if not numeroHabitacion or not idHuesped or not fechaEntrada or not fechaSalida:
                self.vista.mostrarMensaje('Debe completar todos los campos')
                return

            huespedEncontrado = dataHuesped.searchId(idHuesped)
            if not huespedEncontrado:
                self.vista.mostrarMensaje('El huesped no existe')
                return

            habitacionEncontrada = dataHabitacion.buscarHabitacionId(numeroHabitacion)
            if not habitacionEncontrada:
                self.vista.mostrarMensaje('La habitacion no existe')
                return

            estadoHabitacion = habitacionEncontrada[0][4]
            if estadoHabitacion != "Disponible":
                self.vista.mostrarMensaje("La habitacion no esta disponible")
                return

            nuevaReserva = Reserva(0, numeroHabitacion, idHuesped, fechaEntrada, fechaSalida)
            dataReserva.registrarReserva(nuevaReserva)

            dataHabitacion.modificar(numeroHabitacion, "Ocupada")

            self.vista.mostrarMensaje("Reserva creada correctamente")
            self.verReservas()

        except Exception as error:
            self.vista.mostrarMensaje(f"Error al crear reserva: {error}")

    def verReservas(self):
        try:
            arreglo = dataReserva.listarReservas()
            self.vista.limpiarTabla()
            self.vista.cargarListaReservas(arreglo)
        except Exception as error:
            self.vista.mostrarMensaje(f"Error al cargar reservas: {error}")

    def eliminarReserva(self):
        try:
            idReserva = self.vista.obtenerIdReservaSeleccionada()
            if not idReserva:
                self.vista.mostrarMensaje("Seleccione una reserva en la tabla")
                return

            reservaEncontrada = dataReserva.buscarReservaPorId(idReserva)
            if not reservaEncontrada:
                self.vista.mostrarMensaje("Reserva no existe")
                return

            numeroHabitacion = reservaEncontrada[0][1]

            dataReserva.eliminarReserva(idReserva)
            dataHabitacion.modificar(numeroHabitacion, "Disponible")






            self.vista.mostrarMensaje("Reserva eliminada y habitacion liberada")
            self.verReservas()

        except Exception as error:
            self.vista.mostrarMensaje(f"Error al eliminar reserva: {error}")
