import javax.swing.JOptionPane;

public class Principal {

    public static void main(String[] args) {
        
        Operaciones operaciones = new Operaciones();
        char menu;
        int datos;
        String opcion;
        do {

            opcion = JOptionPane.showInputDialog("\nEscoja una opcion"
                +"\n1. Inserta"
                +"\n2. Elimina un elemento"
                +"\n3. Buscar un elemento"
                +"\n4. Imprimir"
                +"\n5. Salir\n"
            );
            menu = opcion.charAt(0);

            switch(menu) {

                case '1':
                    datos = Integer.parseInt(JOptionPane.showInputDialog("Digite los datos"));    
                    operaciones.insertarEnCola(datos);
                    JOptionPane.showMessageDialog(null, "Nodo agregado");
                break;

                case '2':
                    datos = Integer.parseInt(JOptionPane.showInputDialog("Digite los datos"));
                    JOptionPane.showMessageDialog(null, operaciones.eliminar(datos));
                break;

                case '3':
                    datos = Integer.parseInt(JOptionPane.showInputDialog("Digite los datos"));  
                    if (operaciones.buscar(datos))
                        JOptionPane.showMessageDialog(null, "Encontrado");
                    else
                        JOptionPane.showMessageDialog(null, "No encontrado");
                break;

                case '4':
                    JOptionPane.showMessageDialog(null, operaciones.imprimir());
                break;

                case '5':
                    JOptionPane.showMessageDialog(null, "Saliendo del sistema");
                break;

                default:
                    JOptionPane.showMessageDialog(null, "Opcion invalida");
                break;
            }

        }while(menu != '5');

    }// Fin del main

}// Fin de la clase