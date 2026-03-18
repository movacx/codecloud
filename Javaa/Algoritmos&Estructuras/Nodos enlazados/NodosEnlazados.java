public class NodosEnlazados
{
	/*Esta clase es similar a la clase arraylist, nos permite guardar valores
	 * y crear una cadena de nodos enlazados infinita*/

	private Nodo primero;
	private Nodo ultimo;


	public void agregarInicio(int dato)
	{
		Nodo nodoNuevo;
		if(primero == null)
		{

			//no hay elementos

			//Paso 1: Crear un nodo con el dato del usuario
			nodoNuevo = new Nodo(dato);

			//indicamos que nodo primero  y nodo ultimo apunta a ese nodo nuevo que acabamos de crear

			primero = nodoNuevo;
			ultimo=nodoNuevo;

		}else{
			//ya tiene elementos vacios
			nodoNuevo = new Nodo(dato);
			nodoNuevo.setSiguiente(primero);
			primero=nodoNuevo;



		}
	}

	public void agregarFinal(int dato)
	{
		Nodo nodoNuevo;
		if(ultimo == null)
		{
			nodoNuevo = new Nodo(dato);
			ultimo = nodoNuevo;
		}else{
			nodoNuevo = new Nodo(dato);
			ultimo = nodoNuevo;
		}

	}


	public String imprimir()
	{
		Nodo indice = primero;
		String mensaje = "";
		while(indice != null)
		{
			mensaje += indice.getSiguiente().getDato();
		}

		return mensaje;
	}



	private Nodo getAnterior(int valor)
	{
		Nodo indice = primero;
		Nodo anterior = null;

		while(indice != null)
		{
			if(indice.getDato() == valor)
			{
				return anterior;
			}
			anterior = indice;
			indice = indice.getSiguiente();
		}
		return null;
	}



	public void eliminar(int valorABuscar)
	{
		Nodo indice = primero;
		Nodo anterior = null;

		while(indice != null)
		{
			if(indice.getDato() == valorABuscar)
			{
				if(anterior == null)
				{

					primero = indice.getSiguiente();
				}
				else
				{
					anterior.setSiguiente(indice.getSiguiente());
				}
				return;
			}

			anterior = indice;
			indice = indice.getSiguiente();
		}
	}

	public Nodo despuesde(int valor)
	{
		Nodo indice = primero;

		while(indice != null)
		{
			if(indice.getDato() == valor)
			{
				return indice.getSiguiente(); // el siguiente nodo
			}
			indice = indice.getSiguiente();
		}
		return null;
	}
}