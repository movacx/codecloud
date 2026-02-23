import tkinter as tk
from tkinter import messagebox

sans12 = ("Open Sans Extrabold", 12)
sans9 = ("Open Sans Extrabold", 9)

class VentanaAdmin:
    def __init__(self, root, controller):
        self.manejoController = controller
        self.ventana = tk.Toplevel(root)
        self.ventana.title("Panel Administrativo INTELEK")
        self.ventana.geometry("1100x700")

        self.ventana.columnconfigure(0, weight = 0)
        self.ventana.columnconfigure(1, weight = 1)
        self.ventana.rowconfigure(0, weight = 1)
        self.ventana.configure(bg = 'white')

        self.paneles()
        self.botones()
        self.entradas()

    def paneles(self):
        self.contenedor = tk.Frame(self.ventana, bg = "#4b4242")
        self.contenedor.grid(row = 0, column = 0, sticky = 'ns')
        for item in range(10):
            self.contenedor.rowconfigure(item, weight = 1)

        self.areaCentral = tk.Frame(self.ventana, bg='white', padx=40, pady=40)
        self.areaCentral.grid(row=0, column=1, sticky='nsew')

    def botones(self):
        tk.Button(self.contenedor, text="Ver Ventas Totales", command=lambda: self.manejoController.verVentas(), bd=0, bg="#D9D9D9", width=20).grid(row=1, column=0, sticky='nswe', pady=5, padx=(10,10))
        tk.Button(self.contenedor, text="Ver Total Cuentas", command=lambda: self.manejoController.verCuentas(), bd=0, bg="#D9D9D9", width=20).grid(row=2, column=0, sticky='nswe', pady=5, padx=(10,10))
        
        tk.Label(self.contenedor, text="--- REEMBOLSOS ---", bg="#4b4242", fg="white", font=sans9).grid(row=4, column=0, pady=(20, 5))
        self.txtIdFac = tk.Entry(self.contenedor, width=20)
        self.txtIdFac.grid(row=5, column=0, pady=5, padx=(10,10))
        tk.Button(self.contenedor, text="Aceptar Reembolso", command=lambda: self.manejoController.reembolsar("Reembolsado"), bd=0, bg="#E74C3C", fg="white", width=20).grid(row=6, column=0, sticky='nswe', pady=5, padx=(10,10))

    def entradas(self):
        tk.Label(self.areaCentral, text="MANTENIMIENTO DE PRODUCTOS", font=sans12, bg='white').pack(anchor='w', pady=(10, 10))

        self.frameForm = tk.Frame(self.areaCentral, bg='white')
        self.frameForm.pack(fill='x')

        tk.Label(self.frameForm, text="Nombre del producto:", bg='white').grid(row=0, column=0, sticky='w', pady=5)
        self.txtNomPro = tk.Entry(self.frameForm, width=40)
        self.txtNomPro.grid(row=0, column=1, pady=5, padx=10)

        tk.Label(self.frameForm, text="Categoria (Ej: Procesador, Motherboard):", bg='white').grid(row=1, column=0, sticky='w', pady=5)
        self.txtCatPro = tk.Entry(self.frameForm, width=40)
        self.txtCatPro.grid(row=1, column=1, pady=5, padx=10)

        tk.Label(self.frameForm, text="Precio:", bg='white').grid(row=2, column=0, sticky='w', pady=5)
        self.txtPrecioPro = tk.Entry(self.frameForm, width=40)
        self.txtPrecioPro.grid(row=2, column=1, pady=5, padx=10)

        tk.Label(self.frameForm, text="Stock inicial:", bg='white').grid(row=3, column=0, sticky='w', pady=5)
        self.txtStockPro = tk.Entry(self.frameForm, width=40)
        self.txtStockPro.grid(row=3, column=1, pady=5, padx=10)

        tk.Label(self.frameForm, text="Socket (Solo CPU/Motherboard):", bg='white').grid(row=4, column=0, sticky='w', pady=5)
        self.txtSockPro = tk.Entry(self.frameForm, width=40)
        self.txtSockPro.grid(row=4, column=1, pady=5, padx=10)

        tk.Label(self.frameForm, text="Tipo RAM (Solo CPU/Motherboard):", bg='white').grid(row=5, column=0, sticky='w', pady=5)
        self.txtRamPro = tk.Entry(self.frameForm, width=40)
        self.txtRamPro.grid(row=5, column=1, pady=5, padx=10)

        tk.Button(self.frameForm, text="Guardar Producto en CSV", command=lambda: self.manejoController.guardarNuevoPro(), bg="#27AE60", fg="white", bd=0, padx=20, pady=5).grid(row=6, column=0, columnspan=2, pady=20)

    def mostrarMensaje(self, mensaje):
        messagebox.showinfo('Intelek', mensaje, parent=self.ventana)

    def mostrarError(self, mensaje):
        messagebox.showerror('Error', mensaje, parent=self.ventana)