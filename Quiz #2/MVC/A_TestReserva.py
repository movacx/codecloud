from Controller.huespedesController import HuespedesController
import View.huespedesView as vista
def main():
    manejoHuespedes = HuespedesController()

    cerrar = True
    while cerrar:
        try:
            print('1.add |2.List |3.Search |4.Modify |5.Delete |0.Salir')
            op = int(input('Input: '))
            if op == 1:
                nom = input('nombre: ')
                cell = int(input('telefono: '))
                manejoHuespedes.registrarHuesped(nom,cell)
                pass
            elif op == 2:
                manejoHuespedes.listarHuesped()
                pass
            elif op == 3:
                nombre_buscar = input('Nombre: ')
                manejoHuespedes.buscarHuesped(nombre_buscar)
                pass
            elif op == 4:
                id = int(input('Id: '))
                nom = input('nombre: ')
                cell = int(input('telefono: '))
                manejoHuespedes.modificarHuesped(id,nom,cell)
                pass
            elif op == 5:
                id = int(input('Id: '))
                manejoHuespedes.eliminarHuesped(id)
                pass
            elif op == 0:
                vista.mostrarMensaje('Saliendo..')
                cerrar = False
                break
            else:
                vista.mostrarMensaje("Opcion invalida")
        except ValueError:
            vista.mostrarMensaje('Ingrese opciones validas [0-5]\n')

if __name__ == '__main__':
    main()