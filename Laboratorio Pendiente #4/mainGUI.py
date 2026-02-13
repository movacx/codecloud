import tkinter as tkGUI
# Asegúrate de que estas importaciones funcionen en tu estructura de carpetas
from View.huespedesGUI import HuespedGUI 
from View.habitacionGUI import HabitacionGUI
from View.reservasGUI import ReservaGUI

class MainGUI:
    def __init__(self, ventanaPrincipal):
        # 1. Configuración de la Ventana Principal
        self.ventanaPrincipal = ventanaPrincipal
        self.ventanaPrincipal.title('Sistema Costamar')
        self.ventanaPrincipal.geometry('1060x780')
        self.ventanaPrincipal.configure(bg='skyblue')

        # 2. Creación del Contenedor Central
        # Usamos 'self.contenedor' para que sea accesible en toda la clase si hace falta
        self.contenedor = tkGUI.Frame(self.ventanaPrincipal, padx=20, pady=20, bg='white', highlightbackground="gray", highlightthickness=1)
        self.contenedor.place(anchor='center', relx=0.5, rely=0.5)

        # 3. Llamada al menú 
        # (He comentado esto porque no has definido la función crear_menu en este código)
        # self.crear_menu()

        # 4. Botones del Menú Principal
        # Fíjate que ahora el padre es self.contenedor y pasamos self.ventanaPrincipal en los comandos
        
        # Fila 0, Columna 0: Habitación
        tkGUI.Button(self.contenedor, text='Habitación', font=('Arial', 14), width=25, 
                     command=lambda: HabitacionGUI(self.ventanaPrincipal)).grid(row=0, column=0, padx=10, pady=10, ipady=10)

        # Fila 0, Columna 1: Reserva
        tkGUI.Button(self.contenedor, text='Reserva', font=('Arial', 14), width=25, 
                     command=lambda: ReservaGUI(self.ventanaPrincipal)).grid(row=0, column=1, padx=10, pady=10, ipady=10)

        # Fila 1, Columna 0: Huéspedes
        tkGUI.Button(self.contenedor, text='Huéspedes', font=('Arial', 14), width=25, 
                     command=lambda: HuespedGUI(self.ventanaPrincipal)).grid(row=1, column=0, padx=10, pady=10, ipady=10)

        # Fila 1, Columna 1: Reportes
        tkGUI.Button(self.contenedor, text='Reportes', font=('Arial', 14), width=25).grid(row=1, column=1, padx=10, pady=10, ipady=10)

    # Si vas a usar self.crear_menu(), necesitas definirlo aquí dentro de la clase:
    def crear_menu(self):
        pass

if __name__ == "__main__":
    root = tkGUI.Tk()
    app = MainGUI(root)
    root.mainloop()