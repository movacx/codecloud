from Controller.habitacionesController import HabitacionesController
import View.huespedesView as vista


def menuHabitaciones():
	baseHabitaciones = HabitacionesController()
	
	cerrar = True
	while cerrar:
		try:
			print("1.agregar/2.Listar/3.Buscar/4.Cambiar estado/5.Ordenado por precio/6.Eliminar Habitacion")
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
			
if __name__ == "__main__":
	menuHabitaciones()
		
		