//herlin fabian chavarria beita c5e187
public class DatosVentas{
	private int totalUnidadesVendidas;
	private int montoRecaudado;
	
	
	
	public DatosVentas(int totalUnidadesVendidas, int montoRecaudado){
		this.totalUnidadesVendidas = 0;
		this.montoRecaudado = 0;
	}
	
	/*set&get*/
	
	public void setTotalUnidadesVendidas(int nuevoTotalUnidadesVendidas){
		this.totalUnidadesVendidas += nuevoTotalUnidadesVendidas;
	}
	public int getTotalUnidadesVendidas(){
		return this.totalUnidadesVendidas;
	}
	
	
	/*//////////////////////////*/
	
	public void setMontoRecaudado(int nuevoMontoRecaudado){
		this.montoRecaudado += nuevoMontoRecaudado;
	}
	public int getMontoRecaudado(){
		return this.montoRecaudado;
	}
	
	public String toString(){
		return "Test DatoVentas";
	}
	
	
	
	
	
	
	
	
	
	
	
}//Fin clase
