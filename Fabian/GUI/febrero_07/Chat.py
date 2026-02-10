import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext 

class MuestrarioWidgetsGrid(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Catálogo con GRID - Python 2026")
        self.geometry("500x750")
        
        # CONFIGURACIÓN VITAL PARA GRID:
        # Le decimos a la ventana: "Tu columna 0 y fila 0 deben crecer si estiras la ventana"
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        # 8. MenuBar (Igual que antes, no depende del grid)
        self._crear_menu_bar()

#=================================  
        # Contenedor principal
        main_frame = ttk.Frame(self, padding=20)
        # OJO: Cambiamos pack() por grid()
        # sticky="nsew" -> Estírate al Norte, Sur, Este y Oeste (llena todo)
        main_frame.grid(row=0, column=0, sticky="nsew")
        
        # CONFIGURACIÓN DEL FRAME PRINCIPAL:
        # Hacemos que la columna 0 del frame sea elástica para que los Entry ocupen todo el ancho
        main_frame.columnconfigure(0, weight=1)

#=================================  
        # 0. Label
        # row=0: Primera fila
        # sticky="w": West (Oeste/Izquierda)
        ttk.Label(main_frame, text="0. Label: Soy una etiqueta con GRID", 
                  font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", pady=5)

#================================= 
        # 1. Entry
        ttk.Label(main_frame, text="1. Entry (Escribe algo):").grid(row=1, column=0, sticky="w")
        
        self.entrada = ttk.Entry(main_frame)
        # sticky="ew": East-West (Estírate a los lados)
        self.entrada.grid(row=2, column=0, sticky="ew", pady=5)

#================================= 
        # 2. Button
        ttk.Button(main_frame, text="2. Botón Simple (Imprimir Entry)", 
                   command=self.accion_boton).grid(row=3, column=0, sticky="ew", pady=5)

#================================= 
        # 3. Text Area
        ttk.Label(main_frame, text="3. Text Area (Multilínea):").grid(row=4, column=0, sticky="w")
        
        self.txt_area = scrolledtext.ScrolledText(main_frame, height=4, width=40)
        # sticky="ew": Solo a los anchos. Si quisieras que creciera hacia abajo también, sería "nsew"
        self.txt_area.grid(row=5, column=0, sticky="ew", pady=5)

#================================= 
        # 4. Radiobuttons (Selección Única)
        ttk.Label(main_frame, text="4. RadioButton (Ubicados en sub-grid):").grid(row=6, column=0, sticky="w")
        
        self.var_genero = tk.StringVar(value="X")
        
        # Creamos un sub-frame para organizar los radios uno al lado del otro
        frame_radio = ttk.Frame(main_frame)
        frame_radio.grid(row=7, column=0, sticky="w")
        
        # Dentro de este frame pequeño, usamos grid también:
        ttk.Radiobutton(frame_radio, text="Masculino", variable=self.var_genero, value="M").grid(row=0, column=0, padx=5)
        ttk.Radiobutton(frame_radio, text="Femenino", variable=self.var_genero, value="F").grid(row=0, column=1, padx=5)

#================================= 
        # 5 & 6. Checkbuttons
        ttk.Label(main_frame, text="6. Checkbox (Cada uno en su fila):").grid(row=8, column=0, sticky="w", pady=(10,0))
        
        self.var_condiciones = tk.BooleanVar()
        self.var_newsletter = tk.BooleanVar()
        
        # Fila 9 y Fila 10
        ttk.Checkbutton(main_frame, text="Acepto condiciones", 
                        variable=self.var_condiciones).grid(row=9, column=0, sticky="w")
                        
        ttk.Checkbutton(main_frame, text="Suscribirse al boletín", 
                        variable=self.var_newsletter).grid(row=10, column=0, sticky="w")

#================================= 
        # 7. Combobox
        ttk.Label(main_frame, text="7. Combobox (Lista):").grid(row=11, column=0, sticky="w", pady=(10,0))
        
        self.combo = ttk.Combobox(main_frame, values=["Costa Rica", "Panamá", "Nicaragua"], state="readonly")
        self.combo.current(0)
        self.combo.grid(row=12, column=0, sticky="ew") # sticky="ew" para que llene el ancho



    def accion_boton(self):
        info = self.entrada.get()
        print(f"Dato del Entry: {info}")

if __name__ == "__main__":
    app = MuestrarioWidgetsGrid()
    app.mainloop()