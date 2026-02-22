import Data.baseResenas as dataRes

class ResenaController:
    def calcularPromedio(self, idPro):
        todas = dataRes.leerResenas()
        suma = 0
        cant = 0
        for r in todas:
            if r and r[0] == str(idPro):
                suma += int(r[3])
                cant += 1
        if cant == 0: return 0
        return suma / cant