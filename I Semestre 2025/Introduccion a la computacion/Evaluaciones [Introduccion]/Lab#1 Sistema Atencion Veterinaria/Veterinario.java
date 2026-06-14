//autores Ramses guzman C13600  & Fabian Chavarria C5E187

public class Veterinario{
	
	private String nombre;
	private String telefono;
	private int cantidadAtenciones;
	
	//Metodo Constructor
	public Veterinario(String nombre, String telefono, int cantidadAtenciones){
		
		this.nombre = nombre;
		this.telefono = telefono;
		this.cantidadAtenciones = 0;
	}
	
	//Metodo Get
	public String getNombre(){
		
		return nombre;
	}
	
	public String getTelefono(){
		
		return telefono;
	}
	
	public int getCantidadAtenciones(){
		
		return cantidadAtenciones;
	}
	
	//Metodo Set
	public void setNombre(String nombre){
		
		this.nombre=nombre;
	}
	
	public void setTelefono(String telefono){
		
		this.telefono=telefono;
	}
	
	public void setCantidadAtenciones(int cantidadAtenciones){
		
		this.cantidadAtenciones=cantidadAtenciones;
	}
	
	public String toString(){
		
		return " \nNombre: "+nombre+ " \nTelefono: "+telefono+ " \nCantidad de atenciones: "+cantidadAtenciones;
	}
	
	
}
