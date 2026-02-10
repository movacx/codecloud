import tkinter as tk # Lo estándar es usar 'tk'
from tkinter import ttk
from tkinter import messagebox

class HabitacionGUI:
    def __init__(self, baseMainGUI):
        self.ventana_hija = tk.Toplevel(baseMainGUI)
        self.ventana_hija.title("Sistema Habitación")
        self.ventana_hija.geometry("300x250")
        
        self.frame_form = tk.Frame(self.ventana_hija)
        self.frame_form.grid(row=0, column=0, padx=10, pady=10)
        
        self.formularioCrear()
        
    def formularioCrear(self):
        tk.Label(self.frame_form, text="Etiqueta").grid(row=0, column=0)
        self.campoText = tk.Entry(self.frame_form)
        self.campoText.grid(row=0, column=1)
        
if __name__ == "__main__":     
    root = tk.Tk()
    root.title("Ventana Principal")
    app = HabitacionGUI(root)
    root.mainloop()