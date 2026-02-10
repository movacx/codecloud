import tkinter as tkGUI
from tkinter import scrolledtext as textArea


#===============[Ventana principal]==================#
ventana = tkGUI.Tk()
ventana.title('calculadora')
ventana.geometry('359x600')
ventana.configure(bg='beige')


#==========[Contenedor de PanelPrincipal]==============#
panel = tkGUI.Frame(ventana)
panel.place(anchor = 'center', relx = 0.50, rely=0.50)


#=============[Contenedor de Botones]==================#
calculadora = tkGUI.Frame(panel)
calculadora.grid(row=2, column = 0, sticky = 'w')


#=============[SubContenedor]==================#
micro_contenedor = tkGUI.Frame(calculadora)
micro_contenedor.grid(row = 0, column = 0)

contenedor = tkGUI.Frame(calculadora)
contenedor.grid(row = 1, column = 0, sticky = 'w')

caracteres = tkGUI.Frame(calculadora)
caracteres.grid(row = 0, column = 1)

nuevo_contenedor = tkGUI.Frame(calculadora)
nuevo_contenedor.grid(row=0, column = 2)

#Variables
font_sans = font = ('Open Sans Extrabold',14)

# #=========================================[Historial]=====================================================
textArea.ScrolledText(panel, height = 15,width = 40, bg= 'dimgray').grid(row=0,column=0,sticky='ew')



# #=========================================[Barra de texto]===============================================
barra_text =  tkGUI.Entry(panel, width = 1)
barra_text.grid(row=1,column=0,sticky='ew',ipady=8, padx = 5)


# #==========================================[Botones]=====================================================
tkGUI.Button(micro_contenedor, text = 'C', font = font_sans, width = 3).grid(row = 0, column = 0, sticky='w', padx = 5, ipady = 1, pady = 5)
tkGUI.Button(micro_contenedor, text = 'C', font = font_sans, width = 3).grid(row = 0, column = 1, sticky='w', padx = 5, ipady = 1)
tkGUI.Button(micro_contenedor, text = 'C', font = font_sans, width = 3).grid(row = 0, column = 2, sticky='w', padx = 5, ipady = 1)


tkGUI.Button(micro_contenedor, text = '7', font = font_sans, width = 3).grid(row = 1, column = 0, sticky='w', padx = 5, ipady = 1, pady = 5)
tkGUI.Button(micro_contenedor, text = '8', font = font_sans, width = 3).grid(row = 1, column = 1, sticky='w', padx = 5, ipady = 1)
tkGUI.Button(micro_contenedor, text = '9', font = font_sans, width = 3).grid(row = 1, column = 2, sticky='w', padx = 5, ipady = 1)


tkGUI.Button(micro_contenedor, text = '4', font = font_sans, width = 3).grid(row = 2, column = 0, sticky='w', padx = 5, ipady = 1, pady = 5)
tkGUI.Button(micro_contenedor, text = '5', font = font_sans, width = 3).grid(row = 2, column = 1, sticky='w', padx = 5, ipady = 1)
tkGUI.Button(micro_contenedor, text = '6', font = font_sans, width = 3).grid(row = 2, column = 2, sticky='w', padx = 5, ipady = 1)


tkGUI.Button(micro_contenedor, text = '1', font = font_sans, width = 3).grid(row = 3, column = 0, sticky='w', padx = 5, ipady = 1, pady = 5)
tkGUI.Button(micro_contenedor, text = '2', font = font_sans, width = 3).grid(row = 3, column = 1, sticky='w', padx = 5, ipady = 1)
tkGUI.Button(micro_contenedor, text = '3', font = font_sans, width = 3).grid(row = 3, column = 2, sticky='w', padx = 5, ipady = 1)


tkGUI.Button(caracteres, text = '(+)', font = font_sans, width = 3).grid(row = 0, column = 0, sticky='w', padx = 5, ipady = 1, pady = 5)
tkGUI.Button(caracteres, text = '(-)', font = font_sans, width = 3).grid(row = 1, column = 0, sticky='w', padx = 5, ipady = 1, pady = 5)
tkGUI.Button(caracteres, text = '(x)', font = font_sans, width = 3).grid(row = 2, column = 0, sticky='w', padx = 5, ipady = 1, pady = 5)
tkGUI.Button(caracteres, text = '(÷)', font = font_sans, width = 3).grid(row = 3, column = 0, sticky='w', padx = 5, ipady = 1, pady = 5)

tkGUI.Button(contenedor, text = '0', font = font_sans, width = 10).grid(row = 0, column = 0, sticky='w', padx = 5, pady = 5, ipady = 3)
tkGUI.Button(contenedor, text = '.', font = font_sans, width = 3).grid(row = 0, column = 1, sticky= 'w', padx = 5, pady = 5, ipady = 3)

tkGUI.Button(nuevo_contenedor, text = '(=)', font = font_sans, width = 3).grid(row = 0, column = 0, sticky= 'w', padx = 5, pady = 5, ipady = 80)







#Mostrar la ventana
ventana.mainloop()

# def _crear_menu_bar(self):
#     barra_menu = tk.Menu(self)
#     self.config(menu=barra_menu)
#     menu_archivo = tk.Menu(barra_menu, tearoff=0)
#     menu_archivo.add_command(label="Nuevo")
#     menu_archivo.add_separator()
#     menu_archivo.add_command(label="Salir", command=self.quit)
#     barra_menu.add_cascade(label="8. Menú", menu=menu_archivo)