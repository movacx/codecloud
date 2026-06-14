
import javax.swing.*;
public class PruebaRectangulo{
	Rectangulo miRectangulo;
	
	public static void main(String[]args){
		new PruebaRectangulo();
	}
	
	public PruebaRectangulo(){
		//solicitando los valores al usuario
		int base=0, altura=0;
		base = Integer.parseInt(JOptionPane.showInputDialog("Digite la base"));
		altura = Integer.parseInt(JOptionPane.showInputDialog("Digite la altura"));
		
		miRectangulo = new Rectangulo(base, altura);
		System.out.println(miRectangulo);
		
		this.menu();
	}
	public void menu(){
		int modificarBase;
		byte opcion;
		do{
			opcion = Byte.parseByte(JOptionPane.showInputDialog("MENU"
									+"\n1. SACAR AREA."
									+"\n2. SACAR PERIMETRO. "
									+"\n3. VER MEDIDAS DE BASE Y ALTURA. "
									+"\n4. MODIFICAR VALORES DE BASE Y ALTURA. "
									+"\n5. VER MEDIDAS DE LA BASE. "
									+"\n0. SALIR"));
			
			
			
			switch (opcion){
				case 1:
					JOptionPane.showMessageDialog(null, "Area es "+miRectangulo.calcularArea());
					break;
				case 2:
					JOptionPane.showMessageDialog(null, "Perimetro es "+miRectangulo.calcularPerimetro());
					break;
				case 3:
					JOptionPane.showMessageDialog(null, "Base: "+miRectangulo.getBase()+"Altura es: "+miRectangulo.getAltura());
					break;
				case 4:
					modificarBase = Integer.parseInt(JOptionPane.showInputDialog(null, "digite la nueva base"));
					miRectangulo.setBase(modificarBase);
					break;
				case 5:
					JOptionPane.showMessageDialog(null, "la base es" +"dato invalido");
					break;
				case 0:
					break;
				default: JOptionPane.showMessageDialog(null, "Dato Invalido");
					
			}
			
			
		}while(opcion!=0);
	}




}//fin clase
