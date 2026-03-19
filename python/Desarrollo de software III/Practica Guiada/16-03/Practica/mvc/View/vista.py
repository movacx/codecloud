class Vista:
    def mostrar_menu(self):
        opcion = int(input("""
------- SISTEMA DE MATRÍCULA ------

1. Agregar estudiante
2. Agregar curso
3. Matricular estudiante
4. Consultar estudiantes
5. Consultar cursos
6. Consultar matrículas
0. Salir

input: """))
        return opcion

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

    def mostrar_datos(self, arreglo):
        for items in arreglo:
            print(items)