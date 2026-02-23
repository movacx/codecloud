from View.VentanaArmador import VentanaArmador
import Data.baseProductos as dataPro

class ArmadorController:
    def __init__(self, root):
        self.GUI = VentanaArmador(root, self)
        self.listaCpusDisponibles = []
        self.cargarProcesadores()

    def cargarProcesadores(self):
        try:
            inventario = dataPro.listarProductos()
            cpusFormateados = []
            self.listaCpusDisponibles = []

            for items in inventario:
                if items:
                    if items[2] == "Procesador":
                        self.listaCpusDisponibles.append(items)
                        cpusFormateados.append(f"{items[1]} (Socket: {items[5]})")
            
            self.GUI.cbxCpu['values'] = cpusFormateados
            
            for items in self.GUI.tablaMadres.get_children():
                self.GUI.tablaMadres.delete(items)
        except Exception as error:
            self.GUI.mostrarError(f"Error al cargar CPU: {error}")

    def buscarCompatibilidad(self):
        try:
            indiceSeleccionado = self.GUI.cbxCpu.current()
            
            if indiceSeleccionado == -1:
                self.GUI.mostrarError("Seleccione un procesador primero")
                return

            cpuElegido = self.listaCpusDisponibles[indiceSeleccionado]
            socketCpu = cpuElegido[5]

            inventario = dataPro.listarProductos()
            
            for items in self.GUI.tablaMadres.get_children():
                self.GUI.tablaMadres.delete(items)

            encontrado = False
            for items in inventario:
                if items:
                    if items[2] == "Motherboard":
                        if items[5] == socketCpu:
                            self.GUI.tablaMadres.insert('', 'end', values=(items[0], items[1], items[3]))
                            encontrado = True
                    
            if not encontrado:
                self.GUI.mostrarError("No hay tarjetas madre compatibles en inventario")
        except Exception as error:
            self.GUI.mostrarError(f"Error al buscar compatibles: {error}")