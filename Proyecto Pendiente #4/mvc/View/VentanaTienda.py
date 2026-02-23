import tkinter as tk
from tkinter import ttk, messagebox

sans12 = ("Open Sans Extrabold", 12)

class VentanaTienda:
    def __init__(self, root, controller):
        self.manejoController = controller
        self.ventana = tk.Toplevel(root)
        self.ventana.title('Tienda INTELEK')
        self.ventana.geometry("1100x700")

        self.ventana.columnconfigure(0, weight = 0)
        self.ventana.columnconfigure(1, weight = 1)
        self.ventana.rowconfigure(0, weight = 1)
        self.ventana.configure(bg = 'white')

        self.paneles()
        self.botones()
        self.entradas()
        self.insertarTablas()

    def separador(self, contenedor, fila, columna):
        tk.Label(contenedor, text='', bg="#4b4242").grid(row=fila, column=columna)

    def paneles(self):
        self.menuLateral = tk.Frame(self.ventana, bg = "#4b4242")
        self.menuLateral.grid(row = 0, column = 0, sticky = 'ns')
        for item in range(7):
            self.menuLateral.rowconfigure(item, weight = 1)

        self.areaCentral = tk.Frame(self.ventana, bg='white', padx=20, pady=20)
        self.areaCentral.grid(row=0, column=1, sticky='nsew')

    def botones(self):
        self.separador(self.menuLateral, 0, 0)
        tk.Button(self.menuLateral, text='Ver Calificacion', command=lambda: self.manejoController.verEstrellas(), bd=0, bg="#D9D9D9", width=15).grid(row=1, column=0, sticky='nswe', pady=5, padx=(5,5))
        tk.Button(self.menuLateral, text='Agregar a Carrito', command=lambda: self.manejoController.agregarItem(), bd=0, bg="#A9DFBF", width=15).grid(row=2, column=0, sticky='nswe', pady=5, padx=(5,5))
        tk.Button(self.menuLateral, text='Aplicar Cupon', command=lambda: self.manejoController.aplicarDescuento(), bd=0, bg="#F9E79F", width=15).grid(row=3, column=0, sticky='nswe', pady=5, padx=(5,5))
        tk.Button(self.menuLateral, text='Pagar y Facturar', command=lambda: self.manejoController.pagarFactura(), bd=0, bg="#E74C3C", fg="white", width=15).grid(row=4, column=0, sticky='nswe', pady=5, padx=(5,5))

    def entradas(self):
        tk.Label(self.areaCentral, text="Buscador de Productos:", bg='white', font=sans12).pack(anchor='w')
        self.frameBusqueda = tk.Frame(self.areaCentral, bg='white')
        self.frameBusqueda.pack(fill='x', pady=5)
        
        self.txtBusca = tk.Entry(self.frameBusqueda, width=40)
        self.txtBusca.pack(side='left', padx=(0, 10))
        tk.Button(self.frameBusqueda, text="Buscar", command=lambda: self.manejoController.buscarProductos()).pack(side='left')

        tk.Label(self.areaCentral, text="Direccion de envio:", bg='white').pack(anchor='w', pady=(10,0))
        self.txtDir = tk.Entry(self.areaCentral, width=50)
        self.txtDir.pack(anchor='w')

    def insertarTablas(self):
        # Tabla de Inventario
        columnasInv = ['ID', 'Nombre', 'Precio', 'Stock']
        self.tablaInv = ttk.Treeview(self.areaCentral, columns=columnasInv, show='headings', height=8)
        self.tablaInv.pack(fill='both', expand=True, pady=10)
        for col in columnasInv:
            self.tablaInv.heading(col, text=col)

        tk.Label(self.areaCentral, text="--- MI CARRITO DE COMPRAS ---", bg='white', font=sans12).pack(pady=(10, 0))
        
        # Tabla de Carrito
        columnasCarro = ['Producto', 'Cantidad', 'Subtotal']
        self.tablaCarro = ttk.Treeview(self.areaCentral, columns=columnasCarro, show='headings', height=5)
        self.tablaCarro.pack(fill='both', expand=True, pady=5)
        for col in columnasCarro:
            self.tablaCarro.heading(col, text=col)
        
        self.lblTotal = tk.Label(self.areaCentral, text="Total: ₡0", bg='white', font=sans12, fg="blue")
        self.lblTotal.pack(anchor='e')

    def mostrarMensaje(self, mensaje):
        messagebox.showinfo('Intelek', mensaje, parent=self.ventana)

    def mostrarError(self, mensaje):
        messagebox.showerror('Error', mensaje, parent=self.ventana)