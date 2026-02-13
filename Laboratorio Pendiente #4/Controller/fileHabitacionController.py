import tkinter as tkGUI
from tkinter import messagebox
from View.habitacionGUI import HabitacionGUI

class HabitacionController():
	def __init__(self, root):
		self.ventana = root
		self.GUI = HabitacionGUI(root,self)
		
		
		