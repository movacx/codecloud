import tkinter as tkGUI
from tkinter import scrolledtext
from Controller.fileHuespedController import HuespedController
from Controller.fileHabitacionController import HabitacionController
from Controller.fileReportesController import ReportesController

from View.fileReservasGUI import ReservaGUI

def main():
    try:
        root = tkGUI.Tk()
        root.geometry('600x300')
        root.title('Condominios Costa Mar')

        root.columnconfigure(0, weight = 0)
        root.columnconfigure(1, weight = 1)
        root.rowconfigure(0, weight = 1)
        root.configure(bg = 'white')
        

        contenedor = tkGUI.Frame(root, bg = "#4b4242")
        contenedor.grid(row = 0, column = 0, sticky = 'ns')

        contenedor.rowconfigure(0, weight = 1)
        contenedor.rowconfigure(1, weight = 1)
        contenedor.rowconfigure(2, weight = 1)
        contenedor.rowconfigure(3, weight = 1)
        contenedor.rowconfigure(4, weight = 1)
        contenedor.rowconfigure(5, weight = 1)



        tkGUI.Button(contenedor, bd = 0, text = 'Habitaciones', width = 10, command = lambda: HabitacionController(root)).grid(row = 1, column = 0, sticky = 'nswe', pady = 5, padx = (5,5))
        tkGUI.Button(contenedor, bd = 0, text = 'Huesped', width = 10, command = lambda: HuespedController(root)).grid(row = 2, column = 0, sticky = 'nswe', pady = 5, padx = (5,5)) #Completado
        tkGUI.Button(contenedor, bd = 0, text = 'Reservas', width = 10, command = lambda: ReservaGUI(root,None)).grid(row = 3, column = 0, sticky = 'nswe', pady = 5, padx = (5,5))  
        tkGUI.Button(contenedor, bd = 0, text = 'Reportes', width = 10, command = lambda: ReportesController(root)).grid(row = 4, column = 0, sticky = 'nswe', pady = 5, padx = (5,5)) #Completado


        

        root.mainloop()

    except Exception as error:
        print(F'Error {error}')



if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print('Error {error}')
