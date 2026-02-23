import tkinter as tk
from tkinter import messagebox

sans12 = ("Open Sans Extrabold", 12)

class VentanaLogin:
    def __init__(self, root, controller):
        self.manejoController = controller
        self.ventana = root 
        self.ventana.title('Login Intelek')
        self.ventana.geometry('1080x720')
        self.ventana.configure(bg="#0D5577")
        
        self.contenedor = tk.Frame(self.ventana, padx=20, pady=20, bg="#FFFFFF")
        self.contenedor.place(anchor='center', relx=0.5, rely=0.5)

        tk.Label(self.contenedor, text='INTELEK', font=sans12, bg='white').pack()
        self.txtCorreo = tk.Entry(self.contenedor, width=40)
        self.txtCorreo.pack(pady=5)
        self.txtClave = tk.Entry(self.contenedor, width=40, show="*")
        self.txtClave.pack(pady=5)

        tk.Button(self.contenedor, text='Ingresar', command=lambda: self.manejoController.ejecutarLogin()).pack(pady=5)
        tk.Button(self.contenedor, text='Crear Cuenta', command=lambda: self.manejoController.abrirRegistro()).pack()

    def mostrarError(self, mensaje):
        messagebox.showerror('Error', mensaje, parent=self.ventana)