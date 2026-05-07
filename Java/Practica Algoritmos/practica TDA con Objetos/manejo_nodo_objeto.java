public class manejo_nodo_objeto
{
    NodoObjeto primero;

    public manejo_nodo_objeto()
    {
        this.primero = null;
    }

    //=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=//

    public int insertar(String cedula, String nombre, int edad, int posicion)
    {
        Persona nuevaPersona = new Persona(cedula, nombre, edad);
        NodoObjeto nuevo = new NodoObjeto(nuevaPersona);
        int contador = 1;

        if(posicion == 1)
        {
            nuevo.siguiente = primero;
            primero =  nuevo;
            return 1;
        }else{
            NodoObjeto aux = primero;

            while(aux != null && contador < posicion -1)
            {
                aux = aux.siguiente;
                contador++;

            }

            nuevo.siguiente = aux.siguiente;
            aux.siguiente = nuevo;
            return 1;
        }

    }
    //=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=//

    public String validarExistencia(String cedula) {

        NodoObjeto aux = primero;
        String mensaje = "";

        if (aux == null)
        {
            return "No se han encontrado datos";

        }

        while(aux != null) {
            if (aux.dato.getCedula().equals(cedula)) {
                return "["+ aux.dato + "]";
            }

            aux = aux.siguiente;

        }

        return "No se encontró ninguna persona con la cédula: " + cedula;

    }
    //=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=//
    public void imprimirTodos()
    {
        int contador = 1;
        NodoObjeto aux = primero;

        if(aux == null)
        {
            System.out.println("No se han encontrado datos");
            return;
        }else{
            while(aux != null)
            {
                System.out.println(aux.dato.toString());
                aux = aux.siguiente;
            }
        }
    }

    //=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=//
    public void contarMismaEdad(int edad)
    {
        int contador_misma_edad = 0;
        NodoObjeto aux = primero;

        if(aux==null){System.out.println("No se han encontrado datos"); return;}

        while(aux != null)
        {
            if(aux.dato.getEdad() == edad)
            {
                contador_misma_edad++;
            }
            aux = aux.siguiente;
        }

        System.out.println("La cantidad de personas con la misma edad es de: " + contador_misma_edad);
        return;
    }

    //=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-[Método para obtener la posición]-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=//
    public int buscarPosicion(String cedula)
    {
        int contador_posicion = 1;
        NodoObjeto aux = primero;

        if(aux==null) return -1;

        while(aux!=null)
        {
            if(aux.dato.getCedula().equals(cedula))
            {
                return contador_posicion;
            }
            aux = aux.siguiente;
            contador_posicion++;
        }

        return -1;

    }

    //=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=//
    public int eliminarPersona(String cedula)
    {
        NodoObjeto aux = primero;

        //Caso 1. El que se quiere eliminar es el primero de la lista.
        int posicion = buscarPosicion(cedula);

        if(posicion == -1) return -1;

        if(posicion == 1)
        {
            primero = primero.siguiente;
            return 1;

        }else{
            //Caso 2.
            int contador = 1;
            while(aux !=null && contador < posicion -1)
            {
                aux = aux.siguiente;
                contador++;
            }

            aux.siguiente = aux.siguiente.siguiente;
            return 1;

        }

    }






}//fin clase
