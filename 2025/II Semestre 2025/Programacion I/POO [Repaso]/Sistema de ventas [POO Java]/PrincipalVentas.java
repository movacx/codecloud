//herlin fabian chavarria beita c5e187
import javax.swing.JOptionPane;
public class PrincipalVentas{
	private EquipoRefrigeracion refrigeradoraUno;
	private EquipoRefrigeracion refrigeradoraDos;
	private EquipoRefrigeracion refrigeradoraTres;
	private DatosVentas cajaRegistradora;

	
	public static void main(String []args){
		new PrincipalVentas();
	}
	
	public PrincipalVentas(){
		
		this.refrigeradoraUno = new EquipoRefrigeracion("Camara de enfriamiento", 600000, 50, 0);
		this.refrigeradoraDos = new EquipoRefrigeracion("Congelador industria", 900000, 50, 0);
		this.refrigeradoraTres = new EquipoRefrigeracion("Refrigeradora de dos puertas", 800000, 50, 0);
		this.cajaRegistradora = new DatosVentas(0,0);
		
		byte opcionMenu;
		
		do{
			opcionMenu = Byte.parseByte(JOptionPane.showInputDialog(null, 
			" Menú principal. Escoja una opción:"
			 +"\n1. Realizar ventas" 
			 +"\n2. Modificar precio"
			 +"\n3. Mostrar información"
			 +"\n4.Salir del sistema", "“Refrigeracion 3X\"", JOptionPane.PLAIN_MESSAGE));
			switch(opcionMenu){
				case 1:
					opcionUno();
					break;
				case 2:
					opcionDos();
					break;
				case 3:
					opcionTres();
					break;
				case 4:
						JOptionPane.showMessageDialog(null, "Gracias por usar el sistema" );
					break;
				default:
					JOptionPane.showMessageDialog(null, "Opcion Invalida", "Error 801", JOptionPane.ERROR_MESSAGE);
			}
			
		}while(opcionMenu != 4);
		
		
		

	}//Fin constructor
	
	public void opcionUno(){
		int caja;
		byte primeraOpcion;
		byte ventaRefrigeradorUno;
		byte ventaRefrigeradorDos;
		byte ventaRefrigeradorTres;

				
		do{

			primeraOpcion = Byte.parseByte(JOptionPane.showInputDialog(null,
			" Modelos de Refrigeración:"
			+"\n1.  | " + refrigeradoraUno.getModelo() + " | Unidades Disponibles: " + refrigeradoraUno.getUnidadesDisponibles() + " | Precio: " + refrigeradoraUno.getPrecio()
			+"\n2.  | " + refrigeradoraDos.getModelo() + " | Unidades Disponibles: " + refrigeradoraDos.getUnidadesDisponibles() + " | Precio: " + refrigeradoraDos.getPrecio()
			+"\n3.  | " + refrigeradoraTres.getModelo() + " | Unidades Disponibles: " + refrigeradoraTres.getUnidadesDisponibles() + " | Precio: " + refrigeradoraTres.getPrecio()
			+"\n4. Volver al inicio", "“Refrigeracion 3X\"", JOptionPane.PLAIN_MESSAGE));
			
			switch(primeraOpcion){
				case 1:
				
				ventaRefrigeradorUno = Byte.parseByte(JOptionPane.showInputDialog(null, "Digite la cantidad a vender: ", "“Refrigeracion 3X\"", JOptionPane.PLAIN_MESSAGE));
				
				if(ventaRefrigeradorUno <=0){
					JOptionPane.showMessageDialog(null, "Cantidad Invalida", "“Refrigeracion 3X\"", JOptionPane.PLAIN_MESSAGE);

				}else if(ventaRefrigeradorUno > refrigeradoraUno.getUnidadesDisponibles()){
					JOptionPane.showMessageDialog(null, "La cantidad a vender supera el inventario establecido", "Error 802", JOptionPane.WARNING_MESSAGE);

				}else if(  ventaRefrigeradorUno  <= refrigeradoraUno.getUnidadesDisponibles() ||  ventaRefrigeradorUno  >= 1 ){
					
					refrigeradoraUno.setUnidadesDisponibles(ventaRefrigeradorUno); 
					refrigeradoraUno.setUnidadesVendidas(+ ventaRefrigeradorUno );
					JOptionPane.showMessageDialog(null, "Venta completada!"
					+"\nLa cantidad Vendida fue de: " + refrigeradoraUno.getUnidadesVendidas() + " Unidades" , "“Refrigeracion 3X\"", JOptionPane.PLAIN_MESSAGE);
					
					/*caja registradora suma la venta al total*/
					cajaRegistradora.setTotalUnidadesVendidas(ventaRefrigeradorUno);	
					/*caja registradora | registro del dinero*/
					caja = ventaRefrigeradorUno * refrigeradoraUno.getPrecio();
					cajaRegistradora.setMontoRecaudado(+ caja);			
				}
					break;
					
				case 2:
				
				ventaRefrigeradorDos = Byte.parseByte(JOptionPane.showInputDialog(null, "Digite la cantidad a vender: ", "“Refrigeracion 3X\"", JOptionPane.PLAIN_MESSAGE));
				
				if(ventaRefrigeradorDos <=0){
					JOptionPane.showMessageDialog(null, "Cantidad Invalida", "“Refrigeracion 3X\"", JOptionPane.PLAIN_MESSAGE);

				}else if(ventaRefrigeradorDos > refrigeradoraDos.getUnidadesDisponibles()){
					JOptionPane.showMessageDialog(null, "La cantidad a vender supera el inventario establecido", "Error 802", JOptionPane.WARNING_MESSAGE);

				}else if(  ventaRefrigeradorDos  <= refrigeradoraDos.getUnidadesDisponibles() ||  ventaRefrigeradorDos  >= 1 ){
					
					refrigeradoraDos.setUnidadesDisponibles(ventaRefrigeradorDos); 
					refrigeradoraDos.setUnidadesVendidas(+ ventaRefrigeradorDos );
					JOptionPane.showMessageDialog(null, "Venta completada!"
					+"\nLa cantidad Vendida fue de: " + refrigeradoraDos.getUnidadesVendidas() + " Unidades" , "“Refrigeracion 3X\"", JOptionPane.PLAIN_MESSAGE);
					
					/*caja registradora suma la venta al total*/
					cajaRegistradora.setTotalUnidadesVendidas(ventaRefrigeradorDos);
					/*caja registradora | registro del dinero*/
					caja = ventaRefrigeradorDos * refrigeradoraDos.getPrecio();
					cajaRegistradora.setMontoRecaudado(+ caja);	
				}
				
					break;
				case 3:
				
				ventaRefrigeradorTres = Byte.parseByte(JOptionPane.showInputDialog(null, "Digite la cantidad a vender: ", "“Refrigeracion 3X\"", JOptionPane.PLAIN_MESSAGE));
				
				if(ventaRefrigeradorTres <=0){
					JOptionPane.showMessageDialog(null, "Cantidad Invalida", "“Refrigeracion 3X\"", JOptionPane.PLAIN_MESSAGE);

				}else if(ventaRefrigeradorTres > refrigeradoraTres.getUnidadesDisponibles()){
					JOptionPane.showMessageDialog(null, "La cantidad a vender supera el inventario establecido", "Error 802", JOptionPane.WARNING_MESSAGE);

				}else if(  ventaRefrigeradorTres  <= refrigeradoraTres.getUnidadesDisponibles() ||  ventaRefrigeradorTres  >= 1 ){
					
					refrigeradoraTres.setUnidadesDisponibles(ventaRefrigeradorTres); 
					refrigeradoraTres.setUnidadesVendidas(+ ventaRefrigeradorTres );
					JOptionPane.showMessageDialog(null, "Venta completada!"
					+"\nLa cantidad Vendida fue de: " + refrigeradoraTres.getUnidadesVendidas() + " Unidades" , "“Refrigeracion 3X\"", JOptionPane.PLAIN_MESSAGE);
					
					/*caja registradora suma la venta al total*/
					cajaRegistradora.setTotalUnidadesVendidas(ventaRefrigeradorTres);
					/*caja registradora | registro del dinero*/
					caja = ventaRefrigeradorTres * refrigeradoraTres.getPrecio();
					cajaRegistradora.setMontoRecaudado(+ caja);	
				}
				
					break;
				case 4:
					break;
				default:
					JOptionPane.showMessageDialog(null, "la opcion no es valida", "Error 803", JOptionPane.ERROR_MESSAGE);
			}

		}while(primeraOpcion != 4);

	}/*fin OpcionUno*/
	
	
	public void opcionDos(){
		byte opcionCambioPrecio;
		int modificarPrecioUno;
		int modificarPrecioDos;
		int modificarPrecioTres;
		JOptionPane.showMessageDialog(null, "Advertencia!! Estas por entrar a \"Modificacion de precio\" " + "\nCargando...", "Advertencia | CODE 805", JOptionPane.WARNING_MESSAGE);
		
		do{
			
			opcionCambioPrecio = Byte.parseByte(JOptionPane.showInputDialog(null,
			"Modificacion de precios:"
			+"\n1.  | " + refrigeradoraUno.getModelo() +  "          	    | Precio: " + refrigeradoraUno.getPrecio()
			+"\n2.  | " + refrigeradoraDos.getModelo() +  "                   | Precio: " + refrigeradoraDos.getPrecio()
			+"\n3.  | " + refrigeradoraTres.getModelo() + "  				  | Precio: " + refrigeradoraTres.getPrecio()
			+"\n"
			+"\n4. Volver al inicio", "“Refrigeracion 3X\"", JOptionPane.PLAIN_MESSAGE));
			
			
			if(opcionCambioPrecio == 1){
				modificarPrecioUno = Integer.parseInt(JOptionPane.showInputDialog(null, "Ingrese el nuevo precio",  "“Refrigeracion 3X\"", JOptionPane.PLAIN_MESSAGE));
				refrigeradoraUno.setPrecio(modificarPrecioUno);
			}else if(opcionCambioPrecio == 2){
				modificarPrecioDos = Integer.parseInt(JOptionPane.showInputDialog(null, "Ingrese el nuevo precio",  "“Refrigeracion 3X\"", JOptionPane.PLAIN_MESSAGE));
				refrigeradoraDos.setPrecio(modificarPrecioDos);
			}else if(opcionCambioPrecio == 3){
				modificarPrecioTres = Integer.parseInt(JOptionPane.showInputDialog(null, "Ingrese el nuevo precio",  "“Refrigeracion 3X\"", JOptionPane.PLAIN_MESSAGE));
				refrigeradoraTres.setPrecio(modificarPrecioTres);
			}else if(opcionCambioPrecio == 4){
				
			}
			
		}while(opcionCambioPrecio != 4);

	}/*fin opcionDos*/
		
		
		
	public void opcionTres(){
		byte registro;
	
			JOptionPane.showMessageDialog(null, 
			"Reporte:"
			+"\nMonto recaudado por las ventas: " + cajaRegistradora.getMontoRecaudado()
			+"\nTotal de Unidades Vendidas: " + cajaRegistradora.getTotalUnidadesVendidas()
			+"\n"
			+"\n4.Salir del sistema", "“Refrigeracion 3X\"", JOptionPane.PLAIN_MESSAGE);
		
			
			
		

		
		
		
		
		
		
		
		
		
	}/*fin opcionTres*/

	
	
	
	
	
	
	
	
}/*fin clase*/
