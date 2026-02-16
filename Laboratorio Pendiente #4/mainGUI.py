import tkinter as tkGUI
from Controller.fileHuespedController import HuespedController
from Controller.fileHabitacionController import HabitacionController as controllerDavid
from Controller.fileReportesController import ReportesController
from View.fileReservasGUI import ReservaGUI

def main():
    try:
        root = tkGUI.Tk()
        root.geometry('600x300')
        root.title('Condominios Costa Mar')

        contenedor = tkGUI.Frame(root)
        contenedor.grid(row = 0, column = 0)

        tkGUI.Button(contenedor, text = 'Huesped', command = lambda: HuespedController(root)).grid(row = 0, column = 0)
        tkGUI.Button(contenedor, text = 'Reservas', command = lambda: ReservaGUI(root,None)).grid(row = 1, column = 0)
        tkGUI.Button(contenedor, text = 'Reportes', command = lambda: ReportesController(root)).grid(row = 2, column = 0)
        tkGUI.Button(contenedor, text = 'Test Habitacion', command = lambda: controllerDavid(root)).grid(row = 3, column = 0)

        root.mainloop()

    except Exception as error:
        print(f'Error: {error}')

if __name__ == "__main__":
    main()