from model.gastosModel import GastoModel
import data.gastoData as data
import view.gastoView as vista

class GastoController:
    
#--------------------------------------------------------------------
    def registrarGasto(self, descripcion, monto, categoria, fecha):
        nuevoGasto=GastoModel(0,descripcion, monto, categoria, fecha)
        data.registrarListado(nuevoGasto)
        
#---------------------------------------------------------------------
        
    def listar(self):
        arreglo=data.listarTodos()
        for items in arreglo:
            print(items)
            
#-----------------------------------------------------------------------
    def eliminar(self, id):
        arregloEliminar=[]
        arregloEliminar=data.eliminarGasto(id)
        