list = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", True, 19, 0.5, 2003]
print(list[1]) #Accediendo a un elemento de la lista

tupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", False, 2024, 3, 14) #no permite modificar sus elementos
print(tupla[4]) #Accediendo a un elemento de la tupla

#creando un conjunto (set)
conjunto = {"Fabian", "Beita", 21, 1.66}
print(conjunto) #Los conjuntos no permiten elementos repetidos y no se pueden acceder por indice, se puede por un ciclo y son desordenados

#creando un diccionario (dict)
diccionario = {
    'nombre' : "Fabian",
    'apellido' : "Beita",
    'esta feliz' : True,
}
print(diccionario)
print("\n"+diccionario["nombre"])

