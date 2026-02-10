import tkinter as tk

class ReservasGUI:
    def __init__(self, baseMainGUI):
        self.baseMainGUI = FormularioGUI.Toplevel(baseMainGUI)
        self.baseMainGUI.title("Reservas Base")
        self.baseMainGUI.geometry("900x950")
        
        self.frame_form=tkGUI.Frame(baseGUI)
        self.frame+form.grid(row=0, column=0)
        
        self.formularioCrear()
        
    def formularioCrear(self):
        tkGUI.Label(self.frame_form, text="Etiqueta").grind(row = 0, column=0)
        self.campoText=tkGUI.Entry(self.frame_form)
        self.campoText.grid(row=0, column =1)
  
if __name__ == "__main__":
    baseGUI= tkGUI.Tk()
    app= ReservasGUI(baseGUI)
    baseGUI(mainloop())