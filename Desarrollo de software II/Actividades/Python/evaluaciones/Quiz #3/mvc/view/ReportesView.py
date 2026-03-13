import tkinter as tk
from tkinter import ttk, messagebox

class ReporteGUI:
    def __init__(self, root, controller):
        self.ventana = tk.Toplevel(root)
        self.manejoController = controller
        self.ventana.geometry('800x800')
        self.ventana.title('Reporte Banco')
        self.ventana.columnconfigure(0, weight = 1)
        self.ventana.rowconfigure(0, weight = 1)
        tk.Button(self.ventana, text='Mostrar', command=lambda: self.manejoController.cargarDatos()).grid(row=1, column=0, sticky = 'ns')
        self.tablas()

    def tablas(self):
        self.columnas = ['DNI','Cueta','Saldo']
        self.tabla = ttk.Treeview(self.ventana, columns = self.columnas, show = 'headings')
        self.tabla.grid(row =0, column = 0, sticky = 'nswe')

        for items in self.columnas:
            self.tabla.heading(items, text = items)

    
    def cargarTabla(self, arreglo):
        for items in self.tabla.get_children():
            self.tabla.delete(items)
            
        for items in arreglo:
            self.tabla.insert('', tk.END, values = (items[0], items[1], items[2]))

    