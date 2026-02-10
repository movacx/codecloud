import tkinter as tkGUI
#Instancia
ventana = tkGUI.Tk()
#Creamos la ventana

#Definimos el tamaño
ventana.geometry("500x550")
#Definimos el titulo 
ventana.title("UCR")
#Definimos el color
ventana.configure(bg="sky blue")
#-----------------------------------------------------
#Se crea el contenedor el cual almacenara todo el login
contenedor = tkGUI.Frame(ventana, bg="white", padx=30, pady=20)
contenedor.place(relx=0.5, rely=0.5, anchor = "center")
contenedor.columnconfigure(0,weight=1)
contenedor.columnconfigure(1,weight=0)
#-----------------------------------------------------------------
#Etiquetas las cuales meteremos en el contenedor
tkGUI.Label(contenedor,bg=("white"), text = "Tienda inteleK", font= ("arial",14)).grid(row = 0, column=0, columnspan=2)
tkGUI.Label(contenedor,bg=("white"),text = "Usuario: " , font=("arial",14)).grid(row=1, column=0, sticky="w")
tkGUI.Label(contenedor,bg=("white"),text = "Contraseña: " , font=("arial",14)).grid(row=2, column=0, sticky="w")

#Hacemos los texField/Inpu
tkGUI.Entry(contenedor).grid(row=1,column=1)
tkGUI.Entry(contenedor).grid(row=2,column=1)

#Hacemos el boton
tkGUI.Button(contenedor, text="Ingresar").grid(row=3, column=0,columnspan=2, pady=10)




#Se llama el main loop para mostrar la ventana
ventana.mainloop()
