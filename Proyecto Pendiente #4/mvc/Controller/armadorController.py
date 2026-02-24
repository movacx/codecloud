import tkinter as tk
import random
from datetime import datetime
from View.VentanaArmador import VentanaArmador
import Data.baseProductos as dataPro
import Data.baseFacturas as dataFacturas

class ArmadorController:
    def __init__(self, root):
        self.root = root
        self.GUI = VentanaArmador(root, self)
        self.carrito = []
        self.cargarProcesadores()

    def cargarProcesadores(self):
        inventario = dataPro.listarProductos()
        nombresProcesadores = []
        for items in inventario:
            if items and items[2] == "Procesador":
                nombresProcesadores.append(f"{items[1]} (Socket: {items[5]})")
        self.GUI.selectorProcesador['values'] = nombresProcesadores

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

    def meterAlCarrito(self):
        seleccion = self.GUI.tablaOpciones.selection()
        if not seleccion:
            self.GUI.mostrarError('Selecciona un producto primero')
            return
        datos = self.GUI.tablaOpciones.item(seleccion)['values']
        self.carrito.append(datos)
        self.GUI.tablaCarrito.insert('', tk.END, values=datos)

    def limpiarTodo(self):
        self.carrito = []
        self.GUI.selectorCategoria.set('')
        self.GUI.selectorProcesador.set('')
        self.GUI.entradaDireccion.delete(0, tk.END)
        for items in self.GUI.tablaOpciones.get_children():
            self.GUI.tablaOpciones.delete(items)
        for items in self.GUI.tablaCarrito.get_children():
            self.GUI.tablaCarrito.delete(items)

    def finalizar(self):
        direccion = self.GUI.entradaDireccion.get()
        if not self.carrito or not direccion:
            self.GUI.mostrarError("Complete el pedido y la dirección")
            return

        totalCompra = 0
        listaIds = []
        
        for items in self.carrito:
            totalCompra += float(items[3])
            listaIds.append(str(items[0]))

            dataPro.restarStock(items[0], 1)

        idFactura = "FAC-" + str(random.randint(10, 99))
        fechaHoy = datetime.now().strftime("%d/%m/%Y")
        unirIds = "-".join(listaIds)
        filaFactura = [idFactura, unirIds, fechaHoy, totalCompra, direccion]

        if dataFacturas.guardarFactura(filaFactura):
            self.GUI.mostrarInfo(f"Pedido Guardado: {idFactura}\nTotal: ₡{totalCompra}")
            self.limpiarTodo()
            self.GUI.ventana.destroy()
        else:
            self.GUI.mostrarError("No se pudo guardar la factura")