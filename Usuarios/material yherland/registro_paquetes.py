total_paquetes_registrados = 0
cantidad_paquetes_livianos = 0
cantidad_paquetes_medianos = 0
cantidad_paquetes_pesados = 0


while True:
    opcion = int(input('''
1. Registrar la cantidad de paquetes
2. Registrar peso de cada paquete
3. Mostrar Total de paquetes registrados
4. Mostrar Cantidad de paquetes livianos
5. Mostrar Cantidad de paquetes medios
6. Mostrar Cantidad de paquetes pesados
0. Salir
input: '''))
    
    if opcion == 1:
        registro_paquetes = int(input('Ingrese la cantidad de paquetes a registrar: ')) #100
        total_paquetes_registrados += registro_paquetes

    elif opcion == 2:
        peso_paquete = float(input('Ingrese el peso del paquete: ')) #8

        if peso_paquete < 2:
            print('peso liviano, menor a 2 kilos')
            cantidad_paquetes_livianos += 1

        elif peso_paquete >= 2 and peso_paquete < 5:
            print('peso mediano, entre 2 y 5kilos')
            cantidad_paquetes_medianos += 1

        else:
            print('paquete pesado, mayor a 5kl')
            cantidad_paquetes_pesados += 1
        
    elif opcion == 3:
        print(total_paquetes_registrados)

    elif opcion == 4:
        print(cantidad_paquetes_livianos)

    elif opcion == 5:
        print(cantidad_paquetes_medianos)

    elif opcion == 6:
        print(cantidad_paquetes_pesados)

    elif opcion == 0:
        break
