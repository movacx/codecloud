public class NodosEnlazados
{
	//Esta clase es similar a la clase arrayList, nos permite guardar valores y crear una cadena de nodos enlazados infinita
	
	private Nodo primero;
	private Nodo ultimo;
	
	public NodosEnlazados()
	{
	
	}
	public void agregarInicio(int dato)
	{
		//Se puede creear nodo nuevo aqui arriba para hacer el codigo mas eficiente
		//nodoNuevo =new Nodo(dato,siguiente);
		if(primero == null)
		{
			
			//No hay elementos
			//Paso 1: crear nodo con el dato del usuario 
			Nodo nodoNuevo= new Nodo();
			nodoNuevo.setDato(dato);
			//indicamos que nodo primero y nodo nodo ultimo apuntan a ese 
			//nodoNuevo que acabamos de crear
			primero= nodoNuevo;
			ultimo=nodoNuevo;
		}
		else
		{
			//Ya tiene elementos
			Nodo nodoNuevo=new Nodo();
			nodoNuevo.setDato(dato);
			//el nuevo nodo apunta el primero 
			nodoNuevo.setSiguiente(primero);
			//ahora el nodo nuevo pasa a ser el primero
			primero=nodoNuevo;
		}	
	}
	public void agregarFinal(int dato)
	{
		Nodo nodoNuevo = new Nodo();
		nodoNuevo.setDato(dato);

		if(primero == null)
		{
			primero = nodoNuevo;
			ultimo = nodoNuevo;
		}
		else
		{
			ultimo.setSiguiente (nodoNuevo);
			ultimo = nodoNuevo;
		}
	}
	public void imprimir()
	{
		Nodo aux = primero;

		while(aux != null)
		{
			System.out.println(aux.getDato());
			aux = aux.getSiguiente();
		}
	
	}
	public void despuesDe(int valorBuscar, int valorNuevo)
	{
		 Nodo anterior = getAnterior(valorBuscar);

		Nodo nodoNuevo = new Nodo();
		nodoNuevo.setDato(valorNuevo);

		if(anterior == null)
		{
			// Puede ser que sea el primero
			if(primero != null && primero.getDato() == valorBuscar)
			{
				nodoNuevo.setSiguiente(primero.getSiguiente());
				primero.setSiguiente(nodoNuevo);

				if(primero == ultimo)
				{
					ultimo = nodoNuevo;
				}
			}
		}
		else
		{
			Nodo nodoRef = anterior.getSiguiente();

			nodoNuevo.setSiguiente(nodoRef.getSiguiente());
			nodoRef.setSiguiente(nodoNuevo);

			if(nodoRef == ultimo)
			{
				ultimo = nodoNuevo;
			}
		}
	}
	public void eliminar(int valor)
	{
		Nodo anterior = getAnterior(valor);

		// Caso 1: el nodo a eliminar es el primero
		if(anterior == null)
		{
			if(primero != null && primero.getDato() == valor)
			{
				primero = primero.getSiguiente();

				if(primero == null)
				{
					ultimo = null;
				}
			}
		}
		else
		{
			// Caso 2: está en medio o al final
			Nodo nodoEliminar = anterior.getSiguiente();

			anterior.setSiguiente(nodoEliminar.getSiguiente());

			// Si era el último
			if(nodoEliminar == ultimo)
			{
				ultimo = anterior;
			}
		}
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
		} // while

		return null;
	} 
}
