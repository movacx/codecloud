//autores Ramses guzman C13600  & Fabian Chavarria C5E187




import javax.swing.JOptionPane;



public class PrincipalVeterinaria{
	private Mascota mascota1, mascota2, mascota3;
	private Veterinario nombreVeterinario;
	private String telefono;
	private String nombre;
	int precioMedicamentos;

	//private in cantidadAtenciones;
	
	public PrincipalVeterinaria (){
		mascota1 = new Mascota(" Minina ", " Gato ",  2.5);
		mascota2 = new Mascota(" Chigui ", " Perro ",  9.8);
		mascota3 = new Mascota(" Colita ", " Perro ",  6.3);
		
		String nombre = JOptionPane.showInputDialog("Digite el nombre del Veterinario");
		String telefono = JOptionPane.showInputDialog("Digite el numero del Veterinario");
		
		nombreVeterinario = new Veterinario(nombre, telefono, 0);
		menuPrincipal();
	}
	

	
	public static void main(String []args){
		new PrincipalVeterinaria();
		
		
	}
	
	public void menuPrincipal(){
		byte opcionMenu  ;
		
		
		do{
			opcionMenu = Byte.parseByte(JOptionPane.showInputDialog("Bienvenido al sistema de atención veterinaria" 
			+ "\n 1. Atender mascota"
			+ "\n 2. Mostrar información del veterinario "
			+ "\n 3. Modificar peso de una mascota"
			+ "\n 4. Ver reporte"
			+ "\n 5. Salir"));
			
			switch(opcionMenu){
				case 1:
					atenderMascota();
					break;
				case 2:
					break;
				case 3:
					break;
				case 4:
					break;
				case 5:
					break;
				default:
					JOptionPane.showMessageDialog(null, "Opcion Invalida");		
			}
		}while (opcionMenu !=5);
		
	}
	
	
	public void atenderMascota(){
		byte opcionSubmenu;
		int cantidadAtenciones, cantidadMedicamentos = 0;
		String detalleFactura = "";
		int costoTotalMedi = 0;
		int totalFactura = 0;
		
		
		Mascota mascotaSeleccionada = null;
		
		opcionSubmenu = Byte.parseByte(JOptionPane.showInputDialog("Seleccione una mascota" 
		+ "\n 1. Minina – Gato"
		+ "\n 2. Chigui – Perro"
		+ "\n 3. Colita _ Perro"
		+ "\n 4. Salir")); System.out.println("4");
		
		mascotaSeleccionada = mascota1;
		mascotaSeleccionada = mascota2;
		mascotaSeleccionada = mascota3;
		
		switch(opcionSubmenu){
			case 1:
			
				cantidadMedicamentos= Integer.parseInt(JOptionPane.showInputDialog(null, "Cuantos medicamentos le fueron recetados"));
				if (cantidadMedicamentos == cantidadMedicamentos){
				
				for (int contador = 1; contador <= cantidadMedicamentos; contador++) {
					String nombreMedicamentos = JOptionPane.showInputDialog(null, "Ingresá el nombre del medicamento " + contador + ":", "Nombre", JOptionPane.QUESTION_MESSAGE);
					precioMedicamentos = Integer.parseInt(JOptionPane.showInputDialog(null, "¿Cuánto cuesta el " + nombreMedicamentos + "?", "Precio", JOptionPane.QUESTION_MESSAGE));
					
					detalleFactura=detalleFactura+"\n"+nombreMedicamentos +" - "+precioMedicamentos;
					costoTotalMedi = costoTotalMedi + precioMedicamentos;
					totalFactura = costoTotalMedi + 20000;
					}
				}
				 cantidadAtenciones=nombreVeterinario.getCantidadAtenciones() + 1;
				 nombreVeterinario.setCantidadAtenciones(cantidadAtenciones);
					 
				JOptionPane.showMessageDialog(null, "==Factura===" 
				+ "\n Nombre del Veterinario: " + this.nombreVeterinario
				+ mascotaSeleccionada
				+ "\n Precio de la consulta: 20.000 colones" 
				+ "\n Lista de medicamentos: " + detalleFactura
				+ "\n Precio de medicamentos: " + precioMedicamentos
				+ "\n Total de factura "+ totalFactura);
				break;
			case 2:

				cantidadMedicamentos= Integer.parseInt(JOptionPane.showInputDialog(null, "Cuantos medicamentos le fueron recetados"));
				if (cantidadMedicamentos == cantidadMedicamentos){
				
				for (int contador = 1; contador <= cantidadMedicamentos; contador++) {
					String nombreMedicamentos = JOptionPane.showInputDialog(null, "Ingresá el nombre del medicamento " + contador + ":", "Nombre", JOptionPane.QUESTION_MESSAGE);
					precioMedicamentos = Integer.parseInt(JOptionPane.showInputDialog(null, "¿Cuánto cuesta el " + nombreMedicamentos + "?", "Precio", JOptionPane.QUESTION_MESSAGE));
					
					detalleFactura=detalleFactura+"\n"+nombreMedicamentos +" - "+precioMedicamentos;
					costoTotalMedi = costoTotalMedi + precioMedicamentos;
					totalFactura = costoTotalMedi + 20000;
					}
				}
				 cantidadAtenciones=nombreVeterinario.getCantidadAtenciones() + 1;
				 nombreVeterinario.setCantidadAtenciones(cantidadAtenciones);
					 
				JOptionPane.showMessageDialog(null, "==Factura===" 
				+ "\n Nombre del Veterinario: " + this.nombreVeterinario
				+ mascotaSeleccionada
				+ "\n Precio de la consulta: 20.000 colones" 
				+ "\n Lista de medicamentos: " + detalleFactura
				+ "\n Precio de medicamentos: " + precioMedicamentos
				+ "\n Total de factura "+ totalFactura);
			
				break;
			case 3:

				cantidadMedicamentos= Integer.parseInt(JOptionPane.showInputDialog(null, "Cuantos medicamentos le fueron recetados"));
				if (cantidadMedicamentos == cantidadMedicamentos){
				
				for (int contador = 1; contador <= cantidadMedicamentos; contador++) {
					String nombreMedicamentos = JOptionPane.showInputDialog(null, "Ingresá el nombre del medicamento " + contador + ":", "Nombre", JOptionPane.QUESTION_MESSAGE);
					precioMedicamentos = Integer.parseInt(JOptionPane.showInputDialog(null, "¿Cuánto cuesta el " + nombreMedicamentos + "?", "Precio", JOptionPane.QUESTION_MESSAGE));
					
					detalleFactura=detalleFactura+"\n"+nombreMedicamentos +" - "+precioMedicamentos;
					costoTotalMedi = costoTotalMedi + precioMedicamentos;
					totalFactura = costoTotalMedi + 20000;
					}
				}
				 cantidadAtenciones=nombreVeterinario.getCantidadAtenciones() + 1;
				 nombreVeterinario.setCantidadAtenciones(cantidadAtenciones);
					 
				JOptionPane.showMessageDialog(null, "==Factura===" 
				+ "\n Nombre del Veterinario: " + this.nombreVeterinario
				+ mascotaSeleccionada
				+ "\n Precio de la consulta: 20.000 colones" 
				+ "\n Lista de medicamentos: " + detalleFactura
				+ "\n Precio de medicamentos: " + precioMedicamentos
				+ "\n Total de factura "+ totalFactura);

				break;
			default:
				JOptionPane.showMessageDialog(null, "Opcion Invalida");		
		}
		
		
		
	}

















}//fin clase
