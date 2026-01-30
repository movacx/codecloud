import view.gastoView as vista
from controller.gastosController import GastosController

def main():
    manejo_gastos = GastosController()
    x = True

    while x:
        try:
            vista.mostrarMenu()
            op = int(input('input: '))
            
            if op == 1:
                descripcion = input('Descripcion: ')
                monto = input('Monto: ')
                categoria = input('Categoria: ')
                fecha = input('Fecha: ')
                manejo_gastos.registrarGasto(descripcion, monto, categoria, fecha)
                pass
            elif op == 2:
                manejo_gastos.verGastos()
                pass
            elif op == 3:
                manejo_gastos.ver_total_gastado()
                pass
            elif op == 4:
                ide = int(input('Id:'))
                manejo_gastos.eliminarGasto(ide)
                pass
            elif op == 5:
                manejo_gastos.ordenar()
                pass
            elif op == 6:
                manejo_gastos.ordenarMayor()
            else:
                vista.mostrarMensaje('Opcion invalida')
        except ValueError:
            vista.mostrarMensaje('Caracteres no validos')

if __name__ == '__main__':
    main()
        
        
        