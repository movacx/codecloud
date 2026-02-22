import tkinter as tk
from tkinter import messagebox
from VentanaRegistro import VentanaRegistro
from MenuPrincipal import MenuPrincipal

sans12 = ("Open Sans Extrabold", 12)
sans9 = ("Open Sans Extrabold", 9)

class VentanaLogin:
    def __init__(self, root):
        self.root = root
        self.controlador = AuthController()
        self.root.title('Login Intelek')
        self.root.geometry('1080x720')
        self.root.configure(bg="#0D5577")
        self.contenedor = tk.Frame(self.root, padx=20, pady=20, bg="#FFFFFF")
        self.contenedor.place(anchor='center', relx=0.5, rely=0.5)

        tk.Label(self.contenedor, text='INTELEK', font=sans12, bg='white').pack()
        self.txtCorreo = tk.Entry(self.contenedor, width=40)
        self.txtCorreo.pack(pady=5)
        self.txtClave = tk.Entry(self.contenedor, width=40, show="*")
        self.txtClave.pack(pady=5)

        tk.Button(self.contenedor, text='Ingresar', command=self.ejecutarLogin).pack(pady=5)
        tk.Button(self.contenedor, text='Crear Cuenta', command=self.abrirRegistro).pack()
        self.lblMensaje = tk.Label(self.contenedor, text='', fg='red', bg='white')
        self.lblMensaje.pack()

    def ejecutarLogin(self):
        exito, rol, idUsr = self.controlador.procesarLogin(self.txtCorreo.get(), self.txtClave.get())
        if exito:
            self.root.withdraw()
            MenuPrincipal(tk.Toplevel(self.root), rol, idUsr, self.root)
        else:
            self.lblMensaje.config(text="Credenciales invalidas")

    def abrirRegistro(self):
        VentanaRegistro(self.root, self.controlador)

