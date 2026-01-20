#Participantes: 
#Herlin Fabian Chavarria Beita C5E187
#Joseph Campos C4D660
#David Mora Gomez C5H441

# Importamos lo común
from view.comunesView import mostrarMensaje, mostrarTodos, mostrarUno

def gestionCursos():
    print("""
    ==============================
         GESTIÓN DE CURSOS
    ==============================
    1. Crear Curso
    2. Listar Cursos
    3. Modificar Curso
    4. Eliminar Curso
    5. Volver al Menú Principal
    """)
    
def MenuModificacion():
    print("""
    --- MODIFICAR CURSO ---
    1. Modificar Nombre Curso
    2. Modificar Código
    3. Modificar Profe asignado
    0. Cancelar
    """)