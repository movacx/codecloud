
for indice in range (4):
    try:
        password = input('Ingrese la contraseña: ')
    except ValueError:
        print('Caracteres invalidos, vuelva a intentarlo')