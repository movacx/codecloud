#Cree una función llamada es_par(numero) que retorne True si el número es par y False si es impar.
#Solicite un número al usuario y muestre el resultado.

def es_par(numero):
    if numero * 2:
        return "es par"
    else:
        return "no es par"
    
ingreso_numero = int(input("Ingrese un numero"))
print(es_par(ingreso_numero))

#se creo una funcion llamada es par la cual recibe por parametro un numero y este mismo numero se multiplica x 2 ya que todo numero multiplicado x 2 va a ser par
#y si no es asi no va a ser como el 3 por ejemplo y ya despues se imprime