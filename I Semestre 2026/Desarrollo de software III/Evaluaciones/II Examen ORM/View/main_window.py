import tkinter as tk
from tkinter import ttk


from View.report_window import ReportWindow
from View.ventana_juego import GameWindow
from View.ventana_jugador import PlayerWindow


class MainWindow:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Sistema de videojuegos")
        self.root.geometry("500x380")
        self.root.resizable(False, False)

        self._build_ui()

    def _build_ui(self):
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill="both", expand=True)


        ttk.Button(
            frame,
            text="Gestión de Jugadores",
            width=30,
            command=self.open_players
        ).pack(pady=8)

        ttk.Button(
            frame,
            text="Gestión de videojuegos",
            width=30,
            command=self.open_game
        ).pack(pady=8)



        ttk.Button(
            frame,
            text="Reportes",
            width=30,
            command=self.open_reports
        ).pack(pady=8)

        ttk.Button(
            frame,
            text="Salir",
            width=30,
            command=self.root.destroy
        ).pack(pady=(20, 8))

    def open_players(self):
        PlayerWindow(self.root)

    def open_game(self):
        GameWindow(self.root)

    def open_reports(self):
        ReportWindow(self.root)
