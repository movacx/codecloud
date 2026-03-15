from Model import baseProducto

class ProductosController:
    def __init__(self):
        pass

    def registrarProducto(self, nombre, categoria, precio, stock):
        if int(precio) <= 0:
            return "Error: Precio invalido"
        if int(stock) < 0:
            return "Error: Stock invalido"
        
        #Se genera un ID
        listaActual = baseProducto.listarProductos()
        nuevoId = len(listaActual) + 1
        
        # Llamamos a baseProducto para guardar
        baseProducto.guardarProducto(nuevoId, nombre, categoria, precio, stock)
        return f"Producto registrado con ID {nuevoId}"

    def listarProductos(self):
        baseProducto.listarProductos()

    def actualizarProducto(self, id, nombre, categoria, precio, stock):
        encontrado = baseProducto.buscarProductoId(id)
        if encontrado is None:
            return "Error: Producto no existe"

        baseProducto.modificarProducto(id, nombre, categoria, precio, stock)
        return "Producto actualizado correctamente"

    def eliminarProducto(self, id):
        baseProducto.eliminarProductos(id)
        return "Producto eliminado"