from View.testHabitacionGUI import HabitacionGUI

class HabitacionController:
    def __init__(self, root):
        self.GUI = HabitacionGUI(root, self)
        
        self.ventana = root
        