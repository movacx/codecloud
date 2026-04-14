import javax.swing.JOptionPane;

public class Principal {
    public static void main(String[] args) {
        
        Operaciones opera = new Operaciones();
        int menu, datos, posicion;
        String mensaje;

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
                    datos = Integer.parseInt(JOptionPane.showInputDialog("Digite los datos"));
                    posicion = opera.localiza(datos);
                    if(posicion == -1 || posicion == -2)
                        JOptionPane.showMessageDialog(null, "No encontrado");
                    JOptionPane.showMessageDialog(null, "El nodo está en la posición: "+posicion);
                break;

                case 3:
                    posicion = Integer.parseInt(JOptionPane.showInputDialog("Digite la posicion"));
                    datos = opera.recupera(posicion);
                    if(datos == -1)
                        JOptionPane.showMessageDialog(null, "No encontrado");
                    JOptionPane.showMessageDialog(null, "Datos del nodo: "+datos);
                break;

                case 4:
                    posicion = Integer.parseInt(JOptionPane.showInputDialog("Digite la posicion"));
                    mensaje = opera.suprime(posicion);
                    JOptionPane.showMessageDialog(null, mensaje);
                break;

                case 5:
                    opera.anula();
                    JOptionPane.showMessageDialog(null, "Valores reiniciados");
                break;

                case 6:
                    datos = opera.primero();
                    if(datos == -1)
                        JOptionPane.showMessageDialog(null, "No hay nodos");
                    JOptionPane.showMessageDialog(null, "Nodo primero: "+datos);
                break;
                
                case 7:
                    mensaje = opera.imprimirLista();
                    JOptionPane.showMessageDialog(null, mensaje);
                break;

                case 8:
                    JOptionPane.showMessageDialog(null, "Saliendo del sistema");
                break;

                default:
                    JOptionPane.showMessageDialog(null, "Opcion invalida");
                break;
            }

        } while (menu != 8);

    }
}