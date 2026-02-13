import tkinter as tk
import Data.baseHabitacion as habitacion

from View.reportesGUI import ReportesGUI
from tkinter import messagebox

class ReportesController:
    def __init__(self, root):
        self.ventana=root
        
        self.GUI= ReportesGUI(root, self)
        