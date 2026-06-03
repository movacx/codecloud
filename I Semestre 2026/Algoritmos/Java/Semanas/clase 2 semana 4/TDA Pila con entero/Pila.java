public class Pila 
{
    private Nodo cima;

    public Pila() 
    {
        cima = null;
    }

    // Vaciar pila
    public void vaciar() 
    {
        cima = null;
    }

    // Verificar si está vacía
    public boolean estaVacia() 
    {
        return cima == null;
    }

    // Apilar (push)
    public void apilar(int dato) 
    {
        Nodo nuevo = new Nodo(dato);
        nuevo.setSiguiente(cima);
        cima = nuevo;
    }

    // Ver cima (peek)
    public int cima() {
        if (estaVacia()) 
        {
            return -1;
        }
        return cima.getDato();
    }

    // Desapilar (pop)
    public int desapilar() 
    {
        if (estaVacia()) {
            return -1;
        }

        int dato = cima.getDato();
        cima = cima.getSiguiente();
        return dato;
    }

    // Mostrar como texto (para JOptionPane)
    public String mostrarComoTexto() 
    {
        if (estaVacia()) 
        {
            return "Pila vacia";
        }

        String texto = "";
        Nodo actual = cima;

        while (actual != null) 
        {
            texto += actual.getDato() + "\n";
            actual = actual.getSiguiente();
        }

        return texto;
    }
}
