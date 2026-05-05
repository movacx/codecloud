import tkinter as tk

from Repository.personaRepository import PersonaRepository
from Service.personaService import PersonaService
from Controller.personaController import ControladorPersona
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
from Repository.recursosRepository import RecursosRepository
from Service.recursoService import RecursoService
from Controller.recursoController import ControllerRecurso
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
from Repository.asignacionesRepository import AsignacionesRepository
from Service.asignacionService import AsignacionService
from Controller.asignacionController import AsignacionController

from View.pantalla_principal import Cargador

def main():
    root = tk.Tk()

    #============================================ 
    repo = PersonaRepository()
    service = PersonaService(repo)
    #control = ControladorPersona(root, service)
    #============================================
    repo_recurso = RecursosRepository()
    service_recurso = RecursoService(repo_recurso)
    #controller_recurso = ControllerRecurso(root,service_recurso)
    #============================================
    repo_asignacion = AsignacionesRepository()
    service_asignacion = AsignacionService(repo,repo_recurso,repo_asignacion)
    

    def cargarPersona():
        ControladorPersona(root, service)

    def cargarRecurso():
        ControllerRecurso(root,service_recurso)

    def cargarAsignacion():
        AsignacionController(root, service_asignacion)

    Cargador(root, cargarPersona,cargarRecurso,cargarAsignacion)

    root.mainloop()


if __name__ == '__main__':
    main()