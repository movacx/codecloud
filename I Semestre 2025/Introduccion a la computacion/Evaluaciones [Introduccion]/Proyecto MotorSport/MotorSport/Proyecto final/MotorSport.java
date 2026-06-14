/* Autor Herlin Chavarria C5E187 | Nota: Esta clase Principal */



import javax.swing.JOptionPane;
import java.util.Random;



public class MotorSport{
	
	/*Objetos */
	private Usuario jugadorUno, jugadorDos, jugadorTres, jugadorCuatro;
	private Carro vehiculoUno, vehiculoDos, vehiculoTres, vehiculoCuatro, vehiculoPrueba;
	private TallerDeMejoras tuneoUno, tuneoDos, tuneoTres, tuneoCuatro;
	
	/* Login & Usuario */
	private int cantidadJugadores;
	private String nombreTemporalUno = "";
	private String nombreTemporalDos = "";
	private String nombreTemporalTres = "";
	private String nombreTemportalCuatro = "";
	
	/* Despiche */
	private int edad, rentCar, modeloRentCar, menuRegistroUsuario, opcionRentCar, registrarAuto, test1;


	public static void main(String []args){
		
		new MotorSport();
	}
	
	public MotorSport(){
		this.tuneoUno = new TallerDeMejoras();
        this.tuneoDos = new TallerDeMejoras();
        this.tuneoTres = new TallerDeMejoras();
        this.tuneoCuatro = new TallerDeMejoras();

		login();
	}
	
	
	public void login(){

		do{
			
			cantidadJugadores = Integer.parseInt(JOptionPane.showInputDialog(null,  "¿Cuántas personas van a ingresar al evento de Racing Sport?", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE));
			if(cantidadJugadores >4){
				JOptionPane.showMessageDialog(null, "El límite de Jugadores permitidos es de 4", "Error", JOptionPane.ERROR_MESSAGE);
					cantidadJugadores = 0; // Para que el bucle se repita
			}else if(cantidadJugadores < 1){
				 JOptionPane.showMessageDialog(null, "0 no es valido. Ingrese (1, 2, 3 o 4)	", "Error", JOptionPane.ERROR_MESSAGE);
					cantidadJugadores = 0; // Para que el bucle se repita
				}		
		}while(cantidadJugadores >4 || cantidadJugadores <1);
		
		
		if(cantidadJugadores == 1){
			nombreTemporalUno = JOptionPane.showInputDialog(null, "🧑"
			+ "Organizador del evento: ¿Cómo están, amigos? Mi nombre es Cristopher, imagino que vienen a participar en el evento de Racing Sport."
			+ "\n🧑Cristopher: Por favor, escriban su nombre en esta libreta para continuar con el evento." 
			+ "\n ¿Como te llamas?", "Jugador 1", JOptionPane.PLAIN_MESSAGE);
			usuarioUno();
			menuPrincipal();
			
		}
		
		
		if(cantidadJugadores == 2){
			nombreTemporalUno = JOptionPane.showInputDialog(null, "🧑"
			+ "Organizador del evento: ¿Cómo están, amigos? Mi nombre es Cristopher, imagino que vienen a participar en el evento de Racing Sport."
			+ "\n🧑Cristopher: Por favor, escriban su nombre en esta libreta para continuar con el evento." 
			+ "\n ¿Como te llamas?", "Jugador 1", JOptionPane.PLAIN_MESSAGE);
			nombreTemporalDos = JOptionPane.showInputDialog(null, "🧑"
			+ "Organizador del evento: ¿Cómo están, amigos? Mi nombre es Cristopher, imagino que vienen a participar en el evento de Racing Sport."
			+ "\n🧑Cristopher: Por favor, escriban su nombre en esta libreta para continuar con el evento." 
			+ "\n ¿Como te llamas?", "Jugador 2", JOptionPane.PLAIN_MESSAGE);
			usuarioUno();
			usuarioDos();
			menuPrincipal();
		}
		
		
		if(cantidadJugadores == 3){
			nombreTemporalUno = JOptionPane.showInputDialog(null, "🧑"
			+ "Organizador del evento: ¿Cómo están, amigos? Mi nombre es Cristopher, imagino que vienen a participar en el evento de Racing Sport."
			+ "\n🧑Cristopher: Por favor, escriban su nombre en esta libreta para continuar con el evento." 
			+ "\n ¿Como te llamas?", "Jugador 1", JOptionPane.PLAIN_MESSAGE);
			nombreTemporalDos = JOptionPane.showInputDialog(null, "🧑"
			+ "Organizador del evento: ¿Cómo están, amigos? Mi nombre es Cristopher, imagino que vienen a participar en el evento de Racing Sport."
			+ "\n🧑Cristopher: Por favor, escriban su nombre en esta libreta para continuar con el evento." 
			+ "\n ¿Como te llamas?", "Jugador 2", JOptionPane.PLAIN_MESSAGE);
			nombreTemporalTres = JOptionPane.showInputDialog(null, "🧑"
			+ "Organizador del evento: ¿Cómo están, amigos? Mi nombre es Cristopher, imagino que vienen a participar en el evento de Racing Sport."
			+ "\n🧑Cristopher: Por favor, escriban su nombre en esta libreta para continuar con el evento." 
			+ "\n ¿Como te llamas?", "Jugador 3", JOptionPane.PLAIN_MESSAGE);
			usuarioUno();
			usuarioDos();
			usuarioTres();
			menuPrincipal();
		}
		
		
		if(cantidadJugadores == 4){
			nombreTemporalUno = JOptionPane.showInputDialog(null, "🧑"
			+ "Organizador del evento: ¿Cómo están, amigos? Mi nombre es Cristopher, imagino que vienen a participar en el evento de Racing Sport."
			+ "\n🧑Cristopher: Por favor, escriban su nombre en esta libreta para continuar con el evento." 
			+ "\n ¿Como te llamas?", "Jugador 1", JOptionPane.PLAIN_MESSAGE);
			nombreTemporalDos = JOptionPane.showInputDialog(null, "🧑"
			+ "Organizador del evento: ¿Cómo están, amigos? Mi nombre es Cristopher, imagino que vienen a participar en el evento de Racing Sport."
			+ "\n🧑Cristopher: Por favor, escriban su nombre en esta libreta para continuar con el evento." 
			+ "\n ¿Como te llamas?", "Jugador 2", JOptionPane.PLAIN_MESSAGE);
			nombreTemporalTres = JOptionPane.showInputDialog(null, "🧑"
			+ "Organizador del evento: ¿Cómo están, amigos? Mi nombre es Cristopher, imagino que vienen a participar en el evento de Racing Sport."
			+ "\n🧑Cristopher: Por favor, escriban su nombre en esta libreta para continuar con el evento." 
			+ "\n ¿Como te llamas?", "Jugador 3", JOptionPane.PLAIN_MESSAGE);
			nombreTemportalCuatro = JOptionPane.showInputDialog(null, "🧑"
			+ "Organizador del evento: ¿Cómo están, amigos? Mi nombre es Cristopher, imagino que vienen a participar en el evento de Racing Sport."
			+ "\n🧑Cristopher: Por favor, escriban su nombre en esta libreta para continuar con el evento." 
			+ "\n ¿Como te llamas?", "Jugador 4", JOptionPane.PLAIN_MESSAGE);
			usuarioUno();
			usuarioDos();
			usuarioTres();
			usuarioCuatro();
			menuPrincipal();
			
			
			
			
			
		}
		
		
	}/*FinLogin*/ 
	
	/* Sistema de Renta */
	
	public void wangCars(int numeroJugador){
		int opcionRentCar;
		int modeloRentCar;
		Carro carroRentado = null;

		opcionRentCar = Integer.parseInt(JOptionPane.showInputDialog(null,
		 "\nRenta CarsWang. Seleccione una Opcion: "
		+ "\n 1. Mercedes-AMG"
		+ "\n 2. McLaren"
		+ "\n 3. Porsche", "Wang Cars", JOptionPane.PLAIN_MESSAGE));
		
		switch(opcionRentCar){
			case 1:
				modeloRentCar = Integer.parseInt(JOptionPane.showInputDialog(null, "🧑Wang Jiaqi: En CarsWang tenemos una gran variedad de modelos en nuestra disposicion." 
					+ "\n🧑Wang Jiaqi: Sin embargo estos fueron algunos de los vehiculos que hemos traido al evento de Racing Sport: "
					+ "\n 1. AMG ONE 2018 - Azul"
					+ "\n 2. AMG GT3 - Amarillo"
					+ "\n 3. AMG C63 S Coupé - Blanco", "Wang Cars", JOptionPane.PLAIN_MESSAGE));
				
				if(modeloRentCar == 1){
					carroRentado = new Carro("Mercedes-AMG", "AMG ONE 2018", "Azul", 6.1, 5.1, 4.9, 6.8 );
				} else if(modeloRentCar == 2){
					carroRentado = new Carro("Mercedes-AMG", "AMG GT3", "Amarillo", 5.0, 6.4, 6.7, 6.1 );
				} else if(modeloRentCar == 3){
					carroRentado = new Carro("Mercedes-AMG", "AMG C63 S Coupé", "Blanco", 7.4, 2.8, 2.6, 5.4 );
				}
				break;

			case 2:
				modeloRentCar = Integer.parseInt(JOptionPane.showInputDialog(null, "🧑Wang Jiaqi: En CarsWang tenemos una gran variedad de modelos en nuestra disposicion." 
					+ "\n🧑Wang Jiaqi: Sin embargo estos fueron algunos de los vehiculos que hemos traido al evento de Racing Sport: "
					+ "\n 1. McLaren Senna 2018 - Azul"
					+ "\n 2. McLaren Spider 2019 - Amarillo"
					+ "\n 3. McLaren 600LT Coupé - Plateado", "Wang Cars", JOptionPane.PLAIN_MESSAGE));

				if(modeloRentCar == 1){
					carroRentado = new Carro("McLaren", "McLaren Senna 2018", "Azul", 6.1, 5.1, 4.9, 6.8 );
				} else if(modeloRentCar == 2){
					carroRentado = new Carro("McLaren", "McLaren Spider 2019", "Amarillo", 5.0, 6.4, 6.7, 6.1 );
				} else if(modeloRentCar == 3){
					carroRentado = new Carro("McLaren", "McLaren 600LT Coupé", "Plateado", 7.4, 2.8, 2.6, 5.4 );
				}
				break;

			case 3:
				modeloRentCar = Integer.parseInt(JOptionPane.showInputDialog(null, "🧑Wang Jiaqi: En CarsWang tenemos una gran variedad de modelos en nuestra disposicion." 
					+ "\n🧑Wang Jiaqi: Sin embargo estos fueron algunos de los vehiculos que hemos traido al evento de Racing Sport: "
					+ "\n 1. 2021 Porsche 911 GT3 - Naranja"
					+ "\n 2. 2016 Porsche Cayman GT4 - Gris"
					+ "\n 3. 2017 Porsche GT Team 911 RSR - Negro", "Wang Cars", JOptionPane.PLAIN_MESSAGE));

				if(modeloRentCar == 1){
					carroRentado = new Carro("Porsche", "2021 Porsche 911 GT3", "Naranja", 6.1, 5.1, 4.9, 6.8 );
				} else if(modeloRentCar == 2){
					carroRentado = new Carro("Porsche", "2016 Porsche Cayman GT4", "Gris", 5.0, 6.4, 6.7, 6.1 );
				} else if(modeloRentCar == 3){
					carroRentado = new Carro("Porsche", "2017 Porsche GT Team 911 RSR", "Negro", 7.4, 2.8, 2.6, 5.4 );
				}
				break;

			default:
				JOptionPane.showMessageDialog(null, "Opción no válida.", "Error", JOptionPane.ERROR_MESSAGE);
				return;
		}

		if (carroRentado != null) {
			switch(numeroJugador){
				case 1:
					vehiculoUno = carroRentado;
					break;
				case 2:
					vehiculoDos = carroRentado;
					break;
				case 3:
					vehiculoTres = carroRentado;
					break;
				case 4:
					vehiculoCuatro = carroRentado;
					break;
			}

			JOptionPane.showMessageDialog(null, "🧑Wang Jiaqi: ¡Genial! Fue una excelente opción, te diré las características de este vehículo:", "Wang Cars", JOptionPane.PLAIN_MESSAGE);
			JOptionPane.showMessageDialog(null, carroRentado ); /* revisar */
		}
	}
	
	
	/* Sistema para registrar un vehiculo propio */ 
	public void registrarVehiculo(int asignarVehiculo){
		
		String marca = "";
		String modelo = "";
		String color = "";
		
		/* ----------------------------------------- */
		Carro registrarVehiculo = null;
		JOptionPane.showMessageDialog(null, "🧑Cristopher: Bien, llena este formulario para concluir con el registro del vehículo.", "Registro", JOptionPane.PLAIN_MESSAGE);
		marca = JOptionPane.showInputDialog(null, "Seleccione la marca", "Registro", JOptionPane.PLAIN_MESSAGE);
		modelo = JOptionPane.showInputDialog(null, "Seleccione el modelo", "Registro", JOptionPane.PLAIN_MESSAGE);
		color = JOptionPane.showInputDialog(null, "Seleccione la Color", "Registro", JOptionPane.PLAIN_MESSAGE);
		
		
		registrarVehiculo = new Carro(marca, modelo, color, 5.0, 3.1, 3.0, 4.0 );
		

		if(registrarVehiculo != null){
			switch(asignarVehiculo){
				case 1:
					vehiculoUno = registrarVehiculo;
					break;
				case 2:
					vehiculoDos = registrarVehiculo;
					break;
				case 3:
					vehiculoTres = registrarVehiculo;
					break;
				case 4:
					vehiculoCuatro = registrarVehiculo;
					break;

			}
		JOptionPane.showMessageDialog(null, "Advertencia! las especificaciones tecnicas del vehiculo registrado estan de Serie" + "\nPuedes modificar las especificaciones en el Taller de Racing Sport", "Advertencia", JOptionPane.WARNING_MESSAGE);
		JOptionPane.showMessageDialog(null, registrarVehiculo ); 
		}	
	}//Fin Registro de vehiculo
	
	/* Estadisticas /  ***** revisar porque sale como null **** */
	public void estadisticas(){
		
		if(cantidadJugadores == 1){
			JOptionPane.showMessageDialog(null, "🧑Cristopher: Aquí les detallo la información y especificaciones por cada uno de ustedes."  
			+ "\n" +jugadorUno 	+ 	"\n " + vehiculoUno);
		
		}if(cantidadJugadores == 2){
			JOptionPane.showMessageDialog(null, "🧑Cristopher: Aquí les detallo la información y especificaciones por cada uno de ustedes."  
			+ "\n                                               " 
			+ "\n                                          " 
			+ "\n" +jugadorUno 	+ 	"\n " + vehiculoUno
			+ "\n                                               "
			+ "\n" +jugadorDos 	+ 	"\n " + vehiculoDos);
		
		}if(cantidadJugadores == 3){
			JOptionPane.showMessageDialog(null, "🧑Cristopher: Aquí les detallo la información y especificaciones por cada uno de ustedes."  
			+ "\n                                               " 
			+ "\n" +jugadorUno 	+ 	"\n " + vehiculoUno
			+ "\n                                               "
			+ "\n" +jugadorDos 	+ 	"\n " + vehiculoDos
			+ "\n                                               "
			+ "\n" +jugadorTres 	+ 	"\n " + vehiculoTres
			+ "\n                                               ");
			
		}if(cantidadJugadores == 4){
			JOptionPane.showMessageDialog(null, "🧑Cristopher: Aquí les detallo la información y especificaciones por cada uno de ustedes."  
			+ "\n                                               " 
			+ "\n" +jugadorUno 	+ 	"\n " + vehiculoUno
			+ "\n                                               "
			+ "\n" +jugadorDos 	+ 	"\n " + vehiculoDos
			+ "\n                                               "
			+ "\n" +jugadorTres 	+ 	"\n " + vehiculoTres
			+ "\n                                               "
			+ "\n" +jugadorCuatro 	+ 	"\n " + vehiculoCuatro
			);
		}
	}
	
	
	public void estadisticasTunning(){
		
		if(cantidadJugadores == 1){
			JOptionPane.showMessageDialog(null, "🧑Cristopher: Estadisticas Globales"  
			+ "\n" +jugadorUno 	+ 	"\n " + vehiculoUno + "\n" + tuneoUno);
		
		}if(cantidadJugadores == 2){
			JOptionPane.showMessageDialog(null, "🧑Cristopher: Estadisticas Globales"  
			+ "\n                                               " 
			+ "\n                                          " 
			+ "\n" +jugadorUno 	+ 	"\n " + vehiculoUno + "\n" + tuneoUno
			+ "\n                                               "
			+ "\n" +jugadorDos 	+ 	"\n " + vehiculoDos + "\n" + tuneoDos);
		
		}if(cantidadJugadores == 3){
			JOptionPane.showMessageDialog(null, "🧑Cristopher: Estadisticas Globales"  
			+ "\n                                               " 
			+ "\n" +jugadorUno 	+ 	"\n " + vehiculoUno + "\n" + tuneoUno
			+ "\n                                               "
			+ "\n" +jugadorDos 	+ 	"\n " + vehiculoDos + "\n" + tuneoDos
			+ "\n                                               "
			+ "\n" +jugadorTres 	+ 	"\n " + vehiculoTres + "\n" + tuneoTres
			+ "\n                                               ");
			
		}if(cantidadJugadores == 4){
			JOptionPane.showMessageDialog(null, "🧑Cristopher: Estadisticas Globales"  
			+ "\n                                               " 
			+ "\n" +jugadorUno 	+ 	"\n " + vehiculoUno + "\n" + tuneoUno
			+ "\n                                               "
			+ "\n" +jugadorDos 	+ 	"\n " + vehiculoDos + "\n" + tuneoDos
			+ "\n                                               "
			+ "\n" +jugadorTres 	+ 	"\n " + vehiculoTres + "\n" + tuneoTres
			+ "\n                                               "
			+ "\n" +jugadorCuatro 	+ 	"\n " + vehiculoCuatro + "\n" + tuneoCuatro
			);
		}
		
		
		
		
	}

	
	
	
	
	
	
	public void menuPrincipal() {
		byte opcionMenuPrincipal;
		int seleccionGabriela;

		do {
			opcionMenuPrincipal = Byte.parseByte(JOptionPane.showInputDialog(null, "🧑Cristopher: ¡Antes de continuar! Racing Sport ha habilitado una sección especial donde podrán tunear sus vehículos a sus gustos."
			+ "\n🧑Cristopher: Si desean hacer modificaciones, pueden seguir a Gabriela, quien los guiará en el proceso."
			+ "\n🧑Cristopher: Pero si prefieren competir de una vez, pueden dirigirse directamente a la zona de competición con Lucas."
			+ "\n¿A quien deseas seguir?"
			+ "\n"
			+ "\n 1. Gabriela | Ir al Taller de Mejoras"
			+ "\n 2. Lucas    | Competir "
			+ "\n 3. Ver Estadisticas Globales"
			+ "\n 4. Ver Estadisticas Resumidas"
			+ "\n 5. Salir", "Racing Sport", JOptionPane.PLAIN_MESSAGE));

			switch(opcionMenuPrincipal) {
				
				case 1:

					if(cantidadJugadores == 1){
						seleccionGabriela = Byte.parseByte(JOptionPane.showInputDialog(null,
						"\n🧑Gabriela: Sigueme!"
						+ "\n 1. Continuar" 
						+ "\n 0. Salir", JOptionPane.PLAIN_MESSAGE));
						tallerDeAutos(1);
						JOptionPane.showMessageDialog(null, tuneoUno);
					
					}
					if(cantidadJugadores == 2){

						seleccionGabriela = Byte.parseByte(JOptionPane.showInputDialog(null,
						"\n🧑Gabriela: ¿Quien va primero?!"
						+ "\n 1. " + nombreTemporalUno
						+ "\n 2. " + nombreTemporalDos
						+ "\n 0. Salir", JOptionPane.PLAIN_MESSAGE));
						
						if(seleccionGabriela == 1){
							tallerDeAutos(1);
						JOptionPane.showMessageDialog(null, tuneoUno);
						}else if(seleccionGabriela == 2){
							tallerDeAutos(2);
							JOptionPane.showMessageDialog(null, tuneoDos);
						}

					
					}
					if(cantidadJugadores == 3){

						seleccionGabriela = Byte.parseByte(JOptionPane.showInputDialog(null,
						"\n🧑Gabriela: ¿Quien va primero?!"
						+ "\n 1. " + nombreTemporalUno
						+ "\n 2. " + nombreTemporalDos
						+ "\n 3. " + nombreTemporalTres
						+ "\n 0. Salir", JOptionPane.PLAIN_MESSAGE));
						
						if(seleccionGabriela == 1){
							tallerDeAutos(1);
						JOptionPane.showMessageDialog(null, tuneoUno);
						}else if(seleccionGabriela == 2){
							tallerDeAutos(2);
							JOptionPane.showMessageDialog(null, tuneoDos);
						}else if(seleccionGabriela == 3){
							tallerDeAutos(3);
							JOptionPane.showMessageDialog(null, tuneoTres);
						}

						
					}
					if(cantidadJugadores == 4){

						seleccionGabriela = Byte.parseByte(JOptionPane.showInputDialog(null,
						"\n🧑Gabriela: ¿Quien va primero?!"
						+ "\n 1. " + nombreTemporalUno
						+ "\n 2. " + nombreTemporalDos
						+ "\n 3. " + nombreTemporalTres
						+ "\n 4. " + nombreTemportalCuatro
						+ "\n 0. Salir", JOptionPane.PLAIN_MESSAGE));
						
						if(seleccionGabriela == 1){
							tallerDeAutos(1);
						JOptionPane.showMessageDialog(null, tuneoUno);
						}else if(seleccionGabriela == 2){
							tallerDeAutos(2);
							JOptionPane.showMessageDialog(null, tuneoDos);
						}else if(seleccionGabriela == 3){
							tallerDeAutos(3);
							JOptionPane.showMessageDialog(null, tuneoTres);
						}else if(seleccionGabriela == 4){
							tallerDeAutos(4);
							JOptionPane.showMessageDialog(null, tuneoCuatro);
						}
						
					}
				
					opcionGabriela(); // llamando a gabriela!
					break;

				case 2:
					JOptionPane.showMessageDialog(null, "🧑Lucas: ¡Acorrer!", "Carrera", JOptionPane.PLAIN_MESSAGE);
					carrera();
					break;

				case 3:
					estadisticasTunning();
					break;
					
				case 4:
					estadisticas();
					break;

				case 5:
					JOptionPane.showMessageDialog(null, "Tenga un buen dia regrese pronto.", "Racing Sport", JOptionPane.PLAIN_MESSAGE);
					break;

				default:
					JOptionPane.showMessageDialog(null, "Opción no válida.", "Error", JOptionPane.ERROR_MESSAGE);
			}
		} while (opcionMenuPrincipal != 5);
	}
	
	public void opcionGabriela(){
	}
	
	
	
	
	
	public void tallerDeAutos(int asignarMejora){
		byte opcionDeAutos;
			byte opcion1;
				byte subOpcion1;
			byte opcion2;
				byte subOpcion2;
			byte opcion3;
				byte subOpcion3;
			byte opcion4;
				byte subOpcion4;
		

		TallerDeMejoras mejorarVehiculo = null;
		mejorarVehiculo = new TallerDeMejoras("Si", 200, 200, "Serie", "Serie", "Serie", "Serie", "Serie", "Serie");
		
		do{
			opcionDeAutos = Byte.parseByte(JOptionPane.showInputDialog(null,
			"🧑Gabriela: Es un placer conocerte " + ", si no sabes para qué sirve un componente, yo estoy aquí para ayudarte."
			+ "\n\nSelecciona una opción:"
			+ "\n1. Combustible y aire"
			+ "\n2. Plataforma y manejo"
			+ "\n3. Llantas"
			+ "\n4. Tren de transmisión"
			+ "\n0. Volver al menú principal", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE));
			
			switch(opcionDeAutos){
				case 1:
				
				opcion1 = Byte.parseByte(JOptionPane.showInputDialog(null, "🧑Gabriela: La brida de admisión es una pieza que limita la entrada de aire al motor. Al retirarla, se permite más aire, lo que puede aumentar la potencia y el rendimiento del auto."
				+ "\n1. Retirar brida de admisión"
				+ "\n0. Volver", "Combustible y aire", JOptionPane.PLAIN_MESSAGE));
				if(opcion1 == 1){
					subOpcion1 = Byte.parseByte(JOptionPane.showInputDialog(null, "🧑Gabriela: ¿Desea Retirarlo?"
					+ "\n1. Si"
					+ "\n2. No"
					+ "\n0. Volver", JOptionPane.PLAIN_MESSAGE));
					if(subOpcion1 != 1){
						mejorarVehiculo.setBridaDeAdmision("No"); 
					}
					
				}	
					break;
					
					
				case 2:
				
				opcion2 = Byte.parseByte(JOptionPane.showInputDialog(null, "Seleccione una opcion:"
                        + "\n1. Frenos deportivos"
                        + "\n2. Ajustar muelles y amortiguadores"
                        + "\n0. Volver", "Plataforma y manejo", JOptionPane.PLAIN_MESSAGE));
				if(opcion2 == 1){
					subOpcion2 = Byte.parseByte(JOptionPane.showInputDialog(null, "Ayudan a controlar la transferencia de peso manteniendo un mejor control en curvas y en general"
					+ "\n1. Calle"
					+ "\n2. Carreras"
					+ "\n3. Deportivos"
					+ "\n0. Volver", "Tipo de Frenos", JOptionPane.PLAIN_MESSAGE));
					if(subOpcion2 == 1){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Frenos instalados", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setFrenos("Calle"); 
					}else if(subOpcion2 == 2){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Frenos instalados", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setFrenos("carrera"); 
					}else if(subOpcion2 == 3){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Frenos instalados", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setFrenos("Deportivo"); 
					}

				}else if(opcion2 == 2){
					subOpcion2 = Byte.parseByte(JOptionPane.showInputDialog(null, "Ayudan a controlar la transferencia de peso manteniendo un mejor control en curvas y en general"
					+ "\n1. Calle"
					+ "\n2. Carreras"
					+ "\n3. Deportivos"
					+ "\n0. Volver", "muelles y amortiguadores", JOptionPane.PLAIN_MESSAGE));
					if(subOpcion2 == 1){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Suspensión ajustada, mejor comportamiento en curvas.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setMuellesYAmortiguadores("Calle"); 
					}else if(subOpcion2 == 2){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Suspensión ajustada, mejor comportamiento en curvas.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setMuellesYAmortiguadores("deportivo"); 
					}else if(subOpcion2 == 3){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Suspensión ajustada, mejor comportamiento en curvas.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setMuellesYAmortiguadores("carrera"); 
					}
				}
				
					break;
				case 3:
				
				opcion3 = Byte.parseByte(JOptionPane.showInputDialog(null, "Seleccione una opcion:"
                        + "\n1. Cambiar compuesto de llantas "
                        + "\n2. Ajustar ancho de llanta delantera"
                        + "\n3. Ajustar ancho de llanta tracera"
                        + "\n0. Volver", "Llantas", JOptionPane.PLAIN_MESSAGE));
				if(opcion3 == 1){
					subOpcion3 = Byte.parseByte(JOptionPane.showInputDialog(null, "🧑Gabriela: La funcionalidad es maximizar la tracción según las condiciones de la pista y la duración deseada."
					+ "\n1. Compuesto de calle"
					+ "\n2. compuesto deportivo"
					+ "\n3. compuesto de carrera"
					+ "\n0. Volver", "Tipo de llanta", JOptionPane.PLAIN_MESSAGE));
					if(subOpcion3 == 1){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Compuesto cambiado, mejor agarre.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setCompuestoDeLlantas("Calle"); 
					}else if(subOpcion3 == 2){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Compuesto cambiado, mejor agarre.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setCompuestoDeLlantas("deportivo"); 
					}else if(subOpcion3 == 3){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Compuesto cambiado, mejor agarre.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setCompuestoDeLlantas("carrera"); 
					}
					
				}else if(opcion3 == 2){
					subOpcion3 = Byte.parseByte(JOptionPane.showInputDialog(null, "🧑Gabriela: Se instalan llantas mas anchas para mejorar la traccion "
					+ "\n1. 285mm"
					+ "\n2. 295mm"
					+ "\n3. 305mm"
					+ "\n0. Volver", "Ancho de llanta delantera", JOptionPane.PLAIN_MESSAGE));
					if(subOpcion3 == 1){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Ancho de llanta delantera cambiado, mejor agarre.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setFrontTireWidth(285); 
						vehiculoUno.setAceleracion(3.5);
						vehiculoUno.setVelocidad(9.1);
					}else if(subOpcion3 == 2){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Ancho de llanta delantera cambiado, mejor agarre.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setFrontTireWidth(295); 
					}else if(subOpcion3 == 3){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Ancho de llanta delantera cambiado, mejor agarre.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setFrontTireWidth(305); 
					}

					
				}else if(opcion3 == 3){
					subOpcion3 = Byte.parseByte(JOptionPane.showInputDialog(null, "🧑Gabriela: Se instalan llantas mas anchas para mejorar la traccion "
					+ "\n1. 285mm"
					+ "\n2. 295mm"
					+ "\n3. 305mm"
					+ "\n0. Volver", "Ancho de llanta tracera", JOptionPane.PLAIN_MESSAGE));
					if(subOpcion3 == 1){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Ancho de llanta tracera cambiado, mejor agarre.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setRearTireWidth(285); 
					}else if(subOpcion3 == 2){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Ancho de llanta tracera cambiado, mejor agarre.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setRearTireWidth(295); 
					}else if(subOpcion3 == 3){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Ancho de llanta tracera cambiado, mejor agarre.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setRearTireWidth(305); 
					}

				}

					break;
				case 4:
				

				opcion4 = Byte.parseByte(JOptionPane.showInputDialog(null, "Seleccione una opcion:"
 				        + "\n1. Instalar embrague de competición"
                        + "\n2. Ajustar la transmisión"
                        + "\n3. Configurar el diferencial"
                        + "\n0. Volver", "Tren de transmisión", JOptionPane.PLAIN_MESSAGE));
				if(opcion4 == 1){
					subOpcion4 = Byte.parseByte(JOptionPane.showInputDialog(null, "🧑Gabriela: La funcionalidad es maximizar la velocidad de cambios"
					+ "\n1. De calle"
					+ "\n2. De deportivo"
					+ "\n3. De carrera"
					+ "\n0. Volver", "Embrague", JOptionPane.PLAIN_MESSAGE));
					if(subOpcion4 == 1){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Embrague mejorado, cambios más rápidos.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setEmbrague("Calle"); 
					}else if(subOpcion4 == 2){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Embrague mejorado, cambios más rápidos.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setEmbrague("deportivo"); 
					}else if(subOpcion4 == 3){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Embrague mejorado, cambios más rápidos.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setEmbrague("carrera"); 
					}
					
				}else if(opcion4 == 2){
					subOpcion4 = Byte.parseByte(JOptionPane.showInputDialog(null, "🧑Gabriela: La funcionalidad es maximizar la velocidad de cambios "
					+ "\n1. De calle"
					+ "\n2. De deportivo"
					+ "\n3. De carrera"
					+ "\n0. Volver", "Transmisión", JOptionPane.PLAIN_MESSAGE));
					if(subOpcion4 == 1){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Transmisión ajustada para mejor aceleración.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setTransmision("calle"); 
					}else if(subOpcion4 == 2){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Transmisión ajustada para mejor aceleración.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setTransmision("deportivo"); 
					}else if(subOpcion4 == 3){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Transmisión ajustada para mejor aceleración.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setTransmision("carrera"); 
					}

					
				}else if(opcion4 == 3){
					subOpcion4 = Byte.parseByte(JOptionPane.showInputDialog(null, "🧑Gabriela: El diferencial permite que las llantas del vehiculo giren a distintas velocidades asi aumentando la traccion del vehiculo durante una curva"
					+ "\n1. De calle"
					+ "\n2. De deportivo"
					+ "\n3. De carrera"
					+ "\n0. Volver", "Diferencial", JOptionPane.PLAIN_MESSAGE));
					if(subOpcion4 == 1){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Diferencial configurado para mejor tracción.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setDiferencial("calle"); 
					}else if(subOpcion4 == 2){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Diferencial configurado para mejor tracción.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setDiferencial("deportivo"); 
					}else if(subOpcion4 == 3){
						JOptionPane.showMessageDialog(null, "🧑Gabriela: Diferencial configurado para mejor tracción.", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
						mejorarVehiculo.setDiferencial("carrera"); 
						
					}

				}

					break;
				case 0:
				JOptionPane.showMessageDialog(null, "Vuelve pronto!", "Taller ColaPinto", JOptionPane.PLAIN_MESSAGE);
					break;
				default:
					JOptionPane.showMessageDialog(null, "Opción no válida.", "Error", JOptionPane.ERROR_MESSAGE);
			}

		}while (opcionDeAutos != 0);
		
					
			/* Asignar Atributos */
			if(mejorarVehiculo != null){		
				switch(asignarMejora){
					case 1:
						tuneoUno = mejorarVehiculo;
						break;
					case 2:
						tuneoDos = mejorarVehiculo;
						break;
					case 3:
						tuneoTres = mejorarVehiculo;
						break;
					case 4:
						tuneoCuatro = mejorarVehiculo;
						break;
				}
			}
			
			JOptionPane.showMessageDialog(null, mejorarVehiculo);

	}
	

		
	public void carrera() {
		int usuario1, usuario2, usuario3, usuario4;
		Random puntuacion = new Random();

	
		usuario1 = puntuacion.nextInt(1000);
		usuario2 = puntuacion.nextInt(1000);
		usuario3 = puntuacion.nextInt(1000);
		usuario4 = puntuacion.nextInt(1000);

	
		int maxPuntaje = usuario1;
		if (usuario2 > maxPuntaje) {
			maxPuntaje = usuario2;
		}
		if (usuario3 > maxPuntaje) {
			maxPuntaje = usuario3;
		}
		if (usuario4 > maxPuntaje) {
			maxPuntaje = usuario4;
		}

		/* Se crashea al querer cambiar el puntaje */
		String ganador = "";
		if (usuario1 == maxPuntaje) {
			ganador = nombreTemporalUno;
			jugadorUno.setContadorCarrerasGanadas(1);
			jugadorUno.setTablaDePuntuacion(1);
		} else if (usuario2 == maxPuntaje) {
			ganador = nombreTemporalDos;
			jugadorDos.setContadorCarrerasGanadas(1);
			jugadorDos.setTablaDePuntuacion(1);
		} else if (usuario3 == maxPuntaje) {
			ganador = nombreTemporalTres;
			jugadorTres.setContadorCarrerasGanadas(1);
			jugadorTres.setTablaDePuntuacion(1);
		} else if (usuario4 == maxPuntaje) {
			ganador = nombreTemportalCuatro;
			jugadorCuatro.setContadorCarrerasGanadas(1);
			jugadorCuatro.setTablaDePuntuacion(1);
		}

		// Mostrar resultado
		JOptionPane.showMessageDialog(null, "🥇 Primer Lugar: " + ganador, "Carrera", JOptionPane.PLAIN_MESSAGE);

	}
	
	
	
	/* Gestion de Usuarios */
	
	public void usuarioUno(){
		byte menuDeUsuario;
		String nombreDeUsuario;
		String nacionalidad;
		int edad;
		do{
			menuDeUsuario =  Byte.parseByte(JOptionPane.showInputDialog(null,
			"Bienvenido " + nombreTemporalUno + " a \"Racing Sport\""
			+ "\nSeleccione una opcion: "
			+ "\n 1. Registro"
			+ "\n 2. Seleccion de vehiculos"
			+ "\n 3. Continuar", "Jugador 1", JOptionPane.PLAIN_MESSAGE));
            switch (menuDeUsuario) {
                case 1:

                    nombreDeUsuario = JOptionPane.showInputDialog(null, "Ingrese un nombre de usuario:", "Jugador 1", JOptionPane.PLAIN_MESSAGE);
                    edad = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite su Edad:", "Jugador 1", JOptionPane.PLAIN_MESSAGE));
                    nacionalidad = JOptionPane.showInputDialog(null, "Digite su nacionalidad:", "Jugador 1", JOptionPane.PLAIN_MESSAGE);


                    jugadorUno = new Usuario(nombreDeUsuario, nacionalidad, edad, 0, 0);
                    JOptionPane.showMessageDialog(null, "¡Registro de " + jugadorUno.getNombreDeUsuario() + " completado!", "Jugador 1", JOptionPane.PLAIN_MESSAGE);// Usar getNombreDeUsuario()
                    break;

                case 2:

					rentCar = JOptionPane.showConfirmDialog(null, "¿Desea rentar un vehiculo?", "Racing Sport", JOptionPane.YES_NO_OPTION ); /* JOptionPane YES = 0 | NO = 1 */ 
					
					if(rentCar == 0){
						wangCars(1); /* Llama el metodo de renta */ 
						
					}if(rentCar == 1){
						registrarAuto = JOptionPane.showConfirmDialog(null, "🧑Christopher: Veo que tienes un auto. ¿Acaso ese es el que deseas registrar? ", "Jugador 1", JOptionPane.YES_NO_OPTION );
						/* JOptionPane YES = 0 | NO = 1 */ 
						if(registrarAuto == 0){
							
							
						registrarVehiculo(1); /* Llama el metodo de registrar vehiculo */ 
							

						}if(registrarAuto == 1){
							JOptionPane.showMessageDialog(null, "Cristopher: Entonces, alquila un auto si deseas participar; te voy a presentar a Wang Jiaqi, es un asesor de WangCars; él te ayudará con el trámite."+"\n 🧑Wang Jiaqi: 早上好朋友，让我自我介绍一下，我是 WangCars 顾问。", "Jugador 1", JOptionPane.PLAIN_MESSAGE);
							JOptionPane.showMessageDialog(null, "🧑Cristopher:             (...)                                     " + "\n🧑Wang Jiaqi:             (...)                                     " + "\n🧑" +nombreTemporalUno +":             (...)             ", "Silencio Incomodo", JOptionPane.PLAIN_MESSAGE);
							JOptionPane.showMessageDialog(null, "🧑Wang Jiaqi: Es broma, hablo español. \" risas \""  + "\n🧑Wang Jiaqi: Acompáñame para mostrarte los autos. ", "Jugador 1", JOptionPane.PLAIN_MESSAGE);
							wangCars(1); /* Llama el metodo de renta */ 
						}
					}
					    
                    break;



                case 3:
   
                   JOptionPane.showMessageDialog(null, "🧑Cristopher: Siguiente!", "Racing Sport", JOptionPane.PLAIN_MESSAGE);
                    

                    break;

                default:

					JOptionPane.showMessageDialog(null, "Opcion Invalida!", "Jugador 1", JOptionPane.ERROR_MESSAGE);

                    break;
            }
       } while (menuDeUsuario != 3);
    
			



	

	}/*Fin Usuario Uno*/
	
	
	public void usuarioDos(){
		byte menuDeUsuario;
		String nombreDeUsuario;
		String nacionalidad;
		int edad;
		do{
			menuDeUsuario =  Byte.parseByte(JOptionPane.showInputDialog(null,
			"Bienvenido " + nombreTemporalDos + " a \"Racing Sport\""
			+ "\nSeleccione una opcion: "
			+ "\n 1. Registro"
			+ "\n 2. Seleccion de vehiculos"
			+ "\n 3. Continuar", "Jugador 2", JOptionPane.PLAIN_MESSAGE));
            switch (menuDeUsuario) {
                case 1:

                    nombreDeUsuario = JOptionPane.showInputDialog(null, "Ingrese un nombre de usuario:", "Jugador 2", JOptionPane.PLAIN_MESSAGE);
                    edad = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite su Edad:", "Jugador 2", JOptionPane.PLAIN_MESSAGE));
                    nacionalidad = JOptionPane.showInputDialog(null, "Digite su nacionalidad:", "Jugador 2", JOptionPane.PLAIN_MESSAGE);


                    jugadorDos = new Usuario(nombreDeUsuario, nacionalidad, edad, 0, 0);
                    JOptionPane.showMessageDialog(null, "¡Registro de " + jugadorUno.getNombreDeUsuario() + " completado!", "Jugador 2", JOptionPane.PLAIN_MESSAGE);// Usar getNombreDeUsuario()
                    break;

                case 2:

					rentCar = JOptionPane.showConfirmDialog(null, "¿Desea rentar un vehiculo?", "Racing Sport", JOptionPane.YES_NO_OPTION ); /* JOptionPane YES = 0 | NO = 1 */ 
					
					if(rentCar == 0){
						wangCars(2); /* Llama el metodo de renta */ 
						
					}if(rentCar == 1){
						registrarAuto = JOptionPane.showConfirmDialog(null, "🧑Christopher: Veo que tienes un auto. ¿Acaso ese es el que deseas registrar? ", "Jugador 2", JOptionPane.YES_NO_OPTION );
						/* JOptionPane YES = 0 | NO = 1 */ 
						if(registrarAuto == 0){
							
							
						registrarVehiculo(2); /* Llama el metodo de registrar vehiculo */ 
							

						}if(registrarAuto == 1){
							JOptionPane.showMessageDialog(null, "Cristopher: Entonces, alquila un auto si deseas participar; te voy a presentar a Wang Jiaqi, es un asesor de WangCars; él te ayudará con el trámite."+"\n 🧑Wang Jiaqi: 早上好朋友，让我自我介绍一下，我是 WangCars 顾问。", "Jugador 2", JOptionPane.PLAIN_MESSAGE);
							JOptionPane.showMessageDialog(null, "🧑Cristopher:             (...)                                     " + "\n🧑Wang Jiaqi:             (...)                                     " + "\n🧑" +nombreTemporalUno +":             (...)             ", "Silencio Incomodo", JOptionPane.PLAIN_MESSAGE);
							JOptionPane.showMessageDialog(null, "🧑Wang Jiaqi: Es broma, hablo español. \" risas \""  + "\n🧑Wang Jiaqi: Acompáñame para mostrarte los autos. ", "Jugador 2", JOptionPane.PLAIN_MESSAGE);
							wangCars(1); /* Llama el metodo de renta */ 
						}
					}
					    
                    break;



                case 3:
   
                   JOptionPane.showMessageDialog(null, "🧑Cristopher: Siguiente!", "Racing Sport", JOptionPane.PLAIN_MESSAGE);
                    

                    break;

                default:

					JOptionPane.showMessageDialog(null, "Opcion Invalida!", "Jugador 2", JOptionPane.ERROR_MESSAGE);

                    break;
            }
       } while (menuDeUsuario != 3);
    
			


	}/*Fin Usuario Dos*/
	
	
	public void usuarioTres(){
		byte menuDeUsuario;
		String nombreDeUsuario;
		String nacionalidad;
		int edad;
		do{
			menuDeUsuario =  Byte.parseByte(JOptionPane.showInputDialog(null,
			"Bienvenido " + nombreTemporalTres + " a \"Racing Sport\""
			+ "\nSeleccione una opcion: "
			+ "\n 1. Registro"
			+ "\n 2. Seleccion de vehiculos"
			+ "\n 3. Continuar", "Jugador 3", JOptionPane.PLAIN_MESSAGE));
            switch (menuDeUsuario) {
                case 1:

                    nombreDeUsuario = JOptionPane.showInputDialog(null, "Ingrese un nombre de usuario:", "Jugador 3", JOptionPane.PLAIN_MESSAGE);
                    edad = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite su Edad:", "Jugador 3", JOptionPane.PLAIN_MESSAGE));
                    nacionalidad = JOptionPane.showInputDialog(null, "Digite su nacionalidad:", "Jugador 3", JOptionPane.PLAIN_MESSAGE);


                    jugadorTres = new Usuario(nombreDeUsuario, nacionalidad, edad, 0, 0);
                    JOptionPane.showMessageDialog(null, "¡Registro de " + jugadorUno.getNombreDeUsuario() + " completado!", "Jugador 3", JOptionPane.PLAIN_MESSAGE);// Usar getNombreDeUsuario()
                    break;

                case 2:

					rentCar = JOptionPane.showConfirmDialog(null, "¿Desea rentar un vehiculo?", "Racing Sport", JOptionPane.YES_NO_OPTION ); /* JOptionPane YES = 0 | NO = 1 */ 
					
					if(rentCar == 0){
						wangCars(3); /* Llama el metodo de renta */ 
						
					}if(rentCar == 1){
						registrarAuto = JOptionPane.showConfirmDialog(null, "🧑Christopher: Veo que tienes un auto. ¿Acaso ese es el que deseas registrar? ", "Jugador 3", JOptionPane.YES_NO_OPTION );
						/* JOptionPane YES = 0 | NO = 1 */ 
						if(registrarAuto == 0){
							
							
						registrarVehiculo(3); /* Llama el metodo de registrar vehiculo */ 
							

						}if(registrarAuto == 1){
							JOptionPane.showMessageDialog(null, "Cristopher: Entonces, alquila un auto si deseas participar; te voy a presentar a Wang Jiaqi, es un asesor de WangCars; él te ayudará con el trámite."+"\n 🧑Wang Jiaqi: 早上好朋友，让我自我介绍一下，我是 WangCars 顾问。", "Jugador 3", JOptionPane.PLAIN_MESSAGE);
							JOptionPane.showMessageDialog(null, "🧑Cristopher:             (...)                                     " + "\n🧑Wang Jiaqi:             (...)                                     " + "\n🧑" +nombreTemporalUno +":             (...)             ", "Silencio Incomodo", JOptionPane.PLAIN_MESSAGE);
							JOptionPane.showMessageDialog(null, "🧑Wang Jiaqi: Es broma, hablo español. \" risas \""  + "\n🧑Wang Jiaqi: Acompáñame para mostrarte los autos. ", "Jugador 3", JOptionPane.PLAIN_MESSAGE);
							wangCars(1); /* Llama el metodo de renta */ 
						}
					}
					    
                    break;
                    
                case 3:
   
                   JOptionPane.showMessageDialog(null, "🧑Cristopher: Siguiente!", "Racing Sport", JOptionPane.PLAIN_MESSAGE);
                    

                    break;

                default:

					JOptionPane.showMessageDialog(null, "Opcion Invalida!", "Jugador 3", JOptionPane.ERROR_MESSAGE);

                    break;
            }
       } while (menuDeUsuario != 3);
    
	}/*Fin Usuario Tres*/
	
	
	public void usuarioCuatro(){
		byte menuDeUsuario;
		String nombreDeUsuario;
		String nacionalidad;
		int edad;
		do{
			menuDeUsuario =  Byte.parseByte(JOptionPane.showInputDialog(null,
			"Bienvenido " + nombreTemporalTres + " a \"Racing Sport\""
			+ "\nSeleccione una opcion: "
			+ "\n 1. Registro"
			+ "\n 2. Seleccion de vehiculos"
			+ "\n 3. Continuar", "Jugador 4", JOptionPane.PLAIN_MESSAGE));
            switch (menuDeUsuario) {
                case 1:

                    nombreDeUsuario = JOptionPane.showInputDialog(null, "Ingrese un nombre de usuario:", "Jugador 4", JOptionPane.PLAIN_MESSAGE);
                    edad = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite su Edad:", "Jugador 4", JOptionPane.PLAIN_MESSAGE));
                    nacionalidad = JOptionPane.showInputDialog(null, "Digite su nacionalidad:", "Jugador 4", JOptionPane.PLAIN_MESSAGE);


                    jugadorTres = new Usuario(nombreDeUsuario, nacionalidad, edad, 0, 0);
                    JOptionPane.showMessageDialog(null, "¡Registro de " + jugadorUno.getNombreDeUsuario() + " completado!", "Jugador 4", JOptionPane.PLAIN_MESSAGE);// Usar getNombreDeUsuario()
                    break;

                case 2:

					rentCar = JOptionPane.showConfirmDialog(null, "¿Desea rentar un vehiculo?", "Racing Sport", JOptionPane.YES_NO_OPTION ); /* JOptionPane YES = 0 | NO = 1 */ 
					
					if(rentCar == 0){
						wangCars(4); /* Llama el metodo de renta */ 
						
					}if(rentCar == 1){
						registrarAuto = JOptionPane.showConfirmDialog(null, "🧑Christopher: Veo que tienes un auto. ¿Acaso ese es el que deseas registrar? ", "Jugador 4", JOptionPane.YES_NO_OPTION );
						/* JOptionPane YES = 0 | NO = 1 */ 
						if(registrarAuto == 0){
							
							
						registrarVehiculo(4); /* Llama el metodo de registrar vehiculo */ 
							

						}if(registrarAuto == 1){
							JOptionPane.showMessageDialog(null, "Cristopher: Entonces, alquila un auto si deseas participar; te voy a presentar a Wang Jiaqi, es un asesor de WangCars; él te ayudará con el trámite."+"\n 🧑Wang Jiaqi: 早上好朋友，让我自我介绍一下，我是 WangCars 顾问。", "Jugador 4", JOptionPane.PLAIN_MESSAGE);
							JOptionPane.showMessageDialog(null, "🧑Cristopher:             (...)                                     " + "\n🧑Wang Jiaqi:             (...)                                     " + "\n🧑" +nombreTemporalUno +":             (...)             ", "Silencio Incomodo", JOptionPane.PLAIN_MESSAGE);
							JOptionPane.showMessageDialog(null, "🧑Wang Jiaqi: Es broma, hablo español. \" risas \""  + "\n🧑Wang Jiaqi: Acompáñame para mostrarte los autos. ", "Jugador 4", JOptionPane.PLAIN_MESSAGE);
							wangCars(1); /* Llama el metodo de renta */ 
						}
					}
					    
                    break;



                case 3:
   
                   JOptionPane.showMessageDialog(null, "🧑Cristopher: Siguiente!", "Racing Sport", JOptionPane.PLAIN_MESSAGE);
                    

                    break;

                default:

					JOptionPane.showMessageDialog(null, "Opcion Invalida!", "Jugador 4", JOptionPane.ERROR_MESSAGE);

                    break;
            }
       } while (menuDeUsuario != 3);
       


	}/*Fin Usuario cuatro*/
	

	
}/*Fin Clase*/
