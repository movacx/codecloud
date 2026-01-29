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
		if not gastos:
			vista.mostrarMensaje("No se encontro ningun gasto")
		vista.mostrarGastos(gastos)
#--------------------------------------------------------------------------------------------------#
#Ver total
	def verTotal(self):
		total = 0
		gastos = base.listarObjeto()
		for item in gastos:
			total += int(item[2])
		vista.mostrarDatos(total)
#--------------------------------------------------------------------------------------------------#
#Eliminar Gastos 
	def eliminarGastos(self, id):
		eliminado = base.eliminarGastos(id)
		if eliminado == True:
			vista.mostrarMensaje("Eliminado con exito")
		else:
			vista.mostrarMensaje("No se encontro ningun gasto")
		
		
		
		
		
			
			
			