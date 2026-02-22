# Importamos la clase Cliente desde su archivo correspondiente
from Model.Cliente import Cliente  # Cambiamos UsuarioModel por Cliente
import Data.baseUsuarios as dataUsuarios

class AuthController:
    def procesarLogin(self, correoInput, passInput):
        datosUsr = dataUsuarios.validarLogin(correoInput, passInput) 
        if datosUsr:
            # Retorna exito, el Rol (Admin/Cliente) y el ID del usuario 
            return True, datosUsr[4], datosUsr[0] 
        return False, "Credenciales incorrectas", None

    def procesarRegistro(self, nombreN, correoN, claveN):
        # Valida que no existan campos vacios 
        if not nombreN or not correoN or not claveN:
            return False, "Faltan datos por completar"
        
        # El rol por defecto para registros nuevos es Cliente 
        # Instanciamos la clase Cliente en lugar de UsuarioModel
        nuevoUsr = Cliente(0, correoN, claveN, nombreN, "Cliente", "Sin direccion")
        exito = dataUsuarios.registrarUsuario(nuevoUsr) 
        return exito, "Cuenta creada" if exito else "Error al registrar"

    def recuperarPassword(self, correoInput):
        # Buscamos al usuario en la base para devolver la clave 
        listaUsuarios = dataUsuarios.listarTodos()
        for usr in listaUsuarios:
            if usr[1] == correoInput:
                return True, f"Tu clave es: {usr[2]}"
        return False, "Correo no encontrado"