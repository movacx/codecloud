import Data.baseProductos as dataPro
import Data.baseFacturas as dataFac
import datetime
import random

class CheckoutController:
    def __init__(self, carritoControl):
        self.carrito = carritoControl

    def finalizarCompra(self, idUsr, direccion, metodo):
        items = self.carrito.listaItems
        if not items:
            return False, "Carrito vacio"

        # AQUI ESTABA EL ERROR: Ahora usa calcularSubtotal() correctamente
        montoFinal = self.carrito.calcularSubtotal() 
        idFactura = "FAC-" + str(random.randint(100, 999)) 
        fechaActual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

        # Rebajamos el stock de cada producto comprado 
        for it in items:
            dataPro.restarStock(it.producto.ide, it.cantidad)

        # Guardamos la factura con el estado 'Completado' 
        fila = [idFactura, idUsr, fechaActual, montoFinal, direccion]
        dataFac.guardarFactura(fila)
        
        self.carrito.vaciarCarrito()
        return True, f"Compra lista. Factura: {idFactura}"