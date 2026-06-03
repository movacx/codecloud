
public class PruebaNodo
{
	
	public static void main(String[]args)
	{
		Nodo n1 = new Nodo(10);
		Nodo n2 = new Nodo(15);
		Nodo n3 = new Nodo(20);
		Nodo n4 = new Nodo(25);
		Nodo aux = n1;
		
		n1.siguiente = n2;
		n2.siguiente = n3;
		n3.siguiente = n4;

		while(aux !=null)
		{
			System.out.println(aux.dato);
			aux=aux.siguiente;
		}

	}
}
