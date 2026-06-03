public class Nodo {
    String pregunta;
    String atributo;
    double umbral;
    Nodo nodoIzquierdo;
    Nodo nodoDerecho;
    String clasificacionFinal;

    public Nodo(String pregunta, String atributo, double umbral) {
        this.pregunta = pregunta;
        this.atributo = atributo;
        this.umbral = umbral;
        this.clasificacionFinal = null;
    }

    public Nodo(String clasificacionFinal) {
        this.clasificacionFinal = clasificacionFinal;
    }

    public boolean esHoja() {
        return this.clasificacionFinal != null;
    }
}
