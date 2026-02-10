import tkinter as tk

class HuespedGUI:
    def __init__(self, ventana_padre):
        self.ventana_hija = tk.Toplevel(ventana_padre)
        self.ventana_hija.title("Registro de Huéspedes")
        self.ventana_hija.geometry("350x250")
        
        self.frame_contenedor = tk.Frame(self.ventana_hija)
        self.frame_contenedor.grid(row=0, column=0, padx=20, pady=20)
        
        self.formularioCrear()
        
    def formularioCrear(self):
        # Fila 0: ID (Solo lectura/informativo)
        tk.Label(self.frame_contenedor, text="ID Huésped:").grid(row=0, column=0, sticky="e", pady=5)
        self.lbl_id_autogenerado = tk.Label(self.frame_contenedor, text="Pendiente de asignar...", fg="blue")
        self.lbl_id_autogenerado.grid(row=0, column=1, sticky="w", pady=5)
        
        # Fila 1: Nombre Completo
        tk.Label(self.frame_contenedor, text="Nombre del Huésped:").grid(row=1, column=0, sticky="e", pady=5)
        self.ent_nombre_huesped = tk.Entry(self.frame_contenedor, width=25)
        self.ent_nombre_huesped.grid(row=1, column=1, pady=5)
        
        # Fila 2: Teléfono de Contacto
        tk.Label(self.frame_contenedor, text="Teléfono de Contacto:").grid(row=2, column=0, sticky="e", pady=5)
        self.ent_telefono_huesped = tk.Entry(self.frame_contenedor, width=25)
        self.ent_telefono_huesped.grid(row=2, column=1, pady=5)

        # Botón de acción
        self.btn_registrar = tk.Button(self.frame_contenedor, text="Registrar Huésped", bg="#2196F3", fg="white")
        self.btn_registrar.grid(row=3, columnspan=2, pady=15, ipadx=10)