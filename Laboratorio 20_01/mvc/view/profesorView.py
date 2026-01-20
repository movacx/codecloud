#Participantes: 
#Herlin Fabian Chavarria Beita C5E187
#Joseph Campos C4D660
#David Mora Gomez C5H441

# Importamos lo común
from view.comunesView import mostrarMensaje, mostrarTodos, mostrarUno

def gestionProfesor():
    print("""
       GESTIÓN DE PROFESORES
    1. Registrar profesor
    2. Listar profesores
    3. Actualizar profesor
    4. Eliminar profesor
    5. Volver al Menú Principal
    """)

def MenuModificacion():
    print("""
    --- MODIFICAR PROFESOR ---
    1. Modificar Nombre
    2. Modificar Especialidad
    3. Modificar Teléfono
    4. Modificar Correo
    0. Cancelar
    """)