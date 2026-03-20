class Vista:
    def mostrar_menu(self):
        opcion = int(input("""
------- SISTEMA DE BIBLIOTECA -------
1. Agregar estudiante
2. Agregar libro
3. Registrar préstamo
4. Consultar estudiantes
5. Consultar libros
6. Consultar préstamos
7. Consultar categorías
0. Salir

input: """))
        return opcion

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

    def mostrar_datos(self, datos):
            print(datos)

