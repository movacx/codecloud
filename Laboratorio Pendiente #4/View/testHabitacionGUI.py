import tkinter as tk
from tkinter import ttk,messagebox


class HabitacionGUI:
    def __init__(self, root, controller):
        self.manejoController = controller
        self.ventanaHabitacion = tk.Toplevel(root)
        self.ventanaHabitacion.geometry('1270x720')
        self.ventanaHabitacion.title('Registro Habitacion')
        
        self.labels()
        self.combobox()
      #numero, tipo, precio, estado  
    def separador(self, fila, columna):
        tk.Label(self.ventanaHabitacion, text = '').grid(row = fila, column = columna)
        
    def labels(self):
        tk.Label(self.ventanaHabitacion, text = 'Numero Habitacion:').grid(row = 0, column = 0)
        tk.Label(self.ventanaHabitacion, text = 'Tipo de Habitacion:').grid(row = 1, column = 0)
        tk.Label(self.ventanaHabitacion, text = 'Precio de Habitacion:').grid(row = 2, column = 0)
        tk.Label(self.ventanaHabitacion, text = 'Estado de Habitacion:').grid(row = 3, column = 0) 
        self.separador(4,0)
        
    def combobox(self):
        listaHabitaciones = ['101', '102', '103', '104', '105', '106', '107', '108', '109', '110']
        
        habitacioncbx = ttk.Combobox(self.ventanaHabitacion, listaHabitaciones = (lista))
        habitacioncbx.grid(row = 0, column = 1)
        
        tipocbx = ['Sencilla', 'Doble']