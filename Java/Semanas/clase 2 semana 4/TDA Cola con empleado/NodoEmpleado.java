public class NodoEmpleado 
{
    private Empleado dato;
    private NodoEmpleado siguiente;

    public NodoEmpleado(Empleado dato) 
    {
        this.dato = dato;
        this.siguiente = null;
    }

    public Empleado getDato() 
    {
        return dato;
    }

    public NodoEmpleado getSiguiente() 
    {
        return siguiente;
    }

    public void setSiguiente(NodoEmpleado siguiente) 
    {
        this.siguiente = siguiente;
    }
}
