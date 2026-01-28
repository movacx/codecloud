import View.habitacionesView as vista
import Data.baseHabitacion as baseHabitacion
#from Model.HabitacionModel import Habitacion
from Model.habitacionModel import Habitacion

class HabitacionController:
	
	def __init__(self):
		pass
	
	def registrarHabitacion(self, numero, tipo, precio, estado):
		nuevaHabitacion = Habitacion(0, numero, tipo, precio, estado)
		baseHabitacion.registrarHabitacion(nuevaHabitacion)
		
		
	def listarHabitaciones(self):
		mostrarTodos = baseHabitacion.listarHabitaciones()
		
		if not mostrarTodos:
			vista.mostrarMensaje("Error no se encontraron datos")
			return
		
	def imprimir(self,dato):
		vista.mostrarMensaje(dato)
