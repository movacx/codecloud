def mostrarTodos(estudianteObjeto):
    print(estudianteObjeto)
    
def mostrarUno(estudiante):
    print(estudiante)    

def mostrarMensaje(mensaje):
    print(f" {mensaje}")

def gestionEstudiante():
    print("""
    --- GESTIÓN DE ESTUDIANTES ---
    1. Registrar estudiante
    2. Listar estudiantes
    3. Buscar estudiante
    4. Actualizar estudiante
    5. Eliminar estudiante
    6. Volver al Menú Principal
    """)
    
def MenuModificacion():
    print("""
            1. Modificar Nombre
            2. Modificar Edad
            3. Modificar Grado
            4. Modificar Correo
            0. Cancelar
    """)