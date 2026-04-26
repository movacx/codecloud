import tkinter as tk
from tkinter import messagebox


class CustomerFrame(tk.Frame):
    """
    Pestaña de clientes.
    """

    # Este Frame representa la sección de la interfaz donde se registran clientes.
    def __init__(self, parent, controller, query_frame):
        super().__init__(parent)
        self.controller = controller
        self.query_frame = query_frame
        self._build()

    # Construye visualmente todos los componentes del formulario.
    def _build(self):
        labels = ["Identificador:", "Nombre:", "Teléfono:"]

        # Se crean las etiquetas del formulario usando un recorrido.
        for i, text in enumerate(labels):
            tk.Label(self, text=text, font=("Arial", 12)).grid(
                row=i, column=0, padx=10, pady=10, sticky="e"
            )

        # Entradas de texto para capturar los datos del cliente.
        self.entry_customer_id = tk.Entry(self, width=35)
        self.entry_customer_name = tk.Entry(self, width=35)
        self.entry_customer_phone = tk.Entry(self, width=35)

        # Ubicación de las cajas de texto en la cuadrícula.
        self.entry_customer_id.grid(row=0, column=1, padx=10, pady=10)
        self.entry_customer_name.grid(row=1, column=1, padx=10, pady=10)
        self.entry_customer_phone.grid(row=2, column=1, padx=10, pady=10)

        # Botón para registrar un cliente nuevo.
        tk.Button(
            self,
            text="Registrar Cliente",
            font=("Arial", 12, "bold"),
            width=20,
            command=self.register_customer
        ).grid(row=3, column=0, columnspan=2, pady=15)

        # Botón para abrir la pestaña de consultas y listar clientes.
        tk.Button(
            self,
            text="Listar Clientes",
            font=("Arial", 12),
            width=20,
            command=self.query_frame.show_customers
        ).grid(row=4, column=0, columnspan=2, pady=5)

    # Toma los datos escritos por el usuario y solicita al controlador el registro.
    def register_customer(self):
        try:
            identifier = self.entry_customer_id.get()
            name = self.entry_customer_name.get()
            phone = self.entry_customer_phone.get()

            self.controller.add_customer(identifier, name, phone)
            messagebox.showinfo("Éxito", "Cliente registrado correctamente.")
            self.clear_entries()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Limpia las cajas de texto del formulario.
    def clear_entries(self):
        self.entry_customer_id.delete(0, tk.END)
        self.entry_customer_name.delete(0, tk.END)
        self.entry_customer_phone.delete(0, tk.END)
