public class Main1 
{
    public static void main(String[] args) 
    {

        Pila pila = new Pila();

        pila.apilar(10);
        pila.apilar(20);
        pila.apilar(30);

        System.out.println("Pila:");
        pila.mostrar();

        System.out.println("Cima: " + pila.cima());

        System.out.println("Desapilar: " + pila.desapilar());

        pila.mostrar();
    }
}
