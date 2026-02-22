import tkinter as tk

sans12 = ("Open Sans Extrabold", 12)


class VentanaArmador:
    def __init__(self, root):
        self.ventana = tk.Toplevel(root)
        self.ventana.title("Armador de PC VIRTUAL - INTELEK")
        self.ventana.geometry("1100x700")
        self.controlArmador = ArmadorController()

        # Configuracion de grilla principal a su estilo
        self.ventana.columnconfigure(0, weight = 0)
        self.ventana.columnconfigure(1, weight = 1)
        self.ventana.rowconfigure(0, weight = 1)
        self.ventana.configure(bg = 'white')
    #Barra lateral
        contenedor = tk.Frame(self.ventana, bg = "#4b4242")
        contenedor.grid(row = 0, column = 0, sticky = 'ns')
        
        for item in range(8):
            contenedor.rowconfigure(item, weight = 1)

        tk.Button(contenedor, text="Validar Compatibilidad", command=self.elegirCpu, bd=0, bg="#D9D9D9", width=20).grid(row=1, column=0, sticky='nswe', pady=5, padx=(10,10))
        tk.Button(contenedor, text="Limpiar Seleccion", command=self.cargarProcesadores, bd=0, bg="#E74C3C", fg="white", width=20).grid(row=2, column=0, sticky='nswe', pady=5, padx=(10,10))
	#Area central
        areaCentral = tk.Frame(self.ventana, bg='white', padx=40, pady=40)
        areaCentral.grid(row=0, column=1, sticky='nsew')

        tk.Label(areaCentral, text="ARMADOR DE PC VIRTUAL", font=sans12, bg='white', fg="#0D5577").pack(pady=(0, 10))
        
        tk.Label(areaCentral, text="Paso 1: Seleccione su Procesador (CPU)", font=sans12, bg='white').pack(anchor='w', pady=5)
        self.listaCpu = tk.Listbox(areaCentral, width=80, height=10)
        self.listaCpu.pack(fill='both', expand=True, pady=5)

        tk.Label(areaCentral, text="Paso 2: Tarjetas Madre Compatibles", font=sans12, bg='white').pack(anchor='w', pady=(20, 5))
        self.listaMadre = tk.Listbox(areaCentral, width=80, height=10)
        self.listaMadre.pack(fill='both', expand=True, pady=5)

        # Cargar los datos iniciales apenas se abre la ventana
        self.cargarProcesadores()

    #Botones logica
    def cargarProcesadores(self):
        self.listaCpu.delete(0, tk.END)
        self.listaMadre.delete(0, tk.END)
        
        cpus = self.controlArmador.filtrarProcesadores() 
        for cpu in cpus:
            self.listaCpu.insert(tk.END, f"ID:{cpu[0]} | {cpu[1]} | Precio: ₡{cpu[3]} | Socket: {cpu[5]}")
    #Elegir CPU
    def elegirCpu(self):
        seleccion = self.listaCpu.curselection()
        if not seleccion: 
            return
            
        textoItem = self.listaCpu.get(seleccion[0])
        socketSeleccionado = textoItem.split("Socket: ")[1].strip()
        self.controlArmador.seleccionarCpu(socketSeleccionado) 
        
        madres = self.controlArmador.filtrarTarjetasMadre() 
        self.listaMadre.delete(0, tk.END)
        
        if madres:
            for placa in madres:
                self.listaMadre.insert(tk.END, f"ID:{placa[0]} | {placa[1]} | Precio: ₡{placa[3]}")
        else:
            self.listaMadre.insert(tk.END, "No hay tarjetas madre compatibles con ese socket en inventario.")
