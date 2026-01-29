#Creando las listas
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "Hola"
numeros = [2,5,8,10]
numeros_dos = [5,2,9,12]

#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == "ciruela":
        continue
    print(f"Me voy a comer una {fruta}")

#evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for numerot in numeros_dos:
    print(f"numero_dos: {numerot}")
    if numerot == 9:
        break
else:
    print("terminado")


#recorrer una cadena de texto
for letra in cadena:
    print(letra)


#for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)