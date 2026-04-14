
import javax.xml.crypto.Data;

public class OperacionesTDALista {

    Nodo primero, ultimo, rec, rec2, nuevo;
    private int cantidad = 0;

    public void inserta(int datos, int posicion) {
        nuevo  = new Nodo(datos);

        if(esVacia()) {
            primero = nuevo;
            ultimo = nuevo;
        }
        else {
            if(posicion == 0) {
                nuevo.setSiguiente(nuevo);
                primero = nuevo;
            }
            else {
                if(posicion >= cantidad) {
                    ultimo.setSiguiente(nuevo);
                    ultimo = nuevo;
                }
                else {
                    rec = primero;
                    for(int i=1; i < posicion; i++) {
                        rec = rec.getSiguiente();
                        nuevo.setSiguiente(rec.getSiguiente());
                        rec.setSiguiente(nuevo);
                    }
                }
            }
        }
        cantidad++;
    }

    public int localiza(int datos) {
        if(esVacia()) {
            return -2;
        }
        
        rec = primero;
        for(int i=1; i < cantidad; i++) {
            if(rec.getDatos() == datos) {
                return i;
            }
            else {
                rec = rec.getSiguiente();
            }
        }
        return -1;
    }

    public int recupera(int posicion) {
        if(esVacia()) {
            return -2;
        }

        if(posicion > cantidad) {
            return -1;
        }
        
        rec = primero;
        for(int i=1; i < posicion; i++) {
            rec = rec.getSiguiente();
            if(i == posicion) {
                return rec.getDatos();
            }
        }
        return -1;
    }

    public void suprime(int posicion) {
        rec = primero;
        for(int i=1; i < posicion; i++) {
            if(i == posicion) {
                rec2.setSiguiente(rec.getSiguiente());
            }
            else {
                rec2 = rec;
                rec = rec.getSiguiente();
            }
        }
    }

    public void anula() {
        primero = null;
        ultimo = null;
    }

    public String primero() {
        String mensaje = "";

        if(primero == null) {
            mensaje = "La lista está vacía";
        }
        else {
            mensaje += primero.getDatos();
        }
        return mensaje;
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
        if(primero == null) {
            return true;
        }
        else {
            return false;
        }
    }

}