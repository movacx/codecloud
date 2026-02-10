import tkinter as FormularioGUI


class Formulario:
    def __init__(self, baseMainGUI):
        self.baseMainGUI = FormularioGUI.Toplevel(baseMainGUI)
        self.baseMainGUI.title("Huespedes Base")
        self.baseMainGUI.geometry("900x950")
        
        
        