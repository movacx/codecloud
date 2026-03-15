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
        self.serialHabitacion = []
        self.huesped = []


        arreglo1 = self.manejoController.actualizarListaHabitacion()
        arreglo2 = self.manejoController.actualizarListaHuespedes()

        self.actualizarListadHUD(arreglo2)
        self.actualizarListasH(arreglo1)

        self.labels()
        self.entry()
        self.buttons()

        self.tabla()
        #self.estadoDesacomodado()


 
    def actualizarListasH(self, arreglo):
        for items in arreglo:
            self.serialHabitacion.append(items)

    def actualizarListadHUD(self, arreglo):
        for items in arreglo:
            self.huesped.append(items)


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
        
        self.numeroHabitacion = ttk.Combobox(self.contenedor, values = (self.serialHabitacion), state = 'readonly')
        self.numeroHabitacion.grid(row = 0, column = 1, sticky = 'ew', columnspan = 3)

        self.idHuesped = ttk.Combobox(self.contenedor, values=(self.huesped), state = 'readonly')
        self.idHuesped.grid(row = 1, column = 1, sticky = 'ew', columnspan = 3)

        self.fechaEntrada = tk.Entry(self.contenedor)
        self.fechaEntrada.grid(row = 2, column = 1, sticky = 'ew', columnspan = 3)

        self.fechaSalida = tk.Entry(self.contenedor)
        self.fechaSalida.grid(row = 3, column = 1, sticky = 'ew', columnspan = 3)

    def buttons(self):
        tk.Button(self.contenedor, text = 'Crear una reserva', font = font, command = lambda: self.manejoController.registrarReservacion()).grid(row = 5, column = 0, sticky = 'nswe')
        tk.Button(self.contenedor, text = 'Ver reservas', font = font, command = lambda: self.manejoController.mostrarReservaciones()).grid(row = 5, column = 1, sticky = 'nswe')
        tk.Button(self.contenedor, text = 'Validar Disponibilidad', font = font, command = lambda: self.manejoController.mostrarSoloHabitacionDisponibles()).grid(row = 5, column = 2, sticky = 'nswe')
        #tk.Button(self.contenedor, text = 'Modificar Estado', font = font, command = lambda: self.manejoController.modificarEstado()).grid(row = 6, column = 0, sticky = 'nswe')
        tk.Button(self.contenedor, text = 'Eliminar Reservacion', font = font, command = lambda: self.manejoController.eliminarReservacion()).grid(row = 6, column = 0, sticky = 'news', columnspan = 3)
        self.separador(7,0)

#-------------------------------------------------------------------------------------------
    def tabla(self):
        columnas = ['id', 'N° Habitacion', 'id Huesped', 'Entrada', 'Salida']

        self.tablee = ttk.Treeview(self.contenedor, column = columnas, show = 'headings')
        self.tablee.grid(row = 8, column = 0, sticky = 'nwse', columnspan = 3)

        for items in columnas:
            self.tablee.heading(items, text = items.capitalize())
            self.tablee.column(items, width = 200)

    def cargarDatos(self, id, nHabitacion, idHuesped, entrada, salida):
        self.tablee.insert('', tk.END, values = (id, nHabitacion, idHuesped, entrada, salida))
    
    def actualizarTabla(self, arreglo):
        for items in arreglo:
            self.tablee.insert('', tk.END, values = (items[0],items[1],items[2], items[3], items[4]))
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
    def cargarTablaHabitacion(self):
        columnas = ['n°Habitacion','Tipo','Precio','Estado']
        self.tablaHabitacion = ttk.Treeview(self.contenedor, column = columnas, show = 'headings')
        self.tablaHabitacion.grid(row = 8, column = 0, sticky = 'nwse', columnspan = 3)

        for items in columnas:
            self.tablaHabitacion.heading(items, text = items.capitalize())
            self.tablaHabitacion.column(items, width = 200)
    
    def cargarHabitaciones(self, arreglo):
        for items in arreglo:
            self.tablaHabitacion.insert('', tk.END, value = (items[1], items[2], items[3], items[4]))
#-------------------------------------------------------------------------------------------   

    def estadoDesacomodado(self):
        tk.Label(self.contenedor, text = 'Estado (Solo para modificar)').grid(row = 9, column = 1, sticky = 'w') 
        tk.Label(self.contenedor, text = 'Guia: Modificar el estado toca el id de habitacion y el estado a modificar y luego el btn de modificar').grid(row = 10, column = 1, sticky = 'w') 
        opciones = ['Disponible', 'Ocupada']
        self.estadoDesacomodado = ttk.Combobox(self.contenedor, values = (opciones), state = 'readonly')
        self.estadoDesacomodado.grid(row = 9, column = 1, sticky = 'n')

    def mostrarMensaje(self, mensaje):
        messagebox.showinfo('Dialog', f'{mensaje}', parent=self.ventana)

    def limpiarTabla(self):
        for items in self.tablee.get_children():
            self.tablee.delete(items)
    def limpiarCampos(self):
        self.fechaEntrada.delete(0, tk.END)
        self.fechaSalida.delete(0, tk.END)

    def bloquearCampos(self):
        self.fechaEntrada.config(state = 'disabled')
        self.fechaSalida.delete(state = 'disabled')

    def desbloquearCampos(self):
        self.fechaEntrada.config(state = 'normal')
        self.fechaSalida.config(state = 'normal')