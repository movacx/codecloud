import tkinter as tkGUI

# --- CONFIGURACIÓN DE LA VENTANA (La Pared) ---
ventana = tkGUI.Tk()
ventana.title('UCR - Login')
ventana.geometry('400x300')
ventana.configure(bg="#2C3E50") 

# Centramos el contenedor usando .place (Más limpio para ventanas de login únicas)
contenedor = tkGUI.Frame(ventana, bg="white", padx=20, pady=20)
contenedor.place(relx=0.5, rely=0.5, anchor='center')

# --- CONFIGURACIÓN DEL CONTENIDO (El Cuadro) ---
# Aquí es donde aplicamos tu lógica de columnspan

#===================================== [Declarar Contenedor] ================================
lbl_titulo = tkGUI.Label(contenedor, text='Banana Fruit Co.', font=('Arial', 14, 'bold'), bg="white")
lbl_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 15)) # <--- ¡AQUÍ ESTÁ!

#===================================== [establecer etiquetas] ================================
tkGUI.Label(contenedor, text='Usuario:', bg="white").grid(row=1, column=0, sticky='e')
tkGUI.Label(contenedor, text='Clave:', bg="white").grid(row=2, column=0, sticky='e')

#===================================== [establecer inputs] ================================
txtUsuario = tkGUI.Entry(contenedor).grid(row=1, column=1, padx=5, pady=5)
txtPassword = tkGUI.Entry(contenedor, show="*").grid(row=2, column=1, padx=5, pady=5)

# Fila 3: Botón (Ocupa las 2 columnas para verse lleno)
btn_login = tkGUI.Button(contenedor, text='Ingresar', bg="#2C3E50", fg="white")
btn_login.grid(row=3, column=0, columnspan=2, sticky='we', pady=(15, 0)) # <--- ¡AQUÍ TAMBIÉN!




ventana.mainloop()