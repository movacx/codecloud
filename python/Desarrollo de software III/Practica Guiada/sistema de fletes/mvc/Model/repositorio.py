from typing import TypeVar, Generic, List

tipoGen = TypeVar('tipoGen')

class Repositorio(Generic[tipoGen]):
    def __init__(self):
        self.lista = []

    def agregar(self, obj: tipoGen):
        self.lista.append(obj)

    def consultar(self) -> List[tipoGen]:
        return self.lista

    def modificar(self, indice: int, nuevoObjeto: tipoGen) -> bool:
        if 0 <= indice < len(self.lista):
            self.lista[indice] = nuevoObjeto
            return True
        return False