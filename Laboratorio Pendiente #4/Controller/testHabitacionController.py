from View.testHabitacionGUI import HabitacionGUI
import Data.baseHabitacion as data

class HabitacionController:
    def __init__(self, root):
        self.GUI = HabitacionGUI(root, self)
        self.ventana = root
        
    
    def savelog(self, nombreError):
        try:
            data.guardarError(nombreError)
        except Exception as error:
            print(f'No se pudo establecer la coneccion con log.txt >> data + controller = {error}')
            
    def registrarHabitacion(self):
        pass