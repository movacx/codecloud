#Solicite una frase al usuario y determine la palabra más larga, mostrando también su longitud.

cadena_palabras = input("Dime lo que quieras y te calculo la longitud y la cantidad de palabras ingresadas: ")
longitud = len(cadena_palabras)
cantidad_palabras = len(cadena_palabras.split())

print(cadena_palabras.split())
print(f"La cantidad de caracteres es de {longitud} incluyendo espacios, y la cantidad de palabras ingresadas fue de {cantidad_palabras} palabras")
