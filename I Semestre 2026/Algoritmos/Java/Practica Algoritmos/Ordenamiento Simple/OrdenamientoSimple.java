
public class OrdenamientoSimple
{
	int[] numeros;
	
	public OrdenamientoSimple()
	{
		this.numeros = null;
	}
	
	/*-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*/
	public void burbuja()
	{
		int largo;
		int aux;
		int pasada;
		int posicion;
		
		largo = numeros.length;
		pasada = 0;
		
		while(pasada < largo - 1)
		{
			posicion = 0;
			while(posicion < largo - 1 - pasada)
			{
				if(numeros[posicion] > numeros[posicion + 1])
				{
					aux = numeros[posicion];
					numeros[posicion] = numeros[posicion + 1];
					numeros[posicion + 1] = aux;
				}
				posicion++;
			}
			pasada++;
		}
	}
	
	/*-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*/
	public void imprimir_arreglo()
	{
		int indice = 0;
		
		while(indice < numeros.length)
		{
			System.out.println(numeros[indice]);
			indice++;
		}
	}
	
	/*-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*/
	public static void main(String[] args)
	{
		OrdenamientoSimple obj = new OrdenamientoSimple();
		
		obj.numeros = new int[]{64, 25, 12, 99, 7, 43, 31};
		
		System.out.println("Lista original:");
		obj.imprimir_arreglo();
		
		obj.burbuja();
		
		System.out.println("Lista ordenada:");
		obj.imprimir_arreglo();
	}
}

/*
 * Tema: Algoritmos de ordenamiento simples
 *
 * Burbuja: revisa pares de elementos seguidos y los intercambia si
 * estan en orden equivocado. Repite hasta que no haya intercambios.
 *
 * Seleccion: busca el menor de toda la lista y lo pone de primero,
 * luego el menor de lo que queda, y asi hasta terminar.
 *
 * Insercion: toma cada elemento y lo inserta en su posicion correcta
 * dentro de los que ya estan ordenados, como acomodar cartas.
 * C5E187 Herlin Fabian Chavarria Beita
 */
