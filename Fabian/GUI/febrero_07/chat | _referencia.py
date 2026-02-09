import tkinter as tkGUI

#===================================== [Establecer ventana] ================================
ventana = tkGUI.Tk()
ventana.title('UCR - Sistema de Gestión') # Título más profesional
ventana.geometry('600x700')
ventana.configure(bg="#2C3E50") 

#===================================== [LA SOLUCIÓN: Configurar la Cuadrícula] ================================
# Explicación: Estamos creando una cuadrícula de 3x3.
# Fila 0 y 2: Son "resortes" (weight=1). Empujan hacia el centro.
# Fila 1: Es donde vive tu contenido. No tiene weight, así que se ajusta a su tamaño.
# Lo mismo aplica para las columnas.

# 1. Configurar COLUMNAS (Eje X)
ventana.columnconfigure(0, weight=1) # Resorte Izquierdo
ventana.columnconfigure(1, weight=0) # CENTRO (Tu contenido va aquí, no se estira)
ventana.columnconfigure(2, weight=1) # Resorte Derecho

# 2. Configurar FILAS (Eje Y) - ¡Esto es lo que te faltaba!
ventana.rowconfigure(0, weight=1)    # Resorte Superior
ventana.rowconfigure(1, weight=0)    # CENTRO (Tu contenido va aquí)
ventana.rowconfigure(2, weight=1)    # Resorte Inferior

#===================================== [El Contenedor] ================================
# Ahora colocamos el contenedor en el centro exacto de la matriz (1, 1)
contenedor = tkGUI.Frame(ventana, bg="white", padx=20, pady=20) # Le puse color para que lo veas
# No usamos sticky. Dejamos que flote en el centro de su celda (1,1).
contenedor.grid(row=1, column=1)

#===================================== [Establecer etiquetas] ================================
tkGUI.Label(
    contenedor, 
    text='Banana Fruit Company', 
    font=('Arial', 14, 'bold'),
    bg="white", # Coincide con el frame
    fg="#2C3E50"
).grid(row=0, column=0)

#===================================== [Mostrar Panel] ================================
ventana.mainloop()