import View.gastosView as vista
import Data.baseGastos as base
from Model.gastosModel import Gastos

class GastosController:
	
	def __init__(self):
		pass
		
#--------------------------------------------------------------------------------------------------#
#Guardar gasto
	def guardarGasto(self, descripcion, monto, categoria, fecha):
		nuevoGasto = Gastos(0, descripcion, monto, categoria, fecha)
		
		
		base.guardarGastos(nuevoGasto)
		vista.mostrarMensaje("Guardado con exito")
#--------------------------------------------------------------------------------------------------#
#Listar Gastos
	def listarGastos(self):
		gastos = base.listarObjeto()
		for item in gastos:
			print(item)
#--------------------------------------------------------------------------------------------------#
#Ver total
	def verTotal(self):
		total = 0
		gastos = base.listarObjeto()
		for item in gastos:
			total += item[2]
		return total
#--------------------------------------------------------------------------------------------------#
#Eliminar Gastos 
			
		
		
		
			
			
			