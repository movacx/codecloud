
import tkinter as tk
from Tools.scripts.summarize_stats import Columns
from tkinter import ttk, messagebox

class CursoGUI:
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



    #codigo_curso, nombre, creditos
    def separar_campo(self, row, column):
        tk.Label(self.ventana, text='').grid(row=row, column=column)

    def etiquetas(self):
        tk.Label(self.ventana, text = 'Codigo: ', font = 'Arial').grid(row=0,column=0,sticky='w')
        tk.Label(self.ventana, text='Curso: ', font = 'Arial').grid(row=1, column=0, sticky='w')
        tk.Label(self.ventana, text='Creditos: ', font = 'Arial').grid(row=2, column=0, sticky='w')

    def campos_texto(self):
        self.codigo = tk.Entry(self.ventana)
        self.codigo.grid(row=0, column=1, sticky='nswe')
        #---------------------------------------------------
        self.nombre = tk.Entry(self.ventana)
        self.nombre.grid(row=1, column=1, sticky='nswe')
        # ---------------------------------------------------
        self.creditos = tk.Entry(self.ventana)
        self.creditos.grid(row=2, column=1, sticky='nswe')

        #Limpiar una columna:
        self.separar_campo(3,0)

    def agregar_botones(self):
        self.btn_agregar = tk.Button(self.ventana, text = 'Agregar', command = lambda : self.manejo_controller.registrar_curso())
        self.btn_agregar.grid(row=4,column=0, sticky='nswe')
        # ---------------------------------------------------
        self.btn_mostrar = tk.Button(self.ventana, text = 'Mostrar Registros', command = lambda : self.manejo_controller.cargar_registros())
        self.btn_mostrar.grid(row=4,column=1, sticky='nswe')
        # ---------------------------------------------------
        self.btn_buscar = tk.Button(self.ventana, text = 'Buscar', command = lambda : self.manejo_controller.buscar_curso())
        self.btn_buscar.grid(row=4,column=2, sticky='nswe')

        #limpiar una columna:
        self.separar_campo(5,0)

    def agregar_tabla(self):
        columnas = ['Codigo Curso','Nombre Curso','Creditos']
        self.tabla = ttk.Treeview(self.ventana, columns=columnas, show = 'headings')
        self.tabla.grid(row=6,column=0, columnspan=3, sticky='nwse')
        # ---------------------------------------------------
        for items in columnas:
            self.tabla.heading(items, text = items)

    def cargar_tabla(self, arreglo):
        for items in arreglo:
            codigo = items.codigo_curso
            nombre = items.nombre
            creditos = items.creditos
            self.tabla.insert('', tk.END, values=(codigo, nombre, creditos))

    def mostrar_mensajes(self, mensaje):
        messagebox.showinfo('Dialog',f'{mensaje}', parent = self.ventana)

    def mostrar_error(self, error):
        messagebox.showerror('Dialog', f'{error}', parent = self.ventana)

    def limpiar_tabla(self):
        for items in self.tabla.get_children():
            self.tabla.delete(items)