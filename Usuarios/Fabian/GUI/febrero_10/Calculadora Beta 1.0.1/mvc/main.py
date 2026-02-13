import tkinter as tk
from Controller.calculadoraController import Controller

def main():
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()

if __name__ == "__main__":
    main()
