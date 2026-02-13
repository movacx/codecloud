import tkinter as tkGUI
from Controller.fileHuespedController import HuespedController
from Controller.fileHabitacionController import HabitacionController
def main():
    root = tkGUI.Tk() #VENTANA PADRE MAIN LA CUAL SE VA A DISTRIBUIR A LOS HIJOS -> HABITACION,HUESPED,REPORTES,RESERVAS
    
    root.title('Sistema Costamar')
    root.geometry('1060x780')
    root.configure(bg='skyblue')
    

    contenedor = tkGUI.Frame(root, padx=20, pady=20, bg='white', highlightbackground="gray", highlightthickness=1)
    contenedor.place(anchor='center', relx=0.5, rely=0.5)

    tkGUI.Button(contenedor, text='Huéspedes', font=('Arial', 14), width=25, command = lambda: HuespedController(root)).grid(row=1, column=0, padx=10, pady=10, ipady=10)
    tkGUI.Button(contenedor, text='Reportes', font=('Arial', 14), width=25).grid(row=1, column=1, padx=10, pady=10, ipady=10)
    tkGUI.Button(contenedor, text='Habitaciones', font=('Arial', 14), width=25, command = lambda: HabitacionController(root)).grid(row=2, column=0, padx=10, pady=10, ipady=10)




    root.mainloop()



if __name__ == "__main__":
    main()