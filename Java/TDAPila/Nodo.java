public class Nodo {
    int datos;
    Nodo siguiente;

    public Nodo (int datos) {
        this.datos = datos;
        siguiente = null;
    }

    public int getDatos() {
        return datos;
    }

    public Nodo getSiguiente() {
        return siguiente;
    }

    public void setDatos(int datos) {
        this.datos = datos;
    }

    public void setSiguiente(Nodo siguiente) {
        this.siguiente = siguiente;
    }
}