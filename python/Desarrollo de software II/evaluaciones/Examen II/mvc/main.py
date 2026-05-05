import tkinter as tk
from Controller.calculadoraController import Controller

def main():
    root = tk.Tk()
    root.geometry('200x100')
    tk.Button(root, text = 'Abrir calculadora', command = lambda: Controller(root)).pack()
    root.mainloop()

if __name__ == '__main__':
    main()