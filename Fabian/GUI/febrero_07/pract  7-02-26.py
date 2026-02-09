import tkinter as tkGUI
#================================= [ Establecer la ventana ] #================================= 
ventana = tkGUI.Tk()
ventana.title('UCR')
ventana.geometry('750x350')

#================================= [ Establecer panel ] #================================= 
panel = tkGUI.Frame(ventana)
panel.grid(row=6,column=0, columnspan=2)

#================================= [ Configuracion de columnas ] #================================= 
ventana.columnconfigure(0, weight = 0)
ventana.columnconfigure(1, weight = 1)

#================================= [ Configuracion del titulo ] #================================= 
tkGUI.Label(ventana, text = 'Registro Estudiantes', font = ('Arial', 14)).grid(row = 0, column = 0, columnspan = 2, sticky = 'ew', pady = 20)

#================================= [ Configuracion de labels ] #================================= 
tkGUI.Label(ventana, text = 'Nombre:', font = ('Arial', 14)).grid(row = 1, column = 0, sticky = 'w', padx = 10)
tkGUI.Label(ventana, text = 'Apellido:', font = ('Arial', 14)).grid(row = 2, column = 0, sticky = 'w', padx = 10, pady = 15)
tkGUI.Label(ventana, text = 'Carnet', font = ('Arial',14)).grid(row=3, column = 0, sticky ='w', padx = 10)
tkGUI.Label(ventana, text = 'Promedio', font = ('Arial',14)).grid(row=4,column=0,sticky='w',padx=10, pady = 15)
#================================= [ Configuracion de inputs] #================================= 

nombre_txt = tkGUI.Entry(ventana, width = 40)
nombre_txt.grid(row =1, column = 1, sticky = 'ew', ipady = 5, padx = (1,100))
#
apellido_txt = tkGUI.Entry(ventana, width = 40)
apellido_txt.grid(row = 2, column = 1,  sticky = 'ew', ipady = 5, padx = (1,100))
#
carnet_txt = tkGUI.Entry(ventana, width = 40)    
carnet_txt.grid(row = 3, column = 1, sticky = 'ew', ipady = 5, padx = (1,100))
#
promedio_txt = tkGUI.Entry(ventana, width = 40)
promedio_txt.grid(row=4,column=1,sticky='ew',ipady=5, padx = (1,100))

#================================= [ Configuracion de botones] #=================================

guardar_btn = tkGUI.Button(panel, text = 'Guardar', width = 10).grid(row = 0, column = 0, padx = 5)
buscar_btn = tkGUI.Button(panel, text = 'Buscar', width = 10).grid(row=0,column=1, padx = 5)
modificar_btn = tkGUI.Button(panel, text = 'Modificar', width = 10).grid(row=0,column=2,sticky='ew', padx = 5)
elimminar_btn = tkGUI.Button(panel, text = 'Eliminar', width = 0).grid(row=0,column=3,sticky='ew', padx = 5)
limpiar_btn = tkGUI.Button(panel,text='Limpiar', width = 10).grid(row=0,column=4,sticky='ew', padx = 5)
salir_btn = tkGUI.Button(panel, text = 'Salir', width = 10).grid(row=0,column=5,sticky='ew', padx = 5)

#================================= [ Mostrar la ventana ] #================================= 
ventana.mainloop()


