public class Alumno
{
	
	private String nombre, carnet;
	private double primerParcial, segundoParcial, tercerParcial, examenFinal, quices;
	
	public Alumno(String nombre, String carnet, double primerParcial, double segundoParcial, double tercerParcial, double examenFinal, double quices){
		setNombre(nombre);
		setCarnet(carnet);
		setPrimerParcial(primerParcial);
		setSegundoParcial(segundoParcial);
		setTercerParcial(tercerParcial);
		setExamenFinal(examenFinal);
		setQuices(quices);

	}//fin del constructor
	
//++======================================================================================================================++
	public void setNombre(String nombre){
		this.nombre = nombre;
	}//fin set
	

	public String getNombre(){
		return nombre;
	}//fin get

//++======================================================================================================================++

	public void setCarnet(String carnet){
		this.carnet = carnet;
	
	}

	public String getCarnet(){
		return carnet;
	}
	
	
//++======================================================================================================================++

	public void setPrimerParcial(double primerParcial){
		this.primerParcial = primerParcial;
	}
	
	public double getPrimerParcial(){
		return primerParcial;
	}

//++======================================================================================================================++

	public void setSegundoParcial(double segundoParcial){
		this.segundoParcial = segundoParcial;
	}
	
	public double getSegundoParcial(){
		return segundoParcial;
	}

//++======================================================================================================================++

	public void setTercerParcial(double tercerParcial){
		this.tercerParcial = tercerParcial;
	}
	
	public double getTercerParcial(){
		return tercerParcial;
	}


//++======================================================================================================================++


	public void setExamenFinal(double examenFinal){
		this.examenFinal = examenFinal;
	}
	
	public double getExamenFinal(){
		return examenFinal;
	}


//++======================================================================================================================++

	public void setQuices(double quices){
		this.quices = quices;
	}
	
	public double getQuices(){
		return quices;
	}


//++======================================================================================================================++

	public String ToString(){
		return "Carnet:" ;
	}


//++======================================================================================================================++



//++======================================================================================================================++	
	
	
	
	
}//fin clased
