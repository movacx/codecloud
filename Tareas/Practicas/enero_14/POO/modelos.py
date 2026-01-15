# Archivo: modelos.py

class Reservacion:
    def __init__(self, nombre_cliente, costo_total):
        self.nombre_cliente = nombre_cliente
        self.costo_total = costo_total

    def __str__(self):
        return f"Reserva de {self.nombre_cliente} por ${self.costo_total}"