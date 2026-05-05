public class Nodo 
{
    Empleado dato;
    Nodo siguiente;

    public Nodo(Empleado dato) 
    {
        this.dato = dato;
        this.siguiente = null;
    }

    public Empleado getDato() 
    {
        return dato;
    }

    public Nodo getSiguiente() 
    {
        return siguiente;
    }

    public void setSiguiente(Nodo siguiente) 
    {
        this.siguiente = siguiente;
    }
}
