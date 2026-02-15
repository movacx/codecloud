import tkinter as tk
from tkinter import ttk
from tkinter import Menu


class HabitacionGUI:
    def __init__(self, ventanaPadre, habitacionesController):
        self.ventanaHija = tk.Toplevel(ventanaPadre)
        self.ventanaHija.title("Mantenimiento de Habitaciones")
        self.ventanaHija.geometry("700x300")
     
        self.manejoController = habitacionesController


        self.frameContenedor = tk.Frame(self.ventanaHija)
        self.frameContenedor.grid(row=0, column=0, padx=20, pady=20)
        
        self.formularioCrear()
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
        self.btnGuardarHabitacion = tk.Button(self.frameContenedor, text="Guardar Habitación", bg="#4CAF50", fg="white", command=lambda: self.manejoController.registrarHabitacion())
        self.btnGuardarHabitacion.grid(row=4, column = 0, pady=15, ipadx=1)
        self.btnBuscarHabitacion = tk.Button(self.frameContenedor, text ="Buscar Habitacion", bg = "#4CAF50", fg="white")
        self.btnBuscarHabitacion.grid(row=5, column=0, pady=15, ipadx=1)
        self.btnModificarHabitacion = tk.Button(self.frameContenedor, text ="Modificar Habitacion", bg= "#4CAF50", fg="white")
        self.btnModificarHabitacion.grid(row=4, column=1, pady=15, ipadx=1)
        self.btnEliminarHabitacion= tk.Button(self.frameContenedor, text= "Eliminar Habitacion", bg=  "#4CAF50", fg="white")
        self.btnEliminarHabitacion.grid(row=5, column= 1)
        self.btnListarHabitaciones = tk.Button(self.frameContenedor, text = "Listar habitaciones", bg = "#4CAF50", fg="white")
        self.btnListarHabitaciones.grid(row = 5 , column= 3)
        
        
    def table(self):
	self.columnas = ["ID, Numero, Tipo, Precio, Estado"]
	self.tabla ==tk.TreeView(self.contenedor, columns = self.columns, show="headings" )
	
	
	
	
	
	
	
	
	
    def menuBar(self):
	self.barra = tk.Menu(self.ventanaHabitacion)
	
        
        #Paso 1 se asigna la barra a que frame o ventana ira.
        self.barra = tk.Menu(self.ventanaHuesped)
        #Paso 2 se asignan los items desplegables a la barra.
        self.file = tk.Menu(self.barra, tearoff = 0)
        #Paso 3 se asignan los botones por decirlo de cierta manera..
        self.file.add_command(label = 'Reporte1')
        self.file.add_command(label = 'Reporte2')
        self.file.add_command(label = 'Reporte3')
        self.file.add_separator()
        #Paso 4 Ahora se añade (add_cascade) a la barra
        self.barra.add_cascade(label = 'Archivo', menu = self.file)
        #PPaso 5: Decirle a la ventana que use esta barra
        self.ventanaHuesped.config(menu = self.barra)


        
        



def main():
    root = tk.Tk() #ventana padre = root | como si fuera la ventana del main
    app = HabitacionGUI(root, None )
    root.mainloop()
    


if __name__ == "__main__":
    main()
    
    



