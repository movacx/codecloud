import tkinter as tk
from tkinter import ttk

from src.ucr.ac.cr.view.customer_frame import CustomerFrame
from src.ucr.ac.cr.view.freight_frame import FreightFrame
from src.ucr.ac.cr.view.query_frame import QueryFrame


class MainWindow:
    """
    Ventana principal de la aplicación.
    """

    # La ventana principal recibe la raíz de Tkinter y el controlador.
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        # Configuración básica de la ventana.
        self.root.title("Sistema de Gestión de Clientes y Fletes")
        self.root.geometry("1100x720")
        self.root.resizable(False, False)

        self._build()

    # Construye la interfaz principal.
    def _build(self):
        title = tk.Label(
            self.root,
            text="Sistema de Gestión de Clientes y Fletes",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=10)

        # Notebook crea una interfaz por pestañas.
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Se crean las tres secciones principales de la aplicación.
        query_frame = QueryFrame(notebook, self.controller)
        customer_frame = CustomerFrame(notebook, self.controller, query_frame)
        freight_frame = FreightFrame(notebook, self.controller, query_frame)

        # Se le pasa al QueryFrame una referencia al notebook para poder cambiar de pestaña.
        query_frame.set_notebook(notebook)

        # Se agregan las pestañas al notebook.
        notebook.add(customer_frame, text="Clientes")
        notebook.add(freight_frame, text="Fletes")
        notebook.add(query_frame, text="Consultas")
