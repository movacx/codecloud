import Math.ranbd

public class ManejoEstructuras
{
	private Pila cima;
	
	private Cola frente;
	private Cola finalCola;
	
	public ManejoEstructuras()
	{
		this.cima = null;
		this.frente = null;
		this.finalCola = null;
	}
	
	public void ingresarPila()
	{
		int valorAleatorio;
		cima = null;
		
		for (int indice=0; indice<5; indice++)
		{
			valorAleatorio = (int) (Math.random() * 100) + 1;
			
			Pila nuevo = new Pila(valorAleatorio);
			
			nuevo.sig = cima;
			cima = nuevo;
		}
	}
	
}
