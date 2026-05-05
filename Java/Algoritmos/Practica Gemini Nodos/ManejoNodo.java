public class ManejoNodo
{
    private Nodo primero; // Apuntador al inicio de la lista
    
    public ManejoNodo()
    {
        this.primero = null; // Al inicio, la lista esta vacia=
    }
    
    public boolean esVacio()
    {
        return primero == null;
    }
    
    //=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=//
    
    private Nodo obtenerNodo(int posicion)
    {
        Nodo auxiliar = primero;
        int contador = 1;
        
        while (aux != null && contador < posicion)
        {
            aux = aux.getSiguiente();
            contador++;
        }
    }
    
    public void insertar(int dato, int posicion)
    {
        Nodo nuevoNodo = new Nodo(dato);
        //Caso A el vagon va de primero
        //Si la lista esta vacia o el usuario pide la posicion 1
        
        if (esVacio() || posicion == 1)
        {
            nuevoNodo.setSiguiente(primero); //El nuevo ahora paunta al que era el primero
            primero =  nuevoNodo;            //El inicio de la lista ahora es el nuevo
        }else
        { //Caso B: El vagon va en medio o al final
            //Le pedimos al asistente el nodo anterior a donde queremos insertar
            Nodo anterior = obtenerNodo(posicion - 1);
            
            if (anterior != null)
            {
                nuevoNodo.setSiguiente(anterior.getSiguiente());
                anterior.setSiguiente(nuevoNodo);
            }
        }
    }
    
}