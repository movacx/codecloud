from Controller.huespedesController import HuespedesController
import View.huespedesView as vista
def main():
    manejoHuespedes = HuespedesController()

    cerrar = True
    while cerrar:
        print('1.add|2.List|3.Search|4.Modify|4.Delete|0.Salir')
        op = int(input('Input: '))

        if op == 1:
            nom = input('nombre: ')
            cell = int(input('telefono: '))
            manejoHuespedes.registrarHuesped(nom,cell)
            pass
        elif op == 2:
            manejoHuespedes.listarTodos()
            pass
        elif op == 3:
            pass
        elif op == 0:
            cerrar = False
            break
        else:
            vista.mostrarMensaje("Opcion invalida")

if __name__ == '__main__':
    main()