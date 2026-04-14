import javax.swing.JOptionPane;

public class Principal {

    public static void main(String args[]) {

        Operaciones opera = new Operaciones();
        int menu, datos, buscar;

        do {

            menu = Integer.parseInt(JOptionPane.showInputDialog("Escoja una opcion"
            +"\n1. Agregar al inicio"
            +"\n2. Agregar al final"
            +"\n3. Iprimir"
            +"\n4. Agregar despues de"
            +"\n5. Eliminar un elemento"
            +"\n6. Eliminar la lista"
            +"\n7. Salir"));

            switch(menu) {
                case 1:
                    datos = Integer.parseInt(JOptionPane.showInputDialog("Digite un dato"));
                    opera.agregarAlInicio(datos);
                break;

                case 2:
                    datos = Integer.parseInt(JOptionPane.showInputDialog("Digite un dato"));
                    opera.agregarAlFinal(datos);
                break;

                case 3:
                    String mensaje = opera.imprimir();
                    JOptionPane.showMessageDialog(null, mensaje);
                break;

                case 4:
                    datos = Integer.parseInt(JOptionPane.showInputDialog("Digite el dato que desea agregar"));
                    buscar = Integer.parseInt(JOptionPane.showInputDialog("Digite el dato que desea buscar"));
                    opera.agregarDespues(datos, buscar);
                break;

                case 5:

                break;

                case 6:

                break;

                case 7:
                    JOptionPane.showMessageDialog(null, "Saliendo del programa...");
                break;

                default:
                    JOptionPane.showMessageDialog(null, "Digite una opcion valida");
                break;
            }

        }while(menu != 7);

    }

}