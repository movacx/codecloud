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
    #no tengo btn en el main ni nada porque hare un cargador de programa para no tener los botones en el main osea otro view que se encargara de ejecutar la ventana principal
    #y mostrarlo sin que en el main haya alguna interfaz solo el root que se manda por parametros entonces para ver las demas descomenta repo, service,control y comenta lo de abajo

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