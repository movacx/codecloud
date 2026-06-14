public class Queso{
	//Declaracion de los atributos del objeto
	private String tipo;
	private int precio;
	private int unidades;
	//---------------------------------------------------------------------------------------------
	public Queso(String tipo, int precio, int unidades){
		
	setTipo(tipo);
	setPrecio(precio);
	setUnidades(unidades);
		
	}//Fin de constructor con parametros
	//--------------------------------------------------------------------------------------------
	public void setTipo(String tipo){
	this.tipo= tipo;
		
	}//Fin metodo setTipo
	//--------------------------------------------------------------------------------------------
	public String getTipo(){
	return this.tipo;	
	}//Fin metodo getTipo
	//--------------------------------------------------------------------------------------------
	
	public void setPrecio(int precio)
	{
		this.precio=precio;
	}
	//Fin setPrecio
	//--------------------------------------------------------------------------------------------
	public int getPrecio()
	{
		return this.precio;
	}
	//Fin getPrecio
	//--------------------------------------------------------------------------------------------
		
	public void setUnidades(int unidades)
	{
		this.unidades = unidades;
	}
	//Fin setUnidades
	//--------------------------------------------------------------------------------------------
	
	public int getUnidades()
	{
		return this.unidades;
	}
	//Fin getUnidades
	//--------------------------------------------------------------------------------------------
	
	public String toString()
	{
		return "Tipo: "+getTipo()+"\nPrecio"+getPrecio()+"Unidades: "+getUnidades()+"\n";
		
	}//Fin de la clase
}//Fin de la clase Queso

