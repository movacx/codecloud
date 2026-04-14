public class Operaciones {
    Nodo primero, ultimo, nuevo, rec, rec2;
    public void agregarAlInicio(int datos) {

        nuevo = new Nodo(datos);

        if(primero == null) {
            primero = nuevo;
            ultimo = nuevo;
        }
        else {
            nuevo.setSiguiente(primero);
            primero = nuevo;
        }
    }

    public void agregarAlFinal(int datos) {
        nuevo = new Nodo(datos);

        if(primero == null) {
            primero = nuevo;
            ultimo = nuevo;
        }
        else {
            ultimo.setSiguiente(nuevo);
            ultimo = nuevo;
        }
    }

    public String imprimir() {
        String mensaje = "";
        
        if(primero == null) {
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

    public String agregarDespues(int datos, int buscar) {
        String mensaje = "";

        if(primero == null) {
            mensaje = "No hay nodos agregados";
        }
        else {
            rec = primero;
            while(rec != null) {
                if(rec.getDatos() == buscar) {
                    nuevo = new Nodo(datos);
                    nuevo.setSiguiente(rec.getSiguiente());
                    rec.setSiguiente(nuevo);

                    if(rec == ultimo) {
                        ultimo = nuevo;
                    }
                    break;
                }
                else {
                    rec = rec.getSiguiente();
                }
            }
        }

        return mensaje;
    }

    public String eliminar(int buscar) {
        String mensaje = "";

        if(primero == null) {
            mensaje = "No hay nodos agregados";
        }
        else {
            rec = primero;
            while(rec != null) {
                if(rec.getDatos() == buscar) {
                    rec2.setSiguiente(rec.getSiguiente());
                    rec = null;
                    mensaje = "Nodo eliminado";

                    if(rec == ultimo) {
                        rec = null;
                        rec2.setSiguiente(rec);
                    }
                    break;
                }
                else {
                    rec2 = rec;
                    rec = rec.getSiguiente();
                }
            }
        }

        return mensaje;
    }
}
