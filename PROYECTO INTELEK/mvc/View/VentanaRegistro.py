import tkinter as tk

sans12 = ("Open Sans Extrabold", 12)

class VentanaRegistro:
    def __init__(self, root, controlAuth):
        self.ventana = tk.Toplevel(root)
        self.ventana.title("Registro")
        self.ventana.geometry("300x300")
        self.controlador = controlAuth
        
        #Labels
        tk.Label(self.ventana, text="Nombre Completo:").pack(pady=(10, 0))
        self.txtNombre = tk.Entry(self.ventana)
        self.txtNombre.pack(pady=5)
        
        tk.Label(self.ventana, text="Correo Electronico:").pack()
        self.txtCorreo = tk.Entry(self.ventana)
        self.txtCorreo.pack(pady=5)
    
        tk.Label(self.ventana, text="Contrasena:").pack()
        self.txtClave = tk.Entry(self.ventana, show="*")
        self.txtClave.pack(pady=5)
        
        #Buttons
        tk.Button(self.ventana, text="Guardar", command=self.registrar).pack(pady=10)
        self.lblMensaje = tk.Label(self.ventana, text="")
        self.lblMensaje.pack()

    def registrar(self):
        exito, msj = self.controlador.procesarRegistro(self.txtNombre.get(), self.txtCorreo.get(), self.txtClave.get())
        if exito:
            self.lblMensaje.config(text=msj, fg="green")
        else:
            self.lblMensaje.config(text=msj, fg="red")

