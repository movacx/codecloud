import tkinter as tk
from tkinter import ttk

class HistorialView:
    def __init__(self, root, controller):
        self.manejoController = controller
        self.ventana = tk.Toplevel(root)
        self.ventana.geometry('600x600')
        self.ventana.title('Historial de calculadora')
        self.mostrarTabla()

    def mostrarTabla(self):
        columnas = ['Numero 1','Operacion','Numero 2','Resultado','Fecha']
        self.tabla = ttk.Treeview(self.ventana, columns=columnas, show='headings')
        self.tabla.pack(expand=True, fill='both')
        
        for items in columnas:
            self.tabla.heading(items, text=items)