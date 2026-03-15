from Model import baseProducto
from Model import inventarioModel

class InventarioController:
    def __init__(self):
        pass

    def registrarEntrada(self, id, cantidad, fecha):
        producto = baseProducto.buscarProductoId(id)
        if producto is None:
            return "Error: Producto no existe"
        
        # Stock es posicion 4
        stockActual = int(producto[4])
        nuevoStock = stockActual + int(cantidad)
        
        # Actualizamos usando baseProducto
        baseProducto.modificarProducto(id, producto[1], producto[2], producto[3], nuevoStock)
        
        # Guardamos historial
        inventarioModel.guardarMovimiento(id, "Entrada", cantidad, fecha)
        return "Entrada registrada" 

    def registrarSalida(self, id, cantidad, fecha): 
        producto = baseProducto.buscarProductoId(id)
        if producto is None:
            return "Error: Producto no existe"
        
        stockActual = int(producto[4])
        if stockActual < int(cantidad):
            return "Error: Stock insuficiente"
        
        nuevoStock = stockActual - int(cantidad)

        baseProducto.modificarProducto(id, producto[1], producto[2], producto[3], nuevoStock)
        inventarioModel.guardarMovimiento(id, "Salida", cantidad, fecha)
        return "Salida registrada"