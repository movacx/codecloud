#calculadoraController.py
#En el controller se realiza la logica para que las funciones se ejecuten que conecta con el view y el model
#como hacemos la conexion, importando carpeta/archivo

#import model.calculadoraModell
from model.calculadoraModell import calculadoraModell
from view.calculadoraView import calculadoraView

#calculadoraController.py
class calculadoraControllesr:
    
    def agregarDatos(self, datoa, datob):
        _calculadoraModell = calculadoraModell(datoa, datob)
    
    def presentarDatos(self, calculadoraModell):
        calculadoraView.prestardatos(calculadoraModell)