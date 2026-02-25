import os
import csv

dirData = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(dirData, "csv", "usuarios.csv")

#Validar ultimo id
def validarUltimoId():
    try:
        if not os.path.exists(ARCHIVO):
            return 0
            
        ultimoId = 0
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoLeer:
            reader = csv.reader(archivoLeer)
            for items in reader:
                if items:
                    try:
                        idActual = int(items[0])
                        if idActual > ultimoId:
                            ultimoId = idActual
                    except ValueError:
                        continue
        return ultimoId
    except Exception as errorFallo:
        print(f"Error al buscar ID: {errorFallo}")
        return 0
#-----------------------------------------------------------------------------------------------------------------------
#Registrar Usuario
def registrarUsuario(objUsuario):
    try: 
        idNuevo = validarUltimoId() + 1
        objUsuario.ide = idNuevo
        
        with open(ARCHIVO, "a", newline="", encoding="utf-8") as archivoEscribir:
            writer = csv.writer(archivoEscribir)
            writer.writerow(objUsuario.importarToCsv()) 
        return True
    except Exception as errorFallo:
        print(f"Error al registrar: {errorFallo}")
        return False
#-----------------------------------------------------------------------------------------------------------------------
#Validar login 
def validarLogin(correoUsr, passUsr):
    try: 
        if not os.path.exists(ARCHIVO):
            return None
            
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoLeer:
            reader = csv.reader(archivoLeer)
            for items in reader:
                if items:
                    if items[1] == correoUsr and items[2] == passUsr: 
                        return items 
        return None
    except Exception as errorFallo:
        print(f"Error en login: {errorFallo}")
        return None
#-----------------------------------------------------------------------------------------------------------------------
#Listar 
def listarTodos():
    try:
        if not os.path.exists(ARCHIVO):
            return [ ]
            
        listaCompleta = [ ]
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoCsv:
            reader = csv.reader(archivoCsv)
            
            for items in reader:
                if items:
                    listaCompleta.append(items)
        return listaCompleta
    
    except Exception as error:
        print(f"Error al listar: {error}")
        return [ ]
#-----------------------------------------------------------------------------------------------------------------------
#Actualizar contraseña
def actualizarClavePorCorreo(correoUsuario, claveNueva):
    try:
        if not os.path.exists(ARCHIVO):
            return False

        listaUsuarios = []
        usuarioEncontrado = False

        with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoLeer:
            reader = csv.reader(archivoLeer)
            for items in reader:
                if items:
                    if items[1] == correoUsuario:
                        items[2] = claveNueva
                        usuarioEncontrado = True
                    listaUsuarios.append(items)

        if not usuarioEncontrado:
            return False

        with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivoEscribir:
            writer = csv.writer(archivoEscribir)
            for items in listaUsuarios:
                if items:
                    writer.writerow(items)

        return True
    except Exception as errorFallo:
        print(f"Error al actualizar clave: {errorFallo}")
        return False