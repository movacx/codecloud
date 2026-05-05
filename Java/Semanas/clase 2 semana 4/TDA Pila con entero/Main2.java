public class Main2 
{
    public static void main(String[] args) 
    {

        Pila pila = new Pila();

        System.out.println("=== PRUEBA AUTOMÁTICA ===");

        pila.apilar(5);
        pila.apilar(15);
        pila.apilar(25);

        System.out.println("Contenido:");
        pila.mostrar();

        System.out.println("Cima actual: " + pila.cima());

        pila.desapilar();
        System.out.println("Despues de desapilar:");
        pila.mostrar();

        pila.vaciar();
        System.out.println("¿Está vacia? " + pila.estaVacia());
    }
}
