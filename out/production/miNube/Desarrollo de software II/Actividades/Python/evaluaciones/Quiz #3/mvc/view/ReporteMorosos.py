import tkinter as tk
from tkinter import ttk
class ReporteMorosos:
    def __init__(self, root, controller):
        self.manejoController = controller

        self.ventana = tk.Toplevel(root)
        self.ventana.geometry('800x800')
        self.ventana.title('Reporte de Clientes mas morosos y activos')

        self.ventana.rowconfigure(0, weight = 1)
        self.ventana.columnconfigure(0, weight = 1)
        tk.Button(self.ventana, text = 'Mostrar', command = lambda: self.manejoController.mostrarDatos()).grid(row=1,column=0)

        self.crearTabla()

    def crearTabla(self):
        columnas = ['DNI','Monto','Plazo','Cuotas Pagadas',"Estado"]
        self.tabla = ttk.Treeview(self.ventana, columns = columnas, show = 'headings')
        self.tabla.grid(row = 0, column = 0, sticky = 'nswe')
        for items in columnas:
            self.tabla.heading(items, text = items)

        
    def cargarTabla(self, arreglo):
    
        for items in arreglo:
            self.tabla.insert('',tk.END, values = (items[1], items[2], items[3], items[4], items[5])) 
