import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ReservaGUI:

    def __init__(self, root, controller):
        self.manejoController = controller

        self.ventana = tk.Toplevel(root)
        self.ventana.geometry('300x300')
        self.ventana.title('Reservas')
        
        self.contenedor = tk.Frame(self.ventana)
        self.contenedor.grid(row = 0, column = 0, padx = 20, pady = 20, sticky="nw")

        tk.Label(self.contenedor, text = 'Numero Habitacion:').grid(row = 0, column = 0, sticky = 'e', pady=2)
        self.numeroHabitacion = tk.Entry(self.contenedor, width=25)
        self.numeroHabitacion.grid(row = 0, column = 1, sticky = 'w')

        tk.Label(self.contenedor, text = 'Id Huesped:').grid(row = 1, column = 0, sticky = 'e', pady=2)
        self.idHuesped = tk.Entry(self.contenedor, width=25)
        self.idHuesped.grid(row = 1, column = 1, sticky = 'w')

        tk.Label(self.contenedor, text = 'Fecha de entrada:').grid(row = 2, column = 0, sticky = 'e', pady=2)
        self.fechaEntrada = tk.Entry(self.contenedor, width=25)
        self.fechaEntrada.grid(row = 2, column = 1, sticky = 'w')

        tk.Label(self.contenedor, text = 'Fecha de salida:').grid(row = 3, column = 0, sticky = 'e', pady=2)
        self.fechaSalida = tk.Entry(self.contenedor, width=25)
        self.fechaSalida.grid(row = 3, column = 1, sticky = 'w')

        tk.Button(self.contenedor, text = 'Crear una reserva').grid(row = 4, column = 0, pady=10)
        tk.Button(self.contenedor, text = 'Ver reservas').grid(row = 4, column = 1, sticky="w")
        
        tk.Button(self.contenedor, text = 'Modificar Estado').grid(row = 5, column = 0)
        tk.Button(self.contenedor, text = 'Eliminar Reservacion').grid(row = 5, column = 1, sticky="w")

        columnas = ['id', 'N° Habitacion', 'id Huesped', 'Entrada', 'Salida']
        self.tablee = ttk.Treeview(self.contenedor, column = columnas, show = 'headings', height=12)
        self.tablee.grid(row = 6, column = 2, columnspan = 5, padx = 50, pady = 10, sticky="nsew")

        for items in columnas:
            self.tablee.heading(items, text = items)
            self.tablee.column(items, width = 110)

        tk.Button(self.contenedor, text="Limpiar").grid(row=7, column=3, sticky="e")

    def cargarDatos(self, id, nHabitacion, idHuesped, entrada, salida):
        self.tablee.insert('', tk.END, values = (id, nHabitacion, idHuesped, entrada, salida))
    
    def mostrarMensaje(self, mensaje):
        messagebox.showinfo('Dialog', f'{mensaje}')