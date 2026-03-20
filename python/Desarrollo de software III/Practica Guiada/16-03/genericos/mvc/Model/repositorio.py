"""from typing import TypeVar, Generic, List

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
        return False"""


from typing import TypeVar, Generic, List

T = TypeVar("T")

class Repositorio(Generic[T]):
    def __init__(self):
        self.lista = []

    def agregar(self, obj: T):
        self.lista.append(obj)

    def consultar(self) -> list[T]:
        return self.lista

    def modificar(self, indice: int, nuevoObjeto: T) -> bool:
        if 0 <= indice < len(self.lista):
            self.lista[indice] = nuevoObjeto
            return True
        return False

"""    def buscar(self, objPosUno) -> str:
        for items in self.lista:
            if str(items[0]) == str(objPosUno):
                return items

    def buscarr(self, buscar: str):
        for items in self.lista:
            if items == buscar:
                return items
"""