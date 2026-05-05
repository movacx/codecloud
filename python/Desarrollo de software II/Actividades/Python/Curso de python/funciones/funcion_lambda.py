#Lamba es crear una funcion anonima
numeros= [1,2,3,4,5,6,7,8,9]
#creando una funcion lambda para multiplicar por dos
multiplicar_por_dos = lambda x : x*2
print(multiplicar_por_dos(5))

#creando funcion comun que diga si es par o no
def es_par(num):
    if(num%2==0):
        return True

#usando filtrer con una funcion comun
numeros_pares = filter(es_par,numeros)
print(list(numeros_pares))

#creando lo mismo que antes pero con lambda y con numeros impares
lista_de_numeros = [12,13,14,15]
numeros_impares = filter(lambda lista_de_numeros : lista_de_numeros %2 == 1, lista_de_numeros)
print(list(numeros_impares))