

while True:
    opcion = int(input('''
1. Convertir kilometros a metros
2. Convertir metros a centimetros
3. Convertir kilogramos a gramos
4. Convertir litros a mililitros
5. Salir
Input: '''))
    
    if opcion == 1:
        metros_convertidos = float(input('Ingrese los kilometros a convertir: '))
        resultado = metros_convertidos * 1000
        print('La convercion a metros es de: ', resultado, 'm')
        pass
    elif opcion == 2:
        centimetros_convertidos = float(input('Ingrese los Metros a convertir: '))
        resultado = centimetros_convertidos * 100
        print('La conversion a centimetros es de: ', resultado, 'cm')
        pass
    elif opcion == 3:
        gramos_convertidos = float(input('Ingrese los kilogramos a convertir: '))
        resultado = gramos_convertidos * 1000
        print('La conversion a gramos es de: ', resultado, 'g')
        pass
    elif opcion == 4:
        mililitros_convertidos = float(input('Ingrese los mililitros a convertir: '))
        resultado = mililitros_convertidos * 1000
        print('La conversion a mililitros es de: ', resultado, 'ml')
        pass
    elif opcion == 5:
        print('Saliendo.')
        break