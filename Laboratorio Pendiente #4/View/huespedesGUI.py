import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class HuespedGUI:

    def __init__(self, root, controller):
        self.manejoController = controller
        self.ventanaHuesped = tk.Toplevel(root)
        self.ventanaHuesped.title("Registro de Huespedes")
        self.ventanaHuesped.geometry("600x500")
        self.ventanaHuesped.columnconfigure(0, weight = 1)
        

        self.contenedor = tk.Frame(self.ventanaHuesped)
        self.contenedor.grid(row=0, column=0, padx=20, pady=20, sticky = 'nswe')
        self.contenedor.columnconfigure(0, weight = 0)
        self.contenedor.columnconfigure(1, weight = 1)
        self.contenedor.columnconfigure(2, weight = 0)
        self.contenedor.rowconfigure(5, weight = 1)
        
        self.labels()
        self.entry()
        self.buttons()
        self.table()
        
#=========================================[ FIN CONSTRUCTOR ]==============================================#
    def labels(self):
        separador = ' '
        tk.Label(self.contenedor, text="Nombre del Huesped:").grid(row=1, column=0, sticky="e", pady=5)
        tk.Label(self.contenedor, text="Telefono de Contacto:").grid(row=2, column=0, sticky="e", pady=5)
        tk.Label(self.contenedor, text= separador).grid(row=4, column=1)

    def entry(self):
        self.ent_nombre_huesped = tk.Entry(self.contenedor, width=25)
        self.ent_nombre_huesped.grid(row=1, column=1, pady=5, columnspan = 3, sticky = 'ew')

        self.ent_telefono_huesped = tk.Entry(self.contenedor, width=25)
        self.ent_telefono_huesped.grid(row=2, column=1, pady=5, columnspan = 3,sticky = 'ew')

    def buttons(self):
       tk.Button(self.contenedor, text="Registrar Huesped", command = lambda: self.manejoController.agregarHuesped()).grid(row=3, column = 0)
       tk.Button(self.contenedor, text="Buscar Huesped").grid(row=3, column = 1, sticky = 'ew')
       tk.Button(self.contenedor, text="Limpiar").grid(row=3, column = 2, sticky = 'ew')

    def table(self):
        self.columnas = ['id', 'nombre', 'precio']
        self.tabla = ttk.Treeview(self.contenedor, columns= self.columnas, show="headings" )
        

        for items in self.columnas:
            self.tabla.heading(items, text = items.capitalize())
            self.tabla.column(items, width=100)
        self.tabla.grid(row=5, column=0, columnspan=3,sticky='nwse')

#=================================================================================================================#

    def mostrarMensajes(self, mensaje):
        messagebox.showinfo('Dialog', f'{mensaje}')
    
    def cargarDatos(self, id, nombre, telefono):
        self.tabla.insert('', tk.END, values=(id, nombre, telefono))


# def main():
#     root = tk.Tk()
#     app = HuespedGUI(root, None)
#     root.mainloop()

# if __name__ == '__main__':
#     main()