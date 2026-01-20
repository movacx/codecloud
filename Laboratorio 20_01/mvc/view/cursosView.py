def mostrarTodos(cursoObjeto):
    print(cursoObjeto)
    
def mostrarUno(curso):
    print(curso)    

def mostrarMensaje(mensaje):
    print(f" {mensaje}")

def gestionCursos():
    print("""
    --- GESTIÓN DE CURSOS ---
    1. Crear Curso
    2. Listar Cursos
    3. Modificar Curso
    4. Eliminar Curso
    5. Volver al Menú Principal
    """)
    
def MenuModificacion():
    print("""
            1. Modificar Nombre Curso
            2. Modificar Código
            3. Modificar Profe asignado
            0. Cancelar
    """)