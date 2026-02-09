import tkinter as tkGUI

ventana = tkGUI.Tk()
#-----------------------------------------------------------------
ventana.geometry("650x300")
ventana.configure(bg="gray")
#-----------------------------------------------------------------
#Contenedor para los botones
contenedor= tkGUI.Frame(ventana)
contenedor.place(relx=0.5, rely=0.5, anchor="center")

#-----------------------------------------------------------------
#Etiquetas
tkGUI.Label(contenedor,bg="gray", text= "Registro Estudiantes", font= ("aptos display", 14)).grid(row=0,column=0)













ventana.mainloop()