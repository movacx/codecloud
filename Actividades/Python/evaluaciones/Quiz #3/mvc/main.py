import tkinter as tk
from controller.fileCUentaController import CuentaController
from controller.manejoCuentasController import ManejoCuentaController
from controller.fileCreditosController import ControllerCreditos
from controller.fileReporte import ReporteController
from controller.fileMorosos import ControllerMorosos

def main():
    root = tk.Tk()
    tk.Button(root, text = 'Usuario', command = lambda : CuentaController(root)).pack()
    tk.Button(root, text = 'Cuenta', command = lambda : ManejoCuentaController(root)).pack()
    tk.Button(root, text = 'Solicitar Creditos', command = lambda: ControllerCreditos(root)).pack()
    tk.Button(root, text = 'Reporte de cuentas (Mayor-Menor)', command = lambda: ReporteController(root)).pack()
    tk.Button(root, text = 'Reporte de Morosos', command = lambda: ControllerMorosos(root)).pack()
    root.mainloop()
    
if __name__ == '__main__':
    main()
    