# Este archivo solo contiene la clase para cumplir con el requisito de POO
# La persistencia (CSV) la maneja baseProducto.py
class Producto:
    def __init__(self, id, nombre, categoria, precio, stock):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock