import tkinter as tk
from tkinter import messagebox

sans12 = ("Open Sans Extrabold", 12)

class VentanaRegistro:
    def __init__(self, root, controller):
        self.manejoController = controller
        self.ventana = tk.Toplevel(root)
        self.ventana.title("Registro")
        self.ventana.geometry("300x300")
        
        tk.Label(self.ventana, text="Nombre Completo:").pack(pady=(10, 0))
        self.txtNombre = tk.Entry(self.ventana)
        self.txtNombre.pack(pady=5)
        #-----------------------------------------------------------------------------------------------------
        tk.Label(self.ventana, text="Correo Electronico:").pack()
        self.txtCorreo = tk.Entry(self.ventana)
        self.txtCorreo.pack(pady=5)
        #----------------------------------------------------------------------------------------------------
        tk.Label(self.ventana, text="Contrasena:").pack()
        self.txtClave = tk.Entry(self.ventana, show="*")
        self.txtClave.pack(pady=5)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #Button 
        tk.Button(self.ventana, text="Guardar", command=lambda: self.manejoController.registrar()).pack(pady=10)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Mostrar mensaje 
    def mostrarMensaje(self, mensaje):
        messagebox.showinfo('Intelek', mensaje, parent=self.ventana)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #Mostrar Error 
    def mostrarError(self, mensaje):
        messagebox.showerror('Error', mensaje, parent=self.ventana)