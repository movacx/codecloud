import tkinter as tk
from tkinter import ttk, messagebox

sans12 = ("Open Sans Extrabold", 12)

class VentanaResena:
    def __init__(self, root, controller):
        self.manejoController = controller
        self.ventana = tk.Toplevel(root)
        self.ventana.title("Reseña del Producto")
        self.ventana.geometry("420x300")
        self.ventana.configure(bg="white")

        self.frameContenedor = tk.Frame(self.ventana, bg="white", padx=20, pady=20)
        self.frameContenedor.pack(fill="both", expand=True)

        self.armarFormulario()

    def armarFormulario(self):
        tk.Label(self.frameContenedor, text="Producto:", bg="white", font=sans12).grid(row=0, column=0, sticky="w", pady=(0, 8))
        self.comboProductos = ttk.Combobox(self.frameContenedor, state="readonly", width=30)
        self.comboProductos.grid(row=1, column=0, columnspan=2, sticky="we", pady=(0, 12))

        tk.Label(self.frameContenedor, text="Comentario (opcional):", bg="white").grid(row=2, column=0, sticky="w")
        self.txtComentario = tk.Entry(self.frameContenedor, width=35)
        self.txtComentario.grid(row=3, column=0, columnspan=2, sticky="we", pady=(0, 14))

        tk.Label(self.frameContenedor, text="Calificación:", bg="white", font=sans12).grid(row=4, column=0, sticky="w", pady=(0, 8))

        tk.Label(self.frameContenedor, text="1 estrella", bg="white").grid(row=5, column=0, sticky="w", pady=2)
        tk.Button(self.frameContenedor, text="Enviar reseña", command=lambda: self.manejoController.enviarResena(1)).grid(row=5, column=1, sticky="e", pady=2)

        tk.Label(self.frameContenedor, text="2 estrellas", bg="white").grid(row=6, column=0, sticky="w", pady=2)
        tk.Button(self.frameContenedor, text="Enviar reseña", command=lambda: self.manejoController.enviarResena(2)).grid(row=6, column=1, sticky="e", pady=2)

        tk.Label(self.frameContenedor, text="3 estrellas", bg="white").grid(row=7, column=0, sticky="w", pady=2)
        tk.Button(self.frameContenedor, text="Enviar reseña", command=lambda: self.manejoController.enviarResena(3)).grid(row=7, column=1, sticky="e", pady=2)

        tk.Label(self.frameContenedor, text="4 estrellas", bg="white").grid(row=8, column=0, sticky="w", pady=2)
        tk.Button(self.frameContenedor, text="Enviar reseña", command=lambda: self.manejoController.enviarResena(4)).grid(row=8, column=1, sticky="e", pady=2)

        tk.Label(self.frameContenedor, text="5 estrellas", bg="white").grid(row=9, column=0, sticky="w", pady=2)
        tk.Button(self.frameContenedor, text="Enviar reseña", command=lambda: self.manejoController.enviarResena(5)).grid(row=9, column=1, sticky="e", pady=2)

        self.frameContenedor.columnconfigure(0, weight=1)
        self.frameContenedor.columnconfigure(1, weight=0)

    def mostrarMensaje(self, mensaje):
        messagebox.showinfo("Intelek", mensaje, parent=self.ventana)

    def mostrarError(self, mensaje):
        messagebox.showerror("Error", mensaje, parent=self.ventana)