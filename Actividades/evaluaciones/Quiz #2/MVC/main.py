from Controller.habitacionesController import HabitacionesController
import View.huespedesView as vista
from Controller.huespedesController import HuespedesController
import View.huespedesView as vista
from Controller.reservasController import ReservasController
import View.huespedesView as vista 


def main():

    while True:
        print("""
            === SISTEMA DE CONDOMINIOS COSTAMAR ===
            1. Gestión de Habitaciones
            2. Gestión de Huéspedes
            3. Gestión de Reservas
            4. Salir
            """)

        op = input("Seleccione: ")
        if op == "1":
            menuHabitaciones()
        elif op == "2":
            menuHuespedes()

        elif op == "3":
            menuReservas()

        elif op == "4":
            break
        else:
            vista.mostrarMensaje('opcion invalida')

#|-Particiones-
#|Habitaciones = David mora C5H441
#|Huespedes = Herlin Chavarria C5E187
#|Reservas = Joseph Campos C4D660

#-------------------------------------------[MENU DE HABITACIONES!]----------------------------------------------------------------#
def menuHabitaciones():
	baseHabitaciones = HabitacionesController()
	
	cerrar = True
	while cerrar:
		try:
			print("1.agregar/2.Listar/3.Buscar/4.Cambiar estado/5.Ordenado por precio/6.Eliminar Habitacion/0.Salir")
			op = int(input("Input: "))
			print("--------------------------------------------------")
			if op ==1:
				numero = input("Numero de habitacion: " )
				tipo = input("Tipo de habitacion: ")
				precio = int(input("Precio: ")) #precio: input("Precio: ") 
				estado = input("Estado: ") #estado: input("Estado: ")
				baseHabitaciones.registrarHabitacion(numero, tipo, precio, estado)
				
			elif op == 2:
				baseHabitaciones.listarHabitacion()
			elif op ==3:
				idHabitacion= int(input("Digite el ID de la habitacion: "))
				baseHabitaciones.buscarHabitacionId(idHabitacion)
			elif op == 4:
				idHabitacion = int(input("Digite el ID de la habitacion a modificar el estado: "))
				estado = input("¿A que estado desea cambiar la habitacion?\n")
				baseHabitaciones.modificarEstado(idHabitacion, estado)
				pass
			elif op ==5:
				baseHabitaciones.ordenarPorPrecio()
			elif op == 6:
				idHabitacion = int(input("Digite el ID de la habitacion a eliminar: "))
				baseHabitaciones.eliminarHabitacion(idHabitacion)
			elif op == 0:
				cerrar = False
				break
			else:
				vista.mostrarMensaje("Opcion invalida") #vista,mostrarMensaje("Opcion invalida")
		except ValueError:
			vista.mostrarMensaje('-----------------------------------------\nIngrese opciones validas [0-5]\n-----------------------------------------')
			
#-------------------------------------------[MENU DE Huespedes!]----------------------------------------------------------------#
def menuHuespedes():
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

#-------------------------------------------[MENU DE Reservas!]----------------------------------------------------------------#
def menuReservas():
    baseReserva = ReservasController()
    cerrar = True
    while cerrar:
        try:
            print('\n--- GESTIÓN DE RESERVAS ---')
            print('1.Add | 2.List | 3.Search | 4.Modify | 5.Delete | 0.Salir')
            op = int(input('Input: '))

            if op == 1: 
                try:
                    hab = int(input('Numero Habitacion: '))
                    hue = int(input('Id Huesped: '))
                    ent = input('Fecha Entrada: ')
                    sal = input('Fecha Salida: ')
                    baseReserva.crear_reserva(hab, hue, ent, sal)
                except ValueError:
                    vista.mostrarMensaje("Error: Habitacion y Huesped deben ser numeros")

            elif op == 2: 
                baseReserva.listar_reservas()

            elif op == 3: 
                id_reserva = int(input('Id Reserva a buscar: '))
                baseReserva.buscar_reserva(id_reserva) 

            elif op == 4: 
                id_reserva = int(input('Id Reserva a modificar: '))
                hab = int(input('Nuevo Num Habitacion: '))
                hue = int(input('Nuevo Id Huesped: '))
                ent = input('Nueva Entrada: ')
                sal = input('Nueva Salida: ')
                baseReserva.modificar_reserva(id_reserva, hab, hue, ent, sal)

            elif op == 5:
                id_reserva = int(input('Id Reserva a eliminar: '))
                baseReserva.eliminar_reserva(id_reserva)

            elif op == 0:
                vista.mostrarMensaje("Saliendo..")
                cerrar = False
                break

            else:
                vista.mostrarMensaje("Opcion invalida")

        except ValueError:
            vista.mostrarMensaje("Ingrese opciones validas [0-5]\n")

#-------------------------------------------[Fin!]----------------------------------------------------------------#

if __name__ == "__main__":
    main()
