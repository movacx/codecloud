public class OperacionesTDAPila {

    Nodo primero, nuevo;

    public void apila(int datos) {
        nuevo = new Nodo(datos);

        if(esVacia()) {
            primero = nuevo;
        }
        else {
            nuevo.setSiguiente(primero);
            primero = nuevo;
        }
    }

    public int desapila() {
        int valor = -1;
        if(!esVacia()) {
            valor = cima();
            primero = primero.getSiguiente();
        }
        return valor;
    }

    public int cima() {
        if(esVacia())
            return -1;
        else
            return primero.getDatos();
    }

    public boolean esVacia() {
        if(primero == null)
            return true;
        else
            return false;
    }

}