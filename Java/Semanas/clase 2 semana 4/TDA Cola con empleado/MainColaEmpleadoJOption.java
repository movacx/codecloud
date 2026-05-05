import javax.swing.JOptionPane;

public class MainColaEmpleadoJOption 
{
    public static void main(String[] args) 
    {

        ColaEmpleado cola = new ColaEmpleado();
        int opcion = 0;

        do 
        {
            try 
            {
                String menu = """
                        === MENU COLA EMPLEADOS ===
                        1. Encolar empleado
                        2. Desencolar empleado
                        3. Ver frente
                        4. Mostrar cola
                        5. Vaciar cola
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
                        cola.encolar(emp);
                        break;

                    case 2:
                        Empleado eliminado = cola.desencolar();
                        if (eliminado == null) 
                        {
                            JOptionPane.showMessageDialog(null, "Cola vacía");
                        } else 
                        {
                            JOptionPane.showMessageDialog(null,
                                    "Empleado eliminado:\n" + eliminado);
                        }
                        break;

                    case 3:
                        Empleado frente = cola.frente();
                        if (frente == null) 
                        {
                            JOptionPane.showMessageDialog(null, "Cola vacía");
                        } else 
                        {
                            JOptionPane.showMessageDialog(null,
                                    "Frente:\n" + frente);
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
