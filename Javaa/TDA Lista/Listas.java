public class Lista {

    private Nodo listaNodo;


    // 1. inserta(x, p)
    public void inserta(int x, int p) {
        Nodo nuevo = new Nodo(x);

        if (cabeza == null || p <= 1) {
            nuevo.setSiguiente(listaNodo);
            cabeza = nuevo;
            return;
        }

        Nodo actual = listaNodo;
        int contador = 1;

        while (actual.getSiguiente() != null && contador < p - 1) {
            actual = actual.getSiguiente();
            contador++;
        }

        nuevo.setSiguiente(actual.getSiguiente());
        actual.setSiguiente(nuevo);
    }
    
    public void imprimirLista() {
        Nodo actual = listaNodo;

        while (actual != null) {
            System.out.print(actual.getDato() + " -> ");
            actual = actual.getSiguiente();
        }

        System.out.println("null");
    }

    public boolean esVacia() {
        return listaNodo == null;
    }


}
