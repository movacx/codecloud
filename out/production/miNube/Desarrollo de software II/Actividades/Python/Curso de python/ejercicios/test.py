datos = [1,2,3,100,4,5,8]

def encontrar(datos):
    maximo = datos[0]
    minimo = datos[0]

    for i in range(len(datos)):
        if datos[i] > maximo:
            maximo = datos[i]
        elif datos[i] < minimo:
            minimo = datos[i]
    return maximo,minimo
    
maximo,minimo = encontrar(datos)
print(f"el valor maximo de la lista es: {maximo}")
print(f"el valor minimo de la lista es {minimo}")
