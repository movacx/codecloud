/* Author @FabianBeita-C5E187 G02 Introduccion a la computacion. */ 

import javax.swing.JOptionPane;

public class ControlDeEstudio{
	
String nombreEstudiante;
String cursoUni;
int horasDeEstudio;
int bloqueo = 0;
int horasPorDia;
int totalHoras;
int reset = 0;

	
	public static void  main (String []args){
		new ControlDeEstudio();
	}

	public ControlDeEstudio(){
		menuPrincipal();
		
	}
	
	
	public void menuPrincipal(){
	byte menuPrincipal;
		
		do{
			
			menuPrincipal = Byte.parseByte(JOptionPane.showInputDialog(null, "Menu Principal" + "\n 1. Registrar estudiante \n 2. Consultas sobre el estudio \n 3. Calcular promedio de estudio semanal \n 4. Salir", "Control de estudio", JOptionPane.INFORMATION_MESSAGE));

			
			switch(menuPrincipal){
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
					JOptionPane.showMessageDialog(null, "Gracias por usar nuestro sistema", "Control de estudio", JOptionPane.INFORMATION_MESSAGE);
					break;
				default:
					JOptionPane.showMessageDialog(null,  "OPCION INVALIDA", "Control de estudio", JOptionPane.ERROR_MESSAGE);
			}

		}while (menuPrincipal !=4);
	} 
	
	public void opcion1(){
		
		
		if (reset == 1){
			JOptionPane.showMessageDialog(null,  "Ya existen datos ingresados, si continua se borraran.", "Control de estudio", JOptionPane.ERROR_MESSAGE);
		}
		else{
			
		}
		
		
		bloqueo = bloqueo + 1;
		

		nombreEstudiante = JOptionPane.showInputDialog(null,  "Nombre del estudiante" , "Control de estudio", JOptionPane.QUESTION_MESSAGE);
		cursoUni = JOptionPane.showInputDialog(null, "Carrera que cursa" , "Control de estudio", JOptionPane.QUESTION_MESSAGE);
		horasDeEstudio = Integer.parseInt(JOptionPane.showInputDialog(null, "Cantidad de horas que estudia diariamente", "Control de estudio", JOptionPane.QUESTION_MESSAGE));
		
		if(horasDeEstudio < 6 ){
			JOptionPane.showMessageDialog(null, "Su nivel de estudio es Bajo.", "Control de estudio", JOptionPane.INFORMATION_MESSAGE);
			reset = reset + 1;
			
		}
		else{
			if(horasDeEstudio >= 6 & horasDeEstudio < 12  ){
				JOptionPane.showMessageDialog(null, "Su nivel de estudio es medio.", "Control de estudio", JOptionPane.INFORMATION_MESSAGE);
				reset = reset + 1;
			}
			else{
				if (horasDeEstudio >= 12)
				JOptionPane.showMessageDialog(null, "Su nivel de estudio es Alto.", "Control de estudio", JOptionPane.INFORMATION_MESSAGE);
				reset = reset + 1;
			}
			
		}
		
	}
	
	public void opcion2(){
	byte subMenu;
		
		if (bloqueo == 0){
			JOptionPane.showMessageDialog(null, "Sin datos.\n Sin registro del estudiante. \n Pulse \"Aceptar\" para continuar ", "Control de estudio", JOptionPane.WARNING_MESSAGE);
		}
		else{
			JOptionPane.showMessageDialog(null, "Espere un momento.. Cargando...", "Control de estudio", JOptionPane.INFORMATION_MESSAGE);
			
			
			subMenu = Byte.parseByte(JOptionPane.showInputDialog(null, "1. Mostrar información del estudiante \n 2. Evaluar rendimiento de estudio \n 3. Volver al menú principal ", "Control de estudio", JOptionPane.QUESTION_MESSAGE));
			switch(subMenu){
				case 1:
					JOptionPane.showMessageDialog(null, "" 
					+ " \n # Nombre del Estudiante: " + nombreEstudiante + "." 
					+ " \n # Curso del Estudiante: " + cursoUni + "."
					+ " \n # Horas de estudio del Estudiante: " + horasDeEstudio + "." + " hrs. ", 
					"Control de estudio", JOptionPane.INFORMATION_MESSAGE);
					break;
				case 2:
					
					if(horasDeEstudio < 6 ){
						JOptionPane.showMessageDialog(null, ":::::::::::::::::Evaluacion del estudiante::::::::::::::::"+ "\n El nivel de estudio es: \"Insuficiente\" ", "Control de estudio", JOptionPane.WARNING_MESSAGE);
					}
					else{
						if(horasDeEstudio >= 6 & horasDeEstudio < 12  ){
							JOptionPane.showMessageDialog(null, ":::::::::::::::::Evaluacion del estudiante::::::::::::::::"+ "\n El nivel de estudio es: \"Adecuado\" ", "Control de estudio", JOptionPane.INFORMATION_MESSAGE);
						}
						else{
							if (horasDeEstudio >= 12)
							JOptionPane.showMessageDialog(null, ":::::::::::::::::Evaluacion del estudiante::::::::::::::::"+ "\n El nivel de estudio es: \"Muy bueno, sigue asi.\" ", "Control de estudio", JOptionPane.INFORMATION_MESSAGE);
						}
						
					}
					break;
				case 3:
					JOptionPane.showMessageDialog(null, "Redireccionando....", "Control de estudio", JOptionPane.WARNING_MESSAGE);
					break;
				default:
					JOptionPane.showMessageDialog(null, "Opcion Ingresada no es Valida", "Control de estudio", JOptionPane.ERROR_MESSAGE);
				
			}
			
			
			
		}
		
		
	}
	
	
	public void opcion3(){
		
		//no me dio tiempo de revisar el 1 que sale en el panel de la opcion 3
		String [] semanas = {"domingo", "lunes", "martes", "miercoles", "jueves", "viernes", "sabado"};
		
		
			for ( int contador3 = 0; contador3 < semanas.length; contador3++ ){
				horasPorDia = Integer.parseInt(JOptionPane.showInputDialog(null, "¿Cuantas horas estudia el dia " + semanas[contador3] + "?", JOptionPane.INFORMATION_MESSAGE));
				totalHoras = totalHoras + horasPorDia;
			}
	
			if(totalHoras < 6 ){
				JOptionPane.showMessageDialog(null, "Su nivel de estudio es Bajo." + "\n Su promedio diario de estudio fue de " + totalHoras + " horas" , "Control de estudio", JOptionPane.INFORMATION_MESSAGE);

			}
			else{
				if(totalHoras >= 6 & horasDeEstudio < 12  ){
				JOptionPane.showMessageDialog(null, "Su nivel de estudio es medio." + "\n Su promedio diario de estudio fue de " + totalHoras + " horas" , "Control de estudio", JOptionPane.INFORMATION_MESSAGE);

				}
				else{
					if (totalHoras >= 12)
				JOptionPane.showMessageDialog(null, "Su nivel de estudio es Alto." + "\n Su promedio diario de estudio fue de " + totalHoras + " horas" , "Control de estudio", JOptionPane.INFORMATION_MESSAGE);

				}
			
			}
			

	}
	
	
}//Fin






