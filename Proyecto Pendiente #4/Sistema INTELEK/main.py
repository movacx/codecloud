import tkinter as tk
from View.loginGUI import VentanaLogin

def main():
    root = tk.Tk()
    app = VentanaLogin(root, None)
    root.mainloop()

if __name__ == '__main__':
    main()