import Data.baseReserva as dataReserva
import Data.baseHabitacion as dataHabitacion
import Data.huespedData as dataHuesped


from View.fileReservasGUI import ReservaGUI
from Model.reservaModel import Reserva

class ReservaController:
    def __init__(self, root):
        self.GUI  = ReservaGUI(root,self)


    def saveError(self, nombre_error):
        try:
            dataReserva.guardarError(nombre_error)
        except Exception as error:
            print(f'ERROR CRITICO NO SE PUDO CONECTAR EL CONTROLLER ERROR CON EL DATA ERROR>>>SAVELOG {error}')

    def actualizarListaHabitacion(self):
        try:

            numHabitacion = dataHabitacion.listarHabitaciones()
            filtroHabitacion = []
            for habitaciones in numHabitacion:
                filtroHabitacion.append(habitaciones[1])

            return filtroHabitacion
        
        except Exception as error:
            self.saveError(error)

    def actualizarListaHuespedes(self):
        try:

            numHuesped = dataHuesped.listarTodos()
            filtroHuesped = []
            for items in numHuesped:
                filtroHuesped.append(items[0])

            return filtroHuesped

        except Exception as error:
            self.saveError(error)

    def registrarReservacion(self):
        try:

            id = dataReserva.validarUltimoId()
            numHabitcn = self.GUI.numeroHabitacion.get()
            idHuesped = self.GUI.idHuesped.get()
            fEntrada = self.GUI.fechaEntrada.get()
            fSalida = self.GUI.fechaSalida.get()

            if not fEntrada:
                self.GUI.mostrarMensaje('Debe de completar los campos para continuar')
            else:
                if not fSalida:
                    self.GUI.mostrarMensaje('Debe de completar los campos para continuar')
                else:
                    nuevaReservacionOB = Reserva(id, numHabitcn, idHuesped, fEntrada, fSalida)
                    exito = dataReserva.registrarReserva(nuevaReservacionOB)
                    if exito:
                        self.GUI.cargarDatos(id, numHabitcn, idHuesped, fEntrada, fSalida)

                        estado = 'Ocupado'
                        
                        dataHabitacion.modificar(numHabitcn, estado)



                        return self.GUI.mostrarMensaje('Reservacion creada con exito!')
                    else:
                        return self.GUI.mostrarMensaje('Hubo un error.')
            
        except Exception as error:
            self.saveError(error)

    def mostrarReservaciones(self):
        try:
            self.GUI.limpiarTabla()
            arreglo = dataReserva.listarReservas()
            if not arreglo:
                self.GUI.mostrarMensaje('No se encontraron datos pa')
                
            else:
                self.GUI.actualizarTabla(arreglo)

        except Exception as error:
            self.saveError(error)
            self.GUI.mostrarMensaje(f'Error interno {error}')

    def mostrarSoloHabitacionDisponibles(self):
        try:

            self.GUI.limpiarTabla()
            self.GUI.limpiarCampos()

            arreglo = dataHabitacion.listarHabitaciones()
            habDisponibles = []

            for items in arreglo:
                if items[4].lower() == 'disponible':
                    habDisponibles.append(items)
    
            self.GUI.actualizarTabla(habDisponibles)
        except Exception as error:
            self.saveError(error)
            self.GUI.mostrarMensaje(f'Error interno {error}')

    def eliminarReservacion(self):
        try:

            id = self.GUI.numeroHabitacion.get()
            dataReserva.eliminarReserva(id)

            estado = 'Disponible'
            exito = dataHabitacion.modificar(id, estado)
            if exito:
                self.GUI.mostrarMensaje('Exito al eliminar!')
            else:
                self.GUI.mostrarMensaje('Ha ocurrido un error')

        except Exception as error:
            self.savelog(error)
            self.GUI.errorMessage('Hubo un error. Para mas informacion valide el logfile')
    