import tkinter as tkGUI

#====================Definir ventana ==========================
ventana = tkGUI.Tk()
ventana.title('Ventana')
ventana.geometry('800x800')


#======== Keeps =================#
# tkGUI.Label(ventana, text = "etiqueta).grid(row=1, column =0, padx =5, pady= 5) ==> Label

# datoA = tkGUI.Entry(ventana) ==> TextField
# datoA.grid(row=1, column = 1, padx =5, pady= 5)

#====================Definir Etiquetas ==========================                     

titulolbl = tkGUI.Label(ventana, text = 'Manejo Estudiante', font=('Times New Roman',20))


#====================Definir Posicion ============================
titulolbl.grid(row=0, column = 7, padx = 5, pady = 5) #fila=0, columna=0, largo=55, alto=100



#=== Pie de ventana ===#
ventana.mainloop()