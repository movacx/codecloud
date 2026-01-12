#Creando una lista con list()
lista = list(["Hola", "Fabian", 19, 0.3, 22, True])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agrega un elementos a la lista
lista.append("Elemento añadido")

#agregando un elemento a la lista en un indice especifico
lista.insert(2, "Elemento ingresado en el indice (2)")

#agreegando varios elementos a la lista
lista.extend(["A1", "B1"])

#eliminando un elementos de la lista por su indice
lista.pop(0)

#removiendo un elemento de la lista por su valor
lista.remove(True)

#eliminando todos los elementos de la lista
#lista.clear()

print(lista)

#ordena la lista (si usamos el parametro reverse = true lo ordena en reversa)
segunda_lista = list([10,23,244,7,8])
segunda_lista.sort()
segunda_lista.reverse()

#esto es una dupla
print(dir((segunda_lista, 2)))

print(segunda_lista)