public class ManejoNodo
{
	NodoTDA primero;
	
	public ManejoNodo()
	{
		this.primero = null; //Al inicio la lista no tiene nada
	}
	
	/*-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*/
	public boolean esVacia()
	{
		if(primero == null)
		{
			return true; //osea que si esta vacia
		}else{
			return false;
		}
	}
	
	/*-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*/
	public int primero()
	{
		if(primero != null)
		{
			return primero.dato;
			
		}else{
			return -1;
		}
	}
	
	/*-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*/
	public void imprimir_lista()
	{
		NodoTDA aux = primero;
		
		while(aux !=null)
		{
			System.out.println(aux.dato);
			aux = aux.siguiente;
		}
	}
	
	/*-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*/
	public int localiza(int numero_buscar)
	{
		int contador = 1;
		NodoTDA aux = primero;
		
		while(aux !=null)
		{
			if(aux.dato == numero_buscar)
			{
				return contador;
			}
			
			aux = aux.siguiente;
			contador ++;
		}
		return -1;
	}
	/*-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*/
	public int recupera(int posicion)
	{
		int contador = 1;
		NodoTDA aux = primero;
		
		if(posicion <= 0)
		{
			return -1; 
		}
		
		while(aux !=null)
		{
			if(contador == posicion)
			{
				return aux.dato;
			}
			
			aux = aux.siguiente;
			contador ++;
		}
		return -1;
	}
	/*-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*/
	public int insertar(int valor, int posicion)
	{
		NodoTDA nuevo = new NodoTDA(valor);
		int contador = 1;
		
		if(posicion == 1)
		{
			
			nuevo.siguiente = primero;
			primero = nuevo;
			return 1;
			
		}else
		{
			
			NodoTDA aux = primero;
			while(aux != null && contador < posicion -1)
			{
				aux = aux.siguiente;
				contador ++;
			}
			if(aux == null)
			{
				return -1;
			}
			
			nuevo.siguiente = aux.siguiente;
			aux.siguiente = nuevo;

			return 1;
		}
	}
	/*-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*/
	public int suprime(int posicion)
	{
		NodoTDA aux = primero;
		int contador = 1;
		
		if(posicion == 1)
		{
			primero = primero.siguiente;
		}else{
			
			while(aux !=null && contador < posicion -1)
			{
				aux = aux.siguiente;
				contador++;
			}
			
			if(aux == null) return -1;
			
			if(aux.siguiente == null) return -1;
			
			aux.siguiente = aux.siguiente.siguiente;
			
		}
		return 1;
	}
}
	
