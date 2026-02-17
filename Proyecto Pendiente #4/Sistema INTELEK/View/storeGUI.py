import tkinter as tkGUI

class Tienda:
    def __init__(self, root, controller):
        self.controller = controller
        self.ventana = tkGUI.Toplevel(root)
        self.ventana.title('Intelek')
        self.ventana.geometry("1100x700")

        self.ventana.columnconfigure(0, weight = 0)
        self.ventana.columnconfigure(1, weight = 1)
        self.ventana.rowconfigure(0, weight = 1)
        self.ventana.configure(bg = 'white')

        contenedor = tkGUI.Frame(self.ventana, bg = "#4b4242")
        contenedor.grid(row = 0, column = 0, sticky = 'ns')
        contenedor.rowconfigure(0, weight = 1)
        contenedor.rowconfigure(1, weight = 1)
        contenedor.rowconfigure(2, weight = 1)
        contenedor.rowconfigure(3, weight = 1)
        contenedor.rowconfigure(4, weight = 1)
        contenedor.rowconfigure(5, weight = 1)
        contenedor.rowconfigure(6, weight = 1)

        tkGUI.Button(contenedor, bd = 0, text = 'btn1', width = 10).grid(row = 1, column = 0, sticky = 'nswe', pady = 5, padx = (5,5))
        tkGUI.Button(contenedor, bd = 0, text = 'btn2', width = 10).grid(row = 2, column = 0, sticky = 'nswe', pady = 5, padx = (5,5))
        tkGUI.Button(contenedor, bd = 0, text = 'btn3', width = 10).grid(row = 3, column = 0, sticky = 'nswe', pady = 5, padx = (5,5))
        tkGUI.Button(contenedor, bd = 0, text = 'btn3').grid(row = 4, column = 0, sticky = 'nswe', pady = 5, padx = (5,5))

def main():
    root = tkGUI.Tk()
    app = Tienda(root, None)
    root.mainloop()

if __name__ == '__main__':
    main()