import tkinter as tk

class StoreGUI:
    def __init__(self, root, controller):
        self.controller = controller
        self.guiStore = tk.Toplevel(root)

        self.guiStore.title('Intelek')
        self.guiStore.geometry('1080x720')

        