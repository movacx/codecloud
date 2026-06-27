import tkinter as tk
from tkinter import ttk
from View.main_window import MainWindow
#C5E187 HERLIN FABIAN CHAVARRIA BEITA
from Controller.controllerJugador import ControllerJugador
from Controller.controllerJuego import ControllerVideoJuego


def _build_ui():
    ventana = tk.Tk()
    ttk.Button(
        ventana,
        text="Gestión de Jugadores",
        width=30, command=lambda:ControllerJugador(ventana)
    ).pack(pady=8)

    ttk.Button(
        ventana,
        text="Gestión de videojuegos",
        width=30, command=lambda:ControllerVideoJuego(ventana)
    ).pack(pady=8)

    ttk.Button(
        ventana,
        text="Reportes",
        width=30
    ).pack(pady=8)

    ttk.Button(
        ventana,
        text="Salir",
        width=30,
        command=ventana.destroy
    ).pack(pady=(20, 8))

    ventana.mainloop()

if __name__ == "__main__":
    _build_ui()
