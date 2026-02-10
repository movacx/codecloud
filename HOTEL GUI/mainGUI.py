import tkinter as tkGUI

ventanaPrincipal = tkGUI.Tk()

ventanaPrincipal.title('Sistema Costamar')

ventanaPrincipal.geometry('1060x780')
ventanaPrincipal.configure(bg='blue')

contenedor = tkGUI.Frame(ventanaPrincipal, padx = 10, pady = 10)
contenedor.place(anchor='center',relx = 0.5, rely = 0.5)

tkGUI.Label(contenedor, text = 'Sistema Costa Mar', font = ('Arial',14), width = 30).grid(row=0,column=0, columnspan = 2)
tkGUI.Button(contenedor, text = 'Habitacion', font = ('Arial',14), width = 30).grid(row=1,column=0, sticky = 'w', ipady = 10)
tkGUI.Button(contenedor, text = 'Huespedes', font = ('Arial',14), width = 30).grid(row=2,column=0, sticky = 'w', ipady = 10)
tkGUI.Button(contenedor, text = 'Reserva', font = ('Arial',14), width = 30).grid(row=1,column=1, sticky = 'w', ipady = 10)
tkGUI.Button(contenedor, text = 'Reportes', font = ('Arial',14), width = 30).grid(row=2,column=1, sticky = 'w', ipady = 10)


ventanaPrincipal.mainloop()