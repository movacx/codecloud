import javax.swing.JOptionPane;

public class MainColaJOption 
{
    public static void main(String[] args) 
    {

        Cola cola = new Cola();
        int opcion = 0;

        do 
        {
            try 
            {
                String menu = """
                        === MENÚ COLA ===
                        1. Encolar
                        2. Desencolar
                        3. Ver frente
                        4. Mostrar cola
                        5. Vaciar cola
                        6. Salir
                        """;

                opcion = Integer.parseInt(JOptionPane.showInputDialog(menu));

                switch (opcion) 
                {

                    case 1:
                        int dato = Integer.parseInt(
                                JOptionPane.showInputDialog("Ingrese número:")
                        );
                        cola.encolar(dato);
                        break;

                    case 2:
                        int eliminado = cola.desencolar();
                        if (eliminado == -1) 
                        {
                            JOptionPane.showMessageDialog(null, "Cola vacía");
                        } else {
                            JOptionPane.showMessageDialog(null,
                                    "Elemento eliminado: " + eliminado);
                        }
                        break;

                    case 3:
                        int frente = cola.frente();
                        if (frente == -1) 
                        {
                            JOptionPane.showMessageDialog(null, "Cola vacía");
                        } else {
                            JOptionPane.showMessageDialog(null,
                                    "Frente: " + frente);
                        }
                        break;

                    case 4:
                        JOptionPane.showMessageDialog(null,
                                "Contenido:\n" + cola.mostrarComoTexto());
                        break;

                    case 5:
                        cola.vaciar();
                        JOptionPane.showMessageDialog(null, "Cola vaciada");
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
                        "Error: Ingrese solo numeros");
            }

        } while (opcion != 6);
    }
}
