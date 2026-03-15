#Solicite al usuario ingresar 5 nombres y guárdelos en una lista. Luego muestre:
lista_nombres = list([])

contador = 0
while contador < 5:
    registrar_nombres = input("Ingrese 5 nombres a registrar: ")
    lista_nombres.append(registrar_nombres)
    contador +=1
    
cantidad_lista = len(lista_nombres)
print(f"\n{lista_nombres}")
print(f"{lista_nombres[0]}, se ubica en la posicion [0]")
print(f"{lista_nombres[4]}, se ubica en la posicion [4]")
print(f"La lista contiene {cantidad_lista} nombres")


#Al momento de hacer esto vi la necesidad de crear una lista en vacio para ir añadiendo los nombres, con el while repito el input sin la necesidad de
#repetirlo 4 veces mas el append es para añadir un elemento a la lista y ya despues se imprime