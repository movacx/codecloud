from model.canchaModel import CanchaModel
import data.baseCancha as file_csv
import view.canchaView as vista
class CanchaController:
    
    def __init__(self):
        pass
    
#-------------------------------------------------------------------------#    
    def agregarListado(self,numero,tipo,tarifa_hora,estado):
        nueva_cancha = CanchaModel(numero,tipo,tarifa_hora,estado)
        file_csv.addList(nueva_cancha)
#-------------------------------------------------------------------------#        
    def listarCanchas(self):
        listado = file_csv.searchList()
        vista.imprimirListados(listado)
        