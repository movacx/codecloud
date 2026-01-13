#Cree un programa que reciba una palabra y cuente cuántas veces aparece cada vocal.

palabra_ingresada = input("Ingrese una palabra: ").lower()
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contadur_u = 0

for letra in palabra_ingresada:
    if letra == 'a':
        contador_a += 1
    elif letra == 'e':
        contador_e += 1
    elif letra == 'i':
        contador_i += 1
    elif letra == 'o':
        contador_o += 1
    elif letra == 'u':
        contadur_u +=1

print(f"La cantidad usada de la vocal A fue de: {contador_a}")
print(f"La cantidad usada de la vocal E fue de: {contador_e}")
print(f"La cantidad usada de la vocal I fue de: {contador_i}")
print(f"La cantidad usada de la vocal O fue de: {contador_o}")
print(f"La cantidad usada de la vocal U fue de: {contadur_u}")
