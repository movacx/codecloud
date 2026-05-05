from tkinter import ttk, messagebox
import tkinter as tk

#View universal

class RecursoView:
    def __init__(self, root, controller):
        self.controlador = controller
        self.ventana = tk.Toplevel(root)
        self.ventana.geometry('1000x600')

        self.ventana.columnconfigure(0,weight = 0)
        self.ventana.columnconfigure(1, weight = 1)
        self.ventana.rowconfigure(6,weight=1)

        #=-=-=-Llamados=-=-=-=-=-=
        self.labels()
        self.textField()
        #self.comboBox()
        self.btn()
        self.table()
        #=-=-=-=-=-=-=-=-=-=-=-=-=

    def separador(self, x, y):
        tk.Label(self.ventana).grid(row=x,column=y)

    def labels(self):#codigoRecurso, nombre, categoria, cantidadDisponible, costoUnitario
        tk.Label(self.ventana, text = 'Codigo:').grid(row=0,column=0,sticky='w')
        tk.Label(self.ventana, text = 'Nombre:').grid(row=1,column=0,sticky='w')
        tk.Label(self.ventana, text = 'Categoria:').grid(row=2,column=0,sticky='w')
        tk.Label(self.ventana, text = 'Cantidad disponible:').grid(row=3,column=0,sticky='w')
        tk.Label(self.ventana, text = 'Costo unitario:').grid(row=4,column=0,sticky='w')

    # def comboBox(self):
        # arreglo = ['Alta','Media','Baja']
        # self.opcion_combo = ttk.Combobox(self.ventana, values=arreglo, state = 'readonly')
        # self.opcion_combo.grid(row = 4, column = 1, sticky = 'nswe')
        # self.separador(5,0)


    def textField(self):
        self.codigo = tk.Entry(self.ventana)
        self.codigo.grid(row=0, column = 1, sticky = 'nswe')
        #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.nombre = tk.Entry(self.ventana)
        self.nombre.grid(row=1, column = 1, sticky = 'nswe')
        #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.categoria = tk.Entry(self.ventana)
        self.categoria.grid(row=2, column = 1, sticky = 'nswe')
        #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.cantidad_dispo = tk.Entry(self.ventana)
        self.cantidad_dispo.grid(row=3, column = 1, sticky = 'nswe')
        #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.costoUnitario = tk.Entry(self.ventana)
        self.costoUnitario.grid(row=4, column = 1, sticky = 'nswe')


    def btn(self):
        self.btn_guardar = tk.Button(self.ventana, text = 'Guardar', command = lambda: self.controlador.registrar_recurso())
        self.btn_guardar.grid(row = 5, column = 0, sticky = 'w')
        #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.btn_listar = tk.Button(self.ventana, text = 'Listar', command = lambda: self.controlador.imprimir_tabla())
        self.btn_listar.grid(row = 5, column = 1, sticky = 'w')
        #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.btn_buscar = tk.Button(self.ventana, text = 'Buscar')
        self.btn_buscar.grid(row = 5, column = 1, sticky = 'e' )

    def table(self):
        columnas = ['Codigo','Nombre','Categoria','Cantidad Disponible','Costo Unitario']
        self.tabla = ttk.Treeview(self.ventana, columns=columnas, show = 'headings')
        self.tabla.grid(row=6,column=0,columnspan=2,sticky='nswe')

        for items in columnas:
            self.tabla.heading(items, text = items)

    def cargar_tabla(self,arreglo): #codigoRecurso, nombre, categoria, cantidadDisponible, costoUnitario
        for items in arreglo:
            ide = items.codigoRecurso
            nom = items.nombre
            com = items.categoria
            can = items.cantidadDisponible
            soc = items.costoUnitario
            self.tabla.insert('',tk.END, values =(ide,nom,com,can,soc))

    def limpiar_tabla(self):
        for items in self.tabla.get_children():
            self.tabla.delete(items)


    #=-=-=-=-=-=-=-=-=-=-=-=- [Mensajes al usuario] =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def mostrar_mensaje(self, mensaje):
        return messagebox.showinfo('Dialogo', mensaje, parent=self.ventana)

    def mostrar_advertencia(self, adv):
        return messagebox.showwarning('Dialogo', adv, parent=self.ventana)
