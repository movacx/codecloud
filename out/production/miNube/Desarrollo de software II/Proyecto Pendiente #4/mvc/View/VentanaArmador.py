import tkinter as tk
from tkinter import ttk, messagebox

estiloTexto = ("Open Sans Extrabold", 12)

class VentanaArmador:
    def __init__(self, root, controller):
        self.manejoController = controller
        self.ventana = tk.Toplevel(root)
        self.ventana.title("Pedido Personalizado - INTELEK")
        self.ventana.geometry("1100x850")
        self.ventana.columnconfigure(1, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        self.ventana.configure(bg='white')
        self.paneles()
        self.entradas()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def paneles(self):
        self.menuLateral = tk.Frame(self.ventana, bg="#4b4242", width=200)
        self.menuLateral.grid(row=0, column=0, sticky='ns')
        tk.Button(self.menuLateral, text="Limpiar Pedido", command=lambda: self.manejoController.limpiarTodo(), width=20).pack(pady=20, padx=10)

        self.areaCentral = tk.Frame(self.ventana, bg='white', padx=40, pady=20)
        self.areaCentral.grid(row=0, column=1, sticky='nsew')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def entradas(self):
        frameBusqueda = tk.Frame(self.areaCentral, bg='white')
        frameBusqueda.pack(fill='x', pady=5)
        
        tk.Label(frameBusqueda, text="Selección del procesador", font=estiloTexto, bg='white').grid(row=0, column=0, sticky='w')
        self.selectorProcesador = ttk.Combobox(frameBusqueda, state='readonly', width=40)
        self.selectorProcesador.grid(row=1, column=0, pady=5, sticky='w')
        
        tk.Label(frameBusqueda, text="Buscar por piezas", font=estiloTexto, bg='white').grid(row=0, column=1, padx=(20,0), sticky='w')
        self.selectorCategoria = ttk.Combobox(frameBusqueda, values=['Procesador', 'Motherboard', 'Ram', 'Case', 'Ventilador', 'Discos', 'GPU'], state='readonly', width=30)
        self.selectorCategoria.grid(row=1, column=1, padx=(20,0), pady=5, sticky='w')
        
        tk.Button(frameBusqueda, text="Buscar", command=lambda: self.manejoController.buscarOtrasPiezas()).grid(row=1, column=2, padx=10)
        
        tk.Label(self.areaCentral, text="Opciones Disponibles", font=estiloTexto, bg='white').pack(anchor='w', pady=(10, 5))
        columnas = ['ID', 'Categoria', 'Nombre', 'Precio']
        self.tablaOpciones = ttk.Treeview(self.areaCentral, columns=columnas, show='headings', height=8)
        self.tablaOpciones.pack(fill='both', expand=True, pady=5)
        for col in columnas:
            self.tablaOpciones.heading(col, text=col)
            
        tk.Button(self.areaCentral, text="Agregar al Pedido", command=lambda: self.manejoController.meterAlCarrito()).pack(pady=10)
        
        tk.Label(self.areaCentral, text="PC Personalizada:", font=estiloTexto, bg='white').pack(anchor='w', pady=(10, 5))
        self.tablaCarrito = ttk.Treeview(self.areaCentral, columns=columnas, show='headings', height=8)
        self.tablaCarrito.pack(fill='both', expand=True, pady=5)
        for col in columnas:
            self.tablaCarrito.heading(col, text=col)

        frameEnvio = tk.Frame(self.areaCentral, bg='white')
        frameEnvio.pack(fill='x', pady=20)

        tk.Label(frameEnvio, text="Nombre completo:", font=estiloTexto, bg='white').grid(row=0, column=0, sticky='w')
        self.entradaNombre = tk.Entry(frameEnvio, width=80)
        self.entradaNombre.grid(row=1, column=0, pady=5)

        tk.Label(frameEnvio, text="Dirección de entrega:", font=estiloTexto, bg='white').grid(row=2, column=0, sticky='w')
        self.entradaDireccion = tk.Entry(frameEnvio, width=80)
        self.entradaDireccion.grid(row=3, column=0, pady=5)
        
        tk.Button(self.areaCentral, text="Finalizar Compra", command=lambda: self.manejoController.finalizar()).pack(pady=10)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Mostrar error
    def mostrarError(self, mensaje):
        messagebox.showerror('Error', mensaje, parent=self.ventana)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Mostrar info
    def mostrarInfo(self, mensaje):
        messagebox.showinfo('Intelek', mensaje, parent=self.ventana)