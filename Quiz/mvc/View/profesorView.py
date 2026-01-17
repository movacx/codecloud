#Participantes: 
#Herlin Fabian Chavarria Beita C5E187
#Joseph Campos C4D660
#David Mora Gomez C5H441

def mostrarTodos(estudianteObjeto):
    print(estudianteObjeto)
    
def mostrarUno(estudiante):
    print(estudiante)    

def mostrarMensaje(mensaje):
    print(mensaje)

##Gestion Profesor
def gestionProfesor():
    print("""
    1. Registrar profesor
    2. Listar profesor
    3. Actualizar profesor
    4. Eliminar profesor
    5. Volver
    input: """)

def MenuModificacion():
    print(f"""
            1. Modificar Nombre
            2. Modificar Especialidad
            3. Modificar Telefono
            4. Modificar Correo
            0. Volver""")