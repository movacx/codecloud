

while True:
    nombre = input('Ingrese un nombre de usuario: ')
    

    cantidad_palabras = len(nombre)

    if cantidad_palabras <= 5:
        print('Nombre invalido, debe de ingresar un nombre con mas de 6 letras')
    elif ' ' in nombre: #Esto es para evitar que hayan espacios, el enunciado lo pedia
        print('No pueden haber espacios')
    else:
        print('Nombre valido')
        break

 