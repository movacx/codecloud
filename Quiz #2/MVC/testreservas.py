from Controller.reservasController import ReservasController
import View.huespedesView as vista # O View.reservasView si ya creaste el especifico

def menuReservas():
    baseReserva = ReservasController()
    cerrar = True
    while cerrar:
        try:
            # Mismo estilo visual que menuHuespedes
            print('1.Add | 2.List | 3.Search | 4.Modify | 5.Delete | 0.Salir')
            op = int(input('Input: '))

            if op == 1: # Agregar
                try:
                    hab = int(input('Numero Habitacion: '))
                    hue = int(input('Id Huesped: '))
                    ent = input('Fecha Entrada (YYYY-MM-DD): ')
                    sal = input('Fecha Salida (YYYY-MM-DD): ')
                    baseReserva.crear_reserva(hab, hue, ent, sal)
                except ValueError:
                    vista.mostrarMensaje("Error: Habitacion y Huesped deben ser numeros")

            elif op == 2: # Listar
                baseReserva.listar_reservas()

            elif op == 3: # Buscar
                id_reserva = int(input('Id Reserva a buscar: '))
                # Asegurate de tener este metodo en el controller, si no, avisame
                baseReserva.buscar_reserva(id_reserva) 

            elif op == 4: # Modificar
                id_reserva = int(input('Id Reserva a modificar: '))
                hab = int(input('Nuevo Num Habitacion: '))
                hue = int(input('Nuevo Id Huesped: '))
                ent = input('Nueva Entrada: ')
                sal = input('Nueva Salida: ')
                # Asegurate de tener este metodo en el controller
                baseReserva.modificar_reserva(id_reserva, hab, hue, ent, sal)

            elif op == 5: # Eliminar
                id_reserva = int(input('Id Reserva a eliminar: '))
                baseReserva.eliminar_reserva(id_reserva)

            elif op == 0: # Salir
                vista.mostrarMensaje("Saliendo..")
                cerrar = False
                break

            else:
                vista.mostrarMensaje("Opcion invalida")

        except ValueError:
            vista.mostrarMensaje("Ingrese opciones validas [0-5]\n")

if __name__ == "__main__":
    menuReservas()