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
        estadoo = 'ocupado'
        numeroHabitacion = self.vista.numeroHabitacion.get()
        idHuesped = self.vista.idHuesped.get()
        fechaEntrada = self.vista.fechaEntrada.get()
        fechaSalida = self.vista.fechaSalida.get()

        huespedEncontrado = dataHuesped.searchId(idHuesped)

        habitacionEncontrada = dataHabitacion.buscarHabitacionId(numeroHabitacion)


        #id, numeroHabitacion, idHuesped, fechaEntrada, fechaSalida
        nuevaReserva = Reserva(0, numeroHabitacion, idHuesped, fechaEntrada, fechaSalida)
        dataReserva.registrarReserva(nuevaReserva)

        dataHabitacion.modificar(numeroHabitacion, "Ocupada")

        self.vista.mostrarMensaje("Reserva creada correctamente")
        self.verReservas()



    def verReservas(self):
        try:
            arreglo = dataReserva.listarReservas()
            # self.vista.limpiarTabla()
            self.vista.mostrarRegistros(arreglo)
        except Exception as error:
            self.vista.mostrarMensaje(f"Error al cargar reservas: {error}")

    def eliminarReserva(self):
        # try:
        numHabitacion = self.vista.numeroHabitacion.get()
        if not numHabitacion:
            self.vista.mostrarMensaje("Debe de llenar el campo de num Habitacion")
            return

        # reservaEncontrada = dataReserva.buscarReservaPorId(idReserva)
        # if not reservaEncontrada:
        #     self.vista.mostrarMensaje("Reserva no existe")
        #     return

        # numeroHabitacion = reservaEncontrada[0][1]

        dataReserva.eliminarReserva(numHabitacion)
        dataHabitacion.modificar(numHabitacion, "Disponible")


        self.vista.mostrarMensaje("Reserva eliminada y habitacion liberada")
        # self.verReservas()

        # except Exception as error:
        #     self.vista.mostrarMensaje(f"Error al eliminar reserva: {error}")
