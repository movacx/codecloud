import tkinter as tk
from tkinter import ttk, messagebox
class calculadoraView:
    def __init__(self, root, controller):
        self.manejoController = controller
        self.ventana = tk.Toplevel(root)
        self.ventana.geometry('600x600')
        self.ventana.title('Calculadora')
        self.labels()
        self.entry()
        self.radioButon()
        self.botones()

    def labels(self):
        tk.Label(self.ventana, text = 'Numero 1:').grid(row = 0, column = 0, sticky = 'w')
        tk.Label(self.ventana, text = 'Numero 2:').grid(row = 1, column = 0, sticky = 'w')
        tk.Label(self.ventana, text = 'Resultado: ').grid(row = 4, column = 0, sticky = 'w')

    def entry(self):
        self.numeroUno = tk.Entry(self.ventana)
        self.numeroUno.grid(row = 0, column = 1,  sticky = 'w')

        self.numeroDos = tk.Entry(self.ventana)
        self.numeroDos.grid(row = 1, column = 1,  sticky = 'w')

        self.resultado = tk.Entry(self.ventana)
        self.resultado.grid(row = 4, column = 1,  sticky = 'w')
        self.resultado.config(state = tk.DISABLED)

    def radioButon(self):
        self.operacion = tk.StringVar()
        ttk.Radiobutton(self.ventana, text='+', value='+', variable=self.operacion).grid(row=2, column=0)
        ttk.Radiobutton(self.ventana, text='-', value='-', variable=self.operacion).grid(row=2, column=1, sticky = 'w')
        ttk.Radiobutton(self.ventana, text='*', value='*', variable=self.operacion).grid(row=2, column=1, sticky = 'n')
        ttk.Radiobutton(self.ventana, text='/', value='/', variable=self.operacion).grid(row=2, column=1, sticky = 'e')

    def botones(self):
        tk.Button(self.ventana, text = 'Calcular', command = lambda: self.manejoController.calcular()).grid(row = 3, column = 0, sticky = 'w')
        tk.Button(self.ventana, text = 'Historial', command = lambda: self.manejoController.abrirHistorial()).grid(row = 3, column = 1, sticky = 'w')
        tk.Button(self.ventana, text = 'Limpiar', command = lambda: self.limpiar()).grid(row = 3, column = 1, sticky = 'e')

    def mostrarMensajes(self, mensaje):
        messagebox.showinfo('', mensaje)

    def mostrarAdvertencia(self, mensaje):
        messagebox.showwarning('', mensaje)

    def mostrarError(self, mensaje):
        messagebox.showerror('', mensaje)


    def actualizarResultado(self, resultado):
        self.resultado.config(state = tk.NORMAL)
        self.resultado.delete(0, tk.END)
        self.resultado.insert(0, str(resultado))
        self.resultado.config(state = tk.DISABLED)

    def limpiar(self):
        self.numeroUno.delete(0, tk.END)
        self.numeroDos.delete(0, tk.END)
        self.resultado.delete(0, tk.END)