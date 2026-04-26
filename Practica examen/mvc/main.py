import tkinter as tk

from Repository.personaRepository import PersonaRepository
from Service.personaService import PersonaService
from Controller.personaController import ControladorPersona
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
from Repository.recursosRepository import RecursosRepository
from Service.recursoService import RecursoService
from Controller.recursoController import ControllerRecurso
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def main():
    root = tk.Tk()
    #============================================ 
    # repo = PersonaRepository()
    # service = PersonaService(repo)
    # control = ControladorPersona(root, service)
    #============================================
    repo_recurso = RecursosRepository()
    service_recurso = RecursoService(repo_recurso)
    controller_recurso = ControllerRecurso(root,service_recurso)
    #============================================

    root.mainloop()


if __name__ == '__main__':
    main()