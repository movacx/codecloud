#if condicion:
#    accion

edad = int(input ("Ingrese su edad: "))

if edad >= 18:
    print("Mayor edad")
elif edad <= 17:
    print("Menor de edad") 

print("\n ===================================     ")

usuario_real = "movacx"
clave_real = 1234
nombre_usuario = input("Ingrese su nombre de usuario: ")
contraseña_almacenada = int(input(f"Bienvenido {nombre_usuario} Ingrese su contraseña"))

if contraseña_almacenada == clave_real:
    print("Login exitoso")
else:
    print(f"Contraseña incorrecta {nombre_usuario}")
