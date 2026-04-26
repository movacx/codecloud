public class Main 
{
    public static void main(String[] args) 
    {

        Lista listaNumeros = new Lista();

        System.out.println("----- LISTA INICIAL -----");
        listaNumeros.insertar(10);
        listaNumeros.insertar(20);
        listaNumeros.insertar(30);
        listaNumeros.imprimirLista();

        System.out.println();
        System.out.println("----- BUSCAR -----");
        int posicionEncontrada = listaNumeros.buscar(20);
        System.out.println("Posicion del numero 20: " + posicionEncontrada);

        System.out.println();
        System.out.println("----- ELIMINAR -----");
        listaNumeros.eliminar(1);
        listaNumeros.imprimirLista();

        System.out.println();
        System.out.println("----- PRIMER ELEMENTO -----");
        System.out.println("Primer elemento: " + listaNumeros.obtenerPrimero());

        System.out.println();
        System.out.println("----- ESTA VACIA -----");
        System.out.println("Esta vacia: " + listaNumeros.estaVacia());

        System.out.println();
        System.out.println("----- VACIAR LISTA -----");
        listaNumeros.vaciarLista();
        listaNumeros.imprimirLista();

        System.out.println();
        System.out.println("----- FIN DEL PROGRAMA -----");
    }
}
