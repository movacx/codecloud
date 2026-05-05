clave_correcta = 4321 #Esta es la llave que nos permite el acceso
contador_intentos = 3 #Esto es el numero de intentos que el sistema va a permitir

for i in range(3):
    contador_intentos -= 1
    contrase_ingresada = int(input('Ingrese la password: ')) #4321

    if contrase_ingresada != clave_correcta: #Diferente de
        print('Clave incorrecta le quedan ', contador_intentos, 'intentos')

        if contador_intentos == 0:
            print('Acceso bloqueado.')
            break
    else:
        print('Acceso permitido')
        break
    
