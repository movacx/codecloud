#El Controlador (Controller/gastosController.py),
#El cerebro. Aquí debe conectar todo.
#    Método agregar_gasto:
#        Debe validar que el monto sea mayor a cero (no existen gastos negativos).
#        Debe crear el objeto Gasto.
#        Debe mandarlo a baseGastos.
#    Método ver_mis_gastos:
#        Pide la lista a la base.
#        Si está vacía, manda error a la vista.
#        Si hay datos, se los pasa a la vista.
#     El Reto Especial (Lógica de Negocio):
#        Dile que cree un método ver_total_gastado().
#       Este método debe pedir la lista a la base, recorrerla con un for, sumar todos los montos y decirle a la vista: "Has gastado un total de: ₡XXXXX".


from model.gastosModel import GastosModel
import view.gastoView as vista
import data.gastosData as file_csv

class GastosController:
    def __init__(self):
        pass
#‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾#
    def registrarGasto(self, descripcion, monto, categoria, fecha):
        nuevo_gasto = GastosModel(0,descripcion, monto, categoria, fecha)
        file_csv.addList(nuevo_gasto)
        vista.mostrarMensaje('Agregado correctamente!')
        return
#‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾#
    def verGastos(self):
        arreglo = []
        arreglo = file_csv.searhList()
        
        vista.mostrarListados(arreglo)
        
#‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾#
        
    def ver_total_gastado(self):
        almacen_datos = []
        almacen_datos = file_csv.searhList()
        
        total = 0
        
        for items in almacen_datos:
            if items:
                total += items[2]
        
        return vista.mostrarMensaje(f'Total gastado: {total}')
    
#‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾#
    def eliminarGasto(self, id):
        datos_eliminados = file_csv.deleteList(id)
        return datos_eliminados
        
                
    def ordenar(self):
        lista = file_csv.ordenarPrecios()
        vista.mostrarListados(lista)
        
    def ordenarMayor(self):
        lista= file_csv.ordenarPreciosMayor()
        vista.mostrarListados(lista)
        
        
        
        