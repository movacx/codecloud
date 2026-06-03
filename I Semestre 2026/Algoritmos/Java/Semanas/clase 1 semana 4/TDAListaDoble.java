public class TDAListaDoble 
{

    private Nodo primero;

    public TDAListaDoble() 
    {
        primero = null;
    }

    // 1. Insertar al inicio
    public void insertarInicio(int dato) 
    {
        Nodo nuevo = new Nodo(dato);

        if (primero != null) 
        {
            primero.setAnterior(nuevo);
            nuevo.setSiguiente(primero);
        }

        primero = nuevo;
    }

    // 2. Insertar al final
    public void insertarFinal(int dato) 
    {
        Nodo nuevo = new Nodo(dato);

        if (primero == null) 
        {
            primero = nuevo;
            return;
        }

        Nodo actual = primero;

        while (actual.getSiguiente() != null) 
        {
            actual = actual.getSiguiente();
        }

        actual.setSiguiente(nuevo);
        nuevo.setAnterior(actual);
    }

    // 3. Insertar después de un dato
    public void insertarDespues(int datoBuscado, int datoNuevo) 
    {
        Nodo actual = primero;

        while (actual != null && actual.getDato() != datoBuscado) 
        {
            actual = actual.getSiguiente();
        }

        if (actual != null) {
            Nodo nuevo = new Nodo(datoNuevo);

            nuevo.setSiguiente(actual.getSiguiente());
            nuevo.setAnterior(actual);

            if (actual.getSiguiente() != null) 
            {
                actual.getSiguiente().setAnterior(nuevo);
            }

            actual.setSiguiente(nuevo);
        }
    }

    // 4. Insertar antes de un dato
    public void insertarAntes(int datoBuscado, int datoNuevo) 
    {
        Nodo actual = primero;

        while (actual != null && actual.getDato() != datoBuscado) 
        {
            actual = actual.getSiguiente();
        }

        if (actual != null) {
            Nodo nuevo = new Nodo(datoNuevo);

            nuevo.setSiguiente(actual);
            nuevo.setAnterior(actual.getAnterior());

            if (actual.getAnterior() != null) 
            {
                actual.getAnterior().setSiguiente(nuevo);
            } else 
            {
                primero = nuevo;
            }

            actual.setAnterior(nuevo);
        }
    }

    // 5. Eliminar un nodo
    public void eliminar(int dato) 
    {
        Nodo actual = primero;

        while (actual != null && actual.getDato() != dato) 
        {
            actual = actual.getSiguiente();
        }

        if (actual != null) 
        {

            // Si no es el primero
            if (actual.getAnterior() != null) 
            {
                actual.getAnterior().setSiguiente(actual.getSiguiente());
            } else {
                primero = actual.getSiguiente();
            }

            // Si no es el último
            if (actual.getSiguiente() != null) 
            {
                actual.getSiguiente().setAnterior(actual.getAnterior());
            }
        }
    }

    // 6. Imprimir hacia adelante
    public void imprimir() 
    {
        Nodo actual = primero;

        while (actual != null) 
        {
            System.out.print(actual.getDato() + " <-> ");
            actual = actual.getSiguiente();
        }

        System.out.println("null");
    }

    // EXTRA: imprimir hacia atrás
    public void imprimirReversa() 
    {
        Nodo actual = primero;

        if (actual == null) return;

        // Ir al final
        while (actual.getSiguiente() != null) 
        {
            actual = actual.getSiguiente();
        }

        // Recorrer hacia atrás
        while (actual != null) {
            System.out.print(actual.getDato() + " <-> ");
            actual = actual.getAnterior();
        }

        System.out.println("null");
    }
}
