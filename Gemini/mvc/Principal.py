# Imports de Controladores (Clases)
from Controller.productosController import ProductosController
from Controller.inventarioController import InventarioController
from Controller.reportesController import ReportesController

# Imports de Vistas
import View.bodegaView
import View.productosView
import View.inventarioView
import View.reportesView

# Instancias Globales (Como en el Quiz)
nuevoControladorProducto = ProductosController()
nuevoControladorInventario = InventarioController()
nuevoControladorReportes = ReportesController()

def main():
    while True:
        try:
            # Menu Principal
            View.bodegaView.mostrarMenu()
            opcionPrincipal = int(input("Input: "))

            # --- 1. GESTION DE PRODUCTOS ---
            if opcionPrincipal == 1:
                while True:
                    View.productosView.menuProductos()
                    opcionProductos = int(input("Input: "))

                    if opcionProductos == 1: # Registrar
                        print("Ingrese datos del producto:")
                        # Pedimos el ID manual o lo generamos. 
                        # El enunciado dice autogenerado, lo calculamos en el controller.
                        nom = input("Nombre: ")
                        cat = input("Categoria: ")
                        prec = input("Precio: ")
                        stk = input("Stock Inicial: ")
                        
                        mensaje = nuevoControladorProducto.registrarProducto(nom, cat, prec, stk)
                        View.bodegaView.mostrarMensaje(mensaje)

                    elif opcionProductos == 2: # Listar
                        # El baseProducto imprime directo, pero para MVC correcto
                        # capturamos la lista si es posible, o dejamos que imprima.
                        print("\n--- LISTA DE PRODUCTOS ---")
                        nuevoControladorProducto.listarProductos()

                    elif opcionProductos == 3: # Modificar
                        idBuscar = input("ID a modificar: ")
                        nom = input("Nuevo Nombre: ")
                        cat = input("Nueva Categoria: ")
                        prec = input("Nuevo Precio: ")
                        stk = input("Nuevo Stock: ")
                        
                        mensaje = nuevoControladorProducto.actualizarProducto(idBuscar, nom, cat, prec, stk)
                        View.bodegaView.mostrarMensaje(mensaje)

                    elif opcionProductos == 4: # Eliminar
                        idEliminar = input("ID a eliminar: ")
                        mensaje = nuevoControladorProducto.eliminarProducto(idEliminar)
                        View.bodegaView.mostrarMensaje(mensaje)

                    elif opcionProductos == 5: # Volver
                        break
                    else:
                        print("Opcion invalida")

            # --- 2. GESTION DE INVENTARIO ---
            elif opcionPrincipal == 2:
                while True:
                    View.inventarioView.menuInventario()
                    opcionInv = int(input("Input: "))

                    if opcionInv == 1: # Entrada
                        idProd = input("ID Producto: ")
                        cant = input("Cantidad: ")
                        fecha = input("Fecha: ")
                        mensaje = nuevoControladorInventario.registrarEntrada(idProd, cant, fecha)
                        View.bodegaView.mostrarMensaje(mensaje)

                    elif opcionInv == 2: # Salida
                        idProd = input("ID Producto: ")
                        cant = input("Cantidad: ")
                        fecha = input("Fecha: ")
                        mensaje = nuevoControladorInventario.registrarSalida(idProd, cant, fecha)
                        View.bodegaView.mostrarMensaje(mensaje)

                    elif opcionInv == 3: # Volver
                        break
                    else:
                        print("Opcion invalida")

            # --- 3. REPORTES ---
            elif opcionPrincipal == 3:
                while True:
                    View.reportesView.menuReportes()
                    opcionRep = int(input("Input: "))

                    if opcionRep == 1: # Categoria
                        lista = nuevoControladorReportes.reportePorCategoria()
                        View.reportesView.mostrarReporteCategoria(lista)

                    elif opcionRep == 2: # Bajo Stock
                        lista = nuevoControladorReportes.reporteBajoStock()
                        View.reportesView.mostrarReporteBajoStock(lista)

                    elif opcionRep == 3: # Historial
                        lista = nuevoControladorReportes.reporteHistorial()
                        View.reportesView.mostrarHistorial(lista)

                    elif opcionRep == 4: # Volver
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
            print("Error: Ingrese solo numeros")

if __name__ == "__main__":
    main()