public class Operaciones  {
    NodoDoble primero, ultimo, nuevo, rec, rec2;
    int cantidad;

    public void inserta(int datos, int posicion) {
        nuevo = new NodoDoble(datos);
        if(esVacia()) {
            primero = nuevo;
            ultimo = nuevo;
        }
        else {
            if(posicion == 0) {
                nuevo.setSiguiente(primero);
                primero.setAnterior(nuevo);
                primero = nuevo;
            }
            else {
                if(posicion >= cantidad) {
                    ultimo.setSiguiente(nuevo);
                    nuevo.setAnterior(ultimo);
                    ultimo = nuevo;
                }
                else {
                    for(int i=0; i < (posicion-1); i++)
                        rec = rec.getSiguiente();
                    nuevo.setSiguiente(rec.getSiguiente());
                    rec.setSiguiente(nuevo);
                    nuevo.setAnterior(rec);
                    rec = nuevo.getSiguiente();
                    rec.setAnterior(nuevo);
                }
            }
        }
        cantidad++;
    }

    public int localiza(int datos) {
        if(esVacia()) {
            return -1;
        }
        
        int posicion = 0;
        rec = primero;

        while(rec != null) {
            if(rec.getDatos() == datos)
                return posicion;
            rec = rec.getSiguiente();
            posicion++;
        }

        return -2;
    }

    public int recupera(int posicion) {
        int dato;
        if(esVacia())
            return -1;
        
        for(int i=0; i < posicion; i++)
            rec = rec.getSiguiente();

        dato = rec.getDatos();
        return dato;
    }

    public String suprime(int posicion) {
        String mensaje = "La lista se encuentra vacía";
        if(!esVacia()) {
            if(posicion >= cantidad) {
                mensaje = "La posición no se encuentra en la lista";
            }
            else {
                if(posicion == 0) {
                    primero = primero.getSiguiente();
                    primero.setAnterior(null);
                }
                else {
                    if(posicion == (cantidad-1)) {
                        ultimo = ultimo.getAnterior();
                        ultimo.setSiguiente(null);
                    }
                    else {
                        rec = primero;
                        for(int i = 0; i < (posicion-1); i++) {
                            rec = rec.getSiguiente();
                            rec2 = rec.getSiguiente();
                            rec.setSiguiente(rec2.getSiguiente());
                            rec2 = rec2.getSiguiente();
                            rec2.setAnterior(rec);
                        }
                    }
                    cantidad--;
                }
            }
        }

        return mensaje;
    }

    public void anula() {
        primero = null;
        ultimo = null;
        cantidad = 0;
    }

    public int primero() {
        int valor =-1;
        if(esVacia())
            valor = primero.getDatos();
        return valor;
    }

    public String imprimirLista() {
        String mensaje = "";
        
        if(esVacia()) {
            mensaje = "La lista se encuenta vacia";
        }
        else {
            rec = primero;

            while(rec != null) {
                mensaje += rec.getDatos() + "\n";
                rec = rec.getSiguiente();
            }
        }

        return mensaje;
    }

    public boolean esVacia() {
        if(primero == null)
            return true;
        else
            return false;
    }
}