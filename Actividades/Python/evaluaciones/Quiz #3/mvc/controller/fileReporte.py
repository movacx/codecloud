from view.ReportesView import ReporteGUI
from data.baseCuentas import DataCuentas

class ReporteController:
    def __init__(self, root):
        self.GUI = ReporteGUI(root, self)
        self.data = DataCuentas()
        
    def cargarDatos(self):
        arreglo = self.data.ordenar()
        self.GUI.cargarTabla(arreglo)
