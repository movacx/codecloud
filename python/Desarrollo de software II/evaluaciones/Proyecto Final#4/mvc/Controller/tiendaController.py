from View.VentanaTienda import VentanaTienda
from Model.ProductoModel import ProductoModel
from Controller.resenaController import ResenaController
from Model.ItemCarrito import ItemCarrito
from View.VentanaHistorial import VentanaHistorial
import Data.baseProductos as dataPro
import Data.baseFacturas as dataFac
import Data.baseResenas as dataRes
import random
import datetime

class TiendaController:
    def __init__(self, root, idUsr):
        self.idCliente = idUsr
        self.GUI = VentanaTienda(root, self)
        self.listaItemsCarrito = [ ]
        self.totalPagar = 0
        self.buscarProductos() 
#-----------------------------------------------------------------------------------------------------------------------
    #Buscar producto
    def buscarProductos(self):
        try:
            texto = self.GUI.txtBusca.get().lower()
            inventario = dataPro.listarProductos()
            
            for items in self.GUI.tablaInv.get_children():
                self.GUI.tablaInv.delete(items)

            for items in inventario:
                if items:
                    if texto in items[1].lower():
                        self.GUI.tablaInv.insert('', 'end', values=(items[0], items[1], items[3], items[4]))
        except Exception as error:
            self.GUI.mostrarError(f"Error en busqueda: {error}")
#-----------------------------------------------------------------------------------------------------------------------
    #Ordenar productos por precio
    def ordenarPrecio(self):
        try:
            texto = self.GUI.txtBusca.get().lower()
            inventario = dataPro.listarProductos()
            listaFiltrada = [ ]

            for items in inventario:
                if items:
                    if texto in items[1].lower():
                        listaFiltrada.append(items)

            listaFiltrada.sort(key=lambda item: float(item[3]), reverse=True)

            for items in self.GUI.tablaInv.get_children():
                self.GUI.tablaInv.delete(items)

            for items in listaFiltrada:
                if items:
                    self.GUI.tablaInv.insert('', 'end', values=(items[0], items[1], items[3], items[4]))
        except Exception as error:
            self.GUI.mostrarError(f"Error al ordenar: {error}")
#-----------------------------------------------------------------------------------------------------------------------
    #Agregar un producto 
    def agregarItem(self):
        try:
            seleccion = self.GUI.tablaInv.selection()
            if not seleccion:
                self.GUI.mostrarError("Seleccione un producto de la tabla")
                return
                
            valores = self.GUI.tablaInv.item(seleccion[0], "values")
            idPro = valores[0]
            nombre = valores[1]
            precio = valores[2]
            stock = valores[3]

            if int(stock) < 1:
                self.GUI.mostrarError("Sin stock suficiente")
                return

            for items in self.listaItemsCarrito:
                if items:
                    if items.producto.ide == idPro:
                        items.cantidad = int(items.cantidad) + 1
                        self.actualizarCarritoVisual()
                        return

            objProducto = ProductoModel(idPro, nombre, "", precio, stock, "", "")
            nuevoItem = ItemCarrito(objProducto, 1)
            self.listaItemsCarrito.append(nuevoItem)
            self.actualizarCarritoVisual()
            
        except Exception as error:
            self.GUI.mostrarError(f"Error al agregar: {error}")
#-----------------------------------------------------------------------------------------------------------------------
    #Actualizar el carrito de compras 
    def actualizarCarritoVisual(self):
        try:
            for items in self.GUI.tablaCarro.get_children():
                self.GUI.tablaCarro.delete(items)
                
            self.totalPagar = 0
            
            for items in self.listaItemsCarrito:
                if items:
                    subtotal = float(items.producto.precio) * int(items.cantidad)
                    self.GUI.tablaCarro.insert('', 'end', values=(items.producto.ide, items.producto.nombre, items.cantidad, subtotal))
                    self.totalPagar = self.totalPagar + subtotal
                
            self.GUI.lblTotal.config(text=f"Total: ₡{self.totalPagar}")
        except Exception as error:
            self.GUI.mostrarError(f"Error al actualizar: {error}")
#-----------------------------------------------------------------------------------------------------------------------
    #Aplicar los descuentos 
    def aplicarDescuento(self):
        try:
            suerte = random.randint(1, 100) 
            if suerte <= 10:
                self.totalPagar = self.totalPagar * 0.20
                self.GUI.lblTotal.config(text=f"Total con promo: ₡{self.totalPagar} (80% rebajado!)")
            else:
                self.totalPagar = self.totalPagar * 0.75
                self.GUI.lblTotal.config(text=f"Total con promo: ₡{self.totalPagar} (25% rebajado!)")
        except Exception as error:
            self.GUI.mostrarError(f"Error de cupon: {error}")
