#Cuaderno de notas:
# keys()    ->  devuelve las claves (tambien nos sirve para iterar)
# get()     ->  devuelve el valor de una clave
# clear()   ->  elimina todos los elementos
# pop()     ->  elimina un elemento
# items()   ->  para iterar el diccionario
#iterar es recorrer los elementos

diccionario = {
    "nombre" : "Fabian",
    "apellido" : "Beita",
    "edad" : 22
}
#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniuendo un elemento con get(si no encuentra nada el programa continua)
valor_de_kkkk = diccionario.get("kkkk")

#eliminando todo el diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("nombre","edad")

#obteniendo un elemento dict_items iterable

diccionario_iterable = diccionario.items()


print(diccionario_iterable)







