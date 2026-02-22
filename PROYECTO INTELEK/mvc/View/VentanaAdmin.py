import tkinter as tk

sans12 = ("Open Sans Extrabold", 12)
sans9 = ("Open Sans Extrabold", 9)

class VentanaAdmin:
    def __init__(self, root):
        self.ventana = tk.Toplevel(root)
        self.ventana.title("Panel Administrativo INTELEK")
        self.ventana.geometry("1100x700")

        self.controlReporte = ReporteController()
        self.controlAdmin = AdminController()

        # Configuracion de grilla principal
        self.ventana.columnconfigure(0, weight = 0)
        self.ventana.columnconfigure(1, weight = 1)
        self.ventana.rowconfigure(0, weight = 1)
        self.ventana.configure(bg = 'white')

    #Barra lateral
        contenedor = tk.Frame(self.ventana, bg = "#4b4242")
        contenedor.grid(row = 0, column = 0, sticky = 'ns')
        
        for item in range(10):
            contenedor.rowconfigure(item, weight = 1)

        tk.Button(contenedor, text="Ver Ventas Totales", command=self.verVentas, bd=0, bg="#D9D9D9", width=20).grid(row=1, column=0, sticky='nswe', pady=5, padx=(10,10))
        tk.Button(contenedor, text="Ver Total Cuentas", command=self.verCuentas, bd=0, bg="#D9D9D9", width=20).grid(row=2, column=0, sticky='nswe', pady=5, padx=(10,10))
        
        tk.Label(contenedor, text="--- REEMBOLSOS ---", bg="#4b4242", fg="white", font=sans9).grid(row=4, column=0, pady=(20, 5))
        self.txtIdFac = tk.Entry(contenedor, width=20)
        self.txtIdFac.grid(row=5, column=0, pady=5, padx=(10,10))
        tk.Button(contenedor, text="Aceptar Reembolso", command=lambda: self.reembolsar("Reembolsado"), bd=0, bg="#E74C3C", fg="white", width=20).grid(row=6, column=0, sticky='nswe', pady=5, padx=(10,10))
    #Area central 
        areaCentral = tk.Frame(self.ventana, bg='white', padx=40, pady=40)
        areaCentral.grid(row=0, column=1, sticky='nsew')

        self.lblDisplay = tk.Label(areaCentral, text="Bienvenido al Panel de Control", font=sans12, bg='white', fg="#0D5577")
        self.lblDisplay.pack(pady=(0, 20))

        tk.Label(areaCentral, text="MANTENIMIENTO DE PRODUCTOS", font=sans12, bg='white').pack(anchor='w', pady=(10, 10))

        # Formulario ordenado en un frame interno
        frameForm = tk.Frame(areaCentral, bg='white')
        frameForm.pack(fill='x')

        tk.Label(frameForm, text="Nombre del producto:", bg='white').grid(row=0, column=0, sticky='w', pady=5)
        self.txtNomPro = tk.Entry(frameForm, width=40)
        self.txtNomPro.grid(row=0, column=1, pady=5, padx=10)

        tk.Label(frameForm, text="Categoria (Ej: Procesador, Motherboard):", bg='white').grid(row=1, column=0, sticky='w', pady=5)
        self.txtCatPro = tk.Entry(frameForm, width=40)
        self.txtCatPro.grid(row=1, column=1, pady=5, padx=10)

        tk.Label(frameForm, text="Precio:", bg='white').grid(row=2, column=0, sticky='w', pady=5)
        self.txtPrecioPro = tk.Entry(frameForm, width=40)
        self.txtPrecioPro.grid(row=2, column=1, pady=5, padx=10)

        tk.Label(frameForm, text="Stock inicial:", bg='white').grid(row=3, column=0, sticky='w', pady=5)
        self.txtStockPro = tk.Entry(frameForm, width=40)
        self.txtStockPro.grid(row=3, column=1, pady=5, padx=10)

        tk.Label(frameForm, text="Socket (Solo CPU/Motherboard):", bg='white').grid(row=4, column=0, sticky='w', pady=5)
        self.txtSockPro = tk.Entry(frameForm, width=40)
        self.txtSockPro.grid(row=4, column=1, pady=5, padx=10)

        tk.Label(frameForm, text="Tipo RAM (Solo CPU/Motherboard):", bg='white').grid(row=5, column=0, sticky='w', pady=5)
        self.txtRamPro = tk.Entry(frameForm, width=40)
        self.txtRamPro.grid(row=5, column=1, pady=5, padx=10)

        tk.Button(frameForm, text="Guardar Producto en CSV", command=self.guardarNuevoPro, bg="#27AE60", fg="white", bd=0, padx=20, pady=5).grid(row=6, column=0, columnspan=2, pady=20)

    #Botones logica 
    def verVentas(self):
        monto = self.controlReporte.reporteFinanciero() 
        self.lblDisplay.config(text=f"INGRESOS BRUTOS: ₡{monto}", fg="blue")

    def verCuentas(self):
        total = self.controlReporte.reporteCuentas() 
        self.lblDisplay.config(text=f"TOTAL CUENTAS REGISTRADAS: {total}", fg="blue")

    def reembolsar(self, estado):
        idF = self.txtIdFac.get()
        exito, msj = self.controlAdmin.gestionarEstadoFactura(idF, estado) 
        if exito:
            self.lblDisplay.config(text=msj, fg="green")
            self.txtIdFac.delete(0, tk.END)
        else:
            self.lblDisplay.config(text=msj, fg="red")

    def guardarNuevoPro(self):
        nom = self.txtNomPro.get()
        cat = self.txtCatPro.get()
        pre = self.txtPrecioPro.get()
        stk = self.txtStockPro.get()
        sck = self.txtSockPro.get()
        ram = self.txtRamPro.get()

        if not sck: sck = "N/A"
        if not ram: ram = "N/A"

        exito, msj = self.controlAdmin.agregarNuevoProducto(nom, cat, pre, stk, sck, ram) 
        if exito:
            self.lblDisplay.config(text=f"Exito: {msj}", fg="green")
            self.txtNomPro.delete(0, tk.END)
            self.txtPrecioPro.delete(0, tk.END)
            self.txtStockPro.delete(0, tk.END)
        else:
            self.lblDisplay.config(text=f"Error: {msj}", fg="red")
   
