//Se importa la libreria a usar
import javax.swing.JOptionPane;
public class GestorQueso
{
 public static void main(String args[])
 {
	 //Declaracion de variables
	 int precio, unidades, opcion, opcionQueso;
	 String tipo;
	 //Se crea la referencia
	 
	
	 
	 tipo= JOptionPane.showInputDialog("Digite el tipo de queso");
	 precio = Integer.parseInt(JOptionPane.showInputDialog("Digite el precio del queso"));
	 unidades= Integer.parseInt(JOptionPane.showInputDialog("Digite la cantidad de unidades de queso")); 
	 
	
	 Queso queso1= new Queso(tipo, precio, unidades);
	 Queso queso2 = new Queso ("Edam", 4000, 30);//Se crean las referencias e instancias del objeto queso
	 Queso queso3 =new Queso ("Gouda", 5000, 40);
	 
	 do
	 {
		 opcion= Integer.parseInt(JOptionPane.showInputDialog("Seleccione una opción: \n1) Aumentar unidades\n2) Disminuir unidades \n3)Ver precio \n4) Ver informacion \n5) Salir"));
		 
		 switch(opcion)
		 {
			 case 1:
			 do{
				opcionQueso = Integer.parseInt(JOptionPane.showInputDialog("Cual queso desea modificar: "+ "\n1) "+queso1.getTipo()+"\n2) "+queso2.getTipo()+"\n3) "+queso3.getTipo()+"\n4. Regresar al menu principal"));
				if(opcionQueso!=4)
				{
				unidades = Integer.parseInt(JOptionPane.showInputDialog("Cuantas unidades desea aumentar"));
                }
				switch(opcionQueso)
				{
					case 1:
					queso1.setUnidades(queso1.getUnidades()+unidades);
					break;
					
					case 2:
					queso2.setUnidades(queso2.getUnidades()+unidades);;
					break;
					
					case 3:
					queso3.setUnidades(queso3.getUnidades()+unidades);
					break;
					
					case 4:
					JOptionPane.showMessageDialog(null, "Regresando al menu principal");
					break;
					
					default:
					JOptionPane.showMessageDialog(null, "Error, digitar una opcion valida");
					break;
					}
				}while(opcionQueso!=4);
				break;
				
//---------------------------------------------------------------------------------------------------------------------------------------------------------------
			 
			 case 2:
			 do{
				opcionQueso = Integer.parseInt(JOptionPane.showInputDialog("Cual queso desea modificar: "+ "\n1) "+queso1.getTipo()+"\n2) "+queso2.getTipo()+"\n3) "+queso3.getTipo()+"\n4. Regresar al menu principal"));
				if(opcionQueso!=4)
				{
				unidades = Integer.parseInt(JOptionPane.showInputDialog("Cuantas unidades desea aumentar"));
                }
				switch(opcionQueso)
				{
					case 1:
					queso1.setUnidades(queso1.getUnidades()+unidades);
					break;
					
					case 2:
					queso2.setUnidades(queso2.getUnidades()+unidades);;
					break;
					
					case 3:
					queso3.setUnidades(queso3.getUnidades()+unidades);
					break;
					
					case 4:
					JOptionPane.showMessageDialog(null, "Regresando al menu principal");
					break;
					
					default:
					JOptionPane.showMessageDialog(null, "Error, digitar una opcion valida");
					break;
				}
				}while(opcion!=4);
			 break;
			 
//-------------------------------------------------------------------------------------------------------------------------------------------------------------

			 
			 case 3:
			 do{
				opcionQueso = Integer.parseInt(JOptionPane.showInputDialog("Para cual queso desea ver el precio: "+ "\n1) "+queso1.getTipo()+"\n2) "+queso2.getTipo()+"\n3) "+queso3.getTipo()+"\n4. Regresar al menu principal"));
				switch(opcionQueso)
				{
					case 1:
					   JOptionPane.showMessageDialog(null,"El precio del queso es: "+queso1.getPrecio());
					break;
					
					case 2:
	                   JOptionPane.showMessageDialog(null,"El precio del queso es: "+queso2.getPrecio());
					break;
					
					case 3:
				       JOptionPane.showMessageDialog(null,"El precio del queso es: "+queso3.getPrecio());
					break;
					
					case 4:
					  JOptionPane.showMessageDialog(null, "Regresando al menu principal");
					break;
					
					default:
				      JOptionPane.showMessageDialog(null, "Error, digitar una opcion valida");
					break;
				}
				}while(opcionQueso!=4);
				
			 break;
//-------------------------------------------------------------------------------------------------------------------------------------------------------------	 
			 case 4:
			 do{
				opcionQueso = Integer.parseInt(JOptionPane.showInputDialog("Para cual queso desea ver el precio: "+ "\n1) "+queso1.getTipo()+"\n2) "+queso2.getTipo()+"\n3) "+queso3.getTipo()+"\n4. Regresar al menu principal"));
				switch(opcionQueso)
				{
					case 1:
					   JOptionPane.showMessageDialog(null,queso1.toString());
					break;
					
					case 2:
					   JOptionPane.showMessageDialog(null,queso2);
					break;
					
					case 3:
					   JOptionPane.showMessageDialog(null,queso3);
					break;
					
					case 4:
					  JOptionPane.showMessageDialog(null, "Regresando al menu principal");
					break;
					
					default:
				      JOptionPane.showMessageDialog(null, "Error, digitar una opcion valida");
					break;
				}
				}while(opcionQueso!=4);
				
			 break;
//--------------------------------------------------------------------------------------------------------------------------------------------------------------			 
			 case 5:
				 JOptionPane.showMessageDialog(null, "Saliendo del sistema");
			 break;
			 
			 default:
			 JOptionPane.showMessageDialog(null, "Error, digitar una opcion valida");
			 break;
		 }
	 }while(opcion!= 5);
	 
 }//Fin metodo main
	
}//Fin de la clase GestoQueso
