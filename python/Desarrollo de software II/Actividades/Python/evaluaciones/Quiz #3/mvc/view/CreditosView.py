import tkinter as tk
from tkinter import ttk, messagebox
font = 'Arial, 12'
class CreditosGUI:
    def __init__(self, root, controller):
        self.ventana = tk.Toplevel(root)
        self.manejoController = controller

        self.ventana.geometry('800x800')
        self.ventana.title('Creditos Banco')

        self.labels()
        self.entry()
        self.table()
        self.botones()
        
#---------------------------------------------------------------------------------------------------------------------------
    def botones(self):
        self.btnSolicitar = tk.Button(self.ventana, text = 'Solicitar Credito', command = lambda: self.manejoController.solicitarEstado())
        self.btnSolicitar.grid(row = 8, column = 0, sticky = 'w')
        
        self.btnPagar = tk.Button(self.ventana, text = 'Pagar Credito', command = lambda: self.manejoController.pagarEstado())
        self.btnPagar.grid(row = 8, column = 0, sticky = 'e')
        
        self.btnConsultar = tk.Button(self.ventana, text = 'Consultar Estado', command=lambda: self.manejoController.consultarEstado())
        self.btnConsultar.grid(row = 8, column = 1, sticky = 'w')
        
        self.btnAceptar = tk.Button(self.ventana, text = 'Aceptar', command = lambda: self.manejoController.recibirAccion())
        self.btnAceptar.grid(row = 8, column = 1, sticky = 'ns')
        self.btnAceptar.config(state = tk.DISABLED)
        
        self.btnCancelar = tk.Button(self.ventana, text = 'Cancelar', command = lambda: self.manejoController.botonLimpiarCancelar())
        self.btnCancelar.grid(row = 8, column = 1, sticky = 'e')
        self.btnCancelar.config(state = tk.DISABLED)
    
    def separador(self, fila, columna):
        tk.Label(self.ventana, text = '', font = font).grid(row = fila, column = columna)
   
    def entry(self):
        columnas = [12,24,48,96]
        self.txtCantidadCuotas = ttk.Combobox(self.ventana, values= (columnas))
        self.txtCantidadCuotas.grid(row = 4, column = 1)
        
        self.txtDni = tk.Entry(self.ventana)
        self.txtDni.grid(row = 0, column = 1)
        
        self.txtMontoCredito = tk.Entry(self.ventana)
        self.txtMontoCredito.grid(row = 2, column = 1)
        
        self.txtMontoPagar = tk.Entry(self.ventana)
        self.txtMontoPagar.grid(row = 6, column = 1)
        
        
    def labels(self):
        tk.Label(self.ventana, text = 'Dni:', font = font).grid(row = 0, column = 0, sticky = 'w')
        self.separador(1,0)
        
        tk.Label(self.ventana, text = 'Monto de Credito:', font = font).grid(row = 2, column = 0, sticky = 'w')
        self.separador(3,0)
        
        tk.Label(self.ventana, text = 'Cantidad de Cuotas:', font = font).grid(row = 4, column = 0, sticky = 'w')
        self.separador(5,0)
        
        tk.Label(self.ventana, text = 'Monto de la Cuota a Pagar:', font = font).grid(row = 6, column = 0, sticky = 'w')
        self.separador(7,0)
        
    def table(self):
        columnas = ['id', 'dni', 'monto', 'plazo', 'pagadas', 'deuda', 'estado']
        self.tabla = ttk.Treeview(self.ventana, columns = columnas, show = 'headings')
        self.tabla.grid(row = 10, column = 0, columnspan=3)
        for items in columnas:
            self.tabla.heading(items, text = items)
    def cargarTabla(self, arreglo):
        for items in self.tabla.get_children():
            self.tabla.delete(items)
            
        for items in arreglo:
            self.tabla.insert('', tk.END, values = (items[0], items[1], items[2], items[3], items[4], items[5], items[6]))
    
    
    def mostrarMensaje(self, mensaje):
        messagebox.showinfo('Mensaje', f'{mensaje}', parent = self.ventana)
        
    def mostrarError(self, error):
        messagebox.showerror('Banco', f'{error}', parent = self.ventana)
    
    def confirmarAccion(self, mensaje):
        return messagebox.askyesno('Banco', f'mensaje', parent = self.ventana)
    
    def mostrarAdvertencia(self, advertencia):
        messagebox.showwarning('Banco', f'{advertencia}', parent = self.ventana)
        
    
    def bloquearBtn(self):
        self.btnAceptar.config(state = tk.NORMAL)
        self.btnCancelar.config(state = tk.NORMAL)
        self.btnConsultar.config(state = tk.DISABLED)
        self.btnPagar.config(state = tk.DISABLED)
        self.btnSolicitar.config(state = tk.DISABLED)
        
    def desbloquearBtn(self):
        self.btnAceptar.config(state = tk.DISABLED)
        self.btnCancelar.config(state = tk.DISABLED)
        self.btnConsultar.config(state = tk.NORMAL)
        self.btnPagar.config(state = tk.NORMAL)
        self.btnSolicitar.config(state = tk.NORMAL)
        
    def bloquearCampos(self):
        self.txtDni.config(state='disabled')
        self.txtMontoCredito.config(state='disabled')
        self.txtCantidadCuotas.config(state='disabled')
        self.txtMontoPagar.config(state='disabled')
        
    def desbloquearCampos(self):
        self.txtDni.config(state='normal')
        self.txtMontoCredito.config(state='normal')
        self.txtCantidadCuotas.config(state='normal')
        self.txtMontoPagar.config(state='normal')
        
    def limpiarCampos(self):
        self.txtDni.delete(0, 'end')
        self.txtMontoCredito.delete(0, 'end')
        self.txtCantidadCuotas.set('')
        self.txtMontoPagar.delete(0, 'end')

    def prepararSolicitudGUI(self):
        self.desbloquearCampos()
        self.txtMontoPagar.config(state='disabled') 

    def prepararPagoGUI(self):
        self.desbloquearCampos()
        self.txtMontoCredito.config(state='disabled')
        self.txtCantidadCuotas.config(state='disabled')
        
    def prepararConsultaGUI(self):
        self.bloquearCampos()
        self.txtDni.config(state='normal')