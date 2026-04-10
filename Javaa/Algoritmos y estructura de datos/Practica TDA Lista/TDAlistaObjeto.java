//++======================================================================================================================++
public class TDAlistaObjeto 
{
    private Nodo cabeza;

    public TDAlistaObjeto() 
    {
        cabeza = null; 
    }

//++======================================================================================================================++
    public void insertar(Empleado empleado)
    {
        Nodo nuevo; 
        nuevo = new Nodo(empleado); 
        
        nuevo.setSiguiente(cabeza);
        cabeza = nuevo;
    }

//++======================================================================================================================++
    public boolean existeEmpleado(String cedulaBuscar)
    {
        boolean respuesta;
        respuesta = false;
        Nodo temporal;
        temporal = cabeza;
        Empleado empleadoActual;

        while(temporal != null)
        {
            empleadoActual = temporal.getDato(); 

            if(empleadoActual.getCedula().equals(cedulaBuscar))
            {
                respuesta = true;
                break;
            }
            temporal = temporal.getSiguiente();
        }
        return respuesta;
    }

//++======================================================================================================================++
    public int contarPorEdad(int edadBuscar)
    {
        int contador;
        contador = 0;
        Nodo actual;
        actual = cabeza;
        Empleado empleadoEdad;

        while(actual != null)
        {
            empleadoEdad = actual.getDato();

            if(empleadoEdad.getEdad() == edadBuscar)
            {
                contador = contador + 1; 
            }
            actual = actual.getSiguiente();
        }
        return contador;
    }

//++======================================================================================================================++

    public int cantidadEmpleados()
    {
        int contador;
        contador = 0;
        Nodo temporal;
        temporal = cabeza;

        while(temporal != null)
        {
            contador = contador + 1;
            temporal = temporal.getSiguiente();
        }
        
        return contador; 
    }

//++======================================================================================================================++
    public String mostrarLista()
    {
        String texto;
        texto = "";
        Nodo temporal;
        temporal = cabeza;
        Empleado empleado;

        if(temporal == null)
        {
            texto = "No hay registros todavia";
        }
        else
        {
            while(temporal != null)
            {
                empleado = temporal.getDato();
                texto = texto + empleado.mostrarDatos() + "\n";
                temporal = temporal.getSiguiente();
            }
        }
        return texto;
    }

//++======================================================================================================================++
    public void eliminarLista()
    {
        // Solo puse esto para que quede vacio
        cabeza = null;
    }
}
