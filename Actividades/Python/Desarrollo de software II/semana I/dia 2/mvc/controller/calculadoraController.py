#calculadoraController.py

#logica, para que las funciones se ejecuten.
#que conecta el view y el model.

#como hacemos la conexion, importando
#     carpeta/archivo

#import model.calculadoraModell
from model.calculadoraModell import calculadoraModell
import view.calculadoraView as _calculadoraView

class calculadoraController:
    
    def agregardatos(self, datoa, datob):
        _calculadoraModell = calculadoraModell(datoa, datob)
        return _calculadoraModell

    def presntardatos(self, _calculadoraModell):
        _calculadoraView.presntardatos(_calculadoraModell)

   
    def operaciones(self, _calculadoraModell, opcion):
        resultado = 0
        
        if opcion == 1:            
            resultado = _calculadoraModell.sumar()
            _calculadoraView.mostraResultado("suma", resultado)

        elif opcion == 2:            
            resultado = _calculadoraModell.resta()
            _calculadoraView.mostraResultado("Resta", resultado)
            
        elif opcion == 3:         
            resultado = _calculadoraModell.multiplicar()
            _calculadoraView.mostraResultado("Multiplicacion", resultado)

        elif opcion == 4:           
            resultado = _calculadoraModell.dividir()
            _calculadoraView.mostraResultado("Division", resultado)
            
        else:
            print("Opcion invalida")