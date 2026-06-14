//herlin fabian chavarria beita c5e187


public class EquipoRefrigeracion{
	private String modelo;
	private int precio;
	private int unidadesDisponibles;
	private int unidadesVendidas;

	
	
	/*constructor*/
	public EquipoRefrigeracion(String modelo, int precio, int unidadesDisponibles, int unidadesVendidas){
		this.precio = precio;
		this.modelo = modelo;
		this.unidadesDisponibles = unidadesDisponibles;
		this.unidadesVendidas = 0;
	}
	
	/*set&get*/
	
	/*modelo*/
	public void setModelo(String nuevoModelo){
		this.modelo = nuevoModelo;
	}
	public String getModelo(){
		return this.modelo;
	}
	/*unidadesDisponibles*/
	public void setUnidadesDisponibles(int nuevoUnidadesDisponible){
		this.unidadesDisponibles -= nuevoUnidadesDisponible;
	}
	public int getUnidadesDisponibles(){
		return unidadesDisponibles;
	}
	
	
	/*unidadesVendidas*/
	public void setUnidadesVendidas(int nuevoUnidadesVendidas){
		this.unidadesVendidas = nuevoUnidadesVendidas;
	}
	public int getUnidadesVendidas(){
		return unidadesVendidas;
	}
	
	
	
	
	/*precio*/
	public void setPrecio(int nuevoPrecio){
		this.precio = nuevoPrecio;
	}
	public int getPrecio(){
		return this.precio;
	}
	
	
	
	
	public String toString(){
		return "Modelo: " + this.modelo + "\nPrecio: " + this.precio + "\nUnidades disponibles: " + this.unidadesDisponibles + "\nUnidades Vendidas: " + this.unidadesVendidas;
	}
	
	
	
}//fin clase
