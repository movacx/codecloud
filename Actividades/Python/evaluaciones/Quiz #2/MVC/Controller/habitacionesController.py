import View.habitacionesView as vista
from Model.habitacionModel import HabitacionModel
import Data.baseHabitacion as base


class HabitacionesController:

    def __init__(self):
        pass

#--------------------------------------------------------------------------------------------------#

    def registrarHabitacion(self, numeroHabitacion, tipoHabitacion, precioHabitacion, estadoHabitacion):
        nuevaHabitacion = HabitacionModel(
            0,
            numeroHabitacion,
            tipoHabitacion,
            precioHabitacion,
            estadoHabitacion
        )

        base.registrarHabitacion(nuevaHabitacion)
        vista.mostrarMensaje("Agregado correctamente")
                    
#--------------------------------------------------------------------------------------------------#

    def listarHabitacion(self):
        listaHabitaciones = base.listarHabitaciones()

        if not listaHabitaciones:
            return vista.fileNoFound()

        vista.mostrarHabitacion(listaHabitaciones)

#--------------------------------------------------------------------------------------------------#

    def buscarHabitacionId(self, idHabitacion):
        habitacionEncontrada = base.buscarHabitacionId(idHabitacion)
    
        if not habitacionEncontrada:
            return vista.fileNoFound()

        vista.mostrarHabitacion(habitacionEncontrada)
        
#--------------------------------------------------------------------------------------------------#
    def modificarEstado(self, id, estado):
        arregloVacio = base.modificar(id, estado)
    
        if not arregloVacio:
            return vista.fileNoFound()

        vista.mostrarMensaje("Modificado correctamente")
        
#--------------------------------------------------------------------------------------------------#
    def ordenarPorPrecio(self):
        listaOrdenada = base.ordenarPrecio()
        vista.mostrarHabitacion(listaOrdenada)

        
#--------------------------------------------------------------------------------------------------#
    def eliminarHabitacion(self, idHabitacion):
        arregloVacio = base.eliminarHabitacion(idHabitacion)
        vista.mostrarMensaje("Eliminado correctamente")


