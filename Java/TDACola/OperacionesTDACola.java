public class OperacionesTDACola {

    Nodo frente, finalCola, nuevo;

    public void vacia () {
        frente = null;
        finalCola = null;
    }// Fin de vacia

    public int primero () {
        if (esVacia())
            return -1;
        else
            return frente.getDatos();
    }// Fin de primero

    public boolean esVacia () {
        if (frente == null)
            return true;
        else
            return false;
    }// Fin de esVacia

    public void inserta (int datos) {
        nuevo = new Nodo(datos);
        
        if (esVacia()) {
            frente = nuevo;
            finalCola = nuevo;
        }
        else {
            finalCola.setSiguiente(nuevo);
            finalCola = nuevo;
        }//Fin del else
    }//Final de inserta

    public void quitarPrimero () {
        if (!esVacia()) {
            frente = frente.getSiguiente();
        }
    }//Fin de quitarPrimero

}//Fin de la clase