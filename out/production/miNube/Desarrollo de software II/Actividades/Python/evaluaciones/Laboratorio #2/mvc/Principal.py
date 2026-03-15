#Participantes: 
#Herlin Fabian Chavarria Beita C5E187
#Joseph Campos C4D660
#David Mora Gomez C5H441

# Imports de Controladores (Clases)
from Controller.productosController import ProductosController
from Controller.inventarioController import InventarioController
from Controller.reportesController import ReportesController

# Imports de Vistas
import View.bodegaView
import View.productosView
import View.inventarioView
import View.reportesView

# Instancias Globales 
nuevoControladorProducto = ProductosController()
nuevoControladorInventario = InventarioController()
nuevoControladorReportes = ReportesController()

def main():
    while True:
        try:
            # Menu Principal
            View.bodegaView.mostrarMenu()
            opcionPrincipal = int(input("Input: "))

            # 1. Gestor productos
            if opcionPrincipal == 1:
                while True:
                    View.productosView.menuProductos()
                    opcionProductos = int(input("Input: "))
		    #Guardar
                    if opcionProductos == 1: 
                        print("Ingrese datos del producto:")
                        
                        nombre = input("Nombre: ")
                        categoria = input("Categoria: ")
                        precio = input("Precio: ")
                        stock = input("Stock Inicial: ")
                        
                        mensaje = nuevoControladorProducto.registrarProducto(nombre, categoria, precio, stock)
                        View.bodegaView.mostrarMensaje(mensaje)

                    elif opcionProductos == 2:
                        print("\nLista de productos")
                        nuevoControladorProducto.listarProductos()
		     # Modificar
                    elif opcionProductos == 3: 
                        idBuscar = input("Id a modificar: ")
                        nom = input("Nuevo Nombre: ")
                        cat = input("Nueva Categoria: ")
                        prec = input("Nuevo Precio: ")
                        stk = input("Nuevo Stock: ")
                        
                        mensaje = nuevoControladorProducto.actualizarProducto(idBuscar, nom, cat, prec, stk)
                        View.bodegaView.mostrarMensaje(mensaje)
		     # Eliminar
                    elif opcionProductos == 4:
                        idEliminar = input("Id a eliminar: ")
                        mensaje = nuevoControladorProducto.eliminarProducto(idEliminar)
                        View.bodegaView.mostrarMensaje(mensaje)
		     # Volver
                    elif opcionProductos == 5: 
                        break
                    else:
                        print("Opcion invalida")

            #2. Gestor de inventario
            elif opcionPrincipal == 2:
                while True:
                    View.inventarioView.menuInventario()
                    opcionInv = int(input("Input: "))
		    # Entrada
                    if opcionInv == 1:
                        idProd = input("Id Producto: ")
                        cant = input("Cantidad: ")
                        fecha = input("Fecha: ")
                        mensaje = nuevoControladorInventario.registrarEntrada(idProd, cant, fecha)
                        View.bodegaView.mostrarMensaje(mensaje)
		    # Salida
                    elif opcionInv == 2: 
                        idProd = input("Id Producto: ")
                        cant = input("Cantidad: ")
                        fecha = input("Fecha: ")
                        mensaje = nuevoControladorInventario.registrarSalida(idProd, cant, fecha)
                        View.bodegaView.mostrarMensaje(mensaje)
		    # Volver
                    elif opcionInv == 3: 
                        break
                    else:
                        print("Opcion invalida")

            # Reportes
            elif opcionPrincipal == 3:
                while True:
                    View.reportesView.menuReportes()
                    opcionRep = int(input("Input: "))
		    # Categoria
                    if opcionRep == 1:
                        lista = nuevoControladorReportes.reportePorCategoria()
                        View.reportesView.mostrarReporteCategoria(lista)
		     # Bajo Stock
                    elif opcionRep == 2: 
                        lista = nuevoControladorReportes.reporteBajoStock()
                        View.reportesView.mostrarReporteBajoStock(lista)
		     # Historial
                    elif opcionRep == 3: 
                        lista = nuevoControladorReportes.reporteHistorial()
                        View.reportesView.mostrarHistorial(lista)
		     # Volver
                    elif opcionRep == 4: 
                        break
                    else:
                        print("Opcion invalida")

            # --- 4. SALIR ---
            elif opcionPrincipal == 4:
                print("Saliendo del sistema...")
                break
            else:
                print("Opcion Invalida [1-4]")

        except ValueError:
            print("Error Ingrese solo numeros")

if __name__ == "__main__":
    main()