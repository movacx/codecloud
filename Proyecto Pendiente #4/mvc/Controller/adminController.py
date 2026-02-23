from View.VentanaAdmin import VentanaAdmin
from Model.ProductoModel import ProductoModel
import Data.baseProductos as dataPro
import Data.baseFacturas as dataFac
import Data.baseUsuarios as dataUsuarios

class AdminController:
    def __init__(self, root):
        self.GUI = VentanaAdmin(root, self)

    def verVentas(self):
        try:
            listaFacturas = dataFac.leerFacturas()
            totalVentas = 0
            for items in listaFacturas:
                if items:
                    totalVentas = totalVentas + float(items[3])
            
            self.GUI.mostrarMensaje(f"INGRESOS BRUTOS: ₡{totalVentas}")
        except Exception as error:
            self.GUI.mostrarError(f"Error al calcular: {error}")

    def verCuentas(self):
        try:
            todosUsr = dataUsuarios.listarTodos()
            total = len(todosUsr)
            self.GUI.mostrarMensaje(f"TOTAL CUENTAS REGISTRADAS: {total}")
        except Exception as error:
            self.GUI.mostrarError(f"Error al leer cuentas: {error}")

    def reembolsar(self, estado):
        try:
            idF = self.GUI.txtIdFac.get()
            if not (idF):
                self.GUI.mostrarError("Ingrese un ID de factura")
                return
                
            exito = dataFac.cambiarEstadoFactura(idF, estado)
            if exito:
                self.GUI.mostrarMensaje(f"Factura {idF} marcada como {estado}")
                self.GUI.txtIdFac.delete(0, 'end')
            else:
                self.GUI.mostrarError("No se pudo cambiar el estado")
        except Exception as error:
            self.GUI.mostrarError(f"Error al procesar reembolso: {error}")

    def guardarNuevoPro(self):
        try:
            nom = self.GUI.txtNomPro.get()
            cat = self.GUI.txtCatPro.get()
            pre = self.GUI.txtPrecioPro.get()
            stk = self.GUI.txtStockPro.get()
            sck = self.GUI.txtSockPro.get()
            ram = self.GUI.txtRamPro.get()

            if not (nom or cat or pre or stk):
                self.GUI.mostrarError("Faltan datos obligatorios")
                return

            if float(pre) <= 0:
                self.GUI.mostrarError("El precio debe ser mayor a cero")
                return

            if not sck: sck = "N/A"
            if not ram: ram = "N/A"

            nuevoObj = ProductoModel(0, nom, cat, pre, stk, sck, ram)
            exito = dataPro.guardarProducto(nuevoObj)
            
            if exito:
                self.GUI.mostrarMensaje("Producto guardado con exito")
                self.GUI.txtNomPro.delete(0, 'end')
                self.GUI.txtCatPro.delete(0, 'end')
                self.GUI.txtPrecioPro.delete(0, 'end')
                self.GUI.txtStockPro.delete(0, 'end')
                self.GUI.txtSockPro.delete(0, 'end')
                self.GUI.txtRamPro.delete(0, 'end')
            else:
                self.GUI.mostrarError("Error al guardar en base de datos")
        except Exception as error:
            self.GUI.mostrarError(f"Error al guardar: {error}")