import tkinter as tk

class HuespedGUI:
    def __init__(self, ventana_padre):
        self.ventana_hija = ventana_padre
        self.ventana_hija.title("Registro de Huespedes")
        self.ventana_hija.geometry("470x200")
        

        self.ventana_hija.columnconfigure(0, weight = 1)
        self.ventana_hija.rowconfigure(0, weight=1)

        self.frame_contenedor = tk.Frame(self.ventana_hija)
        self.frame_contenedor.grid(row=0, column=0, padx=20, pady=20, sticky = 'nsew')
        self.frame_contenedor.columnconfigure(0, weight = 0)
        self.frame_contenedor.columnconfigure(0, weight = 1)
        
        self.labels()
        self.entry()
        self.buttons()
        




    def labels(self):
        tk.Label(self.frame_contenedor, text="Nombre del Huesped:").grid(row=1, column=0, sticky="e", pady=5)
        tk.Label(self.frame_contenedor, text="Telefono de Contacto:").grid(row=2, column=0, sticky="e", pady=5)

    def entry(self):
        self.ent_nombre_huesped = tk.Entry(self.frame_contenedor, width=25)
        self.ent_nombre_huesped.grid(row=1, column=1, pady=5, columnspan = 3, sticky = 'ew')

        self.ent_telefono_huesped = tk.Entry(self.frame_contenedor, width=25)
        self.ent_telefono_huesped.grid(row=2, column=1, pady=5, columnspan = 3,sticky = 'ew')

    def buttons(self):
       tk.Button(self.frame_contenedor, text="Registrar Huesped").grid(row=3, column = 0)
       tk.Button(self.frame_contenedor, text="Buscar Huesped").grid(row=3, column = 1, sticky = 'ew')
       tk.Button(self.frame_contenedor, text="Limpiar").grid(row=3, column = 2, sticky = 'ew')



def main():
    root = tk.Tk()
    app = HuespedGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()