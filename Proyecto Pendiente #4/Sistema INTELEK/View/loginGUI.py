import tkinter as tk
import storeGUI
sans12 = ('Open Sans Extrabold',12)
sans9 = ('Open Sans Extrabold',9)
separador = '‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾'
class VentanaLogin:
    def __init__(self, root, controller):
        #====================== [Referenciar el controller =====================
        self.manejoController = controller
        #====================== [Establecer Ventana] =====================
        self.ventana = root
        self.ventana.title('Login Intelek')
        self.ventana.geometry('1080x720')
        self.ventana.configure(bg = "#0D5577")

        #====================== [Centrar Login] =====================
        self.contenedor = tk.Frame(self.ventana, padx = 5, pady = 5)
        self.contenedor.place(anchor = 'center', relx = 0.5, rely = 0.5)
        self.contenedor.configure(bg='#FFFFFF')

        self.contenedorBotones = tk.Frame(self.contenedor)
        self.contenedorBotones.grid(row = 4, column = 0)

        self.Labels()
        self.Inputs()
        self.Buttons()

    def Labels(self):
        tk.Label(self.contenedor, text = 'Login Intelek', font = sans12, bg = 'white').grid(row = 0, column = 0, columnspan = 3)
        tk.Label(self.contenedor, text = separador, font = sans12, bg = 'white').grid(row = 1, column = 0, columnspan = 3)
        tk.Label(self.contenedor, text = 'Usuario:', font = sans12, bg = 'white').grid(row = 2, column = 0, sticky = 'w', columnspan = 3)
        tk.Label(self.contenedor, text = 'Contraseña:', font = sans12, bg = 'white').grid(row = 3, column = 0, sticky = 'w', columnspan = 3)

    def Inputs(self):
        UsrEntry = tk.Entry(self.contenedor, width = 50).grid(row = 2, column = 1, sticky = 'e', padx = 10, columnspan = 3)
        usrPassword = tk.Entry(self.contenedor, width = 50).grid(row = 3, column = 1, sticky = 'e', padx = 10, columnspan = 3)


    def Buttons(self):
        ingresarBtn = tk.Button(self.contenedor, text = 'Crear Cuenta', font = sans9, fg = 'white', bg = "#4E5052").grid(row = 4, column = 0, pady = 20)
        olvidePassBtn = tk.Button(self.contenedor, text = 'Ingresar', font = sans9, ).grid(row = 4, column = 1, padx = (30,0))
        registrarsebtn = tk.Button(self.contenedor, text = 'Olvide mi contraseña', font = sans9, fg = 'white', bg = "#820909").grid(row = 4, column = 2, columnspan = 2, padx = (10,0))
#bg="#2C3E50", fg="white"
def main():
    root = tk.Tk()
    app = VentanaLogin(root, None)
    root.mainloop()

if __name__ == '__main__':
    main()