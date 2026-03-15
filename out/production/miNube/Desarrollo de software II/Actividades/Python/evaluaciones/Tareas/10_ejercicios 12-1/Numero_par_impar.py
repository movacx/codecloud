#Cree una función llamada es_par(numero) que retorne True si el número es par y False si es impar.
#Solicite un número al usuario y muestre el resultado.

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
ingreso_numero = int(input("Ingrese un numero"))
print(es_par(ingreso_numero))

