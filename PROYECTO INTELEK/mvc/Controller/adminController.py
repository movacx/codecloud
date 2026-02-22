# Importamos el modelo de producto desde su módulo correspondiente
from Model.ProductoModel import ProductoModel
import Data.baseProductos as dataPro
import Data.baseFacturas as dataFac # Importación agregada

class AdminController:
    def agregarNuevoProducto(self, nombre, cat, precio, stock, socket, ram):
        if float(precio) <= 0:
            return False, "El precio debe ser mayor a cero"
        
        nuevoObj = ProductoModel(0, nombre, cat, precio, stock, socket, ram)
        exito = dataPro.guardarProducto(nuevoObj)
        
        if exito:
            return True, "Producto guardado con exito"
        return False, "Error al guardar en base de datos"

    def quitarProducto(self, idDelProducto):
        exito = dataPro.eliminarProducto(idDelProducto)
        if exito:
            return True, "Producto eliminado"
        return False, "No se pudo eliminar"

    def gestionarEstadoFactura(self, idFac, decision):
        # Llama a la función definida en Data/baseFacturas.py
        exito = dataFac.cambiarEstadoFactura(idFac, decision)
        return exito, f"Factura {idFac} marcada como {decision}"