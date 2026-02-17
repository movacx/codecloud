import tkinter as tkGUI
from Controller.fileHuespedController import HuespedController
from Controller.fileHabitacionController import HabitacionController
from Controller.fileReportesController import ReportesController
from Controller.fileReservacionController import ReservaController 
from View.fileReservasGUI import ReservaGUI

def main():
    try:
        root = tkGUI.Tk()
        root.geometry('500x550')
        root.title('Condominios Costa Mar')

        contenedor = tkGUI.Frame(root)
        contenedor.grid(row = 6, column =4 , columnspan= 2)

        tkGUI.Button(contenedor, text = 'Huesped', command = lambda: HuespedController(root)).grid(row = 0, column = 0)
        tkGUI.Button(contenedor, text = 'Reservas', command = lambda: ReservaController(root)).grid(row = 0, column = 1)
        tkGUI.Button(contenedor, text = 'Reportes', command = lambda: ReportesController(root)).grid(row = 1, column = 0)
        tkGUI.Button(contenedor, text = 'Habitacion', command = lambda: HabitacionController(root)).grid(row = 1, column = 1)

        root.mainloop()

    except Exception as error:
        print(f'Error: {error}')

if __name__ == "__main__":
    main()