#creando una funcion simple
#def saludar():
#    print("Hola fabian, mi maestro como andas")
#saludar()

#Crear una funcion que tenga parametros
def saludar(nombre, sexo):
    sexo = sexo.lower() #convertir una cadena en minusculas
    if sexo == "mujer":
        adjetivo = "reina"
    elif sexo == "hombre":
        adjetivo = "titan"
    else:
        adjetivo = "amor"
    print(f"Hola {nombre}, mi {adjetivo} como andas")
   
saludar("Camila", "mujer")
saludar("Anthony", "Hombre")
saludar("imbecil", "idiota")

#Crear una funcion que nos retorna valores
def crear_contraseña_random(num):
    chars = "shfjdhgpg"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num

#Desempaquetando la funcion
password,primer_numero = crear_contraseña_random(2)

#mostrando los resultados obtenidos y los datos utilizados para obtenerla
print(f"\nTu contraseña nueva es: {password}")
print(f"El numero utilizado para crearla fue: {primer_numero}")