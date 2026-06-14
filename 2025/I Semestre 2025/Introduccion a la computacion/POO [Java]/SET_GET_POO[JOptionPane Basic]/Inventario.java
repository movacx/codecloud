import javax.swing.JOptionPane;
public class Inventario{
	
	
	
	public static void main(String args[]){
		
		String placa, marca, modelo, accesorios, tipo;
		String opcionString;
		char opcion = 'x';
		boolean estado = true;
		boolean control1=false;
		boolean control2=false;
		Equipo equipo1=null;
		Equipo equipo2=null;
		do{
			opcionString = JOptionPane.showInputDialog(null, "Seleccione una opcion: " 
			+ "\nA. Registrar Equipo 1" 
			+ "\nb. Registrar Equipo 2" 
			+ "\nc. Mostrar el modelo del Equipo 1" 
			+ "\nd. Mostrar el tipo del Equipo 2" + "\ne. Informacion"  + "\nf. Salir", "test", JOptionPane.PLAIN_MESSAGE);
			opcion = opcionString.charAt(0);
			switch(opcion){
				case 'a':
				placa = JOptionPane.showInputDialog(null, "Digite la placa");
				marca = JOptionPane.showInputDialog(null, "Digite la marca");
				modelo = JOptionPane.showInputDialog(null, "Digite el modelo");
				accesorios = JOptionPane.showInputDialog(null, "Digite los accesorios");
				tipo = JOptionPane.showInputDialog(null, "Digite la tipo de equipo");
				
				equipo1 = new Equipo(placa, marca, modelo, accesorios, tipo, estado); //se crea la instancia
				control1=true;
				
				break;
				//===============================================================
				case 'b':
				placa = JOptionPane.showInputDialog(null, "Digite la placa");
				marca = JOptionPane.showInputDialog(null, "Digite la marca");
				modelo = JOptionPane.showInputDialog(null, "Digite el modelo");
				accesorios = JOptionPane.showInputDialog(null, "Digite los accesorios");
				tipo = JOptionPane.showInputDialog(null, "Digite la tipo de equipo");
				
				equipo2 = new Equipo(placa, marca, modelo, accesorios, tipo, estado); //se crea la instancia
				control2=true;
				break;
				//===============================================================
				case 'c':
				if(control1){
					JOptionPane.showMessageDialog(null, "El modelo es "+equipo1.getModelo());
				}else{
					JOptionPane.showMessageDialog(null, "Primero debe de ingresar un equipo1");
				}
				
				
				break;
				//===============================================================
				case 'd':
				if(control2){
					JOptionPane.showMessageDialog(null, "El tipo de equipo es "+equipo2.getTipo());
				}else{
					JOptionPane.showMessageDialog(null, "Primero debe de ingresar un equipo2");
				}
				
				
				break;
				//===============================================================
				case 'e':
				
				if(control1 && control2){
					JOptionPane.showMessageDialog(null, equipo1+""+equipo2);
				}else{
					JOptionPane.showMessageDialog(null, "Debe de ingresar los dos equipos");
				}
				break;
				//===============================================================
				case 'f':
				JOptionPane.showMessageDialog(null, "Saliendo del sistema....");
				break;
				//===============================================================
				default:
				JOptionPane.showMessageDialog(null, "ERROR....");
				break;
				//===============================================================

			}
		}while(opcion !='f');
		
		
		
	}
	

	
	
}//Fin clase
