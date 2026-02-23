import tkinter as tk
from tkinter import ttk, messagebox

sans12 = ("Open Sans Extrabold", 12)

class VentanaArmador:
    def __init__(self, root, controller):
        self.manejoController = controller
        self.ventana = tk.Toplevel(root)
        self.ventana.title("Armador de PC VIRTUAL - INTELEK")
        self.ventana.geometry("1100x700")

        self.ventana.columnconfigure(0, weight = 0)
        self.ventana.columnconfigure(1, weight = 1)
        self.ventana.rowconfigure(0, weight = 1)
        self.ventana.configure(bg = 'white')

        self.paneles()
        self.botones()
        self.entradas()

    def paneles(self):
        self.menuLateral = tk.Frame(self.ventana, bg = "#4b4242")
        self.menuLateral.grid(row = 0, column = 0, sticky = 'ns')
        for item in range(8):
            self.menuLateral.rowconfigure(item, weight = 1)

        self.areaCentral = tk.Frame(self.ventana, bg='white', padx=40, pady=40)
        self.areaCentral.grid(row=0, column=1, sticky='nsew')

    def botones(self):
        tk.Button(self.menuLateral, text="Buscar Compatibles", command=lambda: self.manejoController.buscarCompatibilidad(), bd=0, bg="#D9D9D9", width=20).grid(row=1, column=0, sticky='nswe', pady=5, padx=(10,10))
        tk.Button(self.menuLateral, text="Limpiar", command=lambda: self.manejoController.cargarProcesadores(), bd=0, bg="#E74C3C", fg="white", width=20).grid(row=2, column=0, sticky='nswe', pady=5, padx=(10,10))

    def entradas(self):
        tk.Label(self.areaCentral, text="Paso 1: Seleccione su Procesador (CPU)", font=sans12, bg='white').pack(anchor='w', pady=5)
        self.cbxCpu = ttk.Combobox(self.areaCentral, state='readonly', width=80)
        self.cbxCpu.pack(pady=5)

        tk.Label(self.areaCentral, text="Paso 2: Tarjetas Madre Compatibles", font=sans12, bg='white').pack(anchor='w', pady=(20, 5))
        
        # Tabla de Tarjetas Madre
        columnasMadre = ['ID', 'Nombre', 'Precio']
        self.tablaMadres = ttk.Treeview(self.areaCentral, columns=columnasMadre, show='headings', height=10)
        self.tablaMadres.pack(fill='both', expand=True, pady=5)
        for col in columnasMadre:
            self.tablaMadres.heading(col, text=col)

    def mostrarError(self, mensaje):
        messagebox.showerror('Error', mensaje, parent=self.ventana)