from View.VentanaLogin import VentanaLogin
from View.VentanaRegistro import VentanaRegistro
from View.MenuPrincipal import MenuPrincipal
from Model.Cliente import Cliente
import Data.baseUsuarios as dataUsuarios
from Controller.tiendaController import TiendaController
from Controller.armadorController import ArmadorController
from Controller.adminController import AdminController

class AuthController:
    def __init__(self, root):
        self.root = root
        self.idLogueado = 0
        self.GUI = VentanaLogin(self.root, self)
#-----------------------------------------------------------------------------------------------------------------------
     #Ejecutar login 
    def ejecutarLogin(self):
        try:
            correo = self.GUI.txtCorreo.get()
            clave = self.GUI.txtClave.get()
            
            datosUsr = dataUsuarios.validarLogin(correo, clave)
            if datosUsr:
                self.idLogueado = datosUsr[0]
                rolUsuario = datosUsr[4]
                self.root.withdraw()
                self.menuGUI = MenuPrincipal(self.root, self, rolUsuario)
            else:
                self.GUI.mostrarError("Credenciales invalidas")
        except Exception as error:
            self.GUI.mostrarError(f"Error interno: {error}")
#-----------------------------------------------------------------------------------------------------------------------
     #Abrir registro
    def abrirRegistro(self):
        self.registroGUI = VentanaRegistro(self.root, self)
#-----------------------------------------------------------------------------------------------------------------------
    #Registrar
    def registrar(self):
        try:
            nombre = self.registroGUI.txtNombre.get()
            correo = self.registroGUI.txtCorreo.get()
            clave = self.registroGUI.txtClave.get()
            
            if not (nombre or correo or clave):
                self.registroGUI.mostrarError("Faltan datos por completar")
                return
                
            nuevoUsr = Cliente(0, correo, clave, nombre, "Cliente", "Sin direccion")
            exito = dataUsuarios.registrarUsuario(nuevoUsr)
            
            if exito:
                self.registroGUI.mostrarMensaje("Cuenta creada")
                self.registroGUI.ventana.destroy()
            else:
                self.registroGUI.mostrarError("Error al registrar")
        except Exception as error:
            self.registroGUI.mostrarError(f"Error interno: {error}")
#-----------------------------------------------------------------------------------------------------------------------
     #Abrir la tienda
    def abrirTienda(self):
        TiendaController(self.root, self.idLogueado)
#-----------------------------------------------------------------------------------------------------------------------
     #Abrir el armador de la pc
    def abrirArmador(self):
        ArmadorController(self.root)
#-----------------------------------------------------------------------------------------------------------------------
     #Abrir admin
    def abrirAdmin(self):
        AdminController(self.root)
#-----------------------------------------------------------------------------------------------------------------------
    #Cerrar el programa
    def cerrarApp(self):
        self.menuGUI.ventana.destroy()
        self.root.deiconify()