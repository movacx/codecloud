public class Enteros{
	private int[] arregloA, arregloB, arregloC, arregloD;
	
	public Enteros(int longitud){
		arregloA = new int[longitud];
		arregloB = new int[longitud];
		arregloC = new int[longitud];
		arregloD = new int[longitud];
	
	}//fin constructor
	
	
	
//======================================================================
	public void setValor(int valorArregloA, int valorArregloB, int indice)
	{
		arregloA[indice] = valorArregloA;
		arregloB[indice] = valorArregloB;
	}

//======================================================================
	
	public void sumarArreglos()
	{
		for(int indice=0; indice < arregloA.length; indice++)
		{
			arregloC[indice] = arregloA[indice] + arregloB[indice];
		}
	}//fin del sumarArreglos




//======================================================================

	public void multiplicarArreglos()
	{
		arregloD[0] = arregloC[0] * arregloC[0];
		for(int indice=1; indice < arregloC.length; indice++)
		{
			arregloD[indice] = arregloC[indice] * arregloC[indice-1];
		}
	}//fin multiplicarArreglos


//======================================================================
	public int getIndiceNumeroMenor()
	{
		int indiceMenor = 0;
		for(int indice = 1; indice < arregloC.length; indice++)
		{
			if(arregloD[indice] < arregloC[indiceMenor])
			{
				indiceMenor = indice;
			}
		}
		return indiceMenor;
	}//Fin del metodo getIndiceNumeroMenor
	



//======================================================================
	public int getNumeroMenor()
	{
		return arregloD[getIndiceNumeroMenor()];
	}//fin metodo



//======================================================================
	public String getValoresArreglo(int numeroArreglo)
	{
		String valores = "";
		switch(numeroArreglo)
		{
			case 1:
			
				for(int indice=0; indice < arregloA.length; indice++)
				{
					valores += arregloA[indice]+" -";
				}
			
				break;
			case 2:
				for(int indice=0; indice < arregloB.length; indice++)
				{
					valores += arregloB[indice]+" -";
				}
				
				break;
			case 3:
			
				for(int indice=0; indice < arregloC.length; indice++)
				{
					valores += arregloC[indice]+" -";
				}
			
				break;
			case 4:
			
				for(int indice=0; indice < arregloD.length; indice++)
				{
					valores += arregloD[indice]+" -";
				}

				break;
			default:
		}
		return valores;
	}
	
	


	

	


//======================================================================



//======================================================================



//======================================================================
	
	
}//fin clase
