public class Operaciones {
    OperacionesTDAPila pila = new OperacionesTDAPila();
    OperacionesTDAPila aux = new OperacionesTDAPila();

    public void agregar(int datos) {
        pila.apila(datos);
    }

    public String imprimir() {
        String mensaje = "";

        if(pila.esVacia() == true) {
            mensaje = "La pila se encuentra vacía";
        }
        else {
            while (pila.cima() != -1) { 
                int datos = pila.desapila();
                mensaje += datos + "\n";
                aux.apila(datos);
            }

            while(aux.cima() != -1) {
                int datos = aux.desapila();
                pila.apila(datos);
            }
        }
        return mensaje;
    }







    public String borrar(int valor) {
        String mensaje = "No se ha encontrado el nodo con ese valor";

        if(pila.esVacia()) {
            mensaje = "La pila se encuentra vacía";
        }

        while(pila.cima() != -1) {
            int datos = pila.desapila();
            if(datos != valor) {
                aux.apila(datos);
            }
            else {
                mensaje = "Nodo eliminado";
            }
        }

        while(aux.cima() != -1) {
                int datos = aux.desapila();
                pila.apila(datos);
            }

        return mensaje;
    }

}