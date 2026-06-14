import java.util.Random;
public class MatrizEnteros
{
	private int matrizEnteros[][];
	
	public MatrizEnteros()
	{
		matrizEnteros = new int[4][4];
		
	}//fin del constructor sin parametros
	
	public MatrizEnteros(int cantidadFilas, int cantidadColumnas)
	{
		matrizEnteros = new int[cantidadFilas][cantidadColumnas];
		
	}//fin del constructor con parametros
	
	
	
	
	
	
	
	
	//-------------------------------------------------------------------------------------------------------------
	
	public void llenarMatriz()
	{
		Random generarNumeros = new Random();
		
		for(int fila=0; fila < matrizEnteros.length; fila++)
		{
			for(int columna=0; columna < matrizEnteros[0].length; columna++)
			{
				matrizEnteros[fila][columna] = generarNumeros.nextInt(100);
			}
		}
	}//fin del metodo llenar matriz
	
	
	
	//------------------------------------------------------------------------------------------------------------
	public String getArregloBidimensional()
	{
		String imprimir = "Los datos de la matriz son: \n";
		
		for(int fila=0; fila < matrizEnteros.length; fila++)
		{
			for(int columna=0; columna < matrizEnteros[0].length; columna++)
			{
				imprimir+= matrizEnteros[fila][columna]+"  ";
			}
			imprimir+= "\n";
		}
		return imprimir;
		
		
	}//fin del metodo getArregloBidimensional
	
	
	
	
	//------------------------------------------------------------------------------------------------------------
	
	public String getFila(int fila)
	{
		String imprimir = "{";
		

			for(int columna=0; columna < matrizEnteros[0].length; columna++)
			{
				if(columna == matrizEnteros[0].length-1)
				{
					imprimir += matrizEnteros[fila][columna]+"}";
				}
				else
				{
					imprimir += matrizEnteros[fila][columna]+",";
				}
			}
			
		
		return imprimir;
		
		
	}//fin del metodo
	
	
	//------------------------------------------------------------------------------------------------------------
	
	public String getcolumna(int columna)
	{
		String imprimir = "{";
		

			for(int fila=0; fila < matrizEnteros.length; fila++)
			{
				if(fila == matrizEnteros.length-1)
				{
					imprimir += matrizEnteros[fila][columna]+"}";
				}
				else
				{
					imprimir += matrizEnteros[fila][columna]+",";
				}
			}
			
		
		return imprimir;
		
		
	}//fin del metodo getColumna
	

	//------------------------------------------------------------------------------------------------------------


	public void setValor(int fila, int columna, int valor)
	{
		matrizEnteros[fila][columna] = valor;
	}


	//------------------------------------------------------------------------------------------------------------

	public String getDiagonalPrincipalIzquierdaDerecha()
	{
		String imprimir = "{";
		

			for(int indice=0; indice < matrizEnteros.length; indice++)
			{
				if(indice == matrizEnteros.length-1)
				{
					imprimir += matrizEnteros[indice][indice]+"}";
				}
				else
				{
					imprimir += matrizEnteros[indice][indice]+",";
				}
			}
			
		
		return imprimir;
		
		
	}//fin del metodo getDiagonalPrincipalIzquierdaDerecha
	
	
	//------------------------------------------------------------------------------------------------------------

	public String getDiagonalSecundariaDerechaIzquierda()
	{
		String imprimir = "{";
		int columna = matrizEnteros[0].length-1;
		

			for(int fila=0; fila < matrizEnteros.length; fila++)
			{
				if(columna == 0)
				{
					imprimir += matrizEnteros[fila][columna]+"}";
				}
				else
				{
					imprimir += matrizEnteros[fila][columna]+",";
				}
				columna --;
			}
			
		
		return imprimir;
		
		
	}//fin del metodo getDiagonalSecundariaDerechaIzquierda
	
	
//--------------------------------------------------------------------


	public String getDiagonalPrincipalDerechaIzquierda()
	{
		String imprimir = "{";
		

			for(int indice = matrizEnteros.length -1; indice >=0; indice --)
			{
				if(indice == 0)
				{
					imprimir += matrizEnteros[indice][indice]+"}";
				}
				else
				{
					imprimir += matrizEnteros[indice][indice]+",";
				}
			}
			
		
		return imprimir;
		
		
	}//fin del metodo getDiagonalPrincipalDerechaIzquierda
	
//-----------------------------------------------------------------------

	public String getDiagonalSecundariaIzquierdDerecha()
	{
		String imprimir = "{";
		int fila = matrizEnteros.length-1;
		

			for(int columna=0; columna < matrizEnteros[0].length; columna++)
			{
				if(columna == matrizEnteros[0].length -1)
				{
					imprimir += matrizEnteros[fila][columna]+"}";
				}
				else
				{
					imprimir += matrizEnteros[fila][columna]+",";
				}
				fila --;
			}
			
		
		return imprimir;
		
		
	}//fin del metodo getDiagonalSecundariaDerechaIzquierda
	
	
//-----------------------------------------------------------------------

	public int promedio()
	{
		int suma = 0;
		for(int fila=0; fila < matrizEnteros.length; fila++)
		{
			for(int columna=0; columna < matrizEnteros[0].length; columna++)
			{
				suma += matrizEnteros[fila][columna];
			}
		}
		return suma/(matrizEnteros.length + matrizEnteros[0].length);
		
	}//fin del meto promedio
	
//-----------------------------------------------------------------------

	public boolean verificarFila(int fila)
	{
		if((fila>=0)&&(fila<matrizEnteros.length))
		{
			return true;
		}
		else
		{
			return false;
		}
		
	}//verificar fila

//-----------------------------------------------------------------------

	public boolean verificarColumna(int columna)
	{
		if((columna>=0)&&(columna<matrizEnteros[0].length))
		{
			return true;
		}
		else
		{
			return false;
		}
		
	}//verificar columna
//-----------------------------------------------------------------------


}//fin clase

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
