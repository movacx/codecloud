public class Lista 
{
    private Nodo nodoInicio;

    public Lista() 
    {
        nodoInicio = null;
    }

    // 1. inserta(x, p)
    public void inserta(Empleado empleadoNuevo, int posicion) 
    {
        Nodo nodoNuevo = new Nodo(empleadoNuevo);

        if (posicion <= 0 || nodoInicio == null) 
        {
            nodoNuevo.setSiguiente(nodoInicio);
            nodoInicio = nodoNuevo;
            return;
        }

        Nodo nodoActual = nodoInicio;
        int posicionActual = 0;

        while (nodoActual.getSiguiente() != null && posicionActual < posicion - 1) 
        {
            nodoActual = nodoActual.getSiguiente();
            posicionActual++;
        }

        nodoNuevo.setSiguiente(nodoActual.getSiguiente());
        nodoActual.setSiguiente(nodoNuevo);
    }

    // 2. localiza(x)
    public int localiza(String cedulaBuscada) 
    {
        Nodo nodoActual = nodoInicio;
        int posicionActual = 0;

        while (nodoActual != null) {
            if (nodoActual.getDato().getCedula().equals(cedulaBuscada)) 
            {
                return posicionActual;
            }
            nodoActual = nodoActual.getSiguiente();
            posicionActual++;
        }

        return -1;
    }

    // 3. recupera(p)
    public Empleado recupera(int posicion) 
    {
        Nodo nodoActual = nodoInicio;
        int posicionActual = 0;

        while (nodoActual != null) 
        {
            if (posicionActual == posicion) 
            {
                return nodoActual.getDato();
            }
            nodoActual = nodoActual.getSiguiente();
            posicionActual++;
        }

        return null; // no encontrado
    }

    // 4. suprime(p)
    public void suprime(int posicion) 
    {
        if (nodoInicio == null) return;

        if (posicion == 0) 
        {
            nodoInicio = nodoInicio.getSiguiente();
            return;
        }

        Nodo nodoActual = nodoInicio;
        int posicionActual = 0;

        while (nodoActual.getSiguiente() != null && posicionActual < posicion - 1) 
        {
            nodoActual = nodoActual.getSiguiente();
            posicionActual++;
        }

        if (nodoActual.getSiguiente() != null) 
        {
            nodoActual.setSiguiente(nodoActual.getSiguiente().getSiguiente());
        }
    }

    // 5. anula()
    public void anula() 
    {
        nodoInicio = null;
    }

    // 6. primero()
    public Empleado primero() 
    {
        if (nodoInicio != null) 
        {
            return nodoInicio.getDato();
        }
        return null;
    }

    // 7. imprimirLista()
    public void imprimirLista() 
    {
        Nodo nodoActual = nodoInicio;

        while (nodoActual != null) 
        {
            System.out.println("Cedula: " + nodoActual.getDato().getCedula()
                    + " | Edad: " + nodoActual.getDato().getEdad());
            nodoActual = nodoActual.getSiguiente();
        }
    }

    // 8. esVacia()
    public boolean esVacia() 
    {
        return nodoInicio == null;
    }

    // EXTRA (te sirve para la practica)
    public int contarEmpleados() 
    {
        Nodo nodoActual = nodoInicio;
        int cantidad = 0;

        while (nodoActual != null) 
        {
            cantidad++;
            nodoActual = nodoActual.getSiguiente();
        }

        return cantidad;
    }

    public int contarPorEdad(int edadBuscada) 
    {
        Nodo nodoActual = nodoInicio;
        int cantidad = 0;

        while (nodoActual != null) 
        {
            if (nodoActual.getDato().getEdad() == edadBuscada) 
            {
                cantidad++;
            }
            nodoActual = nodoActual.getSiguiente();
        }

        return cantidad;
    }
}
