import tkinter as tkGUI
from tkinter import messagebox
from View.habitacionGUI import HabitacionGUI
import Data.baseHabitacion as data

class HabitacionController():
	def __init__(self, root):
		self.ventana = root
		self.GUI = HabitacionGUI(root,self)
		self.manejoData = data

	def registrarHabitacion():
		pass

	def ListarHabitacion():
		pass
		
	
	def buscarHabitacion():
		pass
		
		
		
	def modificarEstado():
		pass
		
		
		
	def ordenarPorPrecio():
		pass
	
	
	def botonClick(self, boton):
		if boton == "x":
			print("El usuario dio click")
			#showinfo.tk.messagebox("Prueba" , "El usuario clickeo un boton")
		
			