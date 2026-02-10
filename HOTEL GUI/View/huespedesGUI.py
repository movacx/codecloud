import tkinter as tk

class HuespedGUI:
    def __init__(self, ventana_padre):
        self.ventana_hija = tk.Toplevel(ventana_padre)
        self.ventana_hija.title("Registro de Huespedes")
        self.ventana_hija.geometry("350x250")
        
        self.frame_contenedor = tk.Frame(self.ventana_hija)
        self.frame_contenedor.grid(row=0, column=0, padx=20, pady=20)
        
        self.formularioCrear()
        
    def formularioCrear(self):
        tk.Label(self.frame_contenedor, text="Nombre del Huesped:").grid(row=1, column=0, sticky="e", pady=5)
        self.ent_nombre_huesped = tk.Entry(self.frame_contenedor, width=25)
        self.ent_nombre_huesped.grid(row=1, column=1, pady=5)
        
        # Fila 2: Teléfono de Contacto
        tk.Label(self.frame_contenedor, text="Telefono de Contacto:").grid(row=2, column=0, sticky="e", pady=5)
        self.ent_telefono_huesped = tk.Entry(self.frame_contenedor, width=25)
        self.ent_telefono_huesped.grid(row=2, column=1, pady=5)

        # Botón de acción
        self.btn_registrar = tk.Button(self.frame_contenedor, text="Registrar Huesped", bg="#2196F3", fg="white")
        self.btn_registrar.grid(row=3, columnspan=2, pady=15, ipadx=10)