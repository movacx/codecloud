from Model import reportesModel

class ReportesController:
    def __init__(self):
        pass

    def reportePorCategoria(self):
        lista = reportesModel.obtenerTodosProductos()
        # Ordenamos por categoria (indice 2)
        lista.sort(key=lambda x: x[2])
        return lista

    def reporteBajoStock(self):
        lista = reportesModel.obtenerTodosProductos()
        listaBajoStock = []
        for item in lista:
            if int(item[4]) < 5:
                listaBajoStock.append(item)
        return listaBajoStock

    def reporteHistorial(self):
        return reportesModel.obtenerTodosMovimientos()