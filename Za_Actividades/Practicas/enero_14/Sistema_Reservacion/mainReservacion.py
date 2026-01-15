from ObjetoReservacion import Cliente
import manejoReservacion

contador = 0
while contador <= 0:
    print("""
Seleccione una opcion
1. Agregar una reservacion
2. Buscar reservacion por nombre
3. Buscar reservacion por #Reservacion
4. Buscar reservacion por indice[0-#]
5. Eliminar reservacion
6. Mostrar listado de reservaciones
7. Modificar reservacion
0. Salir""")

    opcion = int(input("input: "))
    if opcion == 0:
        print("Saliendo....")
        contador = -1
        break
    
    elif opcion == 1:
        manejoReservacion.agregarCliente("Fabian", 2, False)
        manejoReservacion.agregarCliente("Herlin", 4, True)
        continue
    elif opcion == 2:
        encontrarCliente = input("Ingrese el nombre del cliente: ")
        clienteEncontrado = manejoReservacion.buscarNombre(encontrarCliente)
        if clienteEncontrado != -1:
            print(clienteEncontrado)
        else:
            print(f"No se encontro {encontrarCliente}, en la base de datos")
        continue
    elif opcion == 3:
        numReservacion = int(input("Ingrese el numero de reservacion del cliente a buscar: "))
        print(manejoReservacion.buscarReservacion(numReservacion))
        continue
    elif opcion == 4:
        searchId = int(input("Ingrese un indice a buscar [0->#]: "))
        print(manejoReservacion.buscarIndice(searchId))
        continue
    elif opcion == 5:
        deleteReservacion = int(input("Ingrese el numero de reservacion del cliente a eliminar: "))
        print(manejoReservacion.eliminarReservacion(deleteReservacion))
    elif opcion == 6:
        manejoReservacion.mostrar()
        continue        
    elif opcion == 7:
        idReservacion = int(input("Ingrese el numero de reservacion del cliente a modificar: "))
        modificacion = input("Ingrese el nuevo nombre asignar: ")
        print(manejoReservacion.modificarCliente(idReservacion, modificacion))


