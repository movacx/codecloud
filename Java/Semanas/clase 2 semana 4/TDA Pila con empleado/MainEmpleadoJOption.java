import javax.swing.JOptionPane;
public class MainEmpleadoJOption 
{
    public static void main(String[] args) 
    {

        PilaEmpleado pila = new PilaEmpleado();
        int opcion = 0;

        do 
        {
            try 
            {
                String menu = """
                        === MENÚ PILA EMPLEADOS ===
                        1. Apilar empleado
                        2. Desapilar empleado
                        3. Ver cima
                        4. Mostrar pila
                        5. Vaciar pila
                        6. Salir
                        """;

                opcion = Integer.parseInt(JOptionPane.showInputDialog(menu));

                switch (opcion) 
                {

                    case 1:
                        int id = Integer.parseInt(
                                JOptionPane.showInputDialog("Ingrese ID:")
                        );

                        String nombre = JOptionPane.showInputDialog("Ingrese nombre:");

                        Empleado emp = new Empleado(id, nombre);
                        pila.apilar(emp);
                        break;

                    case 2:
                        Empleado eliminado = pila.desapilar();
                        if (eliminado == null) 
                        {
                            JOptionPane.showMessageDialog(null, "Pila vacía");
                        } else 
                        {
                            JOptionPane.showMessageDialog(null,
                                    "Empleado eliminado:\n" + eliminado);
                        }
                        break;

                    case 3:
                        Empleado cima = pila.cima();
                        if (cima == null) 
                        {
                            JOptionPane.showMessageDialog(null, "Pila vacía");
                        } else 
                        {
                            JOptionPane.showMessageDialog(null,
                                    "Cima:\n" + cima);
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
                        JOptionPane.showMessageDialog(null, "Opción inválida");
                }

            } catch (Exception e) 
            {
                JOptionPane.showMessageDialog(null,
                        "Error: Verifique los datos ingresados");
            }

        } while (opcion != 6);
    }
}
