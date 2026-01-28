import View.habitacionesView as vista
from Model.habitacionModel import HabitacionModel
import Data.baseHabitacion as base
class HabitacionesController:
    
    def __init__(self):
        pass
    
    def registrarHabitacion(self,numero, tipo, precio, estado):
        nuevo_registro = HabitacionModel(0,numero, tipo, precio, estado)
        base.registrarHabitacion(nuevo_registro)
        vista.mostrarMensaje("Agregado correctamente")


    def listarHabitacion(self):
        mostrarTodos = base.listarTodos()
        if not mostrarTodos:
            return vista.mostrarMensaje("No hay ninguna habitacion")