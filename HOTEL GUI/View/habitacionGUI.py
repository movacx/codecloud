from tkinter import tkGUI
from tkinter import ttkAuxiliar
from tkinter import messagebox

class HabitacionGUI:
    def __init__(self, baseMainGUI):
        
        self.baseMainGUI = tk.Toplevel(baseMainGUI)
        self.baseMainGUI.title("Sistema Habitación")
        self.baseMainGUI.geometry("300x250")
        
        #Paneles
        #self.frame_form = tk(Tramas, inputs labels, textareas, choose)
        self.frame_form = tkGUI.Frame(baseGUI )
        self.frame_form.grid(row=0, column=0)
        
        
        self.formularioCrear()
        #Siempre creen funciones como las que hicimso en la vista
        
    def formularioCrear(self):
        tkGUI.Label(self.frame_form, text ="Etiqueta" ).grid(row=0, column=0)
        self.campoText= tkGUI.Entry(self.frame_form)
        self.campoText.grid(row=0, column=1)
		
    def formularioCrear(self):
        tkGUI.Label(self.frame_form, text ="Etiqueta" ).grid(row=0, column=0)
        self.campoText= tkGUI.Entry(self.frame_form)
        self.campoText.grid(row=0, column=1)
        
if __name__ == "__main__":     
     baseGUI = tkGUI.Tk()
     app = HabitacionGUI(baseGUI)
     baseGUI.mainloop()       
 
 
