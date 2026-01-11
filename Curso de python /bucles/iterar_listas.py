#Recordatorio = iterar significa recorrer en este caso recorrer los indices de la lista por medio de un for

animales = list(["gato","perro","loro","cocodrilo"])
numeros = [1,2,3,4] 
numerosDos = list([11,22,33,44,55,6])
#recorriendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')
    
#recorriendo la lista numeros y multiplicando cada valor por 2
for contador in numeros:
    resultado = contador*2
    print(f'Valor: {resultado}')
    
#bucle de numeros
#for num in range(10):
#    print(num)
    
#forma optima y no de recorrer una lista con su indice
print("\nForma no optima de recorrer una lista:\n")
for numm in range(len(numerosDos)):
    print(f"el indice es: {numm} y el valor es: {numerosDos[numm]}")
    
    #________________________________________________________________________________________________________
    
print("\nforma optima de recorrer una lista con su indice")
for num in enumerate(animales):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")