from Model.libroModel import LibroModel
from Repository.practica import ClasePrueba

def main():
    repo = ClasePrueba()
    nuevo_libro = LibroModel('89474', 'Harry Poter Bobeda Secreta', 'J.K')
    #repo.guardar(nuevo_libro)
    for items in repo.listar():
        print(items)    

if __name__ == '__main__':
    main()
