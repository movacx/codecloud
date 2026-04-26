
public class ManejoEstructuras
{

	 // =========================== INGRESAR PILA =========================================== //
	 public void ingresarPila(Pila miPila)
	 {
	
		 miPila.cima = null;
		 
		 
		 for (int indice = 0; indice < 5; indice++) 
		 {
			 int numAleatorio = (int) (Math.random() *100) + 1;
			 

			 Nodo nuevo = new Nodo(numAleatorio);
			 
			  nuevo.siguiente = miPila.cima;
			  

			  miPila.cima = nuevo;
			 
		 }
	 }
	 

	  
	  // =========================== APILAR =========================================== //
	  
	 public void apilar(Pila miPila, int dato)
	 {
		 Nodo nuevo = new Nodo(dato);
		 

		 nuevo.siguiente = miPila.cima;
		 

		 miPila.cima = nuevo;
	 }
	 

	  
	  // =========================== DESAPILAR =========================================== //
	  
	  public int desapilar(Pila miPila)
	  {

		  if (miPila.cima == null)
		  {
			  return -1;
		  }
		  

		  int valor = miPila.cima.dato;
		  

		  
		  miPila.cima = miPila.cima.siguiente;
		  
	
		  return valor;
	  }
	 

	  
	 // =========================== MOSTRARPILA =========================================== //
	public String mostrarPila(Pila miPila)
	{
		if (miPila.cima == null)
		{
			return "La pila esta vacia";
		}
		
		Pila pilaAuxiliar = new Pila();
		String texto = "Pila: ";
		
		
		while (miPila.cima != null)
		{
			int dato = desapilar(miPila);
			texto += "[" + dato + "]";
			apilar(pilaAuxiliar, dato);
		}
		
		
		while (pilaAuxiliar.cima != null)
		{
			apilar(miPila, desapilar(pilaAuxiliar));
		}
		return texto;
	}
	
	// =========================== MOSTRARPILA =========================================== //
	public void invertirPila(Pila miPila)
	{
		if (miPila.cima == null)
		{
			System.out.println("La pila esta vacia");
			return;
		}
		
		Cola temporal = new Cola(); 
		
		while (miPila.cima != null)
		{
			encolar(temporal, desapilar(miPila));
		}
		
		
		while (temporal.primero != null)
		{
			apilar(miPila, desencolar(temporal));
		}
	}
	  
	  
	 
	  
	//==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
	
	//Ingresar Cola
	 public void ingresarCola(Cola miCola)
	 {
		
		 miCola.primero = null;
		 miCola.ultimo = null;
		 
		 for (int indice = 0; indice < 5; indice++) 
		 {
			 int num = (int) (Math.random()*100) +1;
			 Nodo nuevo = new Nodo(num);
			 
			 if (miCola.primero == null)
			 {
				
				 miCola.primero = nuevo;
				 miCola.ultimo = nuevo;
				 
			 }else{
			
				 miCola.ultimo.siguiente = nuevo;
				 
			
				 miCola.ultimo = nuevo;
			 }
			 
		 }
	 }
	  
	//Encolar
	public void encolar(Cola miCola, int dato)
	{
		
		Nodo nuevo = new Nodo(dato);
		
		
		if (miCola.primero == null)
		{
		
			miCola.primero = nuevo;
			miCola.ultimo = nuevo;
		}else{
		
			miCola.ultimo.siguiente = nuevo;
			
		
			miCola.ultimo = nuevo;
		}
	}
	
	public int desencolar(Cola miCola)
	{

		if (miCola.primero == null)
		{
			return -1;
		}
		
	
		int valor = miCola.primero.dato;
		
	
		miCola.primero = miCola.primero.siguiente;
		
	
		if (miCola.primero == null)
		{
			
			miCola.ultimo = null;
		}
		
		return valor;
	}
	
	
	 
}
