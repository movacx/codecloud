import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu

class HuespedGUI:

    def __init__(self, root, controller):
        self.manejoController = controller
        self.ventanaHuesped = tk.Toplevel(root)
        self.ventanaHuesped.title("Registro de Huespedes")
        self.ventanaHuesped.geometry("1070x600")
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
        
        # arreglo = self.manejoController.cargarDatos()
        # self.cargarDatos(arreglo)
#=========================================[ FIN CONSTRUCTOR ]==============================================#
    def labels(self):
        separador = ' '
        tk.Label(self.contenedor, text="Nombre del Huesped:").grid(row=1, column=0, sticky="e", pady=5)
        tk.Label(self.contenedor, text="Telefono de Contacto:").grid(row=2, column=0, sticky="e", pady=5)
        tk.Label(self.contenedor, text= separador).grid(row=5, column=1)

#=========================================[  ]==============================================#
    def entry(self):
        self.ent_nombre_huesped = tk.Entry(self.contenedor, width=25)
        self.ent_nombre_huesped.grid(row=1, column=1, pady=5, columnspan = 3, sticky = 'ew')

        self.ent_telefono_huesped = tk.Entry(self.contenedor, width=25)
        self.ent_telefono_huesped.grid(row=2, column=1, pady=5, columnspan = 3,sticky = 'ew')

#=========================================[  ]==============================================#
    def buttons(self):
       tk.Button(self.contenedor, text="Registrar Huesped", command = lambda : self.manejoController.agregarHuesped()).grid(row=3, column = 0)
       tk.Button(self.contenedor, text="Buscar Huesped", command = lambda: self.manejoController.buscarHuesped()).grid(row=3, column = 1, sticky = 'ew')
       tk.Button(self.contenedor, text="Limpiar", command = lambda: self.limpiarInputs()).grid(row=3, column = 2, sticky = 'ew')
       tk.Button(self.contenedor, text='Eliminar', command = lambda: self.manejoController.EliminarHuesped()).grid(row = 4, column = 0, sticky = 'nswe', columnspan = 2)
       tk.Button(self.contenedor, text='Mostrar Registros', command = lambda : self.manejoController.cargarHuespedes()).grid(row = 4, column = 2)


#=========================================[  ]==============================================#
    def table(self):
        self.columnas = ['id', 'nombre', 'telefono']
        self.tabla = ttk.Treeview(self.contenedor, columns= self.columnas, show="headings", height = 18)
        

        for items in self.columnas:
            self.tabla.heading(items, text = items.capitalize())
            self.tabla.column(items, width=100)
        self.tabla.grid(row=6, column=0, columnspan=3,sticky='nwse')

#=========================================[  ]==============================================#
    def cargarDatos(self, arreglo):
        for items in arreglo:
            if items:
                id = items[0]
                nombre = items[1]
                telefono = items[2]
                self.tabla.insert('', tk.END, values = (id,nombre,telefono))
                
#=========================================[  ]==============================================#
    def cargarNuevoDato(self, id, nombre, telefono):
        self.tabla.insert('', tk.END, values=(id, nombre, telefono))

#=========================================[  ]==============================================#
    def limpiarTabla(self):
        tabla = self.tabla.get_children()
        for items in tabla:
            self.tabla.delete(items)

#=========================================[  ]==============================================#
    def limpiarInputs(self):
        self.ent_nombre_huesped.delete(0, tk.END)
        self.ent_telefono_huesped.delete(0, tk.END)

#=========================================[  ]==============================================#
    def mostrarMensajes(self, mensaje):
        messagebox.showerror('Dialog', f'{mensaje}', parent = self.ventanaHuesped)
    
    def mostrarMensaje(self, mensaje):
        messagebox.showinfo('Dialog', f'{mensaje}', parent = self.ventanaHuesped)

#=========================================[  ]==============================================#

    def mostrarConfirmacion(self, titulo, comentario):
        respuesta = messagebox.askyesno(f'{titulo}', f'{comentario}',parent = self.ventanaHuesped)
        return respuesta
    
    def mensaje(self, error):
        print(f'{error}')
#=========================================[  ]==============================================#
    #Test y pasos
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

















#Test
# def main():
#     root = tk.Tk()
#     app = HuespedGUI(root, None)
#     root.mainloop()

# if __name__ == '__main__':
#     main()