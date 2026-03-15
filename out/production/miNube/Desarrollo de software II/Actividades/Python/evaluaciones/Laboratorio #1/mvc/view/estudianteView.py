# Participantes: 
# Herlin Fabian Chavarria Beita C5E187
# Joseph Campos C4D660
# David Mora Gomez C5H441

# Importamos lo común
from view.comunesView import mostrarMensaje, mostrarTodos, mostrarUno

def gestionEstudiante():
    print("""
       GESTIÓN DE ESTUDIANTES
    1. Registrar estudiante
    2. Listar estudiantes
    3. Buscar estudiante
    4. Actualizar estudiante
    5. Eliminar estudiante
    6. Volver al Menú Principal
    input: """)
    
def MenuModificacion():
    print("""
    --- MODIFICAR ESTUDIANTE ---
    1. Modificar Nombre
    2. Modificar Edad
    3. Modificar Grado
    4. Modificar Correo
    0. Cancelar
    """)