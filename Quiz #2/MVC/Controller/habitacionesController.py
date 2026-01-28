import View.habitacionesView as vista
from Model.habitacionModel import HabitacionModel
import Data.baseHabitacion as base
class HabitacionesController:
    
    def __init__(self):
        pass

    def test(self, data):
        vista.mostrarMensaje(data)
