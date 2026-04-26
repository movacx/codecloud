import tkinter as tk
from tkinter import ttk, messagebox


class QueryFrame(tk.Frame):
    """
    Pestaña de consultas.
    """

    # Este Frame se usa para mostrar listados y resultados de búsqueda.
    def __init__(self, parent, controller, notebook=None):
        super().__init__(parent)
        self.controller = controller
        self.notebook = notebook
        self._build()

    # Permite guardar una referencia al notebook para cambiar de pestaña.
    def set_notebook(self, notebook):
        self.notebook = notebook

    # Construye los controles visuales del área de consultas.
    def _build(self):
        tk.Label(self, text="ID del Cliente:", font=("Arial", 12)).grid(
            row=0, column=0, padx=10, pady=10, sticky="e"
        )

        self.entry_query_customer_id = tk.Entry(self, width=35)
        self.entry_query_customer_id.grid(row=0, column=1, padx=10, pady=10)

        tk.Button(
            self,
            text="Mostrar Fletes del Cliente",
            font=("Arial", 12, "bold"),
            command=self.show_customer_freights
        ).grid(row=1, column=0, columnspan=2, pady=10)

        # Treeview es una tabla visual para mostrar datos.
        self.tree = ttk.Treeview(self, show="headings")
        self.tree.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Barras de desplazamiento vertical y horizontal.
        scrollbar_y = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        scrollbar_y.grid(row=2, column=4, sticky="ns")

        scrollbar_x = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        scrollbar_x.grid(row=3, column=0, columnspan=4, sticky="ew")

        self.tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        # Se da peso a filas y columnas para que la tabla aproveche el espacio.
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(2, weight=1)

    # Lleva al usuario a la pestaña de consultas.
    def go_to_tab(self):
        if self.notebook is not None:
            self.notebook.select(self)

    # Borra todas las filas actuales de la tabla.
    def clear_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    # Configura las columnas, encabezados y tamaños de la tabla.
    def configure_table(self, columns, headings, widths):
        self.tree["columns"] = columns

        # Primero se limpian configuraciones anteriores.
        for col in columns:
            self.tree.heading(col, text="")
            self.tree.column(col, width=0)

        # Luego se aplican los nombres y anchos correctos.
        for col, heading, width in zip(columns, headings, widths):
            self.tree.heading(col, text=heading)
            self.tree.column(col, width=width, anchor="center")

    # Muestra todos los clientes en la tabla.
    def show_customers(self):
        try:
            customers = self.controller.get_all_customers()

            self.go_to_tab()
            self.clear_table()

            columns = ("identifier", "name", "phone")
            headings = ("Identificador", "Nombre", "Teléfono")
            widths = (180, 300, 220)

            self.configure_table(columns, headings, widths)

            for customer in customers:
                self.tree.insert("", tk.END, values=(
                    customer.identifier,
                    customer.name,
                    customer.phone
                ))

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Muestra todos los fletes registrados.
    def show_freights(self):
        try:
            freights = self.controller.get_all_freights()

            self.go_to_tab()
            self.clear_table()

            columns = ("number", "customer", "origin", "destination", "weight", "amount")
            headings = ("Número", "Cliente", "Origen", "Destino", "Peso", "Monto")
            widths = (120, 220, 150, 150, 100, 120)

            self.configure_table(columns, headings, widths)

            for freight in freights:
                self.tree.insert("", tk.END, values=(
                    freight.number,
                    freight.customer_name,
                    freight.origin,
                    freight.destination,
                    freight.weight,
                    f"₡{freight.amount:.2f}"
                ))

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Muestra únicamente los fletes del cliente cuyo id fue escrito en la caja de texto.
    def show_customer_freights(self):
        try:
            customer_id = self.entry_query_customer_id.get()
            freights = self.controller.get_freights_by_customer_id(customer_id)

            self.clear_table()

            columns = ("number", "customer", "origin", "destination", "weight", "amount")
            headings = ("Número", "Cliente", "Origen", "Destino", "Peso", "Monto")
            widths = (120, 220, 150, 150, 100, 120)

            self.configure_table(columns, headings, widths)

            for freight in freights:
                self.tree.insert("", tk.END, values=(
                    freight.number,
                    freight.customer_name,
                    freight.origin,
                    freight.destination,
                    freight.weight,
                    f"₡{freight.amount:.2f}"
                ))

            # Si la lista quedó vacía, se informa al usuario.
            if not freights:
                messagebox.showinfo("Información", "Este cliente no tiene fletes registrados.")

        except Exception as e:
            messagebox.showerror("Error", str(e))
