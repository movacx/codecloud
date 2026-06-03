import java.util.Scanner;

public class MainScanner 
{
    public static void main(String[] args) 
    {

        Scanner sc = new Scanner(System.in);
        TDAListaDoble lista = new TDAListaDoble();

        int opcion;

        do {
            System.out.println("\n--- MENU LISTA DOBLE ---");
            System.out.println("1. Digite el numero que desea insertar al inicio\n");
            System.out.println("2. Digite el numero que desea insertar al final\n");
            System.out.println("3. Digite el numero que desea insertar despues de\n");
            System.out.println("4. Digite el numero que desea insertar antes de\n");
            System.out.println("5. Digite el numero que desea eliminar\n" );
            System.out.println("6. Imprimir lista\n");
            System.out.println("7. Imprimir lista de reversa\n");
            System.out.println("0. Salir\n");
            System.out.print("Opcion: ");

            opcion = sc.nextInt();

            switch (opcion) 
            {

                case 1:
                    System.out.print("Digite dato: ");
                    lista.insertarInicio(sc.nextInt());
                    break;

                case 2:
                    System.out.print("Digite dato: ");
                    lista.insertarFinal(sc.nextInt());
                    break;

                case 3:
                    System.out.print("Dato referencia: ");
                    int ref1 = sc.nextInt();
                    System.out.print("Nuevo dato: ");
                    int nuevo1 = sc.nextInt();
                    lista.insertarDespues(ref1, nuevo1);
                    break;

                case 4:
                    System.out.print("Dato referencia: ");
                    int ref2 = sc.nextInt();
                    System.out.print("Nuevo dato: ");
                    int nuevo2 = sc.nextInt();
                    lista.insertarAntes(ref2, nuevo2);
                    break;

                case 5:
                    System.out.print("Dato a eliminar: ");
                    lista.eliminar(sc.nextInt());
                    break;

                case 6:
                    lista.imprimir();
                    break;

                case 7:
                    lista.imprimirReversa();
                    break;

                case 0:
                    System.out.println("Saliendo...");
                    break;

                default:
                    System.out.println("Opción invalida");
            }

        } while (opcion != 0);

        sc.close();
    }
}
