/* Autor Herlin Chavarria C5E187 | Nota: Esta clase es para la Gestion del Jugador */

public class Usuario {
	private String nombreDeUsuario;
	private String nacionalidad;
	private int edad;
	private int contadorCarrerasGanadas;
	private int tablaDePuntuacion;


	public Usuario(String nombreDeUsuario, String nacionalidad, int edad, int contadorCarrerasGanadas, int tablaDePuntuacion) {
		this.nombreDeUsuario = nombreDeUsuario;
		this.nacionalidad = nacionalidad;
		this.edad = edad;
		this.contadorCarrerasGanadas = 0; 
		this.tablaDePuntuacion = 0;  
	}

	/* setter & getter */

	public void setNombreDeUsuario(String nuevoNombreDeUsuario) {
		this.nombreDeUsuario = nuevoNombreDeUsuario;
	}
	public String getNombreDeUsuario() {
		return this.nombreDeUsuario;
	}


	public void setContadorCarrerasGanadas(int nuevoContadorCarrerasGanadas) {
		this.contadorCarrerasGanadas += nuevoContadorCarrerasGanadas;
	}
	public int getContadorCarrerasGanadas() {
		return this.contadorCarrerasGanadas;
	}


	public void setTablaDePuntuacion(int nuevoTablaDePuntuacion) {
		this.tablaDePuntuacion += nuevoTablaDePuntuacion;
	}
	public int getTablaDePuntuacion() {
		return this.tablaDePuntuacion;
	}


	public void setEdad(int edad) {
		this.edad = edad;
	}
	public int getEdad() {
		return this.edad;
	}

	public void setNacionalidad(String nacionalidad) {
		this.nacionalidad = nacionalidad;
	}
	public String getNacionalidad() {
		return this.nacionalidad;
	}


	
	public String toString() {
		return "Resumen del jugador"
		+ "\nNombre de Usuario: " + this.nombreDeUsuario
		+ "\nEdad: " + this.edad
		+ "\nNacionalidad: " + this.nacionalidad
		+ "\nCarreras ganadas: " + this.contadorCarrerasGanadas
		+ "\nTabla de Puntuacion: " + this.tablaDePuntuacion + "pts";
	}

} // Fin clase Usuario
