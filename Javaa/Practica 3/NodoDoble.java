public class NodoDoble {
    private int datos;
    private NodoDoble anterior, siguiente;

    public NodoDoble(int datos) {
        this.datos = datos;
        anterior = null;
        siguiente = null;
    }

    public int getDatos() {
        return datos;
    }

    public void setDatos(int datos) {
        this.datos = datos;
    }

    public NodoDoble getAnterior() {
        return anterior;
    }

    public void setAnterior(NodoDoble anterior) {
        this.anterior = anterior;
    }

    public NodoDoble getSiguiente() {
        return siguiente;
    }

    public void setSiguiente(NodoDoble siguiente) {
        this.siguiente = siguiente;
    }
}