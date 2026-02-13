import tkinter as tkGUI
# Asegúrate de que estas importaciones funcionen en tu estructura de carpetas
from View.huespedesGUI import HuespedGUI 
from View.habitacionGUI import HabitacionGUI
from View.reservasGUI import ReservaGUI

class MainGUI:
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.ventanaPrincipal.title('Sistema Costamar')
        self.ventanaPrincipal.geometry('1060x780')
        self.ventanaPrincipal.configure(bg='skyblue')


        self.contenedor = tkGUI.Frame(self.ventanaPrincipal, padx=20, pady=20, bg='white', highlightbackground="gray", highlightthickness=1)
        self.contenedor.place(anchor='center', relx=0.5, rely=0.5)

        tkGUI.Button(self.contenedor, text='Habitación', font=('Arial', 14), width=25, 
                     command=lambda: HabitacionGUI(self.ventanaPrincipal)).grid(row=0, column=0, padx=10, pady=10, ipady=10)


        tkGUI.Button(self.contenedor, text='Reserva', font=('Arial', 14), width=25, 
                     command=lambda: ReservaGUI(self.ventanaPrincipal)).grid(row=0, column=1, padx=10, pady=10, ipady=10)


        tkGUI.Button(self.contenedor, text='Huéspedes', font=('Arial', 14), width=25, 
                     command=lambda: HuespedGUI(self.ventanaPrincipal)).grid(row=1, column=0, padx=10, pady=10, ipady=10)


        tkGUI.Button(self.contenedor, text='Reportes', font=('Arial', 14), width=25).grid(row=1, column=1, padx=10, pady=10, ipady=10)


    def crear_menu(self):
        pass

if __name__ == "__main__":
    root = tkGUI.Tk()
    app = MainGUI(root)
    root.mainloop()