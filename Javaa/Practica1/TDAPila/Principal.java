import javax.swing.JOptionPane;

public class Principal {

    public static void main(String[] args) {
        Operaciones operaciones = new Operaciones();
        int menu, datos, valor;
        String mensaje;

        do {

            menu = Integer.parseInt(JOptionPane.showInputDialog("\nEscoja una opcion"
                +"\n1. Agregar nodo"
                +"\n2. Imprimir pila"
                +"\n3. Borrar nodo"
                +"\n4. Salir"
            ));

            switch(menu) {

                case 1:
                    datos = Integer.parseInt(JOptionPane.showInputDialog("Digite los datos"));    
                    operaciones.agregar(datos);
                    JOptionPane.showMessageDialog(null, "Nodo agregado");
                break;

                case 2:
                  
                    JOptionPane.showMessageDialog(null, operaciones.imprimir());
                break;

                case 3:
                    valor = Integer.parseInt(JOptionPane.showInputDialog("Digite el valor a"));  
                    mensaje = operaciones.borrar(valor);
                    JOptionPane.showMessageDialog(null, mensaje);
                break;

                case 4:
                    JOptionPane.showMessageDialog(null, "Saliendo del sistema");
                break;

                default:
                    JOptionPane.showMessageDialog(null, "Opcion invalida");
                break;
            }

        }while(menu != 4);
    }

}