#-----------------------------------------------------------------------------------------------------------------------
    #Ver estrellas 
    def verEstrellas(self):
        try:
            seleccion = self.GUI.tablaInv.selection()
            if not seleccion:
                return
            idPro = self.GUI.tablaInv.item(seleccion[0], "values")[0]
            
            todas = dataRes.leerResenas()
            suma = 0
            cant = 0
            for items in todas:
                if items:
                    if items[0] == str(idPro):
                        suma += int(items[3])
                        cant += 1
            if cant == 0:
                self.GUI.mostrarMensaje("Sin calificaciones")
            else:
                self.GUI.mostrarMensaje(f"Calificacion promedio: {suma / cant} estrellas")
        except Exception as error:
            self.GUI.mostrarError(f"Error al leer estrellas: {error}")
#-----------------------------------------------------------------------------------------------------------------------
    #Eliminar item del carrito
    def eliminarItemCarrito(self):
        try:
            seleccion = self.GUI.tablaCarro.selection()
            if not seleccion:
                self.GUI.mostrarError("Seleccione un item del carrito")
                return

            valores = self.GUI.tablaCarro.item(seleccion[0], "values")
            idPro = valores[0]

            listaNueva = []
            for items in self.listaItemsCarrito:
                if items:
                    if items.producto.ide != idPro:
                        listaNueva.append(items)

            self.listaItemsCarrito = listaNueva
            self.actualizarCarritoVisual()
        except Exception as error:
            self.GUI.mostrarError(f"Error al eliminar: {error}")
#-----------------------------------------------------------------------------------------------------------------------
    #Sumar cantidad
    def sumarCantidad(self):
        try:
            seleccion = self.GUI.tablaCarro.selection()
            if not seleccion:
                self.GUI.mostrarError("Seleccione un item del carrito")
                return

            valores = self.GUI.tablaCarro.item(seleccion[0], "values")
            idPro = valores[0]

            for items in self.listaItemsCarrito:
                if items:
                    if items.producto.ide == idPro:
                        items.cantidad = int(items.cantidad) + 1
                        self.actualizarCarritoVisual()
                        return
        except Exception as error:
            self.GUI.mostrarError(f"Error al sumar: {error}")
#-----------------------------------------------------------------------------------------------------------------------
    #Restar cantidad
    def restarCantidad(self):
        try:
            seleccion = self.GUI.tablaCarro.selection()
            if not seleccion:
                self.GUI.mostrarError("Seleccione un item del carrito")
                return

            valores = self.GUI.tablaCarro.item(seleccion[0], "values")
            idPro = valores[0]

            listaNueva = []
            for items in self.listaItemsCarrito:
                if items:
                    if items.producto.ide == idPro:
                        cantidadNueva = int(items.cantidad) - 1
                        if cantidadNueva > 0:
                            items.cantidad = cantidadNueva
                            listaNueva.append(items)
                    else:
                        listaNueva.append(items)

            self.listaItemsCarrito = listaNueva
            self.actualizarCarritoVisual()
        except Exception as error:
            self.GUI.mostrarError(f"Error al restar: {error}")
#-----------------------------------------------------------------------------------------------------------------------
    #Pagar factura 
    def pagarFactura(self):
        try:
            nombreCompleto = self.GUI.txtNombre.get()
            direccion = self.GUI.txtDir.get()
            
            if not (nombreCompleto):
                self.GUI.mostrarError("Debe escribir su nombre completo")
                return

            if not (direccion):
                self.GUI.mostrarError("Debe escribir una direccion")
                return
                
            if not self.listaItemsCarrito:
                self.GUI.mostrarError("El carrito esta vacio")
                return

            idFactura = "FAC-" + str(random.randint(100, 999))
            fechaActual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            for items in self.listaItemsCarrito:
                if items:
                    dataPro.restarStock(items.producto.ide, items.cantidad)

            filaNueva = [idFactura, self.idCliente, nombreCompleto, fechaActual, self.totalPagar, direccion]
            dataFac.guardarFactura(filaNueva)

            listaProductosComprados = [ ]
            for items in self.listaItemsCarrito:
                if items:
                    listaProductosComprados.append(items.producto.ide)
            
            self.listaItemsCarrito = []
            self.actualizarCarritoVisual()
            self.GUI.mostrarMensaje("Compra exitosa")
            ventanaPadreResena = self.GUI
            if hasattr(self.GUI, "ventana"):
                ventanaPadreResena = self.GUI.ventana
            ResenaController(ventanaPadreResena, self.idCliente, listaProductosComprados)
        except Exception as error:
            self.GUI.mostrarError(f"Error al pagar: {error}")
#-----------------------------------------------------------------------------------------------------------------------
    #Ver historial de facturas
    def verHistorial(self):
        try:
            historialGUI = VentanaHistorial(self.GUI.ventana, self)
            listaFacturas = dataFac.leerFacturas()

            for items in listaFacturas:
                if items:
                    if items[1] == str(self.idCliente):
                        historialGUI.tablaHistorial.insert('', 'end', values=(items[0], items[2], items[3], items[4], items[5], items[6]))
        except Exception as error:
            self.GUI.mostrarError(f"Error al cargar historial: {error}")
            
