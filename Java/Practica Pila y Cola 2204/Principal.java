import javax.swing.JOptionPane;

public class Principal
{
	public static void main(String []args)
	{
		
		//Instancias de las estructuras
		Pila pila = new Pila();
		Cola cola = new Cola();
		
		ManejoEstructuras controlador = new ManejoEstructuras();
		
		
		int opcion;
		do{
			opcion = Integer.parseInt(JOptionPane.showInputDialog(null,
			"\n1. Ingresar en pila" +
			"\n2. Ingresar en cola" +
			"\n3. Invertir pila" +
			"\n4. Invertir cola" +
			"\n5.  Mostrar pila"+
			"\n6. Mostrar cola"+
			"\n7. Salir"
			));
			
			switch(opcion)
			{
				case 1:
					controlador.ingresarPila(pila);
					JOptionPane.showMessageDialog(null, "Pila generada correctamente");
				
				break;
				case 2:
					controlador.ingresarCola(cola);
					JOptionPane.showMessageDialog(null, "Cola genera correctamente");
				break;
				case 3:
					controlador.invertirPila(pila);
				break;
				case 4:
					
				break;
				case 5:
					JOptionPane.showMessageDialog(null, controlador.mostrarPila(pila));
				break;
				case 6:
					JOptionPane.showMessageDialog(null, controlador.mostrarCola(cola));
				break;
				case 7:
					JOptionPane.showMessageDialog(null, "Saliendo del programa");
				return;
				
			}
		}while(opcion != 0);
	}
}
