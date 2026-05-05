public class Lista 
{
    private Nodo nodoInicio;

    public Lista() 
    {
        nodoInicio = null;
    }

    // Insertar al final
    public void insertar(int datoNuevo) 
    {
        Nodo nodoNuevo = new Nodo(datoNuevo);

        if (nodoInicio == null) 
        {
            nodoInicio = nodoNuevo;
        } else 
        {
            Nodo nodoActual = nodoInicio;

            while (nodoActual.getSiguiente() != null) 
            {
                nodoActual = nodoActual.getSiguiente();
            }

            nodoActual.setSiguiente(nodoNuevo);
        }
    }

    // Imprimir lista
    public void imprimirLista() 
    {
        Nodo nodoActual = nodoInicio;

        while (nodoActual != null) 
        {
            System.out.print(nodoActual.getDato() + " -> ");
            nodoActual = nodoActual.getSiguiente();
        }

        System.out.println("null");
    }

    // Buscar elemento
    public int buscar(int datoBuscado) 
    {
        Nodo nodoActual = nodoInicio;
        int posicionActual = 0;

        while (nodoActual != null) 
        {
            if (nodoActual.getDato() == datoBuscado) 
            {
                return posicionActual;
            }
            nodoActual = nodoActual.getSiguiente();
            posicionActual++;
        }

        return -1;
    }

    // Eliminar por posición
    public void eliminar(int posicionAEliminar) 
    {
        if (nodoInicio == null) return;

        if (posicionAEliminar == 0) 
        {
            nodoInicio = nodoInicio.getSiguiente();
            return;
        }

        Nodo nodoActual = nodoInicio;

        for (int posicion = 0; posicion < posicionAEliminar - 1; posicion++) 
        {
            if (nodoActual.getSiguiente() == null) return;
            nodoActual = nodoActual.getSiguiente();
        }

        if (nodoActual.getSiguiente() != null) 
        {
            nodoActual.setSiguiente(nodoActual.getSiguiente().getSiguiente());
        }
    }

    // Obtener primer elemento
    public int obtenerPrimero() 
    {
        if (nodoInicio != null) 
        {
            return nodoInicio.getDato();
        }
        return -1;
    }

    // Verificar si está vacía
    public boolean estaVacia() 
    {
        return nodoInicio == null;
    }

    // Vaciar lista
    public void vaciarLista() 
    {
        nodoInicio = null;
    }
}
