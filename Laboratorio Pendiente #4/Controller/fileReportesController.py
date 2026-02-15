import Data.baseHabitacion as habitacion
import Data.baseReserva as reserva
import Data.huespedData as huesped

from View.fileReportesGUI import ReporteeGUI


class ReportesController:
    def __init__(self, root):
        self.ventanaReportes = root
        self.vista = ReporteeGUI(root, self)

    def cargarTabla(self):
        opcionSeleccionada = self.vista.opcionSeleccionada.get()

        if opcionSeleccionada == 'Huespedes':
              
            arregloHuesped = huesped.listarTodos()
            self.vista.tablas(1)
            self.vista.cargarHuespedes(arregloHuesped)
            
        elif opcionSeleccionada == 'Habitaciones':
            registroHabitacion = habitacion.listarHabitaciones()
            self.vista.tablas(2)
            self.vista.cargarHabitaciones(registroHabitacion)
   
        elif opcionSeleccionada == 'Reservas':
            registroReservaciones = reserva.listarReservas()
            self.vista.tablas(3)
            self.vista.cargarReservas(registroReservaciones)



        
        