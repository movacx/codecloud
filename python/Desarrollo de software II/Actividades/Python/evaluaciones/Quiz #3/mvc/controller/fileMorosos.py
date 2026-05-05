from view.ReporteMorosos import ReporteMorosos
from data.baseCreditos import DataCreditos

class ControllerMorosos:
    def __init__(self, root):
        self.GUI = ReporteMorosos(root, self)
        self.data = DataCreditos()

    def mostrarDatos(self):
        arreglo = self.data.ordenarMorosos()
        self.GUI.cargarTabla(arreglo)