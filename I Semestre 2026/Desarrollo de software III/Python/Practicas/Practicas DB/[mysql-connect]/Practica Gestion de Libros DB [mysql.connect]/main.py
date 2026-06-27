from Repository.repository_biblioteca import BibliotecaRepository
from Service.biblioteca_service import Service
from Controller.biblioteca_controller import BibliotecaController

from Database.conexion import DataBaseConection

def main():
    database = DataBaseConection()
    repositorio_biblioteca = BibliotecaRepository(database)
    service_biblioteca = Service(repositorio_biblioteca)
    controlador_biblioteca = BibliotecaController(service_biblioteca)
    

    controlador_biblioteca.cargar_interfaz()



if __name__ == '__main__':
    main()


