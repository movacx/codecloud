import tkinter as tkGUI




#===================================== [Establecer ventana] ================================
ventana = tkGUI.Tk()
ventana.title('UCR')
ventana.geometry('600x700')
ventana.configure(bg="#2C3E50") 

ventana.columnconfigure(0, weight = 1)
ventana.columnconfigure(1, weight = 0)
ventana.columnconfigure(2, weight = 1)

ventana.rowconfigure(0, weight = 1)
ventana.rowconfigure(1, weight = 0)
ventana.rowconfigure(2, weight = 1)


#===================================== [Declarar Contenedor] ================================
contenedor = tkGUI.Frame(ventana, bg="white", padx=20, pady=20)
contenedor.grid(row=1, column=1)


#===================================== [establecer etiquetas] ================================
tkGUI.Label(contenedor, text = 'Banana Fruit Company', font = ('Arial', 14), bg="white").grid(row=0,column=1,columnspan = 1)



usuariolbl = tkGUI.Label(contenedor, text = 'Usuario:', bg='white').grid(row=1,column=0,sticky='w')
contraseñalbl = tkGUI.Label(contenedor, text = 'Contraseña',bg='white').grid(row=2, column=0,sticky='w')


usuariotxt = tkGUI.Entry(contenedor).grid(row=1,column=1)
passwordtxt = tkGUI.Entry(contenedor).grid(row=2,column=1)

ingresarbtn = tkGUI.Button(contenedor,text='Ingresar').grid(row=3,column=0,columnspan = 2, pady = 10)



#===================================== [Mostrar Panel] ================================
ventana.mainloop()

