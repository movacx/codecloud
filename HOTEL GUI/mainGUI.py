import tkinter as tkGUI
<<<<<<< HEAD

=======
>>>>>>> 2bc4fe4b873fdd712f3a884be7c43a6523a71e50
from View.huespedesGUI import HuespedGUI 
from View.habitacionGUI import HabitacionGUI
from View.reservasGUI import ReservaGUI

class MainGUI:
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.ventanaPrincipal.title('Sistema Costamar')
        self.ventanaPrincipal.geometry('1060x780')
        self.ventanaPrincipal.configure(bg='skyblue')

<<<<<<< HEAD
        # El contenedor se mantiene centrado
        self.contenedor = tkGUI.Frame(self.ventanaPrincipal, padx=20, pady=20, bg='white', highlightbackground="gray", highlightthickness=1)
        self.contenedor.place(anchor='center', relx=0.5, rely=0.5)
=======

contenedor = tkGUI.Frame(ventanaPrincipal, padx=20, pady=20, bg='white', highlightbackground="gray", highlightthickness=1)
contenedor.place(anchor='center', relx=0.5, rely=0.5)
>>>>>>> 2bc4fe4b873fdd712f3a884be7c43a6523a71e50

        self.crear_menu()

<<<<<<< HEAD
    def crear_menu(self):
        # Título del menú
        tkGUI.Label(self.contenedor, text='Sistema Costa Mar', font=('Arial', 18, 'bold'), bg='white').grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Botón Habitación
        tkGUI.Button(self.contenedor, text='Habitación', font=('Arial', 14), width=25, 
                     command=lambda: HabitacionGUI(self.ventanaPrincipal)).grid(row=1, column=0, padx=10, pady=10, ipady=10)

        # Botón Huéspedes
        tkGUI.Button(self.contenedor, text='Huéspedes', font=('Arial', 14), width=25, 
                     command=lambda: HuespedGUI(self.ventanaPrincipal)).grid(row=2, column=0, padx=10, pady=10, ipady=10)

        # Botón Reserva
        tkGUI.Button(self.contenedor, text='Reserva', font=('Arial', 14), width=25, 
                     command=lambda: ReservaGUI(self.ventanaPrincipal)).grid(row=1, column=1, padx=10, pady=10, ipady=10)
=======
# Boton Habitación
tkGUI.Button(contenedor, text='Habitación', font=('Arial', 14), width=25, 
             command=lambda: HabitacionGUI(ventanaPrincipal)).grid(row=1, column=0, padx=10, pady=10, ipady=10)

# Boton Huéspedes
tkGUI.Button(contenedor, text='Huéspedes', font=('Arial', 14), width=25, 
             command=lambda: HuespedGUI(ventanaPrincipal)).grid(row=2, column=0, padx=10, pady=10, ipady=10)

# Boton Reserva (Ahora con su comando)
tkGUI.Button(contenedor, text='Reserva', font=('Arial', 14), width=25, 
             command=lambda: ReservaGUI(ventanaPrincipal)).grid(row=1, column=1, padx=10, pady=10, ipady=10)

# Boton Reportes
tkGUI.Button(contenedor, text='Reportes', font=('Arial', 14), width=25).grid(row=2, column=1, padx=10, pady=10, ipady=10)
>>>>>>> 2bc4fe4b873fdd712f3a884be7c43a6523a71e50

        # Botón Reportes
        tkGUI.Button(self.contenedor, text='Reportes', font=('Arial', 14), width=25).grid(row=2, column=1, padx=10, pady=10, ipady=10)

if __name__ == "__main__":
    root = tkGUI.Tk()
    app = MainGUI(root)
    root.mainloop()