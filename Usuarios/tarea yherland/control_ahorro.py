contador_dias = 0
contador_ahorro_total = 0


while True:
    opcion = int(input('''
1. Ingresar dias a registrar
2. Ingresar ahorro de cada dia
3. Revisar promedio de ahorro
4. Validar tipo de ahorro. 
0. Salir
Input: '''))
    
    if opcion == 1:
        dias_registrar = int(input('Ingrese los dias que vas a registrar: '))
        contador_dias += dias_registrar
        pass
    elif opcion == 2:
        ahorro = int(input('Ingrese el ahorro del dia: '))
        contador_ahorro_total += ahorro
        pass
    elif opcion == 3:
        promedio = contador_dias * contador_ahorro_total
        print('El promedio de ahorro es de: ', promedio)
        pass

    elif opcion == 4:
        if promedio < 5000:
            print('Ahorro bajo, es menor que 5000')
        elif promedio >= 5000 and promedio < 15000:
            print('Ahorro medio, el promedio esta entre 5000 y 15000')
        else:
            print('Ahorro alto, el promedio supera los 20.000')
    elif opcion == 0:
        break
