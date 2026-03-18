import javax.swing.JOptionPane;



public class Prueba
{
	NodosEnlazados nuevoNodo = null;
	
	public static void main(String[]args)
	{
			
			
		int opcion;
		NodosEnlazados nuevoNodo = new NodosEnlazados();

		do {
			opcion = Integer.parseInt(JOptionPane.showInputDialog(null, "1. Crear lista\n6. Salir"));

			switch (opcion) {
				case 1:
					JOptionPane.showMessageDialog(null, "Lista creada");
					nuevoNodo = new NodosEnlazados();
					break;

				case 2:
					System.out.println("Opcion 2");
					break;
			}

		} while (opcion != 6);
			
	}
	
}
