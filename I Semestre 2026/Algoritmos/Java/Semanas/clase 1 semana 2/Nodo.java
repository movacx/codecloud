public class Nodo
{
	private int dato;
	private Nodo siguiente;
	//private Nodo anterios;
	
	public Nodo()
	{
		this.siguiente= null;
		//this.anterior=null;
		this.dato=0;
	}
	public Nodo(int dato)
	{
		this.siguiente= null;
		//this.anterior=null;
		this.dato=dato;
	}
	public Nodo(int dato, Nodo siguiente ) //Nodo anterior
	{
		this.siguiente= siguiente;
		//this.anterior=anterior;
		this.dato=dato;
	}
	public void setDato(int dato)
	{
		this.dato=dato;
	}
	public int getDato()
	{
		return dato;
	}
	public void setSiguiente(Nodo siguiente)
	{
		this.siguiente= siguiente;
	}
	public Nodo getSiguiente()
	{
		return siguiente;
	}
}
