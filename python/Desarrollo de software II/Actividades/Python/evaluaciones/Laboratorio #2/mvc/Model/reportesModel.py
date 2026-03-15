from Model import baseProducto
from Model import inventarioModel

def obtenerTodosProductos():
    return baseProducto.listarProductos()

def obtenerTodosMovimientos():
    return inventarioModel.listarMovimientos()