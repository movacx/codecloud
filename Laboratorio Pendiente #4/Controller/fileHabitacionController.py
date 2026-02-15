import tkinter as tkGUI
from tkinter import messagebox
from View.habitacionGUI import HabitacionGUIz
import Data.baseHabitacion as data
from Model.habitacionModel import HabitacionModel

class HabitacionController():
	def __init__(self, root):
		self.ventana = root
		self.GUI = HabitacionGUI(root,self)
		self.manejoData = data
		
    def obtenerUltimoId(self):
		ultimoId = self.manejoData.validarUltimoId()
		return ultimoId
	
	def registrarHabitacion(self):
		numero =self.GUI.entradaNumeroHabitacion.get()
		tipo = self.GUI.comboboxTipoHabitacion.get()
		precio = self.GUI.entradaPrecioHabitacion.get()
		estado = self.GUI.comboboxEstadoHabitacion.get()
		nuevoRegistro= HabitacionModel(self.obtenerUltimoId(),numero,tipo,precio,estado)
		self.manejoData.registrarHabitacion(nuevoRegistro)
	
	def ListarHabitacion():
		self.manejoData.listarHabitaciones()
		
	
	def buscarHabitacion():
		pass
		
		
		
	def modificarEstado():
		pass
		
		
		
	def ordenarPorPrecio():
		pass
	
	
	def botonClick(self, boton):
		if boton == "x":
			print("El usuario dio click")
			messagebox.showinfo("Prueba" , "El usuario clickeo un boton")
		
			