public class Nodo
{
    private Empleado dato;
    private Nodo siguiente;
    
    public Nodo()
    {
        this.siguiente = null;
        this.dato = null; 
    }
    
    public Nodo(Empleado dato) 
    {
        this.siguiente = null;
        this.dato = dato;
    }
    
    public Nodo(Empleado dato, Nodo siguiente)
    {
        this.siguiente = siguiente;
        this.dato = dato;
    }
    
    public void setDato(Empleado dato)
    {
        this.dato = dato;
    }
    
    public Empleado getDato() 
    {
        return dato;
    }
    
    public void setSiguiente(Nodo siguiente)
    {
        this.siguiente = siguiente;
    }
    
    public Nodo getSiguiente()
    {
        return siguiente;
    }
}
