from Model.inventarioModel import Inventario
from Model.productosModel import Productos
import View.bodegaView as vista


while True:
	try:
		vista.mostrarMenu()
		opcion = int(input("Input: "))
		if opcion == 1:
			continue
		elif opcion == 2:
			continue
		elif opcion == 3:
			continue
		elif opcion == 4:
			break
		else:
			vista.mostrarMensaje("Opcion Invalida")
		
	except ValueError:
		print("Solo se aceptan numeros")
