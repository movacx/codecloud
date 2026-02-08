/*Herlin Fabian Chavarria Beita C5E187*/
public class ManejoEstudiante
{
    private Estudiante vectorEstudiante[] = new Estudiante[10];

    /***************************************************************************/
    public String agregarEstudiante(Estudiante estudiante)
    {
        for(int indice = 0; indice < vectorEstudiante.length; indice++)
        {
            if(vectorEstudiante[indice] == null)
            {
                vectorEstudiante[indice] = estudiante;
                return "Guardado con exito";
            }
        }
        return "No hay espacio suficiente";
    }

    /***************************************************************************/
    public void eliminarEstudiante(String carnet)
    {
        for(int indice = 0; indice < vectorEstudiante.length; indice++)
        {
            if(vectorEstudiante[indice] != null)
            {
                if(vectorEstudiante[indice].getCarnet().equals(carnet))
                {
                    vectorEstudiante[indice] = null;
                }
            }
        }
    }

    /***************************************************************************/
    public Estudiante buscarEstudiante(String buscarCarnet)
    {
        for(int indice = 0; indice < vectorEstudiante.length; indice++)
        {
            if(vectorEstudiante[indice] != null)
            {
                if(vectorEstudiante[indice].getCarnet().equals(buscarCarnet))
                {
                    return vectorEstudiante[indice];
                }
            }
        }
        return null;
    }

    /***************************************************************************/
    public String buscar(String carnet)
    {
        String mensaje = "";
        for(int indice = 0; indice < vectorEstudiante.length; indice++)
        {
            if(vectorEstudiante[indice] != null)
            {
                if(vectorEstudiante[indice].getCarnet().equals(carnet))
                {
                    mensaje += vectorEstudiante[indice];
                }
            }
        }
        return mensaje;
    }

    /***************************************************************************/
    public String modificarDatos(String carnet, String nombre, String carrera, double promedio)
    {
        for(int indice = 0; indice < vectorEstudiante.length; indice++)
        {
            if(vectorEstudiante[indice] != null)
            {
                if(vectorEstudiante[indice].getCarnet().equals(carnet))
                {
                    vectorEstudiante[indice].setNombreEstudiante(nombre);
                    vectorEstudiante[indice].setCarrera(carrera);
					vectorEstudiante[indice].setPromedio(promedio);
					return "Modificacion exitosa";
                }
            }
        }
        return "Estudiante no encontrado";
    }

    /***************************************************************************/
    public String mostrarToString(String carnet)
    {
        for(int indice = 0; indice < vectorEstudiante.length; indice++)
        {
            if(vectorEstudiante[indice] != null)
            {
                if(vectorEstudiante[indice].getCarnet().equals(carnet))
                {
                    return vectorEstudiante[indice].toString();
                }
            }
        }
        return "No se encontro ningun dato";
    }

}

