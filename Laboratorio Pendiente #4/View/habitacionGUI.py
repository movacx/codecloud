import tkinter as tk
from tkinter import ttk

class HabitacionGUI:
<<<<<<< HEAD
    def __init__(self, ventanaPadre, habitacionesController):
        self.ventanaHija = tk.Toplevel(ventanaPadre)
        self.ventanaHija.title("Mantenimiento de Habitaciones")
        self.ventanaHija.geometry("700x300")
=======
    def __init__(self, ventana_padre):
        
        self.ventana_hija = tk.Toplevel(ventana_padre)
        self.ventana_hija.title("Mantenimiento de Habitaciones")
        self.ventana_hija.geometry("350x300")
>>>>>>> 5da4d2745ce45ec343fa8168bda6d3d1c8f8aec3
        
        self.manejoController = habitacionesController
        self.frameContenedor = tk.Frame(self.ventanaHija)
        self.frameContenedor.grid(row=0, column=0, padx=20, pady=20)
        
        self.formularioCrear()
        
    def formularioCrear(self):
        
        tk.Label(self.frameContenedor, text="Numero de Habitación:").grid(row=0, column=0, sticky="e", pady=5)
        self.entradaNumeroHabitacion = tk.Entry(self.frameContenedor)
        self.entradaNumeroHabitacion.grid(row=0, column=1, pady=5)
        
        
        tk.Label(self.frameContenedor, text="Tipo de Habitacion:").grid(row=1, column=0, sticky="e", pady=5)
        self.comboboxTipoHabitacion = ttk.Combobox(self.frameContenedor, values=["Sencilla", "Doble", "Suite"], state="readonly")
        self.comboboxTipoHabitacion.grid(row=1, column=1, pady=5)
        
        
        tk.Label(self.frameContenedor, text="Precio por Noche:").grid(row=2, column=0, sticky="e", pady=5)
        self.entradaPrecioHabitacion = tk.Entry(self.frameContenedor)
        self.entradaPrecioHabitacion.grid(row=2, column=1, pady=5)
        
        
        tk.Label(self.frameContenedor, text="Estado de Habitacion:").grid(row=3, column=0, sticky="e", pady=5)
        self.comboboxEstadoHabitacion = ttk.Combobox(self.frameContenedor, values=["Disponible", "Ocupada"], state="readonly")
        self.comboboxEstadoHabitacion.grid(row=3, column=1, pady=5)

        #Guardar habitacion
        self.btnGuardarHabitacion = tk.Button(self.frameContenedor, text="Guardar Habitación", bg="#4CAF50", fg="white")
        self.btnGuardarHabitacion.grid(row=4, column = 0, pady=15, ipadx=1)
        
<<<<<<< HEAD
        #Buscar habitacion
        self.btnBuscarHabitacion = tk.Button(self.frameContenedor, text ="Buscar Habitacion", bg = "#4CAF50", fg="white")
        self.btnBuscarHabitacion.grid(row=5, column=0, pady=15, ipadx=1)
        
        #Modificar habitacion
        self.btnModificarHabitacion = tk.Button(self.frameContenedor, text ="Modificar Habitacion", bg= "#4CAF50", fg="white")
        self.btnModificarHabitacion.grid(row=4, column=1, pady=15, ipadx=1)
        
        #Eliminar habitacion
        self.btnEliminarHabitacion= tk.Button(self.frameContenedor, text= "Eliminar Habitacion", bg=  "#4CAF50", fg="white")
        self.btnEliminarHabitacion.grid(row=5, column= 1)
    
        #Listar Habitaciones
        self.btnListarHabitaciones = tk.Button(self.frameContenedor, text = "Listar habitaciones", bg = "#4CAF50", fg="white")
        self.btnListarHabitaciones.grid(row = 5 , column= 3)
        

=======
        self.btn_guardar = tk.Button(self.frame_contenedor, text="Guardar Habitación", bg="#4CAF50", fg="white")
        self.btn_guardar.grid(row=4, columnspan=2, pady=15, ipadx=10)


    #BARMENU
>>>>>>> 5da4d2745ce45ec343fa8168bda6d3d1c8f8aec3
