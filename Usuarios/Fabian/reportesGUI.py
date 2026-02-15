import tkinter as tk
from tkinter import Menu

class ReportesGUI:
    def __init__(self, baseMainGUI, controller):
        self.manejoController = controller
        #Construir Ventana
        self.ventana = tk.Toplevel(baseMainGUI)
        self.ventana.title("Reportes Base")
        self.ventana.geometry("900x950")
        
        

        #Llamados de funciones
        self.barMenu()
        
    def barMenu(self):
        #instancia del Barmenu
        self.barraMenu = tk.Menu(self.ventana)

        self.menuDesplegable = tk.Menu(self.barraMenu, tearoff=0)
        
        self.menuDesplegable.add_command(label="Reportes de habitaciones disponibles")
        self.menuDesplegable.add_command(label="Reportes de habitaciones ocupadas")
        self.menuDesplegable.add_command(label="Reportes de reservaciones activas")
        self.menuDesplegable.add_separator()
        self.menuDesplegable.add_command(label="Salir", command=self.ventana.destroy)
        
        self.barraMenu.add_cascade(label="Menu de Reportes", menu=self.menuDesplegable)
        
        self.ventana.config(menu=self.barraMenu)