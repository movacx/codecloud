
import tkinter as tk
from Tools.scripts.summarize_stats import Columns
from tkinter import ttk, messagebox

class EstudianteGUI:
    def __init__(self, root, controller):
        self.ventana = tk.Toplevel(root)
        self.manejo_controller = controller
        self.ventana.geometry('900x700')

        self.etiquetas()
        self.campos_texto()
        self.agregar_botones()
        self.agregar_tabla()

        self.ventana.columnconfigure(0, weight=0)
        self.ventana.columnconfigure(1, weight=1)
        self.ventana.rowconfigure(6,weight=1)



    #Clase clon de curso model: carnet, nombre, carrera
    def separar_campo(self, row, column):
        tk.Label(self.ventana, text='').grid(row=row, column=column)

    def etiquetas(self):
        tk.Label(self.ventana, text = 'Carnet: ', font = 'Arial').grid(row=0,column=0,sticky='w')
        tk.Label(self.ventana, text='Nombre: ', font = 'Arial').grid(row=1, column=0, sticky='w')
        tk.Label(self.ventana, text='Carrera: ', font = 'Arial').grid(row=2, column=0, sticky='w')

    def campos_texto(self):
        self.carnet = tk.Entry(self.ventana)
        self.carnet.grid(row=0, column=1, sticky='nswe')
        #---------------------------------------------------
        self.nombre = tk.Entry(self.ventana)
        self.nombre.grid(row=1, column=1, sticky='nswe')
        # ---------------------------------------------------
        self.carrera = tk.Entry(self.ventana)
        self.carrera.grid(row=2, column=1, sticky='nswe')

        #Limpiar una columna:
        self.separar_campo(3,0)

    def agregar_botones(self):
        self.btn_agregar = tk.Button(self.ventana, text = 'Agregar', command = lambda : self.manejo_controller.registrar_estudiante())
        self.btn_agregar.grid(row=4,column=0, sticky='nswe')
        # ---------------------------------------------------
        self.btn_mostrar = tk.Button(self.ventana, text = 'Mostrar Registros', command = lambda : self.manejo_controller.cargar_registros())
        self.btn_mostrar.grid(row=4,column=1, sticky='nswe')
        # ---------------------------------------------------
        self.btn_buscar = tk.Button(self.ventana, text = 'Buscar', command=lambda :self.manejo_controller.buscar_curso())
        self.btn_buscar.grid(row=4,column=2, sticky='nswe')

        #limpiar una columna:
        self.separar_campo(5,0)

    def agregar_tabla(self):
        columnas = ['Carnet','Nombre estudiante','Carrera']
        self.tabla = ttk.Treeview(self.ventana, columns=columnas, show = 'headings')
        self.tabla.grid(row=6,column=0, columnspan=3, sticky='nwse')
        # ---------------------------------------------------
        for items in columnas:
            self.tabla.heading(items, text = items)

    def limpiar_tabla(self):
        for items in self.tabla.get_children():
            self.tabla.delete(items)

    def cargar_tabla(self, arreglo): #carnet, nombre, carrera
        for items in arreglo:
            carnet = items.carnet
            nombre = items.nombre
            carrera = items.carrera
            self.tabla.insert('', tk.END, values=(carnet, nombre, carrera))

    def mostrar_mensajes(self, mensaje):
        messagebox.showinfo('Dialog',f'{mensaje}', parent = self.ventana)

    def mostrar_error(self, error):
        messagebox.showerror('Dialog', f'{error}', parent = self.ventana)