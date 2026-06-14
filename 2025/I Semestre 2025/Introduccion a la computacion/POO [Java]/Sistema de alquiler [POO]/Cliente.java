public class Cliente{
    private String nombre;
    private String cedula;
    private String telefono;
/* constructor */

	public Cliente(String nombre, String cedula, String telefono){
		this.nombre = nombre;
		this.cedula = cedula;
		this.telefono = telefono;
		
	}
	
/* set&getter*/

	//nombre
	public String getNombre(){
		return nombre;
	}
	public void setNombre(String nombre){
		this.nombre = nombre;
	}
	
	//cedula
	public String getCedula(){
		return cedula;
	}
	public void setCedula(String cedula){
		this.cedula = cedula;
	}
	
	//telefono
	public String getTelefono(){
		return telefono;
	}
	public void setTelefono(){
		this.telefono = telefono;
	}
	
	public String toString() {
		return "nombre "+this.nombre+" - " + "cedula "+this.cedula+" - "+"telefono"+this.telefono;
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
}//fin clase
