public class Equipo{
	
	String placa, marca, modelo, accesorios, tipo;
	boolean estado;
	
	/*constructor*/
	public Equipo(String placa, String marca, String modelo, String accesorios, String tipo, boolean estado){
		this.placa = placa;
		this.marca = marca;
		this.modelo = modelo;
		this.accesorios = accesorios;
		this.tipo = tipo;
		this.estado = estado;
	}
	
	public Equipo(){
		this.placa = "5654";
		this.marca = "canon";
		this.modelo = "Ts";
		this.accesorios = "Estuche - cargador - Bateria Original";
		this.tipo = "Camara fotografica";
		this.estado = true;
	}
		

	
	
//=======================================================================

	public void setPlaca(String placa){
		this.placa = placa;
	}//fin modo set
	public String getPlaca(){
		return placa;
	}//fin modo get
	
//=======================================================================

	public void setModelo(String modelo){
		this.modelo = modelo;
	}//fin modo set
	public String getModelo(){
		return modelo;
	}//fin modo get
//=======================================================================

	public void setAccesorios(String accesorios){
		this.accesorios = accesorios;
	}//fin modo set
	public String getAccesorios(){
		return accesorios;
	}//fin modo get
//=======================================================================
	
	public void setTipo(String tipo){
		this.tipo = tipo;
	}//fin modo set
	public String getTipo(){
		return tipo;
	}//fin modo get
//=======================================================================

	public void setEstado(boolean estado){
		this.estado = estado;
	}//fin modo set
	public boolean getEstado(){
		return estado;
	}//fin modo get
//=======================================================================



	public void setMarca(String marca){
		this.marca = marca;
	}//fin modo set
	public String getMarca(){
		return marca;
	}//fin modo get


	
	public String toString(){
		
		return "Placa: "+ getPlaca()+"\nMarca: "+getMarca()+
		"\nModelo: "+getModelo()+"\nTipo: "+getTipo()+"\nAccesorios: "+getAccesorios()+
		"\nEstado: "+getEstado()+"\n";
	}
	

	
	
}/*fom cñase*/
