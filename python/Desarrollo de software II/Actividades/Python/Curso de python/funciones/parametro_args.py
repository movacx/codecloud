#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])
resultado2 = suma_total([5,2,3,5,7,22])
print(resultado2)

#Lo mismo que lo de arriba pero utilizando el operador * como parametro (args)
def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"
resultado = suma("Lucas",3,54,7,8,4)
print(resultado)

#forma no optima de sumar valores
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados

resultado3 = suma([5,2,3,2])
print(resultado3)