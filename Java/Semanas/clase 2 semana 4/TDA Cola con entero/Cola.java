public class Cola 
{
    private Nodo frente;
    private Nodo fin;

    public Cola() 
    {
        frente = null;
        fin = null;
    }

    // Verificar si está vacía
    public boolean estaVacia() 
    {
        return frente == null;
    }

    // Encolar (insertar al final)
    public void encolar(int dato) 
    {
        Nodo nuevo = new Nodo(dato);

        if (estaVacia()) 
        {
            frente = nuevo;
            fin = nuevo;
        } else 
        {
            fin.setSiguiente(nuevo);
            fin = nuevo;
        }
    }

    // Desencolar (eliminar del frente)
    public int desencolar() 
    {
        if (estaVacia()) 
        {
            return -1;
        }

        int dato = frente.getDato();
        frente = frente.getSiguiente();

        if (frente == null) 
        {
            fin = null;
        }

        return dato;
    }

    // Ver frente
    public int frente() 
    {
        if (estaVacia()) 
        {
            return -1;
        }
        return frente.getDato();
    }

    // Vaciar
    public void vaciar() 
    {
        frente = null;
        fin = null;
    }

    // Mostrar como texto (para JOptionPane)
    public String mostrarComoTexto() 
    {
        if (estaVacia()) 
        {
            return "Cola vacia";
        }

        String texto = "";
        Nodo actual = frente;

        while (actual != null) 
        {
            texto += actual.getDato() + "\n";
            actual = actual.getSiguiente();
        }

        return texto;
    }
}
