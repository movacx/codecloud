import Data.baseHabitacion as habitacion
import Data.baseReserva as reserva
import Data.huespedData as huesped

from View.fileReportesGUI import ReporteeGUI


class ReportesController:
    def __init__(self, root):
        self.ventanaReportes = root
        self.vista = ReporteeGUI(root, self)


    def saveError(self, nombre_error):
        try:

            saveerror1 = habitacion.guardarError(nombre_error)
            saveerror2 = huesped.guardarError(nombre_error)

        except Exception as error:
            print(f'ERROR CRITICO! NO SE PUDO CONECTAR LOS LOGS')


    def cargarTabla(self):
        try:

            opcionSeleccionada = self.vista.opcionSeleccionada.get()
            if opcionSeleccionada == 'Huespedes':
                try:
                    arregloHuesped = huesped.listarTodos()
                    self.vista.tasblas(1)
                    self.vista.cargarHuespedes(arregloHuesped)
                except Exception as error:
                    self.vista.errorMessage(f'Hubo un error, no se puede mostrar la tabla. \nPara mas informacion: /data/log/logfile.txt')
                    self.saveError(f'Dentro del case Huesped: {error}')
                
            elif opcionSeleccionada == 'Habitaciones':
                try:
                    registroHabitacion = habitacion.listarHabitaciones()
                    self.vista.tablas(2)
                    self.vista.cargarHabitaciones(registroHabitacion)
                except Exception as error:
                    self.vista.errorMessage(f'Hubo un error, no se puede mostrar la tabla. \nPara mas informacion: /data/log/logfile.txt')
                    self.saveError(f'Dentro del case Habitaciones: {error}')

            elif opcionSeleccionada == 'Reservas':
                try:
                    registroReservaciones = reserva.listarReservas()
                    self.vista.tablas(3)
                    self.vista.cargarReservas(registroReservaciones)
                except Exception as error:
                    self.vista.errorMessage(f'Hubo un error, no se puede mostrar la tabla. \nPara mas informacion: /data/log/logfile.txt')
                    self.saveError(f'Dentro del case Reservas: {error}')

        except Exception as error:
            self.vista.errorMessage(f'Hubo un error dentro de la funcion cargar tabla! = {error}')



        
        