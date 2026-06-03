public class PilaEmpleado 
{
    private NodoEmpleado cima;

    public PilaEmpleado() 
    {
        cima = null;
    }

    public void vaciar() 
    {
        cima = null;
    }

    public boolean estaVacia() 
    {
        return cima == null;
    }

    public void apilar(Empleado emp) 
    {
        NodoEmpleado nuevo = new NodoEmpleado(emp);
        nuevo.setSiguiente(cima);
        cima = nuevo;
    }

    public Empleado desapilar() 
    {
        if (estaVacia()) 
        {
            return null;
        }

        Empleado emp = cima.getDato();
        cima = cima.getSiguiente();
        return emp;
    }

    public Empleado cima() 
    {
        if (estaVacia()) 
        {
            return null;
        }
        return cima.getDato();
    }

    public String mostrarComoTexto() 
    {
        if (estaVacia()) 
        {
            return "Pila vacía";
        }

        String texto = "";
        NodoEmpleado actual = cima;

        while (actual != null) 
        {
            texto += actual.getDato().toString() + "\n";
            actual = actual.getSiguiente();
        }

        return texto;
    }
}
