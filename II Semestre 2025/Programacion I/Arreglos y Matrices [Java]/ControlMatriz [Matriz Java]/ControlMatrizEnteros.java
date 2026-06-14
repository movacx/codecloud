import javax.swing.JOptionPane;
public class ControlMatrizEnteros
{
	public static void main(String[]args){
		int fila, columna, valor, opcion;
		
		
		MatrizEnteros enteros = new MatrizEnteros();
		do{
			
			opcion = Integer.parseInt(JOptionPane.showInputDialog(null, 
			"\nSeleccione una opcion"
			+"\n\n1. Llenar el arreglo bidimensional de manera aleatoria."
			+"\n\n2. Agregar un valor en un espacio específico del arreglo"
			+"\n\n3. Imprimir todos los valores el arreglo bidimensional."
			+"\n\n4. Imprimir los valores de una fila en específico del arreglo bidimensional"
			+"\n\n5. Imprimir los valores de una columna en específico del arreglo bidimensional."
			+"\n\n6. Imprimir los valores de la diagonal principal de izquierda a derecha."
			+"\n\n7. Imprimir los valores de la diagonal secundaria de derecha a izquierda. "
			+"\n\n8. Imprimir los valores de la diagonal principal de derecha a izquierda. "
			+"\n\n9. Imprimir los valores de la diagonal secundaria de izquierda a derecha. "
			+"\n\n10.Calcular promedio."
			+"\n\n11.Salir."));

			switch(opcion)
			{
				case 1:
				
					enteros.llenarMatriz();
				
				
					break;
					
				//-------------------------------------------------------------------------------------------------------------
				case 2:
					fila = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite la fila en la que desea guardar el valor"));
					columna = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite la columna en la que desea guardar el valor"));
					valor = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite el valor que desea guardar"));
					
					if(	(enteros.verificarColumna (columna-1))	&&	(enteros.verificarFila (fila-1)) )
					{
						enteros.setValor(fila-1, columna-1, valor);
						JOptionPane.showMessageDialog(null, "Numero guardado correctamente");
					}
					else
					{
						JOptionPane.showMessageDialog(null, "El valor no puede ser agregado en la fila y columna indicadas\n"+
						"Valores fuera del rango de la matriz");
					}

					
					
					break;
				//-------------------------------------------------------------------------------------------------------------
				case 3:
					JOptionPane.showMessageDialog(null, enteros.getArregloBidimensional());
					break;
				//-------------------------------------------------------------------------------------------------------------
				case 4:
				fila = Integer.parseInt(JOptionPane.showInputDialog("Digite la fila para la que desea ver el valor"));
				if(enteros.verificarFila(fila -1))
				
					JOptionPane.showMessageDialog(null, enteros.getFila(fila-1));
				else
					JOptionPane.showMessageDialog(null, "La fila no es validaa");
				
					break;
				//-------------------------------------------------------------------------------------------------------------
				case 5:
				columna = Integer.parseInt(JOptionPane.showInputDialog("Digite la columna para la que desea ver el valor"));
				if(enteros.verificarColumna(columna -1))
				
					JOptionPane.showMessageDialog(null, enteros.getcolumna(columna-1));
				else
					JOptionPane.showMessageDialog(null, "La columna no es validaa");
				
					break;
				//-------------------------------------------------------------------------------------------------------------
				case 6:
					JOptionPane.showMessageDialog(null, enteros.getDiagonalPrincipalIzquierdaDerecha());
					break;
				//-------------------------------------------------------------------------------------------------------------
				case 7:
					JOptionPane.showMessageDialog(null, enteros.getDiagonalPrincipalDerechaIzquierda());
					break;
				//-------------------------------------------------------------------------------------------------------------
				case 8:
					JOptionPane.showMessageDialog(null, enteros.getDiagonalSecundariaDerechaIzquierda());
					break;
				//-------------------------------------------------------------------------------------------------------------
				case 9:
					JOptionPane.showMessageDialog(null, enteros.getDiagonalSecundariaIzquierdDerecha());
					break;
				//-------------------------------------------------------------------------------------------------------------
				case 10:
					JOptionPane.showMessageDialog(null, "El promedio del arreglo es: \n" + enteros.promedio());
					break;
				//-------------------------------------------------------------------------------------------------------------
				case 11:
					JOptionPane.showMessageDialog(null, "Saliendo del sistema");
					break;
				//-------------------------------------------------------------------------------------------------------------
				default:
					JOptionPane.showMessageDialog(null, "error");
			}
		
			
			
		}while(opcion !=11);


	
		

	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	}//fin clase
