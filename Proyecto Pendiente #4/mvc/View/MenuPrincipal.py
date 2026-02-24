import tkinter as tk

sans12 = ("Open Sans Extrabold", 12)
sans9 = ("Open Sans Extrabold", 9)

class MenuPrincipal:
    def __init__(self, root, controller, rolUsuario):
        self.manejoController = controller
        self.rol = rolUsuario
        self.ventana = tk.Toplevel(root)
        
        self.ventana.title("Menu Principal INTELEK")
        self.ventana.geometry("1100x700")

        self.ventana.columnconfigure(0, weight = 0)
        self.ventana.columnconfigure(1, weight = 1)
        self.ventana.rowconfigure(0, weight = 1)
        self.ventana.configure(bg = 'white')
        
        self.paneles()
        self.buttons()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     #Paneles
    def paneles(self):
        self.menuLateral = tk.Frame(self.ventana, bg = "#4b4242")
        self.menuLateral.grid(row = 0, column = 0, sticky = 'ns')
        for item in range(7):
            self.menuLateral.rowconfigure(item, weight = 1)
            
        self.areaDerecha = tk.Frame(self.ventana, bg='white')
        self.areaDerecha.grid(row=0, column=1, sticky='nsew')
        
        tk.Label(self.areaDerecha, text=f"Bienvenido a INTELEK\nPerfil activo: {self.rol}", font=sans12, bg='white', fg="#0D5577").pack(expand=True)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Buttons 
    def buttons(self):
        tk.Button(self.menuLateral, bd=0, text='Tienda y Buscador', command=lambda: self.manejoController.abrirTienda(), bg="#D9D9D9", width=20).grid(row=1, column=0, sticky='nswe', pady=5, padx=(10,10))
        tk.Button(self.menuLateral, bd=0, text='Armador de PC', command=lambda: self.manejoController.abrirArmador(), bg="#D9D9D9", width=20).grid(row=2, column=0, sticky='nswe', pady=5, padx=(10,10))

        if self.rol == "Admin": 
            tk.Button(self.menuLateral, bd=0, text='Panel Admin', command=lambda: self.manejoController.abrirAdmin(), bg="#F1C40F", width=20).grid(row=3, column=0, sticky='nswe', pady=5, padx=(10,10))
            
        tk.Button(self.menuLateral, bd=0, text='Cerrar Sesion', command=lambda: self.manejoController.cerrarApp(), bg="#E74C3C", fg="white", width=20).grid(row=5, column=0, sticky='nswe', pady=5, padx=(10,10))