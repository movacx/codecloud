import tkinter as tk
from VentanaTienda import VentanaTienda
from VentanaArmador import VentanaArmador
from VentanaAdmin import VentanaAdmin

sans12 = ("Open Sans Extrabold", 12)
sans9 = ("Open Sans Extrabold", 9)
class MenuPrincipal:
    def __init__(self, ventanaNueva, rolUsuario, idUsr, ventanaLogin):
        self.ventana = ventanaNueva
        self.rol = rolUsuario
        self.idLogueado = idUsr
        self.loginOriginal = ventanaLogin
        
        self.ventana.title("Menu Principal INTELEK")
        self.ventana.geometry("1100x700")

        # Configuración de tu grilla
        self.ventana.columnconfigure(0, weight = 0)
        self.ventana.columnconfigure(1, weight = 1)
        self.ventana.rowconfigure(0, weight = 1)
        self.ventana.configure(bg = 'white')
        
    #Barras laterales
        menuLateral = tk.Frame(self.ventana, bg = "#4b4242")
        menuLateral.grid(row = 0, column = 0, sticky = 'ns')
        
        for item in range(7):
            menuLateral.rowconfigure(item, weight = 1)
        # Botones de navegación
        tk.Button(menuLateral, bd=0, text='Tienda y Buscador', command=self.abrirTienda, bg="#D9D9D9", width=20).grid(row=1, column=0, sticky='nswe', pady=5, padx=(10,10))
        tk.Button(menuLateral, bd=0, text='Armador de PC', command=self.abrirArmador, bg="#D9D9D9", width=20).grid(row=2, column=0, sticky='nswe', pady=5, padx=(10,10))

        # Botón exclusivo para el administrador
        if self.rol == "Admin": 
            tk.Button(menuLateral, bd=0, text='Panel Admin', command=self.abrirAdmin, bg="#F1C40F", width=20).grid(row=3, column=0, sticky='nswe', pady=5, padx=(10,10))
    #Cerrar sesion
        tk.Button(menuLateral, bd=0, text='Cerrar Sesion', command=self.cerrarApp, bg="#E74C3C", fg="white", width=20).grid(row=5, column=0, sticky='nswe', pady=5, padx=(10,10))
        
        areaDerecha = tk.Frame(self.ventana, bg='white')
        areaDerecha.grid(row=0, column=1, sticky='nsew')
        
        tk.Label(areaDerecha, text=f"Bienvenido a INTELEK\nPerfil activo: {self.rol}", font=sans12, bg='white', fg="#0D5577").pack(expand=True)

    # Métodos para abrir las otras ventanas
    def abrirTienda(self):
        VentanaTienda(self.ventana, self.idLogueado) 

    def abrirArmador(self):
        VentanaArmador(self.ventana)

    def abrirAdmin(self):
        VentanaAdmin(self.ventana)

    def cerrarApp(self):
        self.ventana.destroy() 
        self.loginOriginal.deiconify()
