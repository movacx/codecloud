import javax.swing.JOptionPane;

public class MainJOption 
{
    public static void main(String[] args) 
    {

        Pila pila = new Pila();
        int opcion = 0;

        do 
        {
            try 
            {
                String menu = """
                        === MENU PILA ===
                        1. Apilar
                        2. Desapilar
                        3. Ver cima
                        4. Mostrar pila
                        5. Vaciar pila
                        6. Salir
                        """;

                opcion = Integer.parseInt(JOptionPane.showInputDialog(menu));

                switch (opcion) 
                {

                    case 1:
                        int dato = Integer.parseInt(
                                JOptionPane.showInputDialog("Ingrese numero:")
                        );
                        pila.apilar(dato);
                        break;

                    case 2:
                        int eliminado = pila.desapilar();
                        if (eliminado == -1) 
                        {
                            JOptionPane.showMessageDialog(null, "Pila vacia");
                        } else 
                        {
                            JOptionPane.showMessageDialog(null,
                                    "Elemento eliminado: " + eliminado);
                        }
                        break;

                    case 3:
                        int cima = pila.cima();
                        if (cima == -1) 
                        {
                            JOptionPane.showMessageDialog(null, "Pila vacia");
                        } else 
                        {
                            JOptionPane.showMessageDialog(null,
                                    "Cima: " + cima);
                        }
                        break;

                    case 4:
                        JOptionPane.showMessageDialog(null,
                                "Contenido:\n" + pila.mostrarComoTexto());
                        break;

                    case 5:
                        pila.vaciar();
                        JOptionPane.showMessageDialog(null, "Pila vaciada");
                        break;

                    case 6:
                        JOptionPane.showMessageDialog(null, "Saliendo...");
                        break;

                    default:
                        JOptionPane.showMessageDialog(null, "Opción invalida");
                }

            } catch (Exception e) 
            {
                JOptionPane.showMessageDialog(null,
                        "Error: Ingrese solo números");
            }

        } while (opcion != 6);
    }
}
