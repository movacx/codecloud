# Importamos el contenedor de items desde su módulo
from Model.ItemCarrito import ItemCarrito

class CarritoController:
    def __init__(self):
        self.listaItems = []

    def agregarProducto(self, objPro, cant):
        if int(objPro.stock) >= cant:
            # Agregamos al carrito una nueva instancia de ItemCarrito
            self.listaItems.append(ItemCarrito(objPro, cant))
            return True, "Agregado al carrito"
        return False, "Sin stock suficiente"

    def calcularSubtotal(self):
        totalPlata = 0
        for item in self.listaItems:
            totalPlata += float(item.producto.precio) * int(item.cantidad)
        return totalPlata

    def vaciarCarrito(self):
        self.listaItems = []