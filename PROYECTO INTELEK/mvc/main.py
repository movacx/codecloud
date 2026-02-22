import tkinter as tk

# Importamos la nueva vista de login y los controladores necesarios.
from View.VentanaLogin import VentanaLogin
from Controller.authController import AuthController
from Controller.adminController import AdminController
from Controller.reporteController import ReporteController
from Controller.buscadorController import BuscadorController
from Controller.carritoController import CarritoController
from Controller.checkoutController import CheckoutController
from Controller.promoController import PromoController
from Controller.armadorController import ArmadorController
from Controller.resenaController import ResenaController

def iniciarApp() -> None:
    """Inicializa y pone en marcha la aplicación."""
    # Ventana base de la interfaz
    root = tk.Tk()
    # Diccionario con las clases de controladores que se usarán en las vistas
    controllers = {
        'buscador': BuscadorController,
        'carrito': CarritoController,
        'promo': PromoController,
        'resena': ResenaController,
        'checkout': CheckoutController,
        'armador': ArmadorController,
        'reporte': ReporteController,
        'admin': AdminController,
    }
    # Instancia del controlador de autenticación
    auth_ctrl = AuthController()
    # Instanciamos la ventana de login pasando la raíz, el controlador de
    # autenticación y el diccionario de controladores
    VentanaLogin(root, auth_ctrl, controllers)
    # Iniciamos el ciclo de eventos
    root.mainloop()

if __name__ == '__main__':
    iniciarApp()