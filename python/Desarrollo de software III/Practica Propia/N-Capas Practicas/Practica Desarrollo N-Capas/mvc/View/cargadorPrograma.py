import tkinter
from tkinter import Tk

class CargadorPrograma:
    def __init__(self, root, abrir_cursos, abrir_estudiante, abrir_matricula):
        self.ventana = root
        self.ventana.geometry('1920x1080')
        self.ventana.columnconfigure(0, weight = 1)
        self.ventana.columnconfigure(1, weight=1)
        self.ventana.columnconfigure(2, weight=1)

        self.ventana.config(bg='blue')

        tkinter.Button(root, text = 'Directorio de Cursos', command=abrir_cursos, bg='white').grid(row=0,column=0, sticky='nswe')
        tkinter.Button(root, text='Directorio de Estudiantes', command= abrir_estudiante, bg='white').grid(row=0,column=1, sticky='nswe')
        tkinter.Button(root, text='Directorio de Matriculas', command=abrir_matricula, bg='white').grid(row=0, column=2, sticky='nswe')