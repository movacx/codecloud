import javax.swing.JOptionPane;

public class SistemaAlquiler {
    
    private Casa casa1, casa2, casa3;
    private Cliente clienteActual;
    private int totalAlquileres;
    private double montoTotalRecaudado;

    // --- Constructor ---
    public SistemaAlquiler() {
        // Crear las 3 casas con datos iniciales
        casa1 = new Casa("Casa Ancianos", "Cocal", 90000);
        casa2 = new Casa("Casa Vida", "Esparza", 85000);
        casa3 = new Casa("Casa Lucas", "Chacarita", 100000);
        this.totalAlquileres = 0;
        this.montoTotalRecaudado = 0;
    }

    public static void main(String[] args) {
        SistemaAlquiler sistema = new SistemaAlquiler();
        sistema.menuPrincipal();
    }
    
    
        // --- Menú Principal ---
    public void menuPrincipal() {
        byte opcion = 0;
        do {
 
		String menu = String.join("\n",
			" SISTEMA DE ALQUILER  ",
			"1. Alquilar casa",
			"2. Devolver casa y emitir factura",
			"3. Ver disponibilidad de casas",
			"4. Ver informe del sistema",
			"5. Salir"
		);
                opcion = Byte.parseByte(JOptionPane.showInputDialog(menu));

                switch (opcion) {
                    case 1:
							if (casa1.getEstaOcupada()) {
								JOptionPane.showMessageDialog(null, "Lo sentimos, esa casa ya está ocupada.");
							} else {
								String nombre = JOptionPane.showInputDialog("Nombre del cliente:");
								String cedula = JOptionPane.showInputDialog("Cédula del cliente:");
								String telefono = JOptionPane.showInputDialog("Teléfono del cliente:");
								this.clienteActual = new Cliente(nombre, cedula, telefono);

								int dias = Integer.parseInt(JOptionPane.showInputDialog("Cantidad de días a alquilar:"));
								casa1.alquilar(dias);
								this.totalAlquileres++;
								JOptionPane.showMessageDialog(null, "¡Casa alquilada con éxito!");
							}
                        break;
                    case 2:
                        //sintiempo
                        break;
                    case 3:
                        //sintiempo
                        break;
                    case 4:
                        //sintiempo
                        break;
                    case 5:
                        JOptionPane.showMessageDialog(null, "Vuelva pronto!");
                        break;
                    default:
                        JOptionPane.showMessageDialog(null, "Opcion no válida.");
                }

        } while (opcion != 5);
        
        
    }
    





}//fin clase
