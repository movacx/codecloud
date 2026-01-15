from ObjetoReservacion import Cliente
import manejoReservacion

contador = 0
while contador <= 0:
    print("""
Seleccione una opcion
1. Agregar una reservacion
2. Buscar reservacion por id
0. Salir""")
#Cliente(nombre_cliente, noches, costoPor_noche, tipo_habitacion, costo_total)
    opcion = int(input("input: "))
    if opcion == 0:
        print("Saliendo....")
        contador = -1
        break
    elif opcion == 1:
        manejoReservacion.agregarCliente("Fabian", 2, False)
        manejoReservacion.agregarCliente("Herlin", 2, True)
        continue
    elif opcion == 2:
        buscarId = int(input("Ingrese el numero de reservacion a encontrar al cliente: "))
        searchName = input("Ingrese el nombre del cliente a encontrar al cliente: ")
        buscar = manejoReservacion.buscarID(buscarId)
        searchName = manejoReservacion.buscar(searchName)
        print(searchName)
        print(buscar)
        print(Cliente.mostrarDatos)
        continue
    elif opcion == 3: # Supongamos que es una opción nueva
            nombre = input("Ingrese nombre a buscar: ")
            
            # MAGIA DE PYTHON: "Desempaquetamos" los dos resultados en dos variables
            objeto_encontrado, indice_encontrado = manejoReservacion.buscar_cliente_completo(nombre)
            
            if indice_encontrado != -1:
                print(f"✅ ¡Encontrado en la posición {indice_encontrado}!")
                print("Datos del cliente:")
                
                # Como 'objeto_encontrado' es el OBJETO completo, puedes usar sus métodos
                print(objeto_encontrado) # Esto usa tu __str__
                
                # O puedes usar su método mostrarDatos()
                # objeto_encontrado.mostrarDatos()
            else:
                print("❌ Cliente no encontrado.")
    



