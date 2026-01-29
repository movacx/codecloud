from Controller.gastosController import GastosController

def main():
	#Instancia
	manejadorGastos = GastosController()
	while True:
		op = int(input("""--MAIN MENU--
	1.Registrar Gasto.
	2.Ver Gastos
	3.Ver Total Gastado
	4.Eliminar Gasto
	0.Salir
Input: """))
		
		if op == 1:
			descripcion = input("Digite la descripcion del gasto: ")
			monto = int(input("Digite el monto del gasto: "))
			categoria = input("Digite la categoria del gasto: ")
			fecha = input("Digite la fecha del gasto: ")
			manejadorGastos.guardarGasto(descripcion, monto, categoria, fecha)
		elif op== 2:
			manejadorGastos.listarGastos()
		elif op== 3:
			manejadorGastos.VerTotal()
		elif op == 4:
			pass
		elif op== 0:
			pass

		
		else:
			print("Opcion invalida")
	
	
	
	
	
	
	
	
	




if __name__ == "__main__":
	main()