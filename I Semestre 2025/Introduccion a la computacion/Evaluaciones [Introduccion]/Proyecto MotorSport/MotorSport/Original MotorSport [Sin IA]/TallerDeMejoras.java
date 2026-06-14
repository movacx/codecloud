/* Autor Herlin Chavarria C5E187 | Nota: Esta clase es para la Gestion o configuracion del vehiculo */

public class TallerDeMejoras{
	private boolean bridaDeAdmision; 		 // brida de admision / pregunta si desea quitarlo = si y no | por defecto true o por serie
	private int frontTireWidth;				 //Ancho del neumático delantero
	private int rearTireWidth;				 // Ancho del neumático tracero
	private String compuestoDeLlantas;		 // Serie, callejero, deportivo, carreras, aceleracion
	private String frenos;					 // De serie o Carreras
	private String muellesYAmortiguadores;   // Ayudan a controlar la transferencia de peso manteniendo un mejor control en curvas y en general
	private String embrague;				 // El embrague es el vinculo clave entre el motor y la transmision esta mejora gestiona mejor el motor sin causar daños
	private String transmision;				 // Las mejoras en la transmision pueden hacer que los cambios sean mucho mas rapidos y eficientes
	private String diferencial;				 // El diferencial permite que las llantas giren a una distinta velocidad
	
	public TallerDeMejoras(boolean bridaDeAdmision, int frontTireWidth, int rearTireWidth, String compuestoDeLlantas, String frenos, String muellesYAmortiguadores, String embrague, String transmision, String diferencial){
		this.bridaDeAdmision = true;
		this.frontTireWidth = frontTireWidth;
		this.rearTireWidth = rearTireWidth;
		this.compuestoDeLlantas = compuestoDeLlantas;
		this.frenos = frenos;
		this.muellesYAmortiguadores = muellesYAmortiguadores;
		this.embrague = embrague;
		this.transmision = transmision;
		this.diferencial = diferencial;
	}
	
	
	/* setter & getter */
	/* Nota: Muchos autos de competicion estan equipados con un sistema de "brida de admision" lo que hace que limite el aire que entra al motor por lo cual quita potencia al retirarlo el motor puede dar su maximo potencial */
	public void setBridaDeAdmision(boolean nuevoBridaDeAdmision){
		this.bridaDeAdmision = nuevoBridaDeAdmision;
	}
	public boolean getCombustibleAire(){
		return this.bridaDeAdmision;
	}
	/* Ancho neumatico delantero En general cuanta mas goma mejor el rendimiento ya que mejora la traccion de las llantas sobre el pavimiento*/
	public void setFrontTireWidth(int nuevoFrontTireWidth){
		this.frontTireWidth = nuevoFrontTireWidth;
	}
	public int getFrontTireWidth(){
		return this.frontTireWidth;
	}
	/* Ancho de neumatico tracero  */
	public void setRearTireWidth(int nuevoRearTireWidth){
		this.rearTireWidth = nuevoRearTireWidth;
	}
	public int getRearTireWidth(){
		return this.rearTireWidth;
	}
	/* compuesto de llantas ~ serie, callejero, deportivo, carreras, aceleracion */
	public void setCompuestoDeLlantas(String nuevoCompuestoLlantas){
		this.compuestoDeLlantas = nuevoCompuestoLlantas;
	}
	public String getCompuestoDeLlantas(){
		return this.compuestoDeLlantas;
	}
	/* Frenos ~ esta mejoras mejoras aumentan la potencia de frenado y disminuye el desgaste por el calor excesivo */
	public void setFrenos(String nuevoFrenos){
		this.frenos = nuevoFrenos;
	}
	public String getFrenos(){
		return this.frenos;
	}
	/* Muelles ~ Ayudan a controlar la transferencia de peso */
	public void setMuellesYAmortiguadores(String nuevoMuellesYAmortiguadores){
		this.muellesYAmortiguadores = nuevoMuellesYAmortiguadores;
	}
	public String getMuellesYAmortiguadores(){
		return this.muellesYAmortiguadores;
	}
	// El embrague ~ es el vinculo clave entre el motor y la transmision
	public void setEmbrague(String nuevoEmbrague){
		this.embrague = nuevoEmbrague;
	}
	public String getEmbrague(){
		return this.embrague;
	}
	// Transmision ~ Las mejoras en la transmision pueden hacer que los cambios sean mucho mas rapidos y eficientes
	public void setTransmision(String nuevoTransmision){
		this.transmision = nuevoTransmision;
	}
	public String getTransmision(){
		return this.transmision;
	}
	
	public void setDiferencial(String nuevoDiferencial){
		this.diferencial = nuevoDiferencial;
	}
	public String getDiferencial(){
		return this.diferencial;
	}
	
	public String toStrin(){
		return "Brida de Admision: " 				+ this.bridaDeAdmision
		+ "\nAncho de neumaticos delanteros: " 		+ this.frontTireWidth
		+ "\nAncho de neumaticos traceros: " 		+ this.rearTireWidth
		+ "\nCompuesto de llantas: " 				+ this.compuestoDeLlantas
		+ "\nTipo de frenos: " 						+ this.frenos
		+ "\nMuelles y amortiguadores: " 			+ this.muellesYAmortiguadores
		+ "\nEmbrague: " 							+ this.embrague
		+ "\nTransmision: " 						+ this.transmision

		;
	}
	

}//fin clase
