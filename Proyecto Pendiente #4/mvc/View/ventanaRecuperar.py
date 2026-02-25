import tkinter as tk
from tkinter import messagebox

sans12 = ("Open Sans Extrabold", 12)

class VentanaRecuperar:
    #Constructor 
    def __init__(self, root, controller):
        self.manejoController = controller
        self.ventana = tk.Toplevel(root)
        self.ventana.title("Recuperar Contrasena")
        self.ventana.geometry("320x260")
        
	#Label/input
        tk.Label(self.ventana, text="Correo Electronico:").pack(pady=(15, 0))
        self.txtCorreo = tk.Entry(self.ventana, width=35)
        self.txtCorreo.pack(pady=5)
	#Label/input
        tk.Label(self.ventana, text="Nueva Contrasena:").pack(pady=(10, 0))
        self.txtClaveNueva = tk.Entry(self.ventana, width=35, show="*")
        self.txtClaveNueva.pack(pady=5)
	#Label/input
        tk.Label(self.ventana, text="Confirmar Contrasena:").pack(pady=(10, 0))
        self.txtClaveConfirmar = tk.Entry(self.ventana, width=35, show="*")
        self.txtClaveConfirmar.pack(pady=5)
        #Button 
        tk.Button(self.ventana, text="Actualizar", command=lambda: self.manejoController.actualizarClave()).pack(pady=12)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Mostrar mensaje
    def mostrarMensaje(self, mensaje):
        messagebox.showinfo("Intelek", mensaje, parent=self.ventana)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Mostrar error 
    def mostrarError(self, mensaje):
        messagebox.showerror("Error", mensaje, parent=self.ventana)