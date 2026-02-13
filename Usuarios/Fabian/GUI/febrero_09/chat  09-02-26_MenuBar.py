import tkinter as tk

# 1. Crear la ventana
ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title("Mi Menú sin Funciones")

# ---------------------------------------------------------
# PASO 1: Crear la "Barra Maestra" (El riel horizontal)
# ---------------------------------------------------------
barra_principal = tk.Menu(ventana)

# ---------------------------------------------------------
# PASO 2: Crear el Menú "Archivo" (La lista desplegable)
# ---------------------------------------------------------
# tearoff=0 es vital: quita una línea punteada fea que viene por defecto
menu_archivo = tk.Menu(barra_principal, tearoff=0)

# Agregamos las opciones DENTRO de "menu_archivo"
menu_archivo.add_command(label="Nuevo Proyecto")
menu_archivo.add_command(label="Abrir...")
menu_archivo.add_separator()  # Una línea gris para separar
menu_archivo.add_command(label="Salir", command=ventana.destroy) # Cierra la app

# ---------------------------------------------------------
# PASO 3: Crear el Menú "Ayuda" (Otra lista desplegable)
# ---------------------------------------------------------
menu_ayuda = tk.Menu(barra_principal, tearoff=0)

# Agregamos opciones DENTRO de "menu_ayuda"
menu_ayuda.add_command(label="Manual de Usuario")
menu_ayuda.add_command(label="Acerca de...")

# ---------------------------------------------------------
# PASO 4: "Colgar" los menús en la Barra Principal
# ---------------------------------------------------------
# Usamos .add_cascade para decir "Este menú cuelga de esta etiqueta"
barra_principal.add_cascade(label="Archivo", menu=menu_archivo)
barra_principal.add_cascade(label="Ayuda", menu=menu_ayuda)

# ---------------------------------------------------------
# PASO 5: ¡CRUCIAL! Decirle a la ventana que use esa barra
# ---------------------------------------------------------
ventana.config(menu=barra_principal)

ventana.mainloop()