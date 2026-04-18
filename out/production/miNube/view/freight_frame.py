import tkinter as tk
from tkinter import messagebox


class FreightFrame(tk.Frame):
    """
    Pestaña de fletes.
    """

    # Este Frame contiene el formulario para registrar fletes.
    def __init__(self, parent, controller, query_frame):
        super().__init__(parent)
        self.controller = controller
        self.query_frame = query_frame
        self._build()

    # Construye los controles visuales del formulario.
    def _build(self):
        labels = [
            "Número de Flete:",
            "ID Cliente:",
            "Origen:",
            "Destino:",
            "Peso:"
        ]

        # Se crean las etiquetas del formulario de forma repetitiva con un for.
        for i, text in enumerate(labels):
            tk.Label(self, text=text, font=("Arial", 12)).grid(
                row=i, column=0, padx=10, pady=10, sticky="e"
            )

        # Cajas de texto para capturar la información del flete.
        self.entry_freight_number = tk.Entry(self, width=35)
        self.entry_freight_customer_id = tk.Entry(self, width=35)
        self.entry_freight_origin = tk.Entry(self, width=35)
        self.entry_freight_destination = tk.Entry(self, width=35)
        self.entry_freight_weight = tk.Entry(self, width=35)

        # Se colocan las entradas en la interfaz.
        self.entry_freight_number.grid(row=0, column=1, padx=10, pady=10)
        self.entry_freight_customer_id.grid(row=1, column=1, padx=10, pady=10)
        self.entry_freight_origin.grid(row=2, column=1, padx=10, pady=10)
        self.entry_freight_destination.grid(row=3, column=1, padx=10, pady=10)
        self.entry_freight_weight.grid(row=4, column=1, padx=10, pady=10)

        # Botón para registrar el flete usando los datos del formulario.
        tk.Button(
            self,
            text="Registrar Flete",
            font=("Arial", 12, "bold"),
            width=20,
            command=self.register_freight
        ).grid(row=5, column=0, columnspan=2, pady=15)

        # Botón para listar los fletes en la pestaña de consultas.
        tk.Button(
            self,
            text="Listar Fletes",
            font=("Arial", 12),
            width=20,
            command=self.query_frame.show_freights
        ).grid(row=6, column=0, columnspan=2, pady=5)

    # Captura los datos escritos y solicita al controlador registrar el flete.
    def register_freight(self):
        try:
            number = self.entry_freight_number.get()
            customer_id = self.entry_freight_customer_id.get()
            origin = self.entry_freight_origin.get()
            destination = self.entry_freight_destination.get()

            # Se convierte el texto del peso a float antes de enviarlo al sistema.
            weight = float(self.entry_freight_weight.get())

            self.controller.add_freight(number, customer_id, origin, destination, weight)
            messagebox.showinfo("Éxito", "Flete registrado correctamente.")
            self.clear_entries()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Limpia el formulario de fletes.
    def clear_entries(self):
        self.entry_freight_number.delete(0, tk.END)
        self.entry_freight_customer_id.delete(0, tk.END)
        self.entry_freight_origin.delete(0, tk.END)
        self.entry_freight_destination.delete(0, tk.END)
        self.entry_freight_weight.delete(0, tk.END)
