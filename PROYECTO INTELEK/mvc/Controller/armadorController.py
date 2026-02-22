import Data.baseProductos as dataPro

class ArmadorController:
    def __init__(self):
        self.socketElegido = ""

    def filtrarProcesadores(self):
        inv = dataPro.listarProductos()
        cpus = []
        for p in inv:
            if p and p[2] == "Procesador": cpus.append(p)
        return cpus

    def seleccionarCpu(self, socketCpu):
        self.socketElegido = socketCpu

    def filtrarTarjetasMadre(self):
        inv = dataPro.listarProductos()
        madres = []
        for p in inv:
            if p and p[2] == "Motherboard" and p[5] == self.socketElegido:
                madres.append(p)
        return madres