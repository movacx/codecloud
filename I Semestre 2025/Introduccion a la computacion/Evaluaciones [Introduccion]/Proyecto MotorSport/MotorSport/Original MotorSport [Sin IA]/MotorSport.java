import javax.swing.JOptionPane;

public class MotorSport{

	private Usuario jugadorUno, jugadorDos, jugadorTres, jugadorCuatro;
	private Carro vehiculoUno, vehiculoDos, vehiculoTres, vehiculoCuatro; 
	private TallerDeMejoras configCarUno, configCarDos, configCarTres, ConfigCarCuatro;
	private String ingresoPrimerJugador, ingresoSegundoJugador, ingresoTercerJugador, ingresoCuartoJugador;
	private String nombreDeUsuario, nacionalidad ;
	private int edad, rentCar, modeloRentCar, menuRegistroUsuario, opcionRentCar, registrarAuto, test1;
	private int cantidadJugadores;
	private byte opcionTaller;

	

	
	public static void main(String []args){
		new MotorSport();
		
		
		
		
		
	}//Fin main
	
	
	
	
	public MotorSport(){
		/* Registro de los usuarios Usuario */
		login();
		menuPrincipal();
		
				// Ahora sumamos valores
		vehiculoUno.setVelocidad(2.1);  // compuesto
		vehiculoUno.setFrenado(0.9);    // compuesto
		vehiculoUno.setManejo(1.2);     // compuesto
		vehiculoUno.setAceleracion(1.5); // compuesto
		
		
		vehiculoDos.setVelocidad(4.0);  // debería quedar en 7.0
		vehiculoDos.setFrenado(4.0);    // debería quedar en 4.0
		vehiculoDos.setManejo(4.0);     // debería quedar en 5.0
		vehiculoDos.setAceleracion(4.0); // debería quedar en 8.0
		
				
		vehiculoTres.setVelocidad(6.0);  // debería quedar en 7.0
		vehiculoTres.setFrenado(6.0);    // debería quedar en 4.0
		vehiculoTres.setManejo(6.0);     // debería quedar en 5.0
		vehiculoTres.setAceleracion(6.0); // debería quedar en 8.0
		
		vehiculoCuatro.setVelocidad(2.0);  // debería quedar en 7.0
		vehiculoCuatro.setFrenado(2.0);    // debería quedar en 4.0
		vehiculoCuatro.setManejo(2.0);     // debería quedar en 5.0
		vehiculoCuatro.setAceleracion(2.0); // debería quedar en 8.0
		

		
		

		System.out.println("\nDespués de mejorar:");
		System.out.println(vehiculoUno + "\n" + vehiculoDos + "\n" + vehiculoTres + "\n" + vehiculoCuatro );
		
			
	JOptionPane.showMessageDialog(null, configCarUno);
	}
	
	
	
	
	public void login(){
		


		do {
			cantidadJugadores = Integer.parseInt(JOptionPane.showInputDialog("¿Cuántas personas van a ingresar al evento de Racing Sport?"));
			
			if (cantidadJugadores > 4 || cantidadJugadores < 1) {
				JOptionPane.showMessageDialog(null, "El limite de Jugadores permitidos es de 4", "Error", JOptionPane.ERROR_MESSAGE);
			}

		} while (cantidadJugadores > 4 || cantidadJugadores < 1); 


		JOptionPane.showMessageDialog(null, "🧑Organizador del evento: ¿Cómo están, amigos? Mi nombre es Cristopher, imagino que vienen a participar en el evento de Racing Sport." 
		+ "\n🧑Cristopher: Por favor, escriban su nombre en esta libreta para continuar con el evento.");
		if(cantidadJugadores == 1){
			ingresoPrimerJugador = JOptionPane.showInputDialog("  🏁 Bienvenido a Racing Sport🏁        " + "\n¿Como te llamas?: ");
			usuarioUno();
			estadisticas(); 
			
		
		}if(cantidadJugadores == 2){
			ingresoPrimerJugador = JOptionPane.showInputDialog("  🏁 Bienvenido a Racing Sport🏁        " + "\n¿Como te llamas?: ");
			ingresoSegundoJugador = JOptionPane.showInputDialog("  🏁 Bienvenido a Racing Sport🏁        " + "\n¿Como te llamas?: ");
			
			usuarioUno();
			usuarioDos();
			estadisticas();
		}if(cantidadJugadores == 3){
			ingresoPrimerJugador = JOptionPane.showInputDialog("  🏁 Bienvenido a Racing Sport🏁        " + "\n¿Como te llamas?: ");
			ingresoSegundoJugador = JOptionPane.showInputDialog("  🏁 Bienvenido a Racing Sport🏁        " + "\n¿Como te llamas?: ");
			ingresoTercerJugador = JOptionPane.showInputDialog("  🏁 Bienvenido a Racing Sport🏁        " + "\n¿Como te llamas?: ");
			usuarioUno();
			usuarioDos();
			usuarioTres();
			estadisticas();
			
		}if(cantidadJugadores == 4){
			ingresoPrimerJugador = JOptionPane.showInputDialog("  🏁 Bienvenido a Racing Sport🏁        " + "\n¿Como te llamas?: ");
			ingresoSegundoJugador = JOptionPane.showInputDialog("  🏁 Bienvenido a Racing Sport🏁        " + "\n¿Como te llamas?: ");
			ingresoTercerJugador = JOptionPane.showInputDialog("  🏁 Bienvenido a Racing Sport🏁        " + "\n¿Como te llamas?: ");
			ingresoTercerJugador = JOptionPane.showInputDialog("  🏁 Bienvenido a Racing Sport🏁        " + "\n¿Como te llamas?: ");
			usuarioUno();
			usuarioDos();
			usuarioTres();
			usuarioCuatro();
			estadisticas();

			
		}
	
	

	}//fin Login
	
	
	public void usuarioUno(){
		do{
			menuRegistroUsuario = Integer.parseInt(JOptionPane.showInputDialog("Bienvenido " +  ingresoPrimerJugador + " a \"Racing Sport\""
			+ "\nSeleccione una opcion: "
			+ "\n 1. Registro"
			+ "\n 2. Seleccion de vehiculos"
			+ "\n 3. Continuar"));
			
			switch (menuRegistroUsuario){
			case 1:
				nombreDeUsuario = JOptionPane.showInputDialog("Digite su nombre");
				edad = Integer.parseInt(JOptionPane.showInputDialog("Digite su Edad"));
				nacionalidad = JOptionPane.showInputDialog("Digite su nacionalidad");
				jugadorUno = new Usuario(nombreDeUsuario, nacionalidad, edad, 0,0);
				break;
				
			case 2:
				rentCar = JOptionPane.showConfirmDialog(null, "¿Desea rentar un vehiculo?", "Racing Sport", JOptionPane.YES_NO_OPTION ); /* JOptionPane YES = 0 | NO = 1 */ 
				
				if(rentCar == 0){
					wangCars(1); /* Llama el metodo de renta */ 
					
				}if(rentCar == 1){
					registrarAuto = JOptionPane.showConfirmDialog(null, "🧑Christopher: Veo que tienes un auto. ¿Acaso ese es el que deseas registrar? " , "Organizador del Evento: Cristopher", JOptionPane.YES_NO_OPTION ); 
					/* JOptionPane YES = 0 | NO = 1 */ 
					

					if(registrarAuto == 0){
					registrarVehiculo(1); /* Llama el metodo de registrar vehiculo */ 					


					}if(registrarAuto == 1){
						JOptionPane.showMessageDialog(null, "Cristopher: Entonces, alquila un auto si deseas participar; te voy a presentar a Wang Jiaqi, es un asesor de WangCars; él te ayudará con el trámite."
													+"\n 🧑Wang Jiaqi: 早上好朋友，让我自我介绍一下，我是 WangCars 顾问。");
						JOptionPane.showMessageDialog(null, "      ......      ");
						JOptionPane.showMessageDialog(null, "🧑Wang Jiaqi: Es broma, hablo español. \" risas \""  + "\n🧑Wang Jiaqi: Acompáñame para mostrarte los autos. ");
						wangCars(1); /* Llama el metodo de renta */ 
					}
				}
				break;
				
			case 3:
				JOptionPane.showMessageDialog(null, "Gracias por venir");
				break;
				
			default:
				JOptionPane.showMessageDialog(null, "Opcion no valida.", "Error", JOptionPane.ERROR_MESSAGE);
				break;
			}
		}while (menuRegistroUsuario !=3);
	}//Fin UsuarioUno
	

