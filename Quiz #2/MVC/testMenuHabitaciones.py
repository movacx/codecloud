from Controller.habitacionesController import HabitacionController
import View.huespedesView as vista


def main():
	baseHabitaciones = HabitacionController()
	
	cerrar = True
	while cerrar:
		print("1.agregar/2.Listar/3.Buscar/4.Cambiar estado/5.Ordenado por precio")
		op = int(input("Input: "))
		if op ==1:
			numero = input("Numero de habitacion: " )
			tipo = input("Tipo de habitacion: ")
			precio = int(input("Precio: ")) #precio: input("Precio: ") 
			estado = input("Estado: ") #estado: input("Estado: ")
			baseHabitaciones.registrarHabitacion(numero, tipo, precio, estado)
			
		elif op == 2:
			baseHabitaciones.listarHabitaciones()
		elif op ==3:
			baseHabitaciones.imprimir("Hola")
		elif op == 4:
			pass
		elif op ==5:
			pass
		elif op == 0:
			cerrar = False
			break
		else:
			vista.mostrarMensaje("Opcion invalida") #vista,mostrarMensaje("Opcion invalida")
			
if __name__ == "__main__":
	main()
		
		