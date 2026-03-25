//++======================================================================================================================++
import javax.swing.JOptionPane;

public class ControlEmpleados 
{
    String nombreEstudiante;
    TDAlistaObjeto miLista;
    int opcionMenu;
    String cedulaTemp;
    int edadTemp;
    int bandera = 0;

    public static void main(String[] args) 
    {
        new ControlEmpleados();
    }

    public ControlEmpleados()
    {
        miLista = new TDAlistaObjeto();
        menuPrincipal();
    }

//++======================================================================================================================++
    public void menuPrincipal()
    {
        do
        {
            opcionMenu = Integer.parseInt(JOptionPane.showInputDialog(null, 
                "--- *******MENU TRABAJO******** ---" +
                "\n 1. registrar empleado" +
                "\n 2. buscar por cedula" +
                "\n 3. buscar empleados con la misma edad" +
                "\n 4. Ver cantidad total de empleados" +
                "\n 5. mostrar todo" +
                "\n 6. borrar todo" +
                "\n 7. Salir", "Control de Empleados", JOptionPane.INFORMATION_MESSAGE));

            switch(opcionMenu)
            {
                case 1:
                    registrar();
                    break;
                case 2:
                    buscar();
                    break;
                case 3:
                    contar();
                    break;
                case 4:
                    JOptionPane.showMessageDialog(null, "Total: " + miLista.cantidadEmpleados());
                    break;
                case 5:
                    JOptionPane.showMessageDialog(null, miLista.mostrarLista());
                    break;
                case 6:
                    miLista.eliminarLista();
                    JOptionPane.showMessageDialog(null, "Lista limpia");
                    break;
                case 7:
                    JOptionPane.showMessageDialog(null, "Saliendo del sistema...");
                    break;
                default:
                    JOptionPane.showMessageDialog(null, "Esa opcion no sirve");
            }
        } while(opcionMenu != 7);
    }

//++======================================================================================================================++
    public void registrar()
    {
        cedulaTemp = JOptionPane.showInputDialog("Numero de cedula:");
        edadTemp = Integer.parseInt(JOptionPane.showInputDialog("Edad del empleado:"));
        
        Empleado nuevo;
        nuevo = new Empleado(cedulaTemp, edadTemp);
        
        miLista.insertar(nuevo);
        bandera = 1; 
        JOptionPane.showMessageDialog(null, "Guardado con exito");
    }

//++======================================================================================================================++
    public void buscar()
    {
        String buscarCed;
        if(bandera == 0)
        {
            JOptionPane.showMessageDialog(null, "Primero registre a alguien");
        }
        else
        {
            buscarCed = JOptionPane.showInputDialog("Cual cedula busca?");
            if(miLista.existeEmpleado(buscarCed) == true)
            {
                JOptionPane.showMessageDialog(null, "Ese empleado si existe");
            }
            else
            {
                JOptionPane.showMessageDialog(null, "No se encontro");
            }
        }
    }

//++======================================================================================================================++
    public void contar()
    {
        int laEdad;
        laEdad = Integer.parseInt(JOptionPane.showInputDialog("Edad a buscar:"));
        JOptionPane.showMessageDialog(null, "Hay " + miLista.contarPorEdad(laEdad) + " empleados");
    }
}
