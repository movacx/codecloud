#Clase clon de las anteriores GUI adaptada a matricula
# codigo_matricula, carnet_estudiante, codigo_curso, periodo_academico

import tkinter as tk
from tkinter import ttk, messagebox

class MatriculaGUI:
    def __init__(self, root, controller):
        self.ventana = tk.Toplevel(root)
        self.manejo_controller = controller
        self.ventana.geometry('900x700')

        self.etiquetas()
        self.combobox()
        self.campos_texto()
        self.agregar_botones()
        self.agregar_tabla()

        self.ventana.columnconfigure(0, weight=0)
        self.ventana.columnconfigure(1, weight=1)
        self.ventana.rowconfigure(6,weight=1)



    def separar_campo(self, row, column):
        tk.Label(self.ventana, text='').grid(row=row, column=column)

    def etiquetas(self):
        tk.Label(self.ventana, text = 'Codigo matricula: ', font = 'Arial').grid(row=0,column=0,sticky='w')
        tk.Label(self.ventana, text='Carnet estudiante: ', font = 'Arial').grid(row=1, column=0, sticky='w')
        tk.Label(self.ventana, text='Codigo curso: ', font = 'Arial').grid(row=2, column=0, sticky='w')
        tk.Label(self.ventana, text='Periodo academico: ', font='Arial').grid(row=3, column=0, sticky='w')

    def combobox(self):
        #-=-=-=-=-=- ComboBox =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=---=-=-==-==-==-===-=--=-=-
        periodos = ['I Ciclo 2026', 'II Ciclo 2026', 'III Ciclo 2026']
        self.periodo_academico = ttk.Combobox(self.ventana, values=periodos, state = 'readonly')
        self.periodo_academico.grid(row=3, column=1, sticky='nswe')

    def campos_texto(self):
        self.codigo_matricula = tk.Entry(self.ventana)
        self.codigo_matricula.grid(row=0, column=1, sticky='nswe')
        #---------------------------------------------------
        self.carnet_estudiante = tk.Entry(self.ventana)
        self.carnet_estudiante.grid(row=1, column=1, sticky='nswe')
        # ---------------------------------------------------
        self.codigo_curso = tk.Entry(self.ventana)
        self.codigo_curso.grid(row=2, column=1, sticky='nswe')

        #Limpiar una fila:
        self.separar_campo(3,0)

    def agregar_botones(self):
        self.btn_agregar = tk.Button(self.ventana, text = 'Agregar', command = lambda : self.manejo_controller.registrar_matricula())
        self.btn_agregar.grid(row=4,column=0, sticky='nswe')
        # ---------------------------------------------------
        self.btn_mostrar = tk.Button(self.ventana, text = 'Mostrar Registros', command = lambda : self.manejo_controller.cargar_registros())
        self.btn_mostrar.grid(row=4,column=1, sticky='nswe')
        # ---------------------------------------------------
        self.btn_buscar = tk.Button(self.ventana, text = 'Buscar', command=lambda :self.manejo_controller.buscar_curso())
        self.btn_buscar.grid(row=4,column=2, sticky='nswe')

        #limpiar una Fila*:
        self.separar_campo(5,0)

    def limpiar_tabla(self):
        for items in self.tabla.get_children():
            self.tabla.delete(items)

    def agregar_tabla(self):
        columnas = ['Id Matricula','Carnet','Curso','Periodo']
        self.tabla = ttk.Treeview(self.ventana, columns=columnas, show = 'headings')
        self.tabla.grid(row=6,column=0, columnspan=3, sticky='nwse')
        # ---------------------------------------------------
        for items in columnas:
            self.tabla.heading(items, text = items)

    def cargar_tabla(self, arreglo): #carnet, nombre, carrera
        for items in arreglo: #codigo_matricula, carnet_estudiante, codigo_curso, periodo_academico
            codigo_matricula = items.codigo_matricula
            carnet_estudiante = items.carnet_estudiante
            codigo_curso = items.codigo_curso
            periodo_academico = items.periodo_academico
            self.tabla.insert('', tk.END, values=(codigo_matricula, carnet_estudiante, codigo_curso, periodo_academico))

    def mostrar_mensajes(self, mensaje):
        messagebox.showinfo('Dialog',f'{mensaje}', parent = self.ventana)

    def mostrar_error(self, error):
        messagebox.showerror('Dialog', f'{error}', parent = self.ventana)