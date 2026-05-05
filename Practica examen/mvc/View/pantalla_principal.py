import tkinter as tk

class Cargador:
    def __init__(self, root, persona,recurso,asignacion):
        self.ventana = root
        botonPersona = tk.Button(self.ventana, text = 'Persona', command = persona)
        botonPersona.pack()

        botonRecurso = tk.Button(self.ventana, text = 'Recurso', command = recurso)
        botonRecurso.pack()

        botonAsignacion = tk.Button(self.ventana, text = 'Asignacion', command = asignacion)
        botonAsignacion.pack()
    
    