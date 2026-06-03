import javax.swing.JOptionPane;

public class MainVentana 
{
    public static void main(String[] args) 
    {

        TDAListaDoble lista = new TDAListaDoble();
        int opcion;

        do {
            opcion = Integer.parseInt(JOptionPane.showInputDialog(
                    "--- MENU LISTA DOBLE ---\n" +
                    "1. Digite el numero que desea insertar al inicio\n" +
                    "2. Digite el numero que desea insertar al final\n" +
                    "3. Digite el numero que desea insertar despues de\n" +
                    "4. Digite el numero que desea insertar antes de\n" +
                    "5. Digite el numero que desea eliminar\n" +
                    "6. Imprimir lista\n" +
                    "7. Imprimir lista en reversa\n" +
                    "0. Salir"
            ));

            switch (opcion) 
            {

                case 1:
                    int dato1 = Integer.parseInt(JOptionPane.showInputDialog("Digite dato:"));
                    lista.insertarInicio(dato1);
                    break;

                case 2:
                    int dato2 = Integer.parseInt(JOptionPane.showInputDialog("Digite dato:"));
                    lista.insertarFinal(dato2);
                    break;

                case 3:
                    int ref1 = Integer.parseInt(JOptionPane.showInputDialog("Dato referencia:"));
                    int nuevo1 = Integer.parseInt(JOptionPane.showInputDialog("Nuevo dato:"));
                    lista.insertarDespues(ref1, nuevo1);
                    break;

                case 4:
                    int ref2 = Integer.parseInt(JOptionPane.showInputDialog("Dato referencia:"));
                    int nuevo2 = Integer.parseInt(JOptionPane.showInputDialog("Nuevo dato:"));
                    lista.insertarAntes(ref2, nuevo2);
                    break;

                case 5:
                    int eliminar = Integer.parseInt(JOptionPane.showInputDialog("Dato a eliminar:"));
                    lista.eliminar(eliminar);
                    break;

                case 6:
                    lista.imprimir();
                    break;

                case 7:
                    lista.imprimirReversa();
                    break;
            }

        } while (opcion != 0);
    }
}
