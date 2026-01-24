from Model import productosModel
from Model import inventarioModel

def entrada(id, cantidad):
    producto = productosModel.buscarProducto(id)
    if producto is None:
        return "Producto no exite"
    
    nuevoStock = int(producto[4] + cantidad)
    productosModel.modificarProducto(id,
    producto[1],
    producto[2],
    producto[3],
    nuevoStock)

    inventarioModel.guaradarMovimiento(id, "Entrada", cantidad)
    return "Entrada registrada" 


def salida(id, cantidad): 
    producto = productosModel.buscarProducto(id)

    if producto is None:
        return "Producto no existe"
    
    if int(producto[4]) < cantidad:
        return "Stock insuficiente"
    
    nuevoStock = int(producto[4] + cantidad)

    productosModel.modificarProducto(id,
    producto[1],
    producto[2],
    producto[3],
    nuevoStock)


    inventarioModel.guaradarMovimiento(id, "Salida", cantidad)
    return "Salida registrada"