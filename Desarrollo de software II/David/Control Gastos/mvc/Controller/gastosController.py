import View.gastosView as vista
import Data.baseGastos as base
from Model.gastosModel import Gastos

class gastosController:
	
	def __init__():
		pass
		
#--------------------------------------------------------------------------------------------------#
#Guardar gasto
	def guardarGasto(self, descripcion, monto, categoria, fecha):
		nuevoGasto = Gastos(0, descripcion, monto, categoria, fecha)
		
		
		base.guardarGastos(nuevoGasto)
		vista.mostrarMensaje("Guardado con exito")
#--------------------------------------------------------------------------------------------------#
#