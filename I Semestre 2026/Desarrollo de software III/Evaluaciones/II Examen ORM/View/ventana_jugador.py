import tkinter as tk
from tkinter import ttk, messagebox


class PlayerWindow:
    def __init__(self, controller, parent):
        self.controller = controller
        self.window = tk.Toplevel(parent)
        self.window.title("Gestión de Jugadores")
        self.window.geometry("900x620")
        self.window.title("Gestión de Jugadores")
        self.window.geometry("900x620")
        self._build_ui()
        self.mostrar_tabla()

    def mostrar_advertencia(self, adv):
        messagebox.showwarning('',adv, parent=self.window)
    def mostrar_mensaje(self, msj):
        messagebox.showinfo('',msj, parent=self.window)

    def mostrar_tabla(self):
        columns = ("id", "nombre", "correo", "pais")
        self.tree = ttk.Treeview(self.frame, columns=columns, show="headings", height=10)
        self.tree.grid(row=6, column=0, columnspan=4, sticky="nsew", padx=5, pady=15)
        for items in columns:
            self.tree.heading(items, text=items)

    def cargar_tabla(self, arreglo):
        for items in arreglo:
            self.tree.insert("", "end", values=(items.identificacion, items.nombre_completo, items.correo_electronico, items.pais))

    def insertar_tabla(self, items):
        self.tree.insert("", "end", values=(items.identificacion, items.nombre_completo, items.correo_electronico, items.pais))

    def limpiar_tabla(self):
        for items in self.tree.get_children():
            self.tree.delete(items)















    def _build_ui(self):
        self.frame = ttk.Frame(self.window, padding=15)
        self.frame.pack(fill="both", expand=True)

        ttk.Label(self.frame, text="Gestión de Jugadores", font=("Arial", 14, "bold")).grid(
            row=0, column=0, columnspan=4, sticky="w", pady=(0, 15)
        )

        # -------- ENTRIES --------
        self.entry_id = ttk.Entry(self.frame, width=30)
        self.entry_nombre = ttk.Entry(self.frame, width=30)
        self.entry_correo = ttk.Entry(self.frame, width=30)
        self.entry_pais = ttk.Entry(self.frame, width=30)

        ttk.Label(self.frame, text="Identificación:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_id.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(self.frame, text="Nombre completo:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_nombre.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(self.frame, text="Correo electrónico:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.entry_correo.grid(row=3, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(self.frame, text="País:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.entry_pais.grid(row=4, column=1, sticky="w", padx=5, pady=5)

        # -------- BOTONES --------
        ttk.Button(self.frame, text="Registrar", width=18, command = lambda : self.controller.registrar_jugador()).grid(row=5, column=0, padx=5, pady=10)
        ttk.Button(self.frame, text="Buscar por ID", width=18,command=lambda : self.controller.buscar_jugador()).grid(row=5, column=1, padx=5, pady=10)
        ttk.Button(self.frame, text="Buscar por país", width=18, command = lambda: self.controller.buscar_pais()).grid(row=5, column=2, padx=5, pady=10)
        ttk.Button(self.frame, text="Consultar todos", width=18, command = lambda: self.controller.listar_jugados()).grid(row=5, column=3, padx=5, pady=10)

    def tabla_vieja(self):
        # -------- TABLA --------


        self.tree.heading("id", text="Identificación")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("correo", text="Correo")
        self.tree.heading("pais", text="País")
        sample = [
            ("J-101110111", "Ana Gómez", "ana@correo.com", "Portugal"),
            ("J-202220222", "Luis Vargas", "luis@correo.com", "España"),
        ]
        for row in sample:
            self.tree.insert("", "end", values=row)

        ttk.Button(self.frame, text="Volver al menú principal", command=self.window.destroy).grid(
            row=7, column=0, columnspan=4, pady=10
        )

        self.frame.columnconfigure(3, weight=1)
