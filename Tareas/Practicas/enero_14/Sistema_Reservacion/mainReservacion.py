#importar los metodos que tengo en manejoReservacion.py



contador = 0
while contador <= 0:
    print("""
Seleccione una opcion
1. Agregar una reservacion
2.
0. Salir
    """)
    
    opcion = int(input("input: "))
    if opcion == 0:
        print("Saliendo....")
        contador = -1
        break
    