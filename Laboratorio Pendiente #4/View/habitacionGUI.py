import tkinter as tk
from tkinter import ttk

class HabitacionGUI:
    def __init__(self, ventana_padre):
        
        self.ventana_hija = tk.Toplevel(ventana_padre)
        self.ventana_hija.title("Mantenimiento de Habitaciones")
        self.ventana_hija.geometry("350x300")
        
        
        self.frame_contenedor = tk.Frame(self.ventana_hija)
        self.frame_contenedor.grid(row=0, column=0, padx=20, pady=20)
        
        self.formularioCrear()
        
    def formularioCrear(self):
        
        tk.Label(self.frame_contenedor, text="Numero de Habitación:").grid(row=0, column=0, sticky="e", pady=5)
        self.ent_numero_hab = tk.Entry(self.frame_contenedor)
        self.ent_numero_hab.grid(row=0, column=1, pady=5)
        
        
        tk.Label(self.frame_contenedor, text="Tipo de Habitacion:").grid(row=1, column=0, sticky="e", pady=5)
        self.cbx_tipo_hab = ttk.Combobox(self.frame_contenedor, values=["Sencilla", "Doble", "Suite"], state="readonly")
        self.cbx_tipo_hab.grid(row=1, column=1, pady=5)
        
        
        tk.Label(self.frame_contenedor, text="Precio por Noche:").grid(row=2, column=0, sticky="e", pady=5)
        self.ent_precio_hab = tk.Entry(self.frame_contenedor)
        self.ent_precio_hab.grid(row=2, column=1, pady=5)
        
        
        tk.Label(self.frame_contenedor, text="Estado de Habitacion:").grid(row=3, column=0, sticky="e", pady=5)
        self.cbx_estado_hab = ttk.Combobox(self.frame_contenedor, values=["Disponible", "Ocupada"], state="readonly")
        self.cbx_estado_hab.grid(row=3, column=1, pady=5)

        
        self.btn_guardar = tk.Button(self.frame_contenedor, text="Guardar Habitación", bg="#4CAF50", fg="white")
        self.btn_guardar.grid(row=4, columnspan=2, pady=15, ipadx=10)


    #BARMENU