import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu

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
        self.menuBar()
        
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
        self.columnas = ['id', 'nombre', 'telefono']
        self.tabla = ttk.Treeview(self.contenedor, columns= self.columnas, show="headings" )
        

        for items in self.columnas:
            self.tabla.heading(items, text = items.capitalize())
            self.tabla.column(items, width=100)
        self.tabla.grid(row=5, column=0, columnspan=3,sticky='nwse')


    def cargarDatos(self, id, nombre, telefono):
        self.tabla.insert('', tk.END, values=(id, nombre, telefono))


#=================================================================================================================#

    def mostrarMensajes(self, mensaje):
        messagebox.showinfo('Dialog', f'{mensaje}')
    

    
    def menuBar(self):
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


# def main():
#     root = tk.Tk()
#     app = HuespedGUI(root, None)
#     root.mainloop()

# if __name__ == '__main__':
#     main()