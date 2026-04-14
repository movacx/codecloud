public class Operaciones {

    OperacionesTDACola cola = new OperacionesTDACola();
    OperacionesTDACola colaAux = new OperacionesTDACola();

    public String imprimir () {
        String mensaje = "";

        if(cola.esVacia())
            mensaje = "La cola está vacía";
        else {
            while (!cola.esVacia()) {
                mensaje += cola.primero() + " | ";
                colaAux.inserta(cola.primero());
                cola.quitarPrimero();
            }// Fin del while

            while (!colaAux.esVacia()) {
                cola.inserta(colaAux.primero());
                colaAux.quitarPrimero();
            }// Fin del while
        }// Fin del else

        return mensaje;
    }// Fin de imprimir

    public void insertarEnCola (int datos) {
        cola.inserta(datos);
    }// Fin de insertarEnCola

    public String eliminar (int datos) {
        String mensaje = "El elemento no se encuentra en la cola";

        if (cola.esVacia())
            mensaje = "La cola se encuentra vacía";
        else {
            while (!cola.esVacia()) {
                if (cola.primero() == datos) {
                    mensaje = "El valor " + datos + " fue eliminado";
                    cola.quitarPrimero();
                }
                else {
                    colaAux.inserta(cola.primero());
                    cola.quitarPrimero();
                }// Fin del else

            }// Fin del while

            while (!colaAux.esVacia()) {

                cola.inserta(colaAux.primero());
                colaAux.quitarPrimero();
            }// Fin del while

        }// Fin del else

        return mensaje;

    }// Fin de Eliminar 

    public boolean buscar (int datos) {
        boolean existe = false;

        if (!cola.esVacia()) {
            while (!cola.esVacia()) {
                if (cola.primero() == datos) 
                    existe = true;
                colaAux.inserta(cola.primero());
                cola.quitarPrimero();
                
            }// Fin del while

            while (!colaAux.esVacia()) {
                cola.inserta(colaAux.primero());
                colaAux.quitarPrimero();
            }// Fin del while

        }// Fin del if

        return existe;
    }// Fin de buscar

}// Fin de la clase