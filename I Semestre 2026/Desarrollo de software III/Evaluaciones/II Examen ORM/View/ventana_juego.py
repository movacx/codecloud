import tkinter as tk
from tkinter import ttk, messagebox


class GameWindow:
    def __init__(self,controller, parent):
        self.controller = controller
        self.window = tk.Toplevel(parent)
        self.window.title("Gestión de Videojuegos")
        self.window.geometry("1120x620")
        self.window.resizable(False, False)

        self._build_ui()
        self.mostrar_tabla()

    def mostrar_advertencia(self, adv):
        messagebox.showwarning('',adv, parent=self.window)
    def mostrar_mensaje(self, msj):
        messagebox.showinfo('',msj, parent=self.window)

    def mostrar_tabla(self):
        columns = ("codigo", "titulo", "desarrollador", "categoria", "stock")
        self.tree = ttk.Treeview(self.frame, columns=columns, show="headings", height=10)
        self.tree.grid(row=8, column=0, columnspan=4, sticky="nsew", padx=5, pady=15)
        for items in columns:
            self.tree.heading(items, text=items)

    def cargar_tabla(self, arreglo):
        for items in arreglo:
            self.tree.insert("", "end", values=(items.codigo, items.titulo, items.desarrollador, items.categoria, items.licencias_disponibles))

    def insertar_tabla(self, items):
        self.tree.insert("", "end", values=(items.codigo, items.titulo, items.desarrollador, items.categoria, items.licencias_disponibles))

    def limpiar_tabla(self):
        for items in self.tree.get_children():
            self.tree.delete(items)

















    def _build_ui(self):
        self.frame = ttk.Frame(self.window, padding=15)
        self.frame.pack(fill="both", expand=True)

        ttk.Label(self.frame, text="Gestión de Videojuegos", font=("Arial", 14, "bold")).grid(
            row=0, column=0, columnspan=4, sticky="w", pady=(0, 15)
        )

        # -------- ENTRIES --------
        self.entry_codigo = ttk.Entry(self.frame, width=30)
        self.entry_titulo = ttk.Entry(self.frame, width=30)
        self.entry_desarrollador = ttk.Entry(self.frame, width=30)
        self.entry_categoria = ttk.Entry(self.frame, width=30)
        self.entry_stock = ttk.Entry(self.frame, width=30)

        ttk.Label(self.frame, text="Código:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_codigo.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(self.frame, text="Título:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_titulo.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(self.frame, text="Desarrollador:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.entry_desarrollador.grid(row=3, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(self.frame, text="Categoría:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.entry_categoria.grid(row=4, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(self.frame, text="Licencias disponibles:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.entry_stock.grid(row=5, column=1, sticky="w", padx=5, pady=5)

        # -------- BOTONES --------
        ttk.Button(self.frame, text="Registrar", width=18, command=lambda : self.controller.registrar_videoJuego()).grid(row=6, column=0, padx=5, pady=10)
        ttk.Button(self.frame, text="Buscar por código", width=18, command=lambda:self.controller.buscar_video_id()).grid(row=6, column=1, padx=5, pady=10)
        ttk.Button(self.frame, text="Buscar por categoría", width=18, command = lambda: self.controller.buscar_categoria()).grid(row=6, column=2, padx=5, pady=10)
        ttk.Button(self.frame, text="Consultar todos", width=18,command=lambda:self.controller.listar_video_juegos()).grid(row=6, column=3, padx=5, pady=10)

        # -------- TABLA --------
