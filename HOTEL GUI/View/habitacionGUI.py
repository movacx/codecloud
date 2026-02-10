import tkinter as tk 

class HabitacionGUI:
    def __init__(self, baseMainGUI):
        
        self.baseMainGUI = tk.Toplevel(baseMainGUI)
        self.baseMainGUI.title("Habitacion Base")
        self.baseMainGUI.geometry("300x250")