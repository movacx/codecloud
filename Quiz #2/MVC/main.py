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
            4. Reportes
            5. Salir
            """)

        op = input("Seleccione: ")
        if op == "1":
            menuHabitaciones()
        elif op == "2":
            menuHuespedes()

        elif op == "3":
            menuReservas()

        elif op == "4":
            pass

        elif op == "5":
            break
        else:
            vista.mostrarMensaje('opcion invalida')


#|-Menus
#|Habitaciones = David mora
#|Huespedes = Herlin Chavarria
#|Reservas = Joseph Campos

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
            print('1.agregar reservacion |2.Lista de reservaciones |3. |4.Modificar reservaciones |5.eliminar reservacion |0.Salir')
            op = int(input('Input: '))
            if op == 1:
                id_habitacion = int(input('Id habitacion: '))
                id_huesped = int(input('Id huesped: '))
                fecha_entrada = input('Fecha entrada (YYYY-MM-DD): ')
                fecha_salida = input('Fecha salida (YYYY-MM-DD): ')
                baseReserva.crear_reserva(id_habitacion, id_huesped, fecha_entrada, fecha_salida)
                pass
            elif op == 2:
                baseReserva.listar_reservas()
                pass
            elif op == 3:
                id_reserva = int(input('Id reserva: '))
                baseReserva.buscar_reserva(id_reserva)
                pass
            elif op == 4:
                id_reserva = int(input('Id reserva: '))
                id_habitacion = int(input('Id habitacion: '))
                id_huesped = int(input('Id huesped: '))
                fecha_entrada = input('Fecha entrada (YYYY-MM-DD): ')
                fecha_salida = input('Fecha salida (YYYY-MM-DD): ')
                baseReserva.modificar_reserva(id_reserva, id_habitacion, id_huesped, fecha_entrada, fecha_salida)
                pass
            elif op == 5:
                id_reserva = int(input('Id reserva: '))
                baseReserva.eliminar_reserva(id_reserva)
                pass
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
