import tkinter as tk
from tkinter import ttk

class HabitacionGUI:
    def __init__(self, ventana_padre):
        self.ventana_hija = tk.Toplevel(ventana_padre)
        self.ventana_hija.title("Mantenimiento de Habitaciones")
        self.ventana_hija.geometry("350x300")
        
        # Contenedor principal con margen
        self.frame_contenedor = tk.Frame(self.ventana_hija)
        self.frame_contenedor.grid(row=0, column=0, padx=20, pady=20)
        
        self.formularioCrear()
        
    def formularioCrear(self):
        # Fila 0: Número de Habitación
        tk.Label(self.frame_contenedor, text="Número de Habitación:").grid(row=0, column=0, sticky="e", pady=5)
        self.ent_numero_hab = tk.Entry(self.frame_contenedor)
        self.ent_numero_hab.grid(row=0, column=1, pady=5)
        
        # Fila 1: Tipo de Habitación
        tk.Label(self.frame_contenedor, text="Tipo de Habitación:").grid(row=1, column=0, sticky="e", pady=5)
        self.cbx_tipo_hab = ttk.Combobox(self.frame_contenedor, values=["Sencilla", "Doble", "Suite"], state="readonly")
        self.cbx_tipo_hab.grid(row=1, column=1, pady=5)
        
        # Fila 2: Precio por Noche
        tk.Label(self.frame_contenedor, text="Precio por Noche:").grid(row=2, column=0, sticky="e", pady=5)
        self.ent_precio_hab = tk.Entry(self.frame_contenedor)
        self.ent_precio_hab.grid(row=2, column=1, pady=5)
        
        # Fila 3: Estado Actual
        tk.Label(self.frame_contenedor, text="Estado de Habitación:").grid(row=3, column=0, sticky="e", pady=5)
        self.cbx_estado_hab = ttk.Combobox(self.frame_contenedor, values=["Disponible", "Ocupada"], state="readonly")
        self.cbx_estado_hab.grid(row=3, column=1, pady=5)

        # Botón de acción
        self.btn_guardar = tk.Button(self.frame_contenedor, text="Guardar Habitación", bg="#4CAF50", fg="white")
        self.btn_guardar.grid(row=4, columnspan=2, pady=15, ipadx=10)