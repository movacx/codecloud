import Data.baseProductos as dataPro

class BuscadorController:
    def buscarPorNombre(self, textoBusqueda):
        inventario = dataPro.listarProductos()
        resultados = []
        for item in inventario:
            if item and textoBusqueda.lower() in item[1].lower():
                resultados.append(item)
        return resultados