//autores Ramses guzman C13600  & Fabian Chavarria C5E187



public class Mascota{
private String nombre;
private String tipoAnimal;
private double peso;


	public Mascota(String nombre, String tipoAnimal, double peso){
		this.nombre = nombre;
		this.tipoAnimal = tipoAnimal;
		this.peso = peso;
	}
	//set y get

	public void setNombre(String nuevoNombre){
		this.nombre = nuevoNombre;
	}
	public String getNombre(){
		return this.nombre;
	}
	
	public void setTipoAnimal(String nuevoTipoAnimal){
		this.tipoAnimal = nuevoTipoAnimal;
	}
	public String getTipoAnimal(){
		return this.tipoAnimal;
	}
	
	public void setPeso(double nuevoPeso){
		this.peso = nuevoPeso;
	}
	public double getPeso(){
		return this.peso;
	}
	
	public String toString(){
		return "\nnombre del animal: " + this.nombre + "\ntipo de animal: " + this.tipoAnimal + "\npeso del animal: " + this.peso;
		
		
	}
	
	







	}//fin clase
