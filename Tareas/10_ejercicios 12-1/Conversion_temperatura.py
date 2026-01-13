#Cree un programa que solicite al usuario una temperatura en grados Celsius y muestre su equivalente en grados Fahrenheit utilizando la fórmula:

solicitud_temperatura_c = int(input("Ingrese la temperatura en Celsius para convertirla a Fahrenheit "))
convertir_faren = solicitud_temperatura_c*9//5+32
print(f"{convertir_faren}ª Fahrenheit")


#Se le solicita al usuario que ingrese una temperatura seguidamente cree una variable para que contenga la conversion de c a f y el // es para que no me de
#numeros inecesarios como esos decimales 95,80 y que quede en 95f
#osea devuelve un dato int, redondeando ejemplo 12/5 = 2.4 devuelve 2
