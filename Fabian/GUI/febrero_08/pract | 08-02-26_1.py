import tkinter as tkGUI

ventana = tkGUI.Tk()
ventana.title('UCR')
ventana.geometry('600x400')
ventana.configure(bg='')

ventana.columnconfigure(0, weight = 1)
ventana.columnconfigure(1, weight = 0)
ventana.columnconfigure(2, weight = 1)

ventana.rowconfigure(0, weight = 1)
ventana.rowconfigure(1, weight = 0)
ventana.rowconfigure(2, weight = 1)


contenedor = tkGUI.Frame(ventana,bg='grey')
contenedor.grid(row=0,column=1)

#=====================[Configuracion de Columnas y FIlas]==========================
lbl = tkGUI.Label(contenedor, text = 'Bienvenido de nuevo').grid(row=0,column=0)



#=====================[ Ventana]==========================


#=====================[Mostrar Ventana]==========================
ventana.mainloop()

