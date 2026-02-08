import tkinter as tkGUI

#===================================== [Establecer ventana] ================================
ventana = tkGUI.Tk()
ventana.title()
ventana.geometry('600x700')

contenedor = tkGUI.Frame(ventana)
contenedor.grid(row=1, column = 1, columnspan = 2, padx = 5)
#===================================== [Configurar columnas] ================================
ventana.columnconfigure(0,0)

#===================================== [Configurar columnas] ================================


#===================================== [Mostrar Panel] ================================
ventana.mainloop()

