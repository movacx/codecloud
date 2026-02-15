import tkinter as tkGUI
from Controller.fileHuespedController import HuespedController
from Controller.fileHabitacionController import HabitacionController
from Controller.fileReportesController import ReportesController

from View.fileReservasGUI import ReservaGUI

def main():

    root = tkGUI.Tk()
    root.geometry('600x300')
    root.title('Condominios Costa Mar')

    root.columnconfigure(0, weight = 0)
    root.columnconfigure(1, weight = 1)
    root.rowconfigure(0, weight = 1)
    root.configure(bg = 'white')

    contenedor = tkGUI.Frame(root)
    contenedor.grid(row = 0, column = 0, sticky = 'ns')

    contenedor.rowconfigure(0, weight = 1)
    contenedor.rowconfigure(1, weight = 1)
    contenedor.rowconfigure(2, weight = 1)
    contenedor.rowconfigure(3, weight = 1)

    tkGUI.Button(contenedor, text = 'Habitaciones', width = 10, command = lambda: HabitacionController(root)).grid(row = 0, column = 0, sticky = 'nswe' )
    tkGUI.Button(contenedor, text = 'Huesped', width = 10, command = lambda: HuespedController(root)).grid(row = 1, column = 0, sticky = 'nswe') #Completado
    tkGUI.Button(contenedor, text = 'Reservas', width = 10, command = lambda: ReservaGUI(root,None)).grid(row = 2, column = 0, sticky = 'nswe')  
    tkGUI.Button(contenedor, text = 'Reportes', width = 10, command = lambda: ReportesController(root)).grid(row = 3, column = 0, sticky = 'nswe') #Completado





    root.mainloop()



if __name__ == "__main__":
    main()