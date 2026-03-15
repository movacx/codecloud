import tkinter as tk
from tkinter import ttk, messagebox
font = 'Arial, 12'
class RegistroCuentas:
    def __init__(self, root, controller):
        self.manejoController = controller
        self.ventana = tk.Toplevel(root)
        self.ventana.geometry('1270x720')
        self.ventana.title('Registro')
        
        self.labels()
        self.entry()
        self.buttons()
        self.mostrarTabla()
        
        self.ventana.columnconfigure(0, weight = 0)
        self.ventana.columnconfigure(1, weight = 1)
        self.ventana.columnconfigure(2, weight = 0)
        
        self.ventana.rowconfigure(11, weight = 1)
       
        
    
    def separador(self, fila, columna):
        tk.Label(self.ventana, text = '', font = font).grid(row = fila, column = columna)
    
    def labels(self):
        tk.Label(self.ventana, text = 'Dni:', font = font).grid(row = 0, column = 0, sticky = 'w')
        self.separador(1,0)
        tk.Label(self.ventana, text = 'Nombre:', font = font).grid(row = 2, column = 0, sticky = 'w')
        self.separador(3,0)
        tk.Label(self.ventana, text = 'Apellido:', font = font).grid(row = 4, column = 0, sticky = 'w')
        self.separador(5,0)
        tk.Label(self.ventana, text = 'Email:', font = font).grid(row = 6, column = 0, sticky = 'w')
        self.separador(7,0)
        
    def entry(self):
        self.dniTxt = tk.Entry(self.ventana)
        self.dniTxt.grid(row = 0, column = 1, sticky = 'nswe', padx = (10,10))
        
        self.nombreTxt = tk.Entry(self.ventana)
        self.nombreTxt.grid(row = 2, column = 1, sticky = 'nswe', padx = (10,10))
        
        self.apellidoTxt = tk.Entry(self.ventana)
        self.apellidoTxt.grid(row = 4, column = 1, sticky = 'nswe', padx = (10,10))
        
        self.emailTxt = tk.Entry(self.ventana)
        self.emailTxt.grid(row = 6, column = 1, sticky = 'nswe', padx = (10,10))
        
    def buttons(self):
        tk.Button(self.ventana, text = 'Guardar', command = lambda: self.manejoController.agregarCuenta()).grid(row = 8, column = 0, sticky = 'nswe')
        tk.Button(self.ventana, text = 'Modiciar', command = lambda: self.manejoController.modificarCliente()).grid(row = 8, column = 1, sticky = 'nswe')
        tk.Button(self.ventana, text = 'Eliminar', command = lambda: self.manejoController.eliminarCliente()).grid(row = 8, column = 2, sticky = 'nswe')
        tk.Button(self.ventana, text = 'Buscar', command = lambda: self.manejoController.buscarCliente()).grid(row = 9, column = 0, sticky = 'nswe')
        tk.Button(self.ventana, text = 'mostrar Registros', command = lambda : self.manejoController.mostrarRegistros()).grid(row = 9, column = 1, sticky = 'nswe')
        tk.Button(self.ventana, text = 'Limpiar', command = lambda: self.manejoController.limpiarTodo()).grid(row = 9, column = 2, sticky = 'nswe')
        self.separador(10,0)
        
    def mostrarTabla(self):
        columnas = ['Dni', 'Nombre', 'Apellido', 'Email']
        self.tabla = ttk.Treeview(self.ventana, columns = columnas, show = 'headings')
        self.tabla.grid(row = 11, column = 0, sticky = 'nswe', columnspan = 3, padx = (10,10), pady = 10)
        for items in columnas:
            self.tabla.heading(items, text = items)
            
    def cargarTabla(self, arreglo):
        for items in arreglo:
            self.tabla.insert('', tk.END, values = (items[0],items[1], items[2], items[3]))
            
    def actualizarTabla(self, dni, nombre, apellido, email):
        self.tabla.insert('', tk.END, value = (dni, nombre, apellido, email))
            
    def limpiarTabla(self):
        for items in self.tabla.get_children():
            self.tabla.delete(items)
        
    def limpiarCampos(self):
        self.dniTxt.delete(0, tk.END)
        self.nombreTxt.delete(0, tk.END)
        self.apellidoTxt.delete(0, tk.END)
        self.emailTxt.delete(0, tk.END)
        
    def bloquearPrimerCampo(self):
        self.dniTxt.config(state = 'disable')
        
    def desbloquearPrimerCampo(self):
        self.dniTxt.config(state = 'normal')
        
        
    def bloquearCampos(self):
        self.dniTxt.config(state = 'disable')
        self.nombreTxt.config(state = 'disable')
        self.apellidoTxt.config(state = 'disable')
        self.emailTxt.config(state = 'disable')

    def desbloquearCampos(self):
        self.dniTxt.config(state = 'normal')
        self.nombreTxt.config(state = 'normal')
        self.apellidoTxt.config(state = 'normal')
        self.emailTxt.config(state = 'normal')
        
    def dialogoError(self, error):
        messagebox.showerror('Error', f'Hubo un error, no se pudo cargar. \nPara mas informacion valide la terminal o el log file', parent = self.ventana)
        print(f'Hubo un error validar el log file para mas informacion: {error}')
    
    def mostrarMensaje(self, mensaje):
        messagebox.showinfo('Dialogo', f'{mensaje}', parent = self.ventana)
        
    def mostrarAdvertencia(self, mensaje):
        messagebox.showwarning('Advertencia', f'{mensaje}', parent = self.ventana)
    
    def confirmarAccion(self):
        return messagebox.askyesno('Confirmacion', '¿Deseas continuar?', parent = self.ventana)
    
            
def main():
    root = tk.Tk()
    app = RegistroCuentas(root, None )
    root.mainloop()
    
if __name__ == '__main__':
    main()
    
    
    
