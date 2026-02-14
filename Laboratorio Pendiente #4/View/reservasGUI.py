import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
font = 'Arial, 12'

class ReservaGUI:

    def __init__(self, root, controller):
        self.manejoController = controller

        #========= Establacer la ventana ===============
        self.ventana = tk.Toplevel(root)
        self.ventana.geometry('1070x600')
        self.ventana.title('Reservas')

        self.ventana.columnconfigure(0, weight = 1)
        #========= Establecer contenedores =============

        self.contenedor = tk.Frame(self.ventana)
        self.contenedor.grid(row = 0, column = 0, padx = 20, pady = 20, sticky = 'nswe')

        self.contenedor.columnconfigure(0, weight = 0)
        self.contenedor.columnconfigure(1, weight = 1)
        self.contenedor.columnconfigure(2, weight = 0)

        self.labels()
        self.entry()
        self.buttons()
        self.tabla()
        self.barMenu()


    def separador(self, fila, columna):
        self.vacio = tk.Label(self.contenedor, text= ' ').grid(row = fila, column = columna)
        return self.vacio
    
    def labels(self):
        tk.Label(self.contenedor, text = 'Numero Habitacion:', font = font).grid(row = 0, column = 0, sticky = 'w')
        tk.Label(self.contenedor, text = 'Id Huesped:', font = font).grid(row = 1, column = 0, sticky = 'w')
        tk.Label(self.contenedor, text = 'Fecha de entrada:', font = font).grid(row = 2, column = 0, sticky = 'w')
        tk.Label(self.contenedor, text = 'Fecha de salida:', font = font).grid(row=3,column=0, sticky = 'w')
        self.separador(4,0)
    
    def entry(self):
        self.numeroHabitacion = tk.Entry(self.contenedor)
        self.numeroHabitacion.grid(row = 0, column = 1, sticky = 'ew', columnspan = 3)

        self.idHuesped = tk.Entry(self.contenedor)
        self.numeroHabitacion.grid(row = 0, column = 1, )
        self.idHuesped.grid(row = 1, column = 1, sticky = 'ew', columnspan = 3)

        self.fechaEntrada = tk.Entry(self.contenedor)
        self.fechaEntrada.grid(row = 2, column = 1, sticky = 'ew', columnspan = 3)

        self.fechaSalida = tk.Entry(self.contenedor)
        self.fechaSalida.grid(row = 3, column = 1, sticky = 'ew', columnspan = 3)

    def buttons(self):
        tk.Button(self.contenedor, text = 'Crear una reserva', font = font).grid(row = 5, column = 0, sticky = 'nswe')
        tk.Button(self.contenedor, text = 'Ver reservas', font = font).grid(row = 5, column = 1, sticky = 'nswe')
        tk.Button(self.contenedor, text = 'Validar Disponibilidad', font = font).grid(row = 5, column = 2, sticky = 'nswe')
        tk.Button(self.contenedor, text = 'Modificar Estado', font = font).grid(row = 6, column = 0, sticky = 'nswe')
        tk.Button(self.contenedor, text = 'Eliminar Reservacion', font = font).grid(row = 6, column = 1, sticky = 'news', columnspan = 2)
        self.separador(7,0)


    def tabla(self):
        columnas = ['id', 'N° Habitacion', 'id Huesped', 'Entrada', 'Salida']

        self.tablee = ttk.Treeview(self.contenedor, column = columnas, show = 'headings')
        self.tablee.grid(row = 8, column = 0, sticky = 'nwse', columnspan = 3)

        for items in columnas:
            self.tablee.heading(items, text = items.capitalize())
            self.tablee.column(items, width = 200)
            
    def cargarDatos(self, id, nHabitacion, idHuesped, entrada, salida):
        self.tablee.insert('', tk.END, values = (id, nHabitacion, idHuesped, entrada, salida))
    
    def mostrarMensaje(self, mensaje):
        messagebox.showinfo('Dialog', f'{mensaje}')

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
