from ObjetoReservacion import Cliente
import manejoReservacion

contador = 0
while contador <= 0:
    print("""
Seleccione una opcion
1. Agregar una reservacion
2.
0. Salir""")
#Cliente(nombre_cliente, noches, costoPor_noche, tipo_habitacion, costo_total)
    opcion = int(input("input: "))
    if opcion == 0:
        print("Saliendo....")
        contador = -1
        break
    elif opcion == 1:
        nombre = int(input("input: "))
        noches = int(input("input: "))

        