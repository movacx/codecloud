#Cree un programa que solicite al usuario una temperatura en grados Celsius y muestre su equivalente en grados Fahrenheit utilizando la fórmula:

solicitud_temperatura_c = int(input("Ingrese la temperatura en Celsius "))
convertir_faren = solicitud_temperatura_c*9//5+32
print(convertir_faren)

solicitud_temperatura_f = int(input("Ingrese la temperatura en fahrenheit "))
convertir_cels = solicitud_temperatura_f*5/9-32
print(convertir_cels)