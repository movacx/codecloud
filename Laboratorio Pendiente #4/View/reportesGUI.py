import tkinter as tk

class ReportesGUI:
    def __init__(self, baseMainGUI):
        self.ventana=tk.Toplevel(baseMainGUI)
        self.ventana.title("Reportes Base")
        self.ventana.geometry("900x950")
        
    menuReportes = tkMenu(ventana)
    menuReportes = tkMenu(ventana, tearoff=0)
    
    
    menuReportes.addCommand(label= "Reportes")
    menuReportes.addCommand(label= "Reportes de habitaciones disponibles")
    menuReportes.addCommand(label= "Reportes de habitaciones ocupadas")
    menuReportes.addCommand(label= "Reportes de reservaciones activas")
    
    menuReportes.addCascade(label= "Menu de reportes", menuReportes)
    
    ventana.config(menuReportes=menuReportes)
    
        
def main():
    root=tk.Tk()
    app=ReportesGUI(root)
    root.mainloop()
    pass
if __name__== '__main__':
    main()