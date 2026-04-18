import tkinter as tk
from tkinter import scrolledtext as textArea


#Variables GLOBALES
font_sans = font = ('Open Sans Extrabold',14)

class calculadora:
    
    #Constructor
    def __init__(self, ventana_padre, controlador):
        self.controller = controlador
        #============ [Establecer ventana] =================
        self.ventana_calculadora = ventana_padre
        self.ventana_calculadora.title('Calculadora')
        self.ventana_calculadora.geometry('359x600')
        self.ventana_calculadora.configure(bg='beige')

        #============ [Contenedor] =====================
        self.contenedor = tk.Frame(self.ventana_calculadora)
        self.contenedor.place(anchor = 'center', relx = 0.5, rely = 0.5)

        self.panelCalculadora = tk.Frame(self.contenedor)
        self.panelCalculadora.grid(row=2,column=0,sticky = 'w')

        #=========== [SubContenedoresBotones] ===========
        self.padsNumericos = tk.Frame(self.panelCalculadora)
        self.padsNumericos.grid(row = 0, column = 0)

        self.ultimaFila = tk.Frame(self.panelCalculadora)
        self.ultimaFila.grid(row = 1, column = 0, sticky = 'w')

        self.caracteresDerecha = tk.Frame(self.panelCalculadora)
        self.caracteresDerecha.grid(row = 0, column = 1)

        self.ultimaColumna = tk.Frame(self.panelCalculadora)
        self.ultimaColumna.grid(row=0, column = 2)

        self.pantalla()
        self.pad()


    def pantalla(self):
        #Establecer TextArea
        self.pantalla_historial = textArea.ScrolledText(self.contenedor, height = 15, width = 40, bg= 'dimgray')
        self.pantalla_historial.grid(row=0, column=0, sticky='ew')
        self.pantalla_historial.config(state='disabled') 

        
        self.input_texto = tk.Entry(self.contenedor, width = 1)
        self.input_texto.grid(row=1, column=0, sticky='ew', ipady=8, padx = 5)
        self.input_texto.config(state = 'disabled')

    def pad(self):

        #============ [Botones] =====================
        tk.Button(self.padsNumericos, text = 'C', font = font_sans, width = 3, command = lambda: self.controller.recibirMatch('C') ).grid(row = 0, column = 0, sticky='w', padx = 5, ipady = 1, pady = 5)
        tk.Button(self.padsNumericos, text = 'C', font = font_sans, width = 3, command = lambda: self.controller.recibirMatch('C') ).grid(row = 0, column = 1, sticky='w', padx = 5, ipady = 1)
        tk.Button(self.padsNumericos, text = 'C', font = font_sans, width = 3, command = lambda: self.controller.recibirMatch('C') ).grid(row = 0, column = 2, sticky='w', padx = 5, ipady = 1)

        tk.Button(self.padsNumericos, text = '7', font = font_sans, width = 3, command = lambda: self.controller.recibirNumero('7')).grid(row = 1, column = 0, sticky='w', padx = 5, ipady = 1, pady = 5)
        tk.Button(self.padsNumericos, text = '8', font = font_sans, width = 3, command = lambda: self.controller.recibirNumero('8')).grid(row = 1, column = 1, sticky='w', padx = 5, ipady = 1)
        tk.Button(self.padsNumericos, text = '9', font = font_sans, width = 3, command = lambda: self.controller.recibirNumero('9')).grid(row = 1, column = 2, sticky='w', padx = 5, ipady = 1)

        tk.Button(self.padsNumericos, text = '4', font = font_sans, width = 3, command = lambda: self.controller.recibirNumero('4')).grid(row = 2, column = 0, sticky='w', padx = 5, ipady = 1, pady = 5)
        tk.Button(self.padsNumericos, text = '5', font = font_sans, width = 3, command = lambda: self.controller.recibirNumero('5')).grid(row = 2, column = 1, sticky='w', padx = 5, ipady = 1)
        tk.Button(self.padsNumericos, text = '6', font = font_sans, width = 3, command = lambda: self.controller.recibirNumero('6')).grid(row = 2, column = 2, sticky='w', padx = 5, ipady = 1)

        tk.Button(self.padsNumericos, text = '1', font = font_sans, width = 3, command = lambda: self.controller.recibirNumero('1')).grid(row = 3, column = 0, sticky='w', padx = 5, ipady = 1, pady = 5)
        tk.Button(self.padsNumericos, text = '2', font = font_sans, width = 3, command = lambda: self.controller.recibirNumero('2')).grid(row = 3, column = 1, sticky='w', padx = 5, ipady = 1)
        tk.Button(self.padsNumericos, text = '3', font = font_sans, width = 3, command = lambda: self.controller.recibirNumero('3')).grid(row = 3, column = 2, sticky='w', padx = 5, ipady = 1)

        tk.Button(self.caracteresDerecha, text = '(+)', font = font_sans, width = 3, command = lambda: self.controller.recibirMatch('+')).grid(row = 0, column = 0, sticky='w', padx = 5, ipady = 1, pady = 5)
        tk.Button(self.caracteresDerecha, text = '(-)', font = font_sans, width = 3, command = lambda: self.controller.recibirMatch('-')).grid(row = 1, column = 0, sticky='w', padx = 5, ipady = 1, pady = 5)
        tk.Button(self.caracteresDerecha, text = '(x)', font = font_sans, width = 3, command = lambda: self.controller.recibirMatch('*')).grid(row = 2, column = 0, sticky='w', padx = 5, ipady = 1, pady = 5)
        tk.Button(self.caracteresDerecha, text = '(÷)', font = font_sans, width = 3, command = lambda: self.controller.recibirMatch('/')).grid(row = 3, column = 0, sticky='w', padx = 5, ipady = 1, pady = 5)

        tk.Button(self.ultimaFila, text = '0', font = font_sans, width = 10, command = lambda: self.controller.recibirNumero('0')).grid(row = 0, column = 0, sticky='w', padx = 5, pady = 5, ipady = 3)
        tk.Button(self.ultimaFila, text = '.', font = font_sans, width = 3).grid(row = 0, column = 1, sticky= 'w', padx = 5, pady = 5, ipady = 3)
        tk.Button(self.ultimaColumna, text = '(=)', font = font_sans, width = 3, command = lambda: self.controller.recibirMatch('=') ).grid(row = 0, column = 0, sticky= 'w', padx = 5, pady = 5, ipady = 80)


    def actualizar_pantalla(self, texto):
        self.input_texto.config(state = 'normal')
        self.input_texto.delete(0, tk.END)
        self.input_texto.insert(0, texto)
        self.input_texto.config(state = 'readonly') #Nota: Es casi que lo mismo que disabled sinembargo la diferencia es que readonly bloquea el campo de texto pero no lo pone gris.

    def agregar_al_historial(self, texto):
        # 1. DESBLOQUEAR
        self.pantalla_historial.config(state='normal')
        
        self.pantalla_historial.insert(tk.END, texto + "\n")
        self.pantalla_historial.see(tk.END)
        
        # 3. BLOQUEAR OTRA VEZ
        self.pantalla_historial.config(state='disabled')