import View.view as vista
import View.cargador as cargador
#------------------------------------------------------------------#
from Repository.repositoryEstudiantes import EstudianteRepository
from Repository.repositoryEquipos import RepositoryEquipos
from Repository.repositoryCategorias import RepositoryCategorias
#------------------------------------------------------------------#
from Service.estudiante_service import EstudianteService
from Service.equipo_service import EquipoService
from Service.categoria_service import CategoriaService
#-------------------------------------------------------------------#
from Controller.controllerEstudiante import EstudianteController
from Controller.controllerEquipo import EquipoController
from Controller.controllerCategoria import CategoriaController
#--------------------------------------------------------------------#

def main():
    repo_estudiante = EstudianteRepository()
    repo_equipos = RepositoryEquipos()
    repo_categorias = RepositoryCategorias()
    #-------------------------------------------#
    service_estudiante = EstudianteService(repo_estudiante)
    service_equipo = EquipoService(repo_equipos)
    service_categoria = CategoriaService(repo_categorias)
    #-------------------------------------------#
    controller_estudiante = EstudianteController(service_estudiante)
    controller_equipo = EquipoController(service_equipo)
    controller_categoria = CategoriaController(service_categoria)
    #--------------------------------------------#
    cargador.mostrar_programa(vista,controller_estudiante,controller_equipo,controller_categoria)

if __name__ == '__main__':
    main()