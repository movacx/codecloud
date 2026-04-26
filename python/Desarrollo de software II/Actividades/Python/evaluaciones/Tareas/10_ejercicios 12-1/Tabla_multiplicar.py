#Cree una función tabla(n) que muestre la tabla de multiplicar del número n del 1 al 10.
#uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve,diez = valores
#print(uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve,diez)

valores = [1,2,3,4,5,6,7,8,9,10]
lista_resultado = list([])

def tabla_multiplicar(numero):
    for indice in range(len(valores)):
        resultado = valores[indice] * numero
        lista_resultado.append(resultado)
    return lista_resultado

multiplicando = int(input("¿Cual tabla de multiplicar desea visualizar?: "))
print(tabla_multiplicar(multiplicando))
 
    
#Explicacion: En este caso lo que hice fue recorrer la lista valores e ir multiplicando los indices que contiene la lista indice * el numero que se recibe en la
#funcion tabla_multiplicar, el resultado de esa multiplicacion se guarda en una nueva lista llamada lista_resultado y despues se imprime normal