import tkinter as tkGUI
#Instancia
ventana = tkGUI.Tk()
#Creamos la ventana
ventana.geometry("650x300")
ventana.title("UCR")
ventana.configure(bg="sky blue")
#----------------------------------------------------------------------------------------------------------------------
#Creamos un contenedor para los botones 
contenedor= tkGUI.Frame(ventana,bg="sky blue")
contenedor.grid(row=5, column=1,columnspan=2)
#Configuracion de columnas
ventana.columnconfigure(0,weight=0)
ventana.columnconfigure(1,weight=1)
#----------------------------------------------------------------------------------------------------------------------
#Etiquetas
tkGUI.Label(ventana,bg="sky blue", text = "Registro Estudiante", font= ("aptos display",14)).grid(row= 0, column= 0,columnspan=2)
tkGUI.Label(ventana,bg="sky blue", text = "Nombre: ", font=("Britannic Bold", 14)).grid(row=1, column=0, sticky="w")
tkGUI.Label(ventana,bg="sky blue", text = "Apellidos: ", font=("Britannic Bold", 14)).grid(row=2,column=0, sticky = "w")
tkGUI.Label(ventana,bg="sky blue", text = "Carnet: ", font=("Britannic Bold", 14)).grid(row=3,column=0, sticky = "w")
tkGUI.Label(ventana,bg="sky blue", text = "Promedio: ", font=("Britannic Bold", 14)).grid(row=4,column=0, sticky = "w")
#----------------------------------------------------------------------------------------------------------------------
#TextField/Input
tkGUI.Entry(ventana).grid(row=1, column= 1, sticky="ew",padx=(1,20), ipady=3, pady= 5)
tkGUI.Entry(ventana).grid(row=2, column=1, sticky="ew",padx=(1,20), ipady=3, pady= 5)
tkGUI.Entry(ventana).grid(row=3, column=1, sticky="ew",padx=(1,20), ipady=3, pady= 5)
tkGUI.Entry(ventana).grid(row=4, column=1, sticky="ew",padx=(1,20), ipady=3, pady= 5)
#----------------------------------------------------------------------------------------------------------------------
#Botones
tkGUI.Button(contenedor, bg="#9A5BCD", text = "Guardar",width=8).grid(row=1, column=0,padx=5)
tkGUI.Button(contenedor, bg="#9A5BCD", text = "Buscar",width=8).grid(row=1,column=1,padx = 5)
tkGUI.Button(contenedor, bg="#9A5BCD", text = "Modificar",width=8).grid(row=1,column=2,padx = 5)
tkGUI.Button(contenedor, bg="#9A5BCD", text = "Eliminar",width=8).grid(row=1,column=3,padx = 5)
tkGUI.Button(contenedor, bg="#9A5BCD", text = "Limpiar",width=8).grid(row=1,column=4,padx = 5)
tkGUI.Button(contenedor, bg="#9A5BCD", text = "Salir",width=8).grid(row=1,column=5,padx = 5)



ventana.mainloop()

