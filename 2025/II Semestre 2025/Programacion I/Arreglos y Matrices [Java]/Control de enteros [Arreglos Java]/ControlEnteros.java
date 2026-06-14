import javax.swing.JOptionPane;
public class ControlEnteros{
	
	public ControlEnteros()
	{
		Enteros metodosValores = null;
		int opcion;
		int longitud, valorArregloA, valorArregloB;
		int numeroArreglo;
		boolean bloqueo = false;
		do{
			opcion=Integer.parseInt(JOptionPane.showInputDialog("Seleccione una opcion: \n"
			+"\n1)Registrar valores enteros"
			+"\n2)Sumar arreglos A & B"
			+"\n3)Multiplicar arreglo C"
			+"\n4)Ver numero menor de arreglo"
			+"\n5)Mostrar valores de un arreglo"
			+"\n6)Salir"));
			
			switch(opcion){
				case 1:
				
				
				
					longitud = Integer.parseInt(JOptionPane.showInputDialog("Digite la longiud de los arreglos"));
					metodosValores = new Enteros(longitud);
					
					for(int indice=0; indice < longitud; indice++)
					{
						valorArregloA = Integer.parseInt(JOptionPane.showInputDialog("Digite el valor de ArregloA" + "\nEn la posicion"+indice));
						
						valorArregloB = Integer.parseInt(JOptionPane.showInputDialog("Digite el valor de ArregloB" + "\nEn la posicion"+indice));
						metodosValores.setValor(valorArregloA,valorArregloB, indice);

					}
						
						
					
				break;
				case 2:
					if(bloqueo)
					{
						metodosValores.sumarArreglos();
					}else{
						JOptionPane.showMessageDialog(null, "Ingrese primero a la opcion 1 del menu");
					}
					
				break;
				case 3:
					if(bloqueo)
					{
						metodosValores.multiplicarArreglos();
					}else{
						JOptionPane.showMessageDialog(null, "Ingrese primero a la opcion 1 del menu");
					}
					
				break;
				case 4:

					JOptionPane.showMessageDialog(null, "El numero menor del arreglo D es el: " + metodosValores.getNumeroMenor());
				break;
				case 5:
				
				
					if(bloqueo)
					{
						
						numeroArreglo = Integer.parseInt(JOptionPane.showInputDialog(null, "Para cual arreglo desea ver los: "
						+"\nArregloA"
						+"\nArregloB"
						+"\nArregloC"
						+"\nArregloD"));
						JOptionPane.showMessageDialog(null, "Los valores del arreglo son: \n"
						+metodosValores.getValoresArreglo(numeroArreglo));
						
					}else{
						JOptionPane.showMessageDialog(null, "Ingrese primero a la opcion 1 del menu");
					}
				
				

				break;
				case 6:
				break;
				default:
					JOptionPane.showMessageDialog(null, "favor de digitar una opcion valida del menu");
					break;
				
			}

		}while(opcion !=6);
	}//FIN DEL METODO CONSTRUCTOR
	
	public static void main(String args[]){
		
		ControlEnteros control = new ControlEnteros();
		
		
		
	}//FIN DEL MAIN
}//fin clase





