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


##Gestion Estudiantes
def gestionEstudiante():
    print("""
    1. Registrar estudiante
    2. Listar estudiantes
    3. Buscar estudiante
    4. Actualizar estudiante
    5. Eliminar estudiante
    6. Volver
    input: """)
    
def MenuModificacion():
    print(f"""
            1. Modificar Nombre
            2. Modificar Edad
            3. Modificar Grado
            4. Modificar Correo
            0. Volver""")