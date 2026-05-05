
from tkinter import Tk

from Repositorio.estudianteRepository import EstudianteRepository
from Services.estudianteService import EstudianteService
from Controller.estudianteController import EstudianteController
#===================================================================
from Controller.cursoController import CursoController
from Repositorio.cursoRepository import CursoRepository
from Services.cursoService import CursoService
#===================================================================
from Repositorio.matriculaRepository import MatriculaRepository
from Services.matriculaService import MatriculaService
from Controller.matriculaController import MatriculaController
#===================================================================
from View.cargadorPrograma import CargadorPrograma


def main():
    root = Tk()

    repo = CursoRepository()
    service = CursoService(repo)

    repo_e = EstudianteRepository()
    service_e = EstudianteService(repo_e)

    repo_m = MatriculaRepository()
    service_m = MatriculaService(repo_m, repo_e, repo)


    def abrir_curso():
        CursoController(root, service)

    def abrir_estudiante():
        EstudianteController(root, service_e)

    def abrir_matriculas():
        MatriculaController(root, service_m)

    app = CargadorPrograma(root, abrir_curso, abrir_estudiante, abrir_matriculas)
    root.mainloop()

if __name__ == '__main__':
    main()

