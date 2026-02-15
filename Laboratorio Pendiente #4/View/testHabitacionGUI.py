import tkinter as tk
from tkinter import ttk,messagebox


class HabitacionGUI:
    
    def __init__(self, root, controller):
        self.manejoController = controller
        self.ventanaHabitacion = tk.Toplevel(root)
        self.ventanaHabitacion.geometry('1270x720')
        self.ventanaHabitacion.title('Registro Habitacion')
        
        
        self.ventanaHabitacion.columnconfigure(0, weight = 0)
        self.ventanaHabitacion.columnconfigure(1, weight = 1)
        self.ventanaHabitacion.columnconfigure(2, weight = 0)
        self.ventanaHabitacion.rowconfigure(9, weight = 1)
        
        self.labels()
        self.entry()
        self.combobox()
        self.botones()
        self.table()
      #numero, tipo, precio, estado  
    def separador(self, fila, columna):
        tk.Label(self.ventanaHabitacion, text = '').grid(row = fila, column = columna)
        
    def labels(self):
        tk.Label(self.ventanaHabitacion, text = 'Numero Habitacion:').grid(row = 0, column = 0, sticky = 'w')
        self.separador(1,0)
        tk.Label(self.ventanaHabitacion, text = 'Tipo de Habitacion:').grid(row = 2, column = 0, sticky = 'w')
        self.separador(3,0)
        tk.Label(self.ventanaHabitacion, text = 'Precio de Habitacion:').grid(row = 4, column = 0, sticky = 'w')
        self.separador(5,0)
        tk.Label(self.ventanaHabitacion, text = 'Estado de Habitacion:').grid(row = 6, column = 0, sticky = 'w') 
        self.separador(7,0)
        
    def combobox(self):
        listaHabitaciones = ['101', '102', '103', '104', '105', '106', '107', '108', '109', '110']
        
        self.habitacioncbx = ttk.Combobox(self.ventanaHabitacion, values = (listaHabitaciones), state = 'readonly')
        self.habitacioncbx.grid(row = 0, column = 1, sticky = 'nswe')
        
        listaTipoHabitacion = ['Sencilla', 'Doble']
        self.tipoHabitacioncbx = ttk.Combobox(self.ventanaHabitacion, values = (listaTipoHabitacion), state = 'readonly')
        self.tipoHabitacioncbx.grid(row = 2, column = 1, sticky = 'nswe')
        
        listaEstadoHabitacion = ['Disponible', 'Ocupada']
        self.estadoHabitacioncbx = ttk.Combobox(self.ventanaHabitacion, values = (listaEstadoHabitacion), state = 'readonly')
        self.estadoHabitacioncbx.grid(row = 6, column = 1, sticky = 'nswe')
        
    def entry(self):
        self.precioTxt = tk.Entry(self.ventanaHabitacion)
        self.precioTxt.grid(row = 4, column = 1, sticky = 'nswe')
        
        self.numHabitacionTxt = tk.Entry(self.ventanaHabitacion)
        self.numHabitacionTxt.grid(row = 0, column = 1, sticky = 'nswe')
        
    def botones(self):
        self.separador(5,0)
        tk.Button(self.ventanaHabitacion, text = 'Guardar').grid(row = 6, column = 0, sticky = 'nswe')
        tk.Button(self.ventanaHabitacion, text = 'Buscar').grid(row = 6, column = 1, sticky = 'nswe')
        tk.Button(self.ventanaHabitacion, text = 'Modificar').grid(row = 6, column = 2, sticky = 'nswe')
        tk.Button(self.ventanaHabitacion, text = 'Eliminar').grid(row = 7, column = 0, sticky = 'nswe')
        tk.Button(self.ventanaHabitacion, text = 'Guardar').grid(row = 7, column = 1, sticky = 'nswe')
        tk.Button(self.ventanaHabitacion, text = 'Limpiar').grid(row = 7, column = 2, sticky = 'nswe')
        self.separador(8,0)
        
    def table(self):
        columnas = ['n°Habitacion','Tipo','Precio','Estado']
        self.tabla = ttk.Treeview(self.ventanaHabitacion, columns = columnas, height = 24, show = 'headings')
        self.tabla.grid(row = 9, column = 0, columnspan = 4, sticky = 'nswe', padx = (5,5), pady = 5)
        for items in columnas:
            self.tabla.heading(items, text = items.capitalize())
        
    def errorMessage(self, mensaje):
        messagebox.showerror('Error!', f'{mensaje}')
        print(f'Hubo un error, validar el logfile | {mensaje}')
        
    
    