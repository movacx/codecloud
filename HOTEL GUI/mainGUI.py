import tkinter as tkGUI
from View.huespedesGUI import HuespedGUI 
from View.habitacionGUI import HabitacionGUI
from View.reservasGUI import ReservaGUI

ventanaPrincipal = tkGUI.Tk()
ventanaPrincipal.title('Sistema Costamar')
ventanaPrincipal.geometry('1060x780')
ventanaPrincipal.configure(bg='skyblue')


contenedor = tkGUI.Frame(ventanaPrincipal, padx=20, pady=20, bg='white', highlightbackground="gray", highlightthickness=1)
contenedor.place(anchor='center', relx=0.5, rely=0.5)

# Título del menú
tkGUI.Label(contenedor, text='Sistema Costa Mar', font=('Arial', 18, 'bold'), bg='white').grid(row=0, column=0, columnspan=2, pady=(0, 20))

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

ventanaPrincipal.mainloop()