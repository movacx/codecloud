import tkinter as tk
from tkinter import ttk, messagebox

class ReporteeGUI:
    def __init__(self, root, controller):
        self.manejoController = controller
        self.ventanaReportes = tk.Toplevel(root)
        self.ventanaReportes.title("Reportes")
        self.ventanaReportes.geometry('300x300')
        
        self.lbl_info = tk.Label(self.ventanaReportes, text='Seleccione una opcion: ')
        self.lbl_info.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        filas = ['Habitaciones', 'Huespedes', 'Reservas']
        self.opcionSeleccionada = ttk.Combobox(self.ventanaReportes, values=filas, state='readonly', width=20)
        self.opcionSeleccionada.grid(row=0, column=1, pady=10, sticky="w")
        self.opcionSeleccionada.current(0)

        self.btn_enviar = tk.Button(self.ventanaReportes, text='Enviar', 
                                   command=lambda: self.manejoController.cargarTabla())
        self.btn_enviar.grid(row=0, column=2, padx=5)

    def tablas(self, opcion):


        if opcion == 1:
            self.huespedes()
        elif opcion == 2:
            self.habitaciones()
        elif opcion == 3:
            self.reservas()

    def huespedes(self):
        columnas = ['Id', 'Nombre', 'telefono']
        self.tablaHuespedes = ttk.Treeview(self.ventanaReportes, column=columnas, show='headings', height=15)
        self.tablaHuespedes.grid(row=2, column=1, columnspan=3, padx=10, pady=20, sticky="nw")
        for items in columnas:
            self.tablaHuespedes.heading(items, text=items)
            self.tablaHuespedes.column(items, width=100)

    def habitaciones(self):
        columnas = ['Id', 'Numero', 'Tipo', 'Precio', 'Estado']
        self.tablaHabitaciones = ttk.Treeview(self.ventanaReportes, column=columnas, show='headings', height=15)
        self.tablaHabitaciones.grid(row=2, column=1, columnspan=3, padx=10, pady=20, sticky="nw")
        for items in columnas:
            self.tablaHabitaciones.heading(items, text=items)
            self.tablaHabitaciones.column(items, width=100)

    def reservas(self):
        columnas = ['Id', 'Numero Habitacion', 'IdHuesped', 'Entrada', 'Salida']
        self.tablaReservas = ttk.Treeview(self.ventanaReportes, column=columnas, show='headings', height=15)
        self.tablaReservas.grid(row=2, column=1, columnspan=3, padx=10, pady=20, sticky="nw")
        for items in columnas:
            self.tablaReservas.heading(items, text=items)
            self.tablaReservas.column(items, width=100)

    def cargarHuespedes(self, arreglo):
        for items in arreglo:
            self.tablaHuespedes.insert('', tk.END, values=(items[0], items[1], items[2]))

    def cargarHabitaciones(self, arreglo):
        for items in arreglo:
            self.tablaHabitaciones.insert('', tk.END, values=(items[0], items[1], items[2], items[3], items[4]))
    
    def cargarReservas(self, arreglo):
        for items in arreglo:
            self.tablaReservas.insert('', tk.END, values=(items[0], items[1], items[2], items[3], items[4]))

    def errorMessage(self, mensaje):
        messagebox.showerror('Error!', f'{mensaje}', parent=self.ventanaReportes)