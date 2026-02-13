import tkinter as tk
from tkinter import Menu

class ReportesGUI:
    def __init__(self, baseMainGUI, controller):
        self.manejoController = controller
        self.ventana = tk.Toplevel(baseMainGUI)
        self.ventana.title("Reportes Base")
        self.ventana.geometry("900x950")
        
        barra_menu = tk.Menu(self.ventana)
        
        
        self.menu_desplegable = tk.Menu(barra_menu, tearoff=0)
        
        
        self.menu_desplegable.add_command(label="Reportes de habitaciones disponibles")
        self.menu_desplegable.add_command(label="Reportes de habitaciones ocupadas")
        self.menu_desplegable.add_command(label="Reportes de reservaciones activas")
        self.menu_desplegable.add_separator()
        self.menu_desplegable.add_command(label="Salir", command=self.ventana.destroy)
        
        barra_menu.add_cascade(label="Menu de Reportes", menu=self.menu_desplegable)
        
        self.ventana.config(menu=barra_menu)