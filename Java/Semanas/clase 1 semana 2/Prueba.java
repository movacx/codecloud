public class Prueba
{
    public static void main(String[] args)
    {
        NodosEnlazados lista = new NodosEnlazados();

        lista.agregarInicio(5);
        lista.agregarInicio(2);
        lista.agregarFinal(8);

        System.out.println("Lista:");
        lista.imprimir();

        System.out.println("Despues del nuemro 5 agregar 7:");
        lista.despuesDe(5, 7);
        lista.imprimir();

        System.out.println("Eliminar el numero 2:");
        lista.eliminar(2);
        lista.imprimir();
    }
}
