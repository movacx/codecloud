import tkinter as tkGUI

ventana = tkGUI.Tk()
ventana.geometry('600x600')
ventana.configure(bg='black')

contenedor = tkGUI.Frame(ventana, bg = 'white')
contenedor.place(anchor = 'center', relx = 0.5, rely = 0.5)

tkGUI.Label(contenedor, text='UNiversidad de costa rica:', font = ('Arial',14), bg='white').grid(column = 0, row = 0, columnspan = 2)
tkGUI.Label(contenedor, text='Nombre:', font = ('Arial',14), bg='white').grid(column = 0, row = 2, sticky = 'w')
tkGUI.Label(contenedor, text = 'Apellido:',bg='white').grid(column = 0, row = 2, sticky = 'w')

tkGUI.Entry(contenedor).grid(column = 1, row = 1, sticky = 'w')
tkGUI.Entry(contenedor).grid(column = 1, row = 2, sticky = 'w')
ventana.mainloop()