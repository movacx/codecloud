import tkinter as tk
from tkinter import ttk

class HabitacionGUI:
    def __init__(self, ventanaPadre, habitacionesController):
        self.ventanaHija = tk.Toplevel(ventanaPadre)
        self.ventanaHija.title("Mantenimiento de Habitaciones")
        self.ventanaHija.geometry("700x300")
     
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
        self.btnGuardarHabitacion = tk.Button(self.frameContenedor, text="Guardar Habitación", bg="#4CAF50", fg="white", command=lambda: self.manejoController.registrarHabitacion())
        self.btnGuardarHabitacion.grid(row=4, column = 0, pady=15, ipadx=1)
        
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
        



def main():
	root = tk.Tk() #ventana padre = root | como si fuera la ventana del main
	app = HabitacionGUI(root, None )
	root.mainloop()
	


if __name__ == "__main__":
    main()
	
	

