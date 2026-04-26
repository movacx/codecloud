from tkinter import ttk, messagebox
import tkinter as tk



class AsignacionView:
    def __init__(self, root, controller):
        self.controlador = controller
        self.ventana = tk.Toplevel(root)
        self.ventana.geometry('1000x600')

        self.ventana.columnconfigure(0,weight = 0)
        self.ventana.columnconfigure(1, weight = 1)
        self.ventana.rowconfigure(7,weight=1)

        #=-=-=-Llamados=-=-=-=-=-=
        self.labels()
        self.textField()
        #self.comboBox()
        self.btn()
        self.table()
        #=-=-=-=-=-=-=-=-=-=-=-=-=

    def separador(self, x, y):
        tk.Label(self.ventana).grid(row=x,column=y)

    def labels(self):#codigoAsignacion:str, beneficiario:str, recurso:str, cantidadEntregada:int, fecha:str, responsableEntrega:str
        tk.Label(self.ventana, text = 'Codigo asignacion:').grid(row=0,column=0,sticky='w')
        tk.Label(self.ventana, text = 'Ced beneficiario:').grid(row=1,column=0,sticky='w')
        tk.Label(self.ventana, text = 'Codigo Recurso:').grid(row=2,column=0,sticky='w')
        tk.Label(self.ventana, text = 'Cantidad entregada:').grid(row=3,column=0,sticky='w')
        tk.Label(self.ventana, text = 'Fecha:').grid(row=4,column=0,sticky='w')
        tk.Label(self.ventana, text = 'Responsable de entrega:').grid(row=5,column=0,sticky='w')

    #def comboBox(self):
        #arreglo = ['Alta','Media','Baja']
        #self.opcion_combo = ttk.Combobox(self.ventana, values=arreglo, state = 'readonly')
        #self.opcion_combo.grid(row = 4, column = 1, sticky = 'nswe')
        #self.separador(5,0)


    def textField(self):
        self.codigo = tk.Entry(self.ventana)
        self.codigo.grid(row=0, column = 1, sticky = 'nswe')
        #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.beneficiario = tk.Entry(self.ventana)
        self.beneficiario.grid(row=1, column = 1, sticky = 'nswe')
        #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.recurso = tk.Entry(self.ventana)
        self.recurso.grid(row=2, column = 1, sticky = 'nswe')
        #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.cantidad_entregada = tk.Entry(self.ventana)
        self.cantidad_entregada.grid(row=3, column = 1, sticky = 'nswe')
        #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.fecha = tk.Entry(self.ventana)
        self.fecha.grid(row=4, column = 1, sticky = 'nswe')
        #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.responsable = tk.Entry(self.ventana)
        self.responsable.grid(row=5, column = 1, sticky = 'nswe')


    def btn(self):
        self.btn_guardar = tk.Button(self.ventana, text = 'Guardar', command = lambda: self.controlador.nueva_asignacion())
        self.btn_guardar.grid(row = 6, column = 0, sticky = 'w')
        #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.btn_listar = tk.Button(self.ventana, text = 'Listar', command = lambda: self.controlador.imprimir_tabla())
        self.btn_listar.grid(row = 6, column = 1, sticky = 'w')
        #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.btn_buscar = tk.Button(self.ventana, text = 'Buscar')
        self.btn_buscar.grid(row = 6, column = 1, sticky = 'e' )

    def table(self):
        columnas = ['Codigo','Beneficiario','Recurso','Cantidad entregada','fecha', 'Responsable']
        self.tabla = ttk.Treeview(self.ventana, columns=columnas, show = 'headings')
        self.tabla.grid(row=7,column=0,columnspan=2,sticky='nswe')

        for items in columnas:
            self.tabla.heading(items, text = items)

    def cargar_tabla(self,arreglo): #codigoAsignacion:str, beneficiario:str, recurso:str, cantidadEntregada:int, fecha:str, responsableEntrega:str
        for items in arreglo:
            ide = items.codigoAsignacion
            nom = items.beneficiario
            com = items.recurso
            can = items.cantidadEntregada
            soc = items.fecha
            rep = items.responsableEntrega
            self.tabla.insert('',tk.END, values =(ide,nom,com,can,soc,rep))

    def limpiar_tabla(self):
        for items in self.tabla.get_children():
            self.tabla.delete(items)


    #=-=-=-=-=-=-=-=-=-=-=-=- [Mensajes al usuario] =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def mostrar_mensaje(self, mensaje):
        return messagebox.showinfo('Dialogo', mensaje, parent=self.ventana)

    def mostrar_advertencia(self, adv):
        return messagebox.showwarning('Dialogo', adv, parent=self.ventana)
