import tkinter as tk
from tkinter import ttk, messagebox

sans12 = ("Open Sans Extrabold", 12)

class VentanaHistorial:
    def __init__(self, root, controller):
        self.manejoController = controller
        self.ventana = tk.Toplevel(root)
        self.ventana.title("Historial de Facturas")
        self.ventana.geometry("1400x420")
        self.ventana.configure(bg="white")

        tk.Label(self.ventana, text="--- MIS FACTURAS ---", bg="white", font=sans12).pack(pady=10)

        columnas = ['ID', 'Nombre', 'Fecha', 'Total', 'Direccion', 'Estado']
        self.tablaHistorial = ttk.Treeview(self.ventana, columns=columnas, show='headings', height=12)
        self.tablaHistorial.pack(fill='both', expand=True, padx=10, pady=10)

        for col in columnas:
            self.tablaHistorial.heading(col, text=col)

    def mostrarError(self, mensaje):
        messagebox.showerror("Error", mensaje, parent=self.ventana)