def mostrarTodos(profeObjeto):
    print(profeObjeto)
    
def mostrarUno(profe):
    print(profe)    

def mostrarMensaje(mensaje):
    print(f" {mensaje}")

def gestionProfesor():
    print("""
    --- GESTIÓN DE PROFESORES ---
    1. Registrar profesor
    2. Listar profesores
    3. Actualizar profesor
    4. Eliminar profesor
    5. Volver al Menú Principal
    """)

def MenuModificacion():
    print("""
            1. Modificar Nombre
            2. Modificar Especialidad
            3. Modificar Teléfono
            4. Modificar Correo
            0. Cancelar
    """)