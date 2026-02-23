import tkinter as tk
from Controller.authController import AuthController

def main():
    try:
        root = tk.Tk()
        
        controladorAcceso = AuthController(root)
        root.mainloop()
    except Exception as error:
        print(f'Error grave en el sistema: {error}')

if __name__ == '__main__':
    main()