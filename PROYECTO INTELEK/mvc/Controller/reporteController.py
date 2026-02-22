import Data.baseFacturas as dataFac
import Data.baseUsuarios as dataUsuarios

class ReporteController:
    def reporteFinanciero(self):
        listaFacturas = dataFac.leerFacturas()
        totalVentas = 0
        for f in listaFacturas:
            if f:
                totalVentas = totalVentas + float(f[3]) # Suma columna de total [cite: 133]
        return totalVentas

    def reporteCuentas(self):
        # Cuenta cuantos usuarios hay en el sistema [cite: 36]
        todosUsr = dataUsuarios.listarTodos()
        return len(todosUsr)

    def verMisCompras(self, idUsuario):
        lista = dataFac.leerFacturas()
        misFac = []
        for f in lista:
            if f and f[1] == str(idUsuario): # Filtra por ID de cliente [cite: 139]
                misFac.append(f)
        return misFac