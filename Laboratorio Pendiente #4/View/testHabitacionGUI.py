import tkinter as tk

class HabitacionGUI:
    def __init__(self, root, controller):
        self.manejoController = controller
        self.ventanaHabitacion = tk.Toplevel(root)
        self.ventanaHabitacion.geometry('2070,720')
        self.title('Registro Habitacion')