	public void usuarioDos(){
		
		do{
			menuRegistroUsuario = Integer.parseInt(JOptionPane.showInputDialog("🧑Cristopher: Bienvenido " +  ingresoSegundoJugador + " a \"Racing Sport\""
			+ "\nSeleccione una opcion: "
			+ "\n 1. Registro"
			+ "\n 2. Seleccion de vehiculos"
			+ "\n 3. Continuar"));
			
			switch (menuRegistroUsuario){
			case 1:
				nombreDeUsuario = JOptionPane.showInputDialog("Digite su nombre");
				edad = Integer.parseInt(JOptionPane.showInputDialog("Digite su Edad"));
				nacionalidad = JOptionPane.showInputDialog("Digite su nacionalidad");
				jugadorDos = new Usuario(nombreDeUsuario, nacionalidad, edad, 0,0);										/* Se actualizan los valores */
				break;
				
			case 2:
				rentCar = JOptionPane.showConfirmDialog(null, "¿Desea rentar un vehiculo?", "Racing Sport", JOptionPane.YES_NO_OPTION ); /* JOptionPane YES = 0 | NO = 1 */ 
				
				if(rentCar == 0){
					wangCars(2); /* Llama el metodo de renta */ 
					
				}if(rentCar == 1){
					registrarAuto = JOptionPane.showConfirmDialog(null, "🧑Christopher: Veo que tienes un auto. ¿Acaso ese es el que deseas registrar? " , "Organizador del Evento: Cristopher", JOptionPane.YES_NO_OPTION ); 
					/* JOptionPane YES = 0 | NO = 1 */ 
					
					if(registrarAuto == 0){
					registrarVehiculo(2); /* Llama el metodo de registrar vehiculo */ 

					}if(registrarAuto == 1){
						JOptionPane.showMessageDialog(null, "Cristopher: Entonces, alquila un auto si deseas participar; te voy a presentar a Wang Jiaqi, es un asesor de WangCars; él te ayudará con el trámite."
													+"\n 🧑Wang Jiaqi: 早上好朋友，让我自我介绍一下，我是 WangCars 顾问。");
						JOptionPane.showMessageDialog(null, "      ......      ");
						JOptionPane.showMessageDialog(null, "🧑Wang Jiaqi: Es broma, hablo español. \" risas \""  + "\n🧑Wang Jiaqi: Acompáñame para mostrarte los autos. ");
						wangCars(2); /* Llama el metodo de renta */ 
					}
				}
				break;
				
			case 3:
				JOptionPane.showMessageDialog(null, "Gracias por venir");
				break;
				
			default:
				JOptionPane.showMessageDialog(null, "Opcion no valida.", "Error", JOptionPane.ERROR_MESSAGE);
				break;
			}
		}while (menuRegistroUsuario !=3);
	}//Fin UsuarioDos
	
	public void usuarioTres(){

		do{
			menuRegistroUsuario = Integer.parseInt(JOptionPane.showInputDialog("🧑Cristopher: Bienvenido " +  ingresoTercerJugador + " a \"Racing Sport\""
			+ "\nSeleccione una opcion: "
			+ "\n 1. Registro"
			+ "\n 2. Seleccion de vehiculos"
			+ "\n 3. Continuar"));
			
			switch (menuRegistroUsuario){
			case 1:
				nombreDeUsuario = JOptionPane.showInputDialog("Digite su nombre");
				edad = Integer.parseInt(JOptionPane.showInputDialog("Digite su Edad"));
				nacionalidad = JOptionPane.showInputDialog("Digite su nacionalidad");
				jugadorTres = new Usuario(nombreDeUsuario, nacionalidad, edad, 0,0);										/* Se actualizan los valores */
				break;
				
			case 2:
				rentCar = JOptionPane.showConfirmDialog(null, "¿Desea rentar un vehiculo?", "Racing Sport", JOptionPane.YES_NO_OPTION ); /* JOptionPane YES = 0 | NO = 1 */ 
				
				if(rentCar == 0){
					wangCars(3); /* Llama el metodo de renta */ 
					
				}if(rentCar == 1){
					registrarAuto = JOptionPane.showConfirmDialog(null, "🧑Christopher: Veo que tienes un auto. ¿Acaso ese es el que deseas registrar? " , "Organizador del Evento: Cristopher", JOptionPane.YES_NO_OPTION ); 
					/* JOptionPane YES = 0 | NO = 1 */ 
					if(registrarAuto == 0){
						
					registrarVehiculo(3); /* Llama el metodo de registrar vehiculo */ 
					
					}if(registrarAuto == 1){
						JOptionPane.showMessageDialog(null, "Cristopher: Entonces, alquila un auto si deseas participar; te voy a presentar a Wang Jiaqi, es un asesor de WangCars; él te ayudará con el trámite."
													+"\n 🧑Wang Jiaqi: 早上好朋友，让我自我介绍一下，我是 WangCars 顾问。");
						JOptionPane.showMessageDialog(null, "      ......      ");
						JOptionPane.showMessageDialog(null, "🧑Wang Jiaqi: Es broma, hablo español. \" risas \""  + "\n🧑Wang Jiaqi: Acompáñame para mostrarte los autos. ");
						wangCars(3); /* Llama el metodo de renta */ 
					}
				}
				break;
				
			case 3:
				JOptionPane.showMessageDialog(null, "Gracias por venir");
				break;
				
			default:
				JOptionPane.showMessageDialog(null, "Opcion no valida.", "Error", JOptionPane.ERROR_MESSAGE);
				break;
			}
		}while (menuRegistroUsuario !=3);
	}//Fin UsuarioTres
		
		
	public void usuarioCuatro(){

		do{
			menuRegistroUsuario = Integer.parseInt(JOptionPane.showInputDialog("🧑Cristopher: Bienvenido " +  ingresoCuartoJugador + " a \"Racing Sport\""
			+ "\nSeleccione una opcion: "
			+ "\n 1. Registro"
			+ "\n 2. Seleccion de vehiculos"
			+ "\n 3. Continuar"));
			
			switch (menuRegistroUsuario){
			case 1:
				nombreDeUsuario = JOptionPane.showInputDialog("Digite su nombre");
				edad = Integer.parseInt(JOptionPane.showInputDialog("Digite su Edad"));
				nacionalidad = JOptionPane.showInputDialog("Digite su nacionalidad");
				jugadorCuatro = new Usuario(nombreDeUsuario, nacionalidad, edad, 0,0);										/* Se actualizan los valores */
				break;
				
			case 2:
				rentCar = JOptionPane.showConfirmDialog(null, "¿Desea rentar un vehiculo?", "Racing Sport", JOptionPane.YES_NO_OPTION ); /* JOptionPane YES = 0 | NO = 1 */ 
				
				if(rentCar == 0){
					wangCars(4); /* Llama el metodo de renta */ 
					
				}if(rentCar == 1){
					registrarAuto = JOptionPane.showConfirmDialog(null, "🧑Christopher: Veo que tienes un auto. ¿Acaso ese es el que deseas registrar? " , "Organizador del Evento: Cristopher", JOptionPane.YES_NO_OPTION ); 
					/* JOptionPane YES = 0 | NO = 1 */ 
					if(registrarAuto == 0){
						
						
					registrarVehiculo(4); /* Llama el metodo de registrar vehiculo */ 
						

					}if(registrarAuto == 1){
						JOptionPane.showMessageDialog(null, "Cristopher: Entonces, alquila un auto si deseas participar; te voy a presentar a Wang Jiaqi, es un asesor de WangCars; él te ayudará con el trámite."
													+"\n 🧑Wang Jiaqi: 早上好朋友，让我自我介绍一下，我是 WangCars 顾问。");
						JOptionPane.showMessageDialog(null, "      ......      ");
						JOptionPane.showMessageDialog(null, "🧑Wang Jiaqi: Es broma, hablo español. \" risas \""  + "\n🧑Wang Jiaqi: Acompáñame para mostrarte los autos. ");
						wangCars(4); /* Llama el metodo de renta */ 
					}
				}
				break;
				
			case 3:
				JOptionPane.showMessageDialog(null, "Gracias por venir");
				break;
				
			default:
				JOptionPane.showMessageDialog(null, "Opcion no valida.", "Error", JOptionPane.ERROR_MESSAGE);
				break;
			}
		}while (menuRegistroUsuario !=3);
	}//Fin usuarioCuatro
		
	
	public void wangCars(int numeroJugador){
		Carro carroRentado = null;

		opcionRentCar = Integer.parseInt(JOptionPane.showInputDialog(
		 "\nRenta CarsWang. Seleccione una Opcion: "
		+ "\n 1. Mercedes-AMG"
		+ "\n 2. McLaren"
		+ "\n 3. Porsche"));
		
		switch(opcionRentCar){
			case 1:
				modeloRentCar = Integer.parseInt(JOptionPane.showInputDialog("🧑Wang Jiaqi: En CarsWang tenemos una gran variedad de modelos en nuestra disposicion." 
					+ "\n🧑Wang Jiaqi: Sin embargo estos fueron algunos de los vehiculos que hemos traido al evento de Racing Sport: "
					+ "\n 1. AMG ONE 2018 - Azul"
					+ "\n 2. AMG GT3 - Amarillo"
					+ "\n 3. AMG C63 S Coupé - Blanco"));
				
				if(modeloRentCar == 1){
					carroRentado = new Carro("Mercedes-AMG", "AMG ONE 2018", "Azul", 6.1, 5.1, 4.9, 6.8 );
				} else if(modeloRentCar == 2){
					carroRentado = new Carro("Mercedes-AMG", "AMG GT3", "Amarillo", 5.0, 6.4, 6.7, 6.1 );
				} else if(modeloRentCar == 3){
					carroRentado = new Carro("Mercedes-AMG", "AMG C63 S Coupé", "Blanco", 7.4, 2.8, 2.6, 5.4 );
				}
				break;

			case 2:
				modeloRentCar = Integer.parseInt(JOptionPane.showInputDialog("🧑Wang Jiaqi: En CarsWang tenemos una gran variedad de modelos en nuestra disposicion." 
					+ "\n🧑Wang Jiaqi: Sin embargo estos fueron algunos de los vehiculos que hemos traido al evento de Racing Sport: "
					+ "\n 1. McLaren Senna 2018 - Azul"
					+ "\n 2. McLaren Spider 2019 - Amarillo"
					+ "\n 3. McLaren 600LT Coupé - Plateado"));

				if(modeloRentCar == 1){
					carroRentado = new Carro("McLaren", "McLaren Senna 2018", "Azul", 6.1, 5.1, 4.9, 6.8 );
				} else if(modeloRentCar == 2){
					carroRentado = new Carro("McLaren", "McLaren Spider 2019", "Amarillo", 5.0, 6.4, 6.7, 6.1 );
				} else if(modeloRentCar == 3){
					carroRentado = new Carro("McLaren", "McLaren 600LT Coupé", "Plateado", 7.4, 2.8, 2.6, 5.4 );
				}
				break;

			case 3:
				modeloRentCar = Integer.parseInt(JOptionPane.showInputDialog("🧑Wang Jiaqi: En CarsWang tenemos una gran variedad de modelos en nuestra disposicion." 
					+ "\n🧑Wang Jiaqi: Sin embargo estos fueron algunos de los vehiculos que hemos traido al evento de Racing Sport: "
					+ "\n 1. 2021 Porsche 911 GT3 - Naranja"
					+ "\n 2. 2016 Porsche Cayman GT4 - Gris"
					+ "\n 3. 2017 Porsche GT Team 911 RSR - Negro"));

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

			JOptionPane.showMessageDialog(null, "🧑Wang Jiaqi: ¡Genial! Fue una excelente opción, te diré las características de este vehículo:");
			JOptionPane.showMessageDialog(null, carroRentado ); /* revisar */
		}
	}
	
	public void registrarVehiculo(int asignarVehiculo){
		
		String marca = "";
		String modelo = "";
		String color = "";
		
		/* ----------------------------------------- */
		Carro registrarVehiculo = null;
		JOptionPane.showMessageDialog(null, "🧑Cristopher: Bien, llena este formulario para concluir con el registro del vehículo.");
		marca = JOptionPane.showInputDialog("Seleccione la marca");
		modelo = JOptionPane.showInputDialog("Seleccione el modelo");
		color = JOptionPane.showInputDialog("Seleccione la Color");
		
		
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



	public void menuPrincipal() {
		byte opcionMenu;
		int opcionTaller, subOpcion;
		double sumaVelocidad, sumaFrenado, sumaManejo, sumaAceleracion;
		TallerDeMejoras configCarUno = new TallerDeMejoras(true, 205, 225, "Serie", "Serie", "De serie", "De serie", "De serie", "De serie");
		TallerDeMejoras configCarDos = new TallerDeMejoras(true, 205, 225, "Serie", "Serie", "De serie", "De serie", "De serie", "De serie");
		TallerDeMejoras configCarTres = new TallerDeMejoras(true, 205, 225, "Serie", "Serie", "De serie", "De serie", "De serie", "De serie");
		TallerDeMejoras ConfigCarCuatro = new TallerDeMejoras(true, 205, 225, "Serie", "Serie", "De serie", "De serie", "De serie", "De serie");

		

		do {
			opcionMenu = Byte.parseByte(JOptionPane.showInputDialog("🧑Cristopher: ¡Antes de continuar! Racing Sport ha habilitado una sección especial donde podrán tunear sus vehículos a sus gustos."
			+ "\n🧑Cristopher: Si desean hacer modificaciones, pueden seguir a Gabriela, quien los guiará en el proceso."
			+ "\n🧑Cristopher: Pero si prefieren competir de una vez, pueden dirigirse directamente a la zona de competición con Lucas."
			+ "\n¿A quien deseas seguir?"
			+ "\n"
			+ "\n 1. Gabriela | Ir al Taller de Mejoras"
			+ "\n 2. Lucas    | Competir "
			+ "\n 3. Ver Estadisticas"
			+ "\n 4. Salir"));

			switch(opcionMenu) {
				
				case 1:
					opcionGabriela();
					break;

				case 2:
					JOptionPane.showMessageDialog(null, "🧑Lucas: ¡Competencias próximamente disponibles!");
					break;

				case 3:
					estadisticas(); 
					break;

				case 4:
					JOptionPane.showMessageDialog(null, "Tenga un buen dia regrese pronto.");
					break;

				default:
					JOptionPane.showMessageDialog(null, "Opcion Invalida");
			}
		} while (opcionMenu != 4);
	}
	
	public void opcionGabriela(){
		int seleccionUsuarios;
		
		if(cantidadJugadores == 1){
		seleccionUsuarios = Integer.parseInt(JOptionPane.showInputDialog("\nSeleccione su Usuario "
		+ "\n 1. " + jugadorUno
		+ "\n 0. Salir"));
		
		if(cantidadJugadores == 1){
			
		}
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		}if(cantidadJugadores == 2){
		opcionRentCar = Integer.parseInt(JOptionPane.showInputDialog("\nSeleccione su Usuario "
		+ "\n 1. " + jugadorUno
		+ "\n 2. " + jugadorDos
		+ "\n 0. Salir"));
		
		}if(cantidadJugadores == 3){
		opcionRentCar = Integer.parseInt(JOptionPane.showInputDialog("\nSeleccione su Usuario "
		+ "\n 1. " + jugadorUno
		+ "\n 2. " + jugadorDos
		+ "\n 3. " + jugadorTres
		+ "\n 0. Salir"));
		
		
		
			
		}if(cantidadJugadores == 4){
		opcionRentCar = Integer.parseInt(JOptionPane.showInputDialog("\nSeleccione su Usuario "
		+ "\n 1. " + jugadorUno
		+ "\n 2. " + jugadorDos
		+ "\n 3. " + jugadorTres
		+ "\n 4. " + jugadorCuatro
		+ "\n 0. Salir"));
		}
		
		
		
		

		
		
		
		
	}


	




}//Fin Clase
