import tkinter as tk

class ReservaGUI:
    def __init__(self, ventana_padre):
        self.ventana_hija = tk.Toplevel(ventana_padre)
        self.ventana_hija.title("Gestión de Reservaciones")
        self.ventana_hija.geometry("400x350")
        
        self.frame_contenedor = tk.Frame(self.ventana_hija)
        self.frame_contenedor.grid(row=0, column=0, padx=20, pady=20)
        
        self.formularioCrear()
        
    def formularioCrear(self):
        # Fila 0: ID de la Reserva
        tk.Label(self.frame_contenedor, text="Folio de Reserva:").grid(row=0, column=0, sticky="e", pady=5)
        self.lbl_folio_reserva = tk.Label(self.frame_contenedor, text="000-NEW", font=("Arial", 9, "bold"))
        self.lbl_folio_reserva.grid(row=0, column=1, sticky="w", pady=5)
        
        # Fila 1: Asociación con Habitación
        tk.Label(self.frame_contenedor, text="Número Habitación:").grid(row=1, column=0, sticky="e", pady=5)
        self.ent_asig_habitacion = tk.Entry(self.frame_contenedor)
        self.ent_asig_habitacion.grid(row=1, column=1, pady=5)
        
        # Fila 2: Asociación con Huésped
        tk.Label(self.frame_contenedor, text="ID del Huésped:").grid(row=2, column=0, sticky="e", pady=5)
        self.ent_asig_huesped = tk.Entry(self.frame_contenedor)
        self.ent_asig_huesped.grid(row=2, column=1, pady=5)
        
        # Fila 3: Fechas
        tk.Label(self.frame_contenedor, text="Fecha de Entrada:").grid(row=3, column=0, sticky="e", pady=5)
        self.ent_fecha_checkin = tk.Entry(self.frame_contenedor)
        self.ent_fecha_checkin.grid(row=3, column=1, pady=5)
        
        tk.Label(self.frame_contenedor, text="Fecha de Salida:").grid(row=4, column=0, sticky="e", pady=5)
        self.ent_fecha_checkout = tk.Entry(self.frame_contenedor)
        self.ent_fecha_checkout.grid(row=4, column=1, pady=5)

        # Botón de acción
        self.btn_confirmar = tk.Button(self.frame_contenedor, text="Confirmar Reservación", bg="#FF9800", fg="white")
        self.btn_confirmar.grid(row=5, columnspan=2, pady=15, ipadx=10)