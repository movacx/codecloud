import tkinter as tk
import random
from datetime import datetime
from View.VentanaArmador import VentanaArmador
import Data.baseProductos as dataPro
import Data.baseFacturas as dataFacturas

class ArmadorController:
    def __init__(self, root, idUsr):
        self.root = root
        self.idCliente = idUsr
        self.GUI = VentanaArmador(root, self)
        self.carrito = [ ]
        self.mapaProcesadores = { }
        self.cargarProcesadores()
#-----------------------------------------------------------------------------------------------------------------------
    #Cargar procesadores 
    def cargarProcesadores(self):
        inventario = dataPro.listarProductos()
        nombresProcesadores = [ ]
        
        for items in inventario:
            if items and items[2] == "Procesador":
                textoMostrar = f"{items[1]} (Socket: {items[5]})"
                nombresProcesadores.append(textoMostrar)
                self.mapaProcesadores[textoMostrar] = items
                
        self.GUI.selectorProcesador['values'] = nombresProcesadores
#-----------------------------------------------------------------------------------------------------------------------
     #Buscar piezas
    def buscarOtrasPiezas(self):
        categoria = self.GUI.selectorCategoria.get()
        if not categoria:
            self.GUI.mostrarError('Seleccione una categoria')
            return
        
        for items in self.GUI.tablaOpciones.get_children():
            self.GUI.tablaOpciones.delete(items)
        inventario = dataPro.listarProductos()
        
        for items in inventario:
            if items and items[2] == categoria:
                self.GUI.tablaOpciones.insert('', tk.END, values=(items[0], items[2], items[1], items[3]))
#-----------------------------------------------------------------------------------------------------------------------
     #Meter al carrito productos
    def meterAlCarrito(self):
        seleccion = self.GUI.tablaOpciones.selection()
        
        if not seleccion:
            self.GUI.mostrarError('Selecciona un producto primero')
            return
        datos = self.GUI.tablaOpciones.item(seleccion)['values']
        self.carrito.append(datos)
        self.GUI.tablaCarrito.insert('', tk.END, values=datos)
#-----------------------------------------------------------------------------------------------------------------------
     #Limpiar 
    def limpiarTodo(self):
        self.carrito = []
        self.GUI.selectorCategoria.set('')
        self.GUI.selectorProcesador.set('')
        self.GUI.entradaDireccion.delete(0, tk.END)
        
        for items in self.GUI.tablaOpciones.get_children():
            self.GUI.tablaOpciones.delete(items)
            
        for items in self.GUI.tablaCarrito.get_children():
            self.GUI.tablaCarrito.delete(items)
#-----------------------------------------------------------------------------------------------------------------------
     #Finalizar compra 
    def finalizar(self):
        nombreCompleto = self.GUI.entradaNombre.get()
        direccion = self.GUI.entradaDireccion.get()
        procesadorSeleccionado = self.GUI.selectorProcesador.get()
        
        if not (nombreCompleto):
            self.GUI.mostrarError("Digite su nombre completo")
            return
        
        if not procesadorSeleccionado:
            self.GUI.mostrarError("Seleccione un procesador")
            return
        
        if not direccion:
            self.GUI.mostrarError("Digite la dirección")
            return

        itemProcesador = self.mapaProcesadores.get(procesadorSeleccionado)
        if itemProcesador:
            datosProcesador = [itemProcesador[0], itemProcesador[2], itemProcesador[1], itemProcesador[3]]
            existe = False
            for items in self.carrito:
                if items and str(items[0]) == str(itemProcesador[0]):
                    existe = True
            if not existe:
                self.carrito.append(datosProcesador)
                self.GUI.tablaCarrito.insert('', tk.END, values=datosProcesador)

        if not self.carrito:
            self.GUI.mostrarError("Complete el pedido")
            return

        totalCompra = 0
        listaIds = [ ]
        
        for items in self.carrito:
            totalCompra += float(items[3])
            listaIds.append(str(items[0]))

            dataPro.restarStock(items[0], 1)

        idFactura = "FAC-" + str(random.randint(10, 99))
        fechaHoy = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        filaFactura = [idFactura, self.idCliente, nombreCompleto, fechaHoy, totalCompra, direccion]

        if dataFacturas.guardarFactura(filaFactura):
            self.GUI.mostrarInfo(f"Pedido Guardado: {idFactura}\nTotal: ₡{totalCompra}")
            self.limpiarTodo()
            self.GUI.ventana.destroy()
        else:
            self.GUI.mostrarError("No se pudo guardar la factura")
            
            