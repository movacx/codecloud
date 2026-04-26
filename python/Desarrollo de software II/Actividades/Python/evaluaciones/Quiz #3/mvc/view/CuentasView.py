import tkinter as tk
from tkinter import ttk, messagebox
font = 'Arial, 12'
class ManejoCuentas:
    def __init__(self, root, controller):
        self.manejoController = controller
        self.ventana = tk.Toplevel(root)
        self.ventana.geometry('1000x520')
        self.ventana.title('Manejo Cuentas')
        self.labels()
        self.entry()
        self.Insertartabla()
        self.buttons()
        
        self.ventana.columnconfigure(0, weight = 0)
        self.ventana.columnconfigure(1, weight = 0)
        self.ventana.columnconfigure(2, weight = 0)
        self.ventana.columnconfigure(3, weight = 0)
        self.ventana.columnconfigure(4, weight = 1)
        #self.ventana.columnconfigure(5, weight = 0)
        
        self.ventana.rowconfigure(0, weight = 1)
        self.ventana.rowconfigure(1, weight = 1)
        self.ventana.rowconfigure(2, weight = 1)
        self.ventana.rowconfigure(3, weight = 1)
        self.ventana.rowconfigure(4, weight = 1)
        #self.ventana.rowconfigure(5, weight = 1)
        
        #self, numero_cuenta, dni_cliente, saldo)
        
    def labels(self):
        tk.Label(self.ventana, text = 'Ingrese Dni:' ,font = font).grid(row = 0 ,column = 0, sticky = 'nsw', padx = 5)
        tk.Label(self.ventana, text = 'n°Cuenta:' ,font = font).grid(row = 1 ,column = 0, sticky = 'nsw', padx = 5)
        tk.Label(self.ventana, text = 'Monto' ,font = font).grid(row = 2 ,column = 0, sticky = 'nsw', padx = 5)        
        #tk.Label(self.ventana, text = 'Retirar:' ,font = font).grid(row = 3 ,column = 0, sticky = 'nsw', padx = 5)
        
        pass
    
    def entry(self):
        self.dnitxt = tk.Entry(self.ventana)
        self.dnitxt.grid(row = 0, column = 1, sticky='we', ipady = 15)
        
        self.nCuentatxt = tk.Entry(self.ventana)
        self.nCuentatxt.grid(row = 1, column = 1, sticky='we', ipady = 15)
        
        self.montoTxt = tk.Entry(self.ventana)
        self.montoTxt.grid(row = 2, column = 1, sticky='we', ipady = 15)
        #self.montoRetiro = tk.Entry(self.ventana).grid(row = 3, column = 1, sticky='we', ipady = 15)
        self.bloquearCampos()
        
    
    def Insertartabla(self):
        columnas = ['Dni','n°Cuenta','Saldo']
        self.tabla = ttk.Treeview(self.ventana, columns = columnas, show = 'headings')
        self.tabla.grid(row = 0, column = 4, sticky='nswe', rowspan=5, padx = (30,30), pady = (30,30))
        for items in columnas:
            self.tabla.heading(items, text = items)
        
    
    def buttons(self):
        self.btnApertura = tk.Button(self.ventana, text='Apertura', command=lambda: self.manejoController.aperturaDeCuenta())
        self.btnApertura.grid(row=0, column=5, sticky='nswe')

        self.btnConsultar = tk.Button(self.ventana, text='Consultar', command = lambda: self.manejoController.consultarCuenta()) 
        self.btnConsultar.grid(row=1, column=5, sticky='nswe')

        self.btnDepositar = tk.Button(self.ventana, text='Depositar', command = lambda: self.manejoController.depositoDeCuenta()) 
        self.btnDepositar.grid(row=2, column=5, sticky='nswe')

        self.btnRetirar = tk.Button(self.ventana, text='Retirar', command = lambda: self.manejoController.retiroDeCuenta()) 
        self.btnRetirar.grid(row=3, column=5, sticky='nswe', rowspan=2)

        self.botonAceptar = tk.Button(self.ventana, text='Aceptar', command=lambda: self.manejoController.recibirAceptar())
        self.botonAceptar.grid(row=4, column=0, sticky='we', columnspan=2, padx=30)
        
        
    def cargarTabla(self, arreglo):
        for items in self.tabla.get_children():
            self.tabla.delete(items)
            
        for items in arreglo:
            self.tabla.insert('', tk.END, values = (items[0], items[1], items[2]))
        

    def mostrarMensaje(self, mensaje):
        messagebox.showinfo('Mensaje', f'{mensaje}', parent = self.ventana)
        
    def mostrarError(self, error):
        messagebox.showerror('Banco', f'{error}', parent = self.ventana)
    
    def confirmarAccion(self, mensaje):
        return messagebox.askyesno('Banco', f'mensaje', parent = self.ventana)
    
    def mostrarAdvertencia(self, advertencia):
        messagebox.showwarning('Banco', f'{advertencia}', parent = self.ventana)
        
    def bloquearCampos(self):
        self.dnitxt.config(state='disabled')
        self.nCuentatxt.config(state='disabled')
        self.montoTxt.config(state='disabled')
        
    def desbloquearCampos(self):
        self.dnitxt.config(state = 'normal')
        self.nCuentatxt.config(state = 'normal')
        self.montoTxt.config(state = 'normal')
        
    def bloquearBtn(self):
        self.btnApertura.config(state='disabled')
        self.btnConsultar.config(state='disabled')
        self.btnDepositar.config(state='disabled')
        self.btnRetirar.config(state='disabled')

    def desbloquearBtn(self):
        self.btnApertura.config(state='normal')
        self.btnConsultar.config(state='normal')
        self.btnDepositar.config(state='normal')
        self.btnRetirar.config(state='normal')
        
    def bloquearNCUENTA(self):
        self.nCuentatxt.config(state='disabled')
        
    def bloquearDNI(self):
        self.dnitxt.config(state='disabled')

    def desbloquearDNI(self):
        self.dnitxt.config(state='normal')
        
    def limpiarCampos(self):
        self.dnitxt.delete(0, 'end')
        self.nCuentatxt.delete(0, 'end')
        self.montoTxt.delete(0, 'end')
