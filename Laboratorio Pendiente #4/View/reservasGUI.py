import tkinter as tk

class ReservaGUI:
    def __init__(self, ventana_padre, controller):
        self.manejoController=controller
        self.ventana_hija = tk.Toplevel(ventana_padre)
        self.ventana_hija.title("Gestion de Reservaciones")
        self.ventana_hija.geometry("400x350")
        
        self.frame_contenedor = tk.Frame(self.ventana_hija)
        self.frame_contenedor.grid(row=0, column=0, padx=20, pady=20)
        
        self.formularioCrear()
        
    def formularioCrear(self):

        
        tk.Label(self.frame_contenedor, text="Numero Habitacion:").grid(row=1, column=0, sticky="e", pady=5)
        self.ent_asig_habitacion = tk.Entry(self.frame_contenedor)
        self.ent_asig_habitacion.grid(row=1, column=1, pady=5)
        
        tk.Label(self.frame_contenedor, text="ID del Huesped:").grid(row=2, column=0, sticky="e", pady=5)
        self.ent_asig_huesped = tk.Entry(self.frame_contenedor)
        self.ent_asig_huesped.grid(row=2, column=1, pady=5)
        
        tk.Label(self.frame_contenedor, text="Fecha de Entrada:").grid(row=3, column=0, sticky="e", pady=5)
        self.ent_fecha_checkin = tk.Entry(self.frame_contenedor)
        self.ent_fecha_checkin.grid(row=3, column=1, pady=5)
        
        tk.Label(self.frame_contenedor, text="Fecha de Salida:").grid(row=4, column=0, sticky="e", pady=5)
        self.ent_fecha_checkout = tk.Entry(self.frame_contenedor)
        self.ent_fecha_checkout.grid(row=4, column=1, pady=5)

        self.btn_confirmar = tk.Button(self.frame_contenedor, text="Confirmar Reservacion", bg="#FF9800", fg="white")
        self.btn_confirmar.grid(row=5, columnspan=2, pady=15, ipadx=10)