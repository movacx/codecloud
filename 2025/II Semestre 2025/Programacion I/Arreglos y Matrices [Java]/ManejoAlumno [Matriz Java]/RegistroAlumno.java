public class RegistroAlumno
{
	private Alumno matrizAlumno[][];
	private double matrizNotas[][];
	
	public RegistroAlumno()
	{
		matrizAlumno = new Alumno[5][3];
		matrizNotas = new double[5][3];
	}//fin del constructor
	
//++======================================================================================================================++

	public boolean existeAlumno(String carnet)
	{
		boolean existe = false;
		for(int fila = 0; fila < matrizAlumno.length; fila++)
		{
			for(int columna=0; columna < matrizAlumno[0].length; columna++)
			{
				if(matrizAlumno[fila][columna] != null)
				{
					if(matrizAlumno[fila][columna].getCarnet().equals(carnet))
					{
						existe = true;
						break;
					}
				}
			}
		
		}
	return existe;
	}//fin del metodo existeAlumno




//++======================================================================================================================++


	public boolean verificarFilaColumna(int fila, int columna)
	{
		fila --;
		columna --;
		
		if(	(fila-1 >= 0) && (fila < matrizAlumno.length) && (columna >= 0) && (columna < matrizAlumno[0].length)	)
		{
			return true;
		}
		else
		{
			return false;
		}
	
	}

//++======================================================================================================================++



	public String agregarAlumno(int fila, int columna, Alumno alumno)
	{
		String mensaje = "";
		if(existeAlumno(alumno.getCarnet())== false)
		{
			if(verificarFilaColumna(fila,columna))
			{
				if(matrizAlumno[fila][columna] == null)
				{
					matrizAlumno[fila][columna] = alumno;
					mensaje = "Alumno guardado correctamente";
				}
				else
				{
					mensaje = "El campo aguardar esta ocupado";
				}
			}
			else
			{
				mensaje = "Error al guardar; Ingrese la fila en el rango de 1 a 5 \n Y la columna de 1 a 3";
			}
		}else
		{
			mensaje = "ya se encuentra registrado un alumno con el carnet digitado";
		}
		
		return mensaje;
	}




//++======================================================================================================================++

	public String modificarPorcentaje(String carnet, int opcionPorcentaje, double nuevoPorcentaje)
	{
		String mensaje="";
		if(existeAlumno(carnet))
		{
			for(int fila=0; fila < matrizAlumno.length; fila++)
			{
				for (int columna=0; columna < matrizAlumno[0].length; columna++)
				{
					if(matrizAlumno[fila][columna] !=null)

						if(matrizAlumno[fila][columna].getCarnet().equals(carnet))
						{
							switch(opcionPorcentaje)
							{
								case 1:
									matrizAlumno[fila][columna].setPrimerParcial(nuevoPorcentaje);
									mensaje = "Primer Parcial modificado correctamente";
									break;
								case 2:
									matrizAlumno[fila][columna].setSegundoParcial(nuevoPorcentaje);
									mensaje = "Segundo Parcial modificado correctamente";
									break;
								case 3:
									matrizAlumno[fila][columna].setTercerParcial(nuevoPorcentaje);
									mensaje = "Examen final modificado correctamente";
									break;
								case 4:
									matrizAlumno[fila][columna].setQuices(nuevoPorcentaje);
									mensaje = "Quices modificado correctamente";
									break;
									
							}//fin switch
						}
				}//fin del if que verifica el campo vacio
			}
		}
		else
		{
			mensaje = "No hay registro de un alumno con el carnet digitado";
		}
		

		return mensaje;
		
	}//Fin del metodo





//++======================================================================================================================++

	public String getNotasEstudiante(String carnet)
	{
		String mensaje = "";
		double notasEstudiante = 0;
		if (existeAlumno(carnet))
		{
			for(int fila = 0; fila < matrizAlumno.length; fila++)
			{
				for(int columna=0; columna < matrizAlumno[0].length; columna++)
				{
					if(matrizAlumno[fila][columna] !=null)
					{
						if(matrizAlumno[fila][columna].getCarnet().equals(carnet))
						{
							notasEstudiante = matrizAlumno[fila][columna].getPrimerParcial()+
							matrizAlumno[fila][columna].getSegundoParcial()+
							matrizAlumno[fila][columna].getExamenFinal()+
							matrizAlumno[fila][columna].getQuices();
							
							mensaje = "La nota del estudiante "+matrizAlumno[fila][columna].getNombre() + "\nEs " + notasEstudiante;
						}
					}
				}
			}
		}
		return mensaje;
	}
//++======================================================================================================================++

	public String getNotasEstudiantes()
	{
		String listadoNotas = "listado notas: \n\n";
		double notaAlumno = 0;
		//se recorre la matriz
	
		
			for(int fila = 0; fila < matrizAlumno.length; fila++)
			{
				
				
				for(int columna=0; columna < matrizAlumno[0].length; columna++)
				{//se verifica que se encuentre un objeto en la posicion de cada interaccion
					
					
					if(matrizAlumno[fila][columna] !=null)
					{//se suman los porcentaje para a nota del alumno
					

						
							notaAlumno = matrizAlumno[fila][columna].getPrimerParcial()+
							matrizAlumno[fila][columna].getSegundoParcial()+
							matrizAlumno[fila][columna].getExamenFinal()+
							matrizAlumno[fila][columna].getQuices();
							
							listadoNotas = "La nota del estudiante "+matrizAlumno[fila][columna].getNombre() + "\nEs " + notaAlumno;
						
					}
				}
			}
		
		return listadoNotas;
	}

//++======================================================================================================================++
	public String eliminarEstudiante(String carnet)
	{
		String mensaje = "";

		if (existeAlumno(carnet))
		{
			for(int fila = 0; fila < matrizAlumno.length; fila++)
			{
				for(int columna=0; columna < matrizAlumno[0].length; columna++)
				{
					if(matrizAlumno[fila][columna] !=null)
					{
						if(matrizAlumno[fila][columna].getCarnet().equals(carnet))
						{
							
							matrizAlumno[fila][columna]=null;//elimina el estudiante en esa posicion
							matrizNotas[fila][columna]=0; //Elimina la nota asociada al estudiante eliminado pero de la matriz notas
							mensaje = "Estudiante eliminado correctamente";
							break;
						}
					}
				}
			}
		}
		else
		{
			mensaje = "no hay registro de un alumno con el carnet digitado";
		}
		return mensaje;
	}

//++======================================================================================================================++
	public String getPosicionEstudiante(String carnet)
	{
		String mensaje = "";

		if (existeAlumno(carnet))
		{
			for(int fila = 0; fila < matrizAlumno.length; fila++)
			{
				for(int columna=0; columna < matrizAlumno[0].length; columna++)
				{
					if(matrizAlumno[fila][columna] !=null)
					{
						if(matrizAlumno[fila][columna].getCarnet().equals(carnet))
						{
							
							mensaje = "El estudiante esta en:   [" +(fila+1)+"] ["+(columna+1)+"]";
							break;
						}
					}
				}
			}
		}
		else
		{
			mensaje = "no hay registro de un alumno con el carnet digitado";
		}
		return mensaje;
	}

//++======================================================================================================================++
	
}//fin clase
