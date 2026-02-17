import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class HuespedGUI:

    def __init__(self, root, controller):
        self.manejoController = controller
        self.ventanaHuesped = tk.Toplevel(root)
        self.ventanaHuesped.title("Registro de Huespedes")
        self.ventanaHuesped.geometry("900x500")
        
        self.contenedor = tk.Frame(self.ventanaHuesped)
        self.contenedor.grid(row=0, column=0, padx=20, pady=20)
        
        self.labels()
        self.entry()
        self.buttons()
        self.table()

    def labels(self):
        tk.Label(self.contenedor, text="Nombre del Huesped:").grid(row=0, column=0, sticky="e", pady=5)
        tk.Label(self.contenedor, text="Telefono de Contacto:").grid(row=1, column=0, sticky="e", pady=5)

    def entry(self):
        self.entradaNombreHuesped = tk.Entry(self.contenedor, width=20)
        self.entradaNombreHuesped.grid(row=0, column=1, sticky="w")

        self.entradaTelefonoHuesped = tk.Entry(self.contenedor, width=40)
        self.entradaTelefonoHuesped.grid(row=1, column=1, sticky="w")

    def buttons(self):
        tk.Button(self.contenedor, text="Registrar Huesped", 
                  command=lambda: self.manejoController.agregarHuesped()).grid(row=2, column=0, pady=10)
        
        tk.Button(self.contenedor, text="Buscar Huesped", 
                  command=lambda: self.manejoController.buscarHuesped()).grid(row=2, column=1, sticky="w")
        
        tk.Button(self.contenedor, text="Eliminar", 
                  command=lambda: self.manejoController.EliminarHuesped()).grid(row=3, column=0)
        
        tk.Button(self.contenedor, text="Mostrar Registros", 
                  command=lambda: self.manejoController.cargarHuespedes()).grid(row=3, column=1, sticky="w")
        tk.Button(self.contenedor, text="Limpiar", 
                  command=lambda: self.limpiarTabla()).grid(row=5, column=3, sticky="e")

    def table(self):
        self.columnas = ['id', 'nombre', 'telefono']
        self.tabla = ttk.Treeview(self.contenedor, columns=self.columnas, show="headings", height=10)
        for items in self.columnas:
            self.tabla.heading(items, text=items)
            self.tabla.column(items, width=120)
            
        self.tabla.grid(row=4, column=3, columnspan=2, pady=20)

    def cargarDatos(self, arreglo):
        for items in arreglo:
            if items:
                self.tabla.insert('', tk.END, values=(items[0], items[1], items[2]))
                
    def cargarNuevoDato(self, id, nombre, telefono):
        self.tabla.insert('', tk.END, values=(id, nombre, telefono))

    def limpiarTabla(self):
        for items in self.tabla.get_children():
            self.tabla.delete(items)

        self.entradaNombreHuesped.delete(0,tk.END)
        self.entradaTelefonoHuesped.delete(0,tk.END)

    def mostrarMensajes(self, mensaje):
        messagebox.showerror('Dialog', f'{mensaje}', parent=self.ventanaHuesped)
    
    def mostrarMensaje(self, mensaje):
        messagebox.showinfo('Dialog', f'{mensaje}', parent=self.ventanaHuesped)

    def mostrarConfirmacion(self, titulo, comentario):
        return messagebox.askyesno(f'{titulo}', f'{comentario}', parent=self.ventanaHuesped)
