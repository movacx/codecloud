import tkinter as tk
from tkinter import messagebox

from Model.ProductoModel import ProductoModel

sans12 = ("Open Sans Extrabold", 12)

class VentanaTienda:
    def __init__(self, root, idUsr):
        self.idCliente = idUsr
        self.ventana = tk.Toplevel(root)
        self.ventana.title('Tienda INTELEK')
        self.ventana.geometry("1100x700")

        # Inicializamos los controladores
        self.controlBusca = BuscadorController()
        self.controlCarrito = CarritoController()
        self.controlPromo = PromoController()
        self.controlResena = ResenaController()
        self.controlCheckout = CheckoutController(self.controlCarrito)

        # Configuracion de grilla principal
        self.ventana.columnconfigure(0, weight = 0)
        self.ventana.columnconfigure(1, weight = 1)
        self.ventana.rowconfigure(0, weight = 1)
        self.ventana.configure(bg = 'white')

    #Barra lateral
        contenedor = tk.Frame(self.ventana, bg = "#4b4242")
        contenedor.grid(row = 0, column = 0, sticky = 'ns')
        
        # Le damos peso a las filas para que los botones se distribuyan
        for item in range(7):
            contenedor.rowconfigure(item, weight = 1)

        # Botones de accion en la barra lateral
        tk.Button(contenedor, text='Ver Calificacion', command=self.verEstrellas, bd=0, bg="#D9D9D9", width=15).grid(row=1, column=0, sticky='nswe', pady=5, padx=(5,5))
        tk.Button(contenedor, text='Agregar a Carrito', command=self.agregarItem, bd=0, bg="#A9DFBF", width=15).grid(row=2, column=0, sticky='nswe', pady=5, padx=(5,5))
        tk.Button(contenedor, text='Aplicar Cupon', command=self.aplicarDescuento, bd=0, bg="#F9E79F", width=15).grid(row=3, column=0, sticky='nswe', pady=5, padx=(5,5))
        tk.Button(contenedor, text='Pagar y Facturar', command=self.pagar, bd=0, bg="#E74C3C", fg="white", width=15).grid(row=4, column=0, sticky='nswe', pady=5, padx=(5,5))

    #Area central
        areaCentral = tk.Frame(self.ventana, bg='white', padx=20, pady=20)
        areaCentral.grid(row=0, column=1, sticky='nsew')
        
    #Labels
        tk.Label(areaCentral, text="Buscador de Productos:", bg='white', font=sans12).pack(anchor='w')
        frameBusqueda = tk.Frame(areaCentral, bg='white')
        frameBusqueda.pack(fill='x', pady=5)
        
        #Inputs
        self.txtBusca = tk.Entry(frameBusqueda, width=40)
        self.txtBusca.pack(side='left', padx=(0, 10))
        tk.Button(frameBusqueda, text="Buscar", command=self.buscar).pack(side='left')
    #Lista
        self.listaInv = tk.Listbox(areaCentral, width=80, height=10)
        self.listaInv.pack(fill='both', expand=True, pady=10)
        
    #Carrito
        tk.Label(areaCentral, text="--- MI CARRITO DE COMPRAS ---", bg='white', font=sans12).pack(pady=(10, 0))
        self.listaCarro = tk.Listbox(areaCentral, width=80, height=6)
        self.listaCarro.pack(fill='both', expand=True, pady=5)
        
        self.lblTotal = tk.Label(areaCentral, text="Total: ₡0", bg='white', font=sans12, fg="blue")
        self.lblTotal.pack(anchor='e')

    #Direccion
        tk.Label(areaCentral, text="Direccion de envio:", bg='white').pack(anchor='w', pady=(10,0))
        self.txtDir = tk.Entry(areaCentral, width=50)
        self.txtDir.pack(anchor='w')
        self.buscar()

     #Buscar 
    def buscar(self):
        res = self.controlBusca.buscarPorNombre(self.txtBusca.get())
        self.listaInv.delete(0, tk.END)
        for r in res:
            self.listaInv.insert(tk.END, f"ID:{r[0]} | {r[1]} | ₡{r[3]} | Stock:{r[4]} | Sock:{r[5]} | RAM:{r[6]}")
    #Ver estrellas 
    def verEstrellas(self):
        sel = self.listaInv.curselection()
        if sel:
            texto = self.listaInv.get(sel[0])
            idPro = texto.split("|")[0].replace("ID:", "").strip()
            prom = self.controlResena.calcularPromedio(idPro) 
            messagebox.showinfo("Reseñas", f"Calificación promedio: {prom} estrellas")
    #Agregar item
    def agregarItem(self):
        sel = self.listaInv.curselection()
        if sel:
            texto = self.listaInv.get(sel[0]).split("|")
            idPro = texto[0].replace("ID:", "").strip()
            nom = texto[1].strip()
            precio = texto[2].replace("₡", "").strip()
            stock = texto[3].replace("Stock:", "").strip()
    
            obj = ProductoModel(idPro, nom, "", precio, stock, "", "")
            exito, msj = self.controlCarrito.agregarProducto(obj, 1) 
            if exito:
                self.actualizarCarro()
            else:
                messagebox.showerror("Error", msj)
    #Actualizar carro
    def actualizarCarro(self):
        self.listaCarro.delete(0, tk.END)
        for item in self.controlCarrito.listaItems:
            self.listaCarro.insert(tk.END, f"{item.producto.nombre} x{item.cantidad}")
        self.lblTotal.config(text=f"Total: ₡{self.controlCarrito.calcularSubtotal()}") 
   #Aplicar descuento
    def aplicarDescuento(self):
        total = self.controlCarrito.calcularSubtotal()
        nuevo, msj = self.controlPromo.aplicarSuerte(total) 
        self.lblTotal.config(text=f"Total con promo: ₡{nuevo} ({msj})")
    #Pagar
    def pagar(self):
        exito, msj = self.controlCheckout.finalizarCompra(self.idCliente, self.txtDir.get(), "Efectivo") 
        if exito:
            self.actualizarCarro()
            messagebox.showinfo("Éxito", msj)
        else:
            messagebox.showerror("Error", msj)



