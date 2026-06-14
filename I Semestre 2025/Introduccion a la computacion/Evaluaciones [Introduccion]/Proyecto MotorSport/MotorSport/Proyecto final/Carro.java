/* Autor Herlin Chavarria C5E187 | Nota: Esta clase es para la personalizacion del vehiculo */

public class Carro {
	/* Aspecto visual del auto */
	private String marca;
	private String modelo;
	private String color;
	/* Especificaciones Tecnicas */
	private double velocidad;
	private double frenado;
	private double manejo;
	private double aceleracion;


	public Carro() {
		this.marca = "Sin Marca";
		this.modelo = "Sin Modelo";
		this.color = "Sin Color";
		this.velocidad = 0.0;
		this.frenado = 0.0;
		this.manejo = 0.0;
		this.aceleracion = 0.0;
	}

	// Constructor
	public Carro(String marca, String modelo, String color, double velocidad, double frenado, double manejo, double aceleracion) {
		/* Aspecto visual del auto */
		this.marca = marca;
		this.modelo = modelo;
		this.color = color;
		/* Especificaciones Tecnicas */
		this.velocidad = velocidad;
		this.frenado = frenado;
		this.manejo = manejo;
		this.aceleracion = aceleracion;
	}

	/* set & get */

	/* Aspecto visual del auto */
	public void setMarca(String nuevoMarca) {
		this.marca = nuevoMarca;
	}
	public String getMarca() {
		return this.marca;
	}
	public void setModelo(String nuevoModelo) {
		this.modelo = nuevoModelo;
	}
	public String getModelo() {
		return this.modelo;
	}
	public void setColor(String nuevoColor) {
		this.color = nuevoColor;
	}
	public String getColor() {
		return this.color;
	}

	/* Especificaciones Tecnicas */

	// Velocidad
	public void setVelocidad(double nuevoVelocidad) {
		this.velocidad += nuevoVelocidad; 
	}
	public double getVelocidad() {
		return this.velocidad;
	}
	// Frenado
	public void setFrenado(double nuevoFrenado) {
		this.frenado += nuevoFrenado; 
	}
	public double getFrenado() {
		return this.frenado;
	}
	// Manejo
	public void setManejo(double nuevoManejo) {
		this.manejo += nuevoManejo; 
	}
	public double getManejo() {
		return this.manejo;
	}
	// Aceleracion
	public void setAceleracion(double nuevoAceleracion) {
		this.aceleracion += nuevoAceleracion; 
	}
	public double getAceleracion() {
		return this.aceleracion;
	}

	public String toString() {
		//Nota String.format(%.1f, ) Sirve para mostrar las especificaciones técnicas con un solo decimal - me daba ejemplo: 1.999999999999999999999999999999 eso lo convierto a 1.9
		
		
		
		return "Marca:" + this.marca + "           Modelo: " + this.modelo + "           Color: " + this.color
		+ "\nVelocidad: " + String.format("%.1f", this.velocidad)
		+ "           | Frenado: " + String.format("%.1f", this.frenado)
		+ "\nAceleracion: " + String.format("%.1f", this.aceleracion)
		+ "           | Manejo: " + String.format("%.1f", this.manejo)
		;
	}

} // Fin clase Carro
