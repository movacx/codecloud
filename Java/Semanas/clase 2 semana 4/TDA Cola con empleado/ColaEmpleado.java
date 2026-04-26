public class ColaEmpleado 
{
    private NodoEmpleado frente;
    private NodoEmpleado fin;

    public ColaEmpleado() 
    {
        frente = null;
        fin = null;
    }

    public boolean estaVacia() 
    {
        return frente == null;
    }

    // Encolar
    public void encolar(Empleado emp) 
    {
        NodoEmpleado nuevo = new NodoEmpleado(emp);

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

    // Desencolar
    public Empleado desencolar() 
    {
        if (estaVacia()) 
        {
            return null;
        }

        Empleado emp = frente.getDato();
        frente = frente.getSiguiente();

        if (frente == null) 
        {
            fin = null;
        }

        return emp;
    }

    // Ver frente
    public Empleado frente() 
    {
        if (estaVacia()) 
        {
            return null;
        }
        return frente.getDato();
    }

    public void vaciar() 
    {
        frente = null;
        fin = null;
    }

    public String mostrarComoTexto() 
    {
        if (estaVacia()) 
        {
            return "Cola vacia";
        }

        String texto = "";
        NodoEmpleado actual = frente;

        while (actual != null) 
        {
            texto += actual.getDato().toString() + "\n";
            actual = actual.getSiguiente();
        }

        return texto;
    }
}
