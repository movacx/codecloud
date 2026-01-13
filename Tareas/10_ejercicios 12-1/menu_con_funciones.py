#Implemente un menú con:
    #1. Saludar 2. Sumar dos números 3. Salir

contador = 0
while contador != 3:
    print("\nMenu Principal",
        "\n1. Saludar",
        "\n2. Sumar dos numeros",
        "\n3. Salir")
    opcion_menu = int(input("Seleccion una opcion [1-3]: "))
    
    if opcion_menu == 1:
        print("Hola!")
    elif opcion_menu == 2:
        num_uno = int(input("Ingrese el primer valor: "))
        num_dos = int(input("Ingrese el primer valor: "))
        resultado = num_uno + num_dos
        print(f"El resultado de la suma fue de: {resultado}")
    elif opcion_menu == 3:
        break
    else:
        print("Seleccione una opcion valida")
    
    
#me quedo fino, no hace falta explicacion se entiende muy bien