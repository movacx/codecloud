import View.habitacionesView as vista
import Data.baseHabitacion as baseHabitacion
from Model.HabitacionModel import Habitacion
class habitacionController:
	
	def __init__(self):
		pass
	
	def registrarHabitacion(numero, tipo, precio, estado):
		nuevaHabitacion = Habitacion(0, numero, tipo, precio, estado)
		baseHabitacion.agregarListado(nuevaHabitacion)
		
		
	def listarHabitaciones():
		
		mostrarTodos = baseHabitacion.listarHabitaciones()
		if not mostrarTodos:
			vista.mostrarMensaje("Error no se encontraron datos")
			return
		return vista.mostrarDatos(mostrarTodos)