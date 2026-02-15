import tkinter as tk
from tkinter import ttk, messagebox

#Variables GLobales
separador = ' '

class ReporteeGUI:
    def __init__(self, root, controller):
        #Controller
        self.manejoController = controller
        #Construir la ventana
        self.ventanaReportes = tk.Toplevel(root)
        self.ventanaReportes.geometry('1270x600')
        #Configurar Columnas
        self.ventanaReportes.columnconfigure(1, weight = 1)
        # opcion = self.manejoController.cargarTabla()
        self.etiquetas()
        self.comboBox()
        self.buttons()
        

    def etiquetas(self):
        tk.Label(self.ventanaReportes, text = 'Seleccione una opcion: ').grid(row = 0, column = 0)
        #Separador
        tk.Label(self.ventanaReportes, text = separador).grid(row = 1, column = 0)

    def comboBox(self):
        filas = ['Habitaciones','Huespedes','Reservas']
        self.opcionSeleccionada = ttk.Combobox(self.ventanaReportes, values = (filas), state = 'readonly')
        self.opcionSeleccionada.grid(row = 0, column = 1, sticky = 'nswe')
        self.opcionSeleccionada.current(0)

    def buttons(self):
        tk.Button(self.ventanaReportes, text = 'Enviar', command = lambda: self.manejoController.cargarTabla()).grid(row = 0, column = 3)
       
    #=============================================================================================================================================#

    def tablas(self, opcion):
        if hasattr(self, 'tablaHuespedes'):
            self.tablaHuespedes.destroy()
        if hasattr(self, 'tablaHabitaciones'):
            self.tablaHabitaciones.destroy()
        if hasattr(self, 'tablaReservas'):
            self.tablaReservas.destroy()

        if opcion == 1:
            self.huespedes()
            return
        
        elif opcion == 2:
            self.habitaciones()
            return
        
        elif opcion == 3:
            self.reservas()
            return
        

    #=============================================================================================================================================#

    #Tablas
    def huespedes(self):
        columnas = ['Id','Nombre','telefono']
        self.tablaHuespedes = ttk.Treeview(self.ventanaReportes, column = columnas, show = 'headings', height = 20)
        self.tablaHuespedes.grid(row = 2, column = 1, sticky = 'nswe')

        for items in columnas:
            self.tablaHuespedes.heading(items, text = items) #heading=titulo(posicionColumna, text = nombredecolumna)

    def habitaciones(self):
        columnas = ['Id','Numero','Tipo','Precio','Estado']
        self.tablaHabitaciones = ttk.Treeview(self.ventanaReportes, column = columnas, show = 'headings', height = 20)
        self.tablaHabitaciones.grid(row = 2, column = 1, sticky = 'nswe')

        for items in columnas:
            self.tablaHabitaciones.heading(items, text = items)

    def reservas(self):
        columnas = ['Id','Numero Habitacion','IdHuesped','Entrada','Salida']

        self.tablaReservas =ttk.Treeview(self.ventanaReportes, column = columnas, show = 'headings',height = 30)
        self.tablaReservas.grid(row = 2, column = 1, sticky = 'nswe')

        for items in columnas:
            self.tablaReservas.heading(items, text = items)

    #=============================================================================================================================================#

    #Cargar las tablas
    def cargarHuespedes(self, arreglo):
        for items in arreglo:
            self.tablaHuespedes.insert('', tk.END, values = (items[0], items[1], items[2]))

    def cargarHabitaciones(self, arreglo):
        for items in arreglo:
            self.tablaHabitaciones.insert('', tk.END, values = (items[0], items[1], items[2], items[3], items[4]))
    
    def cargarReservas(self, arreglo):
        for items in arreglo:
            self.tablaReservas.insert('', tk.END, values = (items[0], items[1], items[2], items[3], items[4]))

    #=============================================================================================================================================#

    #Dialogos de errores

    def errorMessage(self, mensaje):
        messagebox.showerror('Error!', f'{mensaje}', parent = self.ventanaReportes)
        print(f'Hubo un error! {mensaje}')

# def main():
#     root = tk.Tk()
#     app = ReporteeGUI(root, None)
#     root.mainloop()

# if __name__ == '__main__':
#     main()