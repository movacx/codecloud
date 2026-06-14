/* Fabian Chavarria Beita */
/* C5E187 */

import javax.swing.JOptionPane;

public class ciclos {
	
/* Variables */ 
	
/* Opcion 1 */
int b = 99;
int a = 1;

/* opcion 2 */ 
String[] frutas = {"manzana", "pera", "platano", "naranja", "mandarina", "limon", "sandia", "melon", "fresa", "frabuesa", "mora", "arandano", "cereza", "ciruela", "cacao", "rompopexd", "kiwi", "mango", "cacao", "cebolla" };
int precio;
int total;

/* opcion 3 */

int suma = 0;
int i = 1;
int n;

/* opcion 4 */ 
int numero;
int contador2 = 1;



	
	public static void main(String[] args) {
		new ciclos();
	}
	
	public ciclos(){
		menu();
	}
	

/* Menu principal */
		public void menu(){
			byte menu;
			
			
			do{
				menu = Byte.parseByte(JOptionPane.showInputDialog("Menu de aplicaciones \n 1. Generar series numéricas \n 2. Ingrese el precio de 20 frutas \n 3. Calcular la suma 1 + 2 + 3 + 4 + .... + N. \n 4. Tabla de multiplicar \n 5. Tomar un descanso \n 0. Salir"));
				
				switch (menu){
					case 1:
						opcion1();
						break;
					case 2:
						opcion2();
						break;
					case 3:
						opcion3();
						break;
					case 4:
						opcion4();
						break;
					case 5:
						heladeria();
						break;
						
					case 0:
						JOptionPane.showMessageDialog(null, "Adios");
						break;
					default:
						JOptionPane.showMessageDialog(null, "Opcion Invalida", "Opcion Invalida", JOptionPane.WARNING_MESSAGE);
				}

			} while (menu != 0);
			
	}
	
	
	
/* 1.    Realizar las siguientes dos series numéricas utilizando las estructuras repetitivas: for, while y do‐while.
//utilice un condicional para evitar que imprima la coma después del ultimo numero. */

	
		public void opcion1(){
			
			System.out.println("Imprimiendo series numericas");

			for (int contador = 1; contador <= 5; contador++){

				if (contador < 5){
					JOptionPane.showMessageDialog(null, a + "." + b + "." );
					System.out.print(a + "," + b + " " );
					a++;
					b--;
				}
				else{
					JOptionPane.showMessageDialog(null, a + "." + b);
					System.out.print(a + "," + b);
					a++;
					b--;
				}
			}
			System.out.println(".");

			for (int contador = 1; contador <= 5; contador++){

				if (contador < 5){
					System.out.print(contador + "," );

				}
				else{
					System.out.print(contador  + "."  );
				}
			}
			Object[] opciones = { "Aceptar" };
				JOptionPane.showOptionDialog(null, "pulsa \"Aceptar\" para volver al menu principal" , "Introduccion a la computacion", JOptionPane.DEFAULT_OPTION, JOptionPane.WARNING_MESSAGE, null, opciones, opciones[0]);

		}//fin Opcion1
		

		
/* 2.   Realice un programa en java que solicite el precio de 20 artículos diferentes, uno por uno y los sume, de manera que se imprima un solo monto al final. */ 

		public void opcion2(){
			for ( int contador3 = 0; contador3 < frutas.length; contador3++ ){
				precio = Integer.parseInt(JOptionPane.showInputDialog("¿Cual es el valor que desea asignarle a la" + frutas[contador3] + "?"));
				total = total + precio;
			}
			JOptionPane.showMessageDialog(null, "La suma de todos los precios anteriormente digitalizados es de: " + precio );
			
			Object[] opciones = { "Aceptar" };
				JOptionPane.showOptionDialog(null, "pulsa \"Aceptar\" para volver al menu principal" , "Introduccion a la computacion", JOptionPane.DEFAULT_OPTION, JOptionPane.WARNING_MESSAGE, null, opciones, opciones[0]);
			
			
		}// fin Opcion2
		
/* 3.   Desarrollar un programa en java que permita calcular la suma 1 + 2 + 3 + 4 + .... + N., */

		public void opcion3(){

			 n = Integer.parseInt(JOptionPane.showInputDialog("¿Hasta que numero queres sumar?"));


			while (i <= n) {
				suma = suma + i;
				i++;
			}
			System.out.println("** Imprimiendo la suma 1 + 2 + 3 + 4 + .... + N **");
			JOptionPane.showMessageDialog(null, "La suma desde 1 hasta " + n + " es: " + suma);
			
			
			System.out.println("La suma desde 1 hasta " + n + " es: " + suma);

			
			Object[] opciones = { "Aceptar" };
				JOptionPane.showOptionDialog(null, "pulsa \"Aceptar\" para volver al menu principal" , "Introduccion a la computacion", JOptionPane.DEFAULT_OPTION, JOptionPane.WARNING_MESSAGE, null, opciones, opciones[0]);
			
		}//fin Opcion3
		
/* 4.   Desarrolla un programa en java que imprimir la tabla de multiplicar de un número entero positivo ingresado por el usuario utilizando la clase JOptionPane. */
		
		public void opcion4(){

			numero = Integer.parseInt(JOptionPane.showInputDialog("¿De qué número quieres la tabla de multiplicar?"));
			System.out.println("**Imprimiendo tabla del " + numero + "**");

			while (contador2 <= 10) {
				JOptionPane.showMessageDialog(null, numero + " x " + contador2 + " = " + (numero * contador2));
				
				System.out.println(numero + " x " + contador2 + " = " + (numero * contador2));
				contador2++;
			}
			
			Object[] opciones = { "Aceptar" };
				JOptionPane.showOptionDialog(null, "pulsa \"Aceptar\" para volver al menu principal" , "Introduccion a la computacion", JOptionPane.DEFAULT_OPTION, JOptionPane.WARNING_MESSAGE, null, opciones, opciones[0]);

		}
		
//prueba


	/* Precios de los Helados */
	final int cono = 1000;
	final int bowl = 5500;
	final int sundae = 2500;


	/* Contador */
	int contadorBowl = 0;
	int contadorConos = 0;
	int contadorSundae = 0;
	int totalRecaudado =0;


	/* Variables opcionMenu1 */
	int cantidadConos, cantidadBowl, cantidadSundae;
	int subtotalCono;
	int subtotalBowl;
	int subtotalSundae;

	double precioFinalCono;
	double precioFinalBowl;
	double precioFinalSundae;

	/* Descuentos */
	double descuento;
	double porcentaje;
	double digito;

		public void heladeria(){
					byte opcionMenu;


			opcionMenu = Byte.parseByte(JOptionPane.showInputDialog( ""
			+ " \n ===============La Heladeria del Abuelo ==============="
			+ "\n Menú Principal"
			+ "\n Seleccione una opción:"
			+ "\n 1. Comprar Helado"
			+ "\n 2. Consulta de precios"
			+ "\n 0. Volver "
			+ "\n ===============La Heladeria del Abuelo ===============" ));

			switch (opcionMenu) {
				case 1:
					realizarVenta();
					break;
				case 2:
					JOptionPane.showMessageDialog(null, ""
					+ " \n ===============Consulta de precios ==============="
					+ "\n Cono - ₡1.000"
					+ "\n Bowl - ₡5.000"
					+ "\n Sundae - ₡2.500"
					+ " \n ===============La Heladeria del Abuelo ===============");
					break;
				case 0:
					JOptionPane.showMessageDialog(null, "¡Disfrute su helado!");
					break;
				default:
					Object[] opciones = { "Aceptar" };
					JOptionPane.showOptionDialog(null, "La opcion ingresada no es valida, haga click en \"Aceptar\"" , "Advertencia", JOptionPane.DEFAULT_OPTION, JOptionPane.WARNING_MESSAGE, null, opciones, opciones[0]);

			}
	}


	/* Segundo menu */
	public void realizarVenta(){

		byte opcionMenu1;

		opcionMenu1 = Byte.parseByte(JOptionPane.showInputDialog(""
		+ "\n Seleccione el tipo de producto"
		+ "\n 1. Cono - ₡1.000 "
		+ "\n 2. Bowl - ₡5.000 "
		+ "\n 3. Sundae - ₡2.500 "));


		switch(opcionMenu1){

			case 1:	/* Opcion = 1. Cono - ₡1.000 */

				cantidadConos = Integer.parseInt(JOptionPane.showInputDialog("¿Cuantos conos desea?"));
				contadorConos = cantidadConos + contadorConos; /* contador de conos +1 */
				subtotalCono = cono * cantidadConos; /* cantidad de conos que eligio el cliente */


				if (subtotalCono > 7000 && subtotalCono <= 10000) {
					descuento = subtotalCono * 0.05;
					precioFinalCono = subtotalCono - descuento;
					digito = descuento / subtotalCono;
					porcentaje = digito * 100;

				}
				if (subtotalCono <= 6999){
					precioFinalCono = cono * cantidadConos;
				}

				if (subtotalCono > 10000 && subtotalCono <= 15000) {
					descuento = subtotalCono * 0.08;
					precioFinalCono = subtotalCono - descuento;
					digito = descuento / subtotalCono;
					porcentaje = digito * 100;

				}
				else{
					if (subtotalCono > 15000 ) {
						descuento = subtotalCono * 0.20;
						precioFinalCono = subtotalCono - descuento;
						digito = descuento / subtotalCono;
						porcentaje = digito * 100;

					}
				}

				totalRecaudado = (int)(totalRecaudado + precioFinalCono);
				JOptionPane.showMessageDialog(null,  "=============== resumen de compra ==============="
				+ "\n Cantidad de conos " + cantidadConos
				+ "\n Subtotal: " + subtotalCono 
				+ "\n Monto del descuento: " + descuento
				+ "\n Total a pagar: " + precioFinalCono
				+ "\n =============== resumen de compra ==============="
				+ "\n **cash register version status 0.21**");
				JOptionPane.showMessageDialog(null, "¡Disfrute su helado!");

				break;


			case 2: /* Opcion = 2. Bowl - ₡5.500 */
				cantidadBowl = Integer.parseInt(JOptionPane.showInputDialog(null, "¿ Cuantos Bowl desea ?"));

				contadorBowl = contadorBowl + cantidadBowl; // + al contador de Bowl
				subtotalBowl = bowl * cantidadBowl; // multiplica el browl por la cantidad que eligio el cliente

				if (subtotalBowl > 7000 && subtotalBowl <= 10000 ){
				descuento = subtotalBowl * 0.05;
				precioFinalBowl = subtotalBowl - descuento;
				porcentaje = descuento * 100;
				digito = descuento / subtotalBowl;
				porcentaje = digito * 100;
				}
				else{
					if (subtotalBowl > 10000 && subtotalBowl <= 15000 ){
						descuento = subtotalBowl * 0.08 ;
						precioFinalBowl = subtotalBowl - descuento;
						digito = descuento / subtotalBowl;
						porcentaje = digito * 100;
					}
				}
				if (subtotalBowl > 15000){
					descuento = subtotalBowl * 0.20;
					precioFinalBowl = subtotalBowl - descuento;
					digito = descuento / subtotalBowl;
					porcentaje = digito	* 100;
				}
				if (subtotalBowl <= 6999){
					precioFinalBowl = bowl * cantidadBowl;
				}

				totalRecaudado = (int)(totalRecaudado + precioFinalBowl);
				JOptionPane.showMessageDialog(null,  "=============== resumen de compra ==============="
				+ "\n Cantidad de Browls " + cantidadBowl
				+ "\n Subtotal: " + subtotalBowl
				+ "\n Monto del descuento: " + descuento
				+ "\n Total a pagar: " + precioFinalBowl
				+ "\n =============== resumen de compra ==============="
				+ "\n **cash register version status 0.21**");
				JOptionPane.showMessageDialog(null, "¡Disfrute su helado!");

				break;



			case 3: /* Opcion = 3. Sundae - ₡2.500  */

				cantidadSundae = Integer.parseInt(JOptionPane.showInputDialog (null, "Cuantos sundae desea"));
				contadorSundae = contadorSundae + cantidadSundae;
				subtotalSundae = sundae * cantidadSundae;



				if (subtotalSundae > 7000 && subtotalSundae <= 10000 ){
				descuento = subtotalSundae * 0.05;
				precioFinalSundae = subtotalSundae - descuento;
				porcentaje = descuento * 100;
				digito = descuento / subtotalSundae;
				porcentaje = digito * 100;
				}
				else{
					if (subtotalSundae > 10000 && subtotalSundae <= 15000 ){
						descuento = subtotalSundae * 0.08 ;
						precioFinalSundae = subtotalSundae - descuento;
						digito = descuento / subtotalSundae;
						porcentaje = digito * 100;
					}
				}
				if (subtotalSundae > 15000){
					descuento = subtotalSundae * 0.20;
					precioFinalSundae = subtotalSundae - descuento;
					digito = descuento / subtotalSundae;
					porcentaje = digito	* 100;
				}
				else{

					if (subtotalSundae <= 6999){
						precioFinalSundae = sundae * cantidadSundae;
					}
				}


				totalRecaudado = (int)(totalRecaudado + precioFinalSundae);
				JOptionPane.showMessageDialog(null,  "=============== resumen de compra ==============="
				+ "\n Cantidad de Browls " + cantidadSundae
				+ "\n Subtotal: " + subtotalSundae
				+ "\n Monto del descuento: " + descuento
				+ "\n Total a pagar: " + precioFinalSundae
				+ "\n =============== resumen de compra ==============="
				+ "\n **cash register version status 0.21**");
				JOptionPane.showMessageDialog(null, "¡Disfrute su helado!");

				break;
			default:

				Object[] opciones = { "Aceptar" };
				JOptionPane.showOptionDialog(null, "La opcion ingresada no es valida, haga click en \"Aceptar\"" , "Advertencia", JOptionPane.DEFAULT_OPTION, JOptionPane.WARNING_MESSAGE, null, opciones, opciones[0]);



		}

		}
		
		

}
