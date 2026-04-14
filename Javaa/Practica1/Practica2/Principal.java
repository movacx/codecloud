
import javax.swing.JOptionPane;

public class Principal {
    public static void main(String args[]) {

        Operaciones opera = new Operaciones();
        int menu, datos, posicion;
        do {

            menu = Integer.parseInt(JOptionPane.showInputDialog("\nEscoja una opcion"
                +"\n1. Insertar nodo"
                +"\n2. Localizar nodo"
                +"\n3. Recuperar"
                +"\n4. Suprimir"
                +"\n5. Anular"
                +"\n6. Primero"
                +"\n7. Imprimir lista"
                +"\n8. Salir"
            ));

            switch(menu) {
                case 1:
                    datos = Integer.parseInt(JOptionPane.showInputDialog("Digite los datos"));
                    posicion = Integer.parseInt(JOptionPane.showInputDialog("Digite la posicion"));
                    opera.inserta(datos, posicion);
                break;

                case 2:
                    
                break;

                case 3:

                break;

                case 4:

                break;

                case 5:

                break;

                case 6:

                break;
                
                case 7:

                break;

                case 8:
                    JOptionPane.showMessageDialog(null, "Saliendo del sistema");
                break;

                default:
                    JOptionPane.showMessageDialog(null, "Opcion invalida");
                break;
            }

        }while(menu != 8);

    }

}