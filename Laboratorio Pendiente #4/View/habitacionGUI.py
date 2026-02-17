import tkinter as tk
from tkinter import ttk
from tkinter import Menu


class HabitacionGUI:
    def __init__(self, ventanaPadre, habitacionesController):
        self.ventanaHija = tk.Toplevel(ventanaPadre)
        self.ventanaHija.title("Mantenimiento de Habitaciones")
        self.ventanaHija.geometry("1000x550")
     
        self.manejoController = habitacionesController


        self.frameContenedor = tk.Frame(self.ventanaHija)
        self.frameContenedor.grid(row=0, column=0, padx=20, pady=20)
        
        self.labels()
        self.entry()
        self.button()
        self.table()
#=========================================[ FIN CONSTRUCTOR ]==============================================#
        
    def labels(self):
        tk.Label(self.frameContenedor, text="Numero de Habitación:").grid(row=0, column=0, sticky="e", pady=5)
        tk.Label(self.frameContenedor, text="Tipo de Habitacion:").grid(row=1, column=0, sticky="e", pady=5)
        tk.Label(self.frameContenedor, text="Precio por Noche:").grid(row=2, column=0, sticky="e", pady=5)
        tk.Label(self.frameContenedor, text="Estado de Habitacion:").grid(row=3, column=0, sticky="e", pady=5)
        
    def entry(self):
        self.entradaNumeroHabitacion = tk.Entry(self.frameContenedor)
        self.entradaNumeroHabitacion.grid(row=0, column=1, pady=5)
        self.entradaPrecioHabitacion = tk.Entry(self.frameContenedor)
        self.entradaPrecioHabitacion.grid(row=2, column=1, pady=5)
        #ComboBox
        self.comboboxTipoHabitacion = ttk.Combobox(self.frameContenedor, values=["Sencilla", "Doble", "Suite"], state="readonly")
        self.comboboxTipoHabitacion.grid(row=1, column=1, pady=5)
        self.comboboxEstadoHabitacion = ttk.Combobox(self.frameContenedor, values=["Disponible", "Ocupada"], state="readonly")
        self.comboboxEstadoHabitacion.grid(row=3, column=1, pady=5)
        
    def button(self):
        self.btnGuardarHabitacion = tk.Button(self.frameContenedor, text="Registrar Habitación", command=lambda: self.manejoController.guardarHabitacion())
        self.btnGuardarHabitacion.grid(row=4, column = 0, pady=15, ipadx=1)
        self.btnBuscarHabitacion = tk.Button(self.frameContenedor, text ="Buscar Habitacion", command = lambda: self.manejoController.buscarHabitacion())
        self.btnBuscarHabitacion.grid(row=5, column=0, pady=15, ipadx=1)
        self.btnModificarHabitacion = tk.Button(self.frameContenedor, text ="Modificar Estado", command = lambda: self.manejoController.modificarHabitacion())
        self.btnModificarHabitacion.grid(row=4, column=1, pady=15, ipadx=1)
        self.btnEliminarHabitacion= tk.Button(self.frameContenedor, text= "Eliminar Habitacion", command = lambda: self.manejoController.eliminarHabitacion())
        self.btnEliminarHabitacion.grid(row=5, column= 1)
        self.btnListarHabitaciones = tk.Button(self.frameContenedor, text = "Listar habitaciones", command = lambda: self.manejoController.listarHabitacion())
        self.btnListarHabitaciones.grid(row = 5 , column= 2)
        self.btnListarHabitaciones = tk.Button(self.frameContenedor, text = "Ordenar por precio", command = lambda: self.manejoController.ordenarHabitacionPrecio())
        self.btnListarHabitaciones.grid(row=4, column=2)
        self.btnLimpiarTabla = tk.Button(self.frameContenedor, text = "Limpiar", command = lambda: self.limpiarTabla())
        self.btnLimpiarTabla.grid(row = 10 , column= 5)

    def table(self):
        self.columnas = ["Numero", "Tipo", "Precio", "Estado"]
        self.tabla = ttk.Treeview(self.frameContenedor, columns= self.columnas, show="headings" )
        for items in self.columnas:
            self.tabla.heading(items, text = items.capitalize())
            self.tabla.column(items, width=100)
            self.tabla.grid(row=6, column=4, columnspan=3,sticky='nwse')
            
            
    def actualizarTabla(self, arreglo):
        for item in arreglo:
            self.tabla.insert("",tk.END,value=(item[1], item[2], item[3], item[4]))
            
            print(item)
            
    
    def limpiarTabla(self):
        for items in self.tabla.get_children():
            self.tabla.delete(items)

        self.entradaNumeroHabitacion.delete(0,tk.END)
        self.entradaPrecioHabitacion.delete(0,tk.END)
        

    
    





