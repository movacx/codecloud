import os
import csv

# Rutas dinámicas para que funcione en cualquier carpeta de tu Arch Linux [cite: 11]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(BASE_DIR, "csv", "usuarios.csv")

def validarUltimoId():
    """Busca el ID más alto en el CSV para el autoincremento[cite: 11]."""
    try:
        if not os.path.exists(ARCHIVO):
            return 0
            
        ultimoId = 0
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoLeer:
            reader = csv.reader(archivoLeer)
            for item in reader:
                if item:
                    try:
                        # La primera columna siempre es el ID 
                        idActual = int(item[0])
                        if idActual > ultimoId:
                            ultimoId = idActual
                    except ValueError:
                        continue
        return ultimoId
    except Exception as errorFallo:
        print(f"Error al buscar ID: {errorFallo}")
        return 0

def registrarUsuario(objUsuario):
    """Guarda un nuevo objeto usuario en el archivo CSV[cite: 1, 11]."""
    try: 
        # Generamos el ID automático antes de guardar
        idNuevo = validarUltimoId() + 1
        objUsuario.ide = idNuevo
        
        with open(ARCHIVO, "a", newline="", encoding="utf-8") as archivoEscribir:
            writer = csv.writer(archivoEscribir)
            # Usamos el método importarToCsv definido en tu Model [cite: 1, 11]
            writer.writerow(objUsuario.importarToCsv()) 
        return True
    except Exception as errorFallo:
        print(f"Error al registrar: {errorFallo}")
        return False

def validarLogin(correoUsr, passUsr):
    """Verifica si las credenciales coinciden con algún registro[cite: 1, 11]."""
    try: 
        if not os.path.exists(ARCHIVO):
            return None
            
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoLeer:
            reader = csv.reader(archivoLeer)
            for item in reader:
                # Comparamos correo (columna 1) y contraseña (columna 2) [cite: 1, 11]
                if item and item[1] == correoUsr and item[2] == passUsr: 
                    return item 
        return None
    except Exception as errorFallo:
        print(f"Error en login: {errorFallo}")
        return None

def listarTodos():
    """Retorna la lista completa de usuarios para reportes y búsquedas."""
    try:
        if not os.path.exists(ARCHIVO):
            return []
            
        listaCompleta = []
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivoCsv:
            lector = csv.reader(archivoCsv)
            for fila in lector:
                if fila:
                    listaCompleta.append(fila)
        return listaCompleta
    except Exception as e:
        print(f"Error al listar: {e}")
        return []