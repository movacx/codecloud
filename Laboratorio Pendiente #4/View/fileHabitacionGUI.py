import tkinter as tk
from tkinter import ttk

class HabitacionGUI:
    def __init__(self, ventanaPadre, habitacionesController):
        self.ventanaHija = tk.Toplevel(ventanaPadre)
        self.ventanaHija.title("Mantenimiento de Habitaciones")
        self.ventanaHija.geometry("700x300")
        self.ventanaHija.columnconfigure(0,weight=0)
        self.ventanaHija.columnconfigure(1,weight=1)
        self.manejoController = habitacionesController
        self.tablas()

        self.frameContenedor = tk.Frame(self.ventanaHija)
        self.frameContenedor.grid(row=0, column=0, padx=20, pady=20)
        
        self.formularioCrear()
        
    def formularioCrear(self):
        tk.Label(self.ventanaHija, text="Numero de Habitación:").grid(row=0, column=0, sticky="e", pady=5)
        self.entradaNumeroHabitacion = tk.Entry(self.ventanaHija)
        self.entradaNumeroHabitacion.grid(row=0, column=1, pady=5)
        
        
        tk.Label(self.ventanaHija, text="Tipo de Habitacion:").grid(row=1, column=0, sticky="e", pady=5)
        self.comboboxTipoHabitacion = ttk.Combobox(self.ventanaHija, values=["Sencilla", "Doble", "Suite"], state="readonly")
        self.comboboxTipoHabitacion.grid(row=1, column=1, pady=5)
        
        
        tk.Label(self.ventanaHija, text="Precio por Noche:").grid(row=2, column=0, sticky="e", pady=5)
        self.entradaPrecioHabitacion = tk.Entry(self.ventanaHija)
        self.entradaPrecioHabitacion.grid(row=2, column=1, pady=5)
        
        
        tk.Label(self.ventanaHija, text="Estado de Habitacion:").grid(row=3, column=0, sticky="e", pady=5)
        self.comboboxEstadoHabitacion = ttk.Combobox(self.ventanaHija, values=["Disponible", "Ocupada"], state="readonly")
        self.comboboxEstadoHabitacion.grid(row=3, column=1, pady=5)

        #Guardar habitacion
        self.btnGuardarHabitacion = tk.Button(self.ventanaHija, text="Guardar Habitación", bg="#4CAF50", fg="white", command=lambda: self.manejoController.registrarHabitacion())
        self.btnGuardarHabitacion.grid(row=4, column = 0, pady=15, ipadx=1)
        
        
        #Buscar habitacion
        self.btnBuscarHabitacion = tk.Button(self.ventanaHija, text ="Buscar Habitacion", bg = "#4CAF50", fg="white")
        self.btnBuscarHabitacion.grid(row=5, column=0, pady=15, ipadx=1)
        
        #Modificar habitacion
        self.btnModificarHabitacion = tk.Button(self.ventanaHija, text ="Modificar Habitacion", bg= "#4CAF50", fg="white")
        self.btnModificarHabitacion.grid(row=4, column=1, pady=15, ipadx=1)
        
        #Eliminar habitacion
        self.btnEliminarHabitacion= tk.Button(self.ventanaHija, text= "Eliminar Habitacion", bg=  "#4CAF50", fg="white")
        self.btnEliminarHabitacion.grid(row=5, column= 1)
    
        #Listar Habitaciones
        self.btnListarHabitaciones = tk.Button(self.ventanaHija, text = "Listar habitaciones", bg = "#4CAF50", fg="white")
        self.btnListarHabitaciones.grid(row = 5 , column= 3)
        
    def tablas(self):
        arregloColumnas = ["ID, Numero, Tipo, Precio, Estado"]
        self.table = ttk.Treeview(self.ventanaHija, columns = arregloColumnas, show= "headings")
        self.table.grid(row = 0, column = 1)
        #self.table.place(ancho = "center", relx=0.5,rely=0.5)
        self.table.heading(1,text= "Hola mundo")
        






