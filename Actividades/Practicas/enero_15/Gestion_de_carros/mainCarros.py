#Herlin Fabian Chavarria Beita C5E187
import manejadorCarros

contador = 0
while contador <= 0:
    opcion = int(input("""
Menu Principal
1. Registrar Vehiculos.
2. Mostrar vehiculos registrados
3. Buscar vehiculos por id
4. Modificar vehiculo por id.
5. Eliminar un carro por su ID.
0. Salir
input: """))
    if opcion == 1:
        manejadorCarros.registrarVehiculo("Hyundai", "Verna", "Turqueza", "BBZ880")
        manejadorCarros.registrarVehiculo("Toyota", "Corolla", "Blanco", "LOD187")
        print("Vehiculos registrado!")
    elif opcion == 2:
        print(manejadorCarros.mostrarVehiculos())
        
        continue
    elif opcion == 3:
        buscarId = int(input("Ingrese el identificador del vehiculo a buscar: "))
        print(manejadorCarros.buscarVehiculo(buscarId))
        continue
    elif opcion == 4:
        buscarV = int(input("Ingrese el identificador del vehiculo a encontrar: "))
        
        print("""
              1. Modificar Marca
              2. Modificar Modelo
              3. Modificar Color
              4. Modificar Placa
              0. Volver
              """)
        seleccion = int(input("Input: ")
                        )
        if seleccion == 1:
            nuevoDato = input("Ingrese el nuevo dato a registrar: ") 
            print(manejadorCarros.modificarDatos(buscarV, nuevoDato, seleccion))
        elif seleccion == 2:
            nuevoDato = input("Ingrese el nuevo dato a registrar: ") 
            print(manejadorCarros.modificarDatos(buscarV, nuevoDato, seleccion))
        elif seleccion == 3:
            nuevoDato = input("Ingrese el nuevo dato a registrar: ") 
            print(manejadorCarros.modificarDatos(buscarV, nuevoDato, seleccion))
        elif seleccion == 4:
            nuevoDato = input("Ingrese el nuevo dato a registrar: ") 
            print(manejadorCarros.modificarDatos(buscarV, nuevoDato, seleccion))
        elif seleccion == 0:
            continue
        else:
            print("Opcion invalida [Valores dentro de 1-4]")
        
        
    elif opcion == 5:
        print(manejadorCarros.mostrarVehiculos())
        eliminarVehiculo = int(input("Ingrese el identificador del vehiculo a eliminar: "))
        print(manejadorCarros.eliminarVehiculo(eliminarVehiculo))
        continue
    elif opcion == 0:
        print("Saliendo del sistema")
        break
    else:
        print("Opcion Invalida [Opciones validas: 1-5]")
    