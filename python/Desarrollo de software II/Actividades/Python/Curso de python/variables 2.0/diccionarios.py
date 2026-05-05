#Creando diccionarios con dict()
diccionario = dict(nombre="lucas",apellido="dalto")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["Fabian","rancio"]): "Test"}

#creando diccionarios con fromkeys()
diccionario = dict.fromkeys(["nombre","apellido","suscriptores"])

#creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido",],"no se")

print(diccionario)