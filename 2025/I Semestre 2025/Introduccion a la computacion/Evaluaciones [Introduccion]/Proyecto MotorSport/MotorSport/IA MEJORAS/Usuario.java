/* Autor Herlin Chavarria C5E187 | Nota: Esta clase es para la Gestion del Jugador */

public class Usuario {
	private String nombreDeUsuario;
	private String nacionalidad;
	private int edad;
	private int contadorCarrerasGanadas;
	private int tablaDePuntuacion;

	// Constructor:
	// La lógica es que 'contadorCarrerasGanadas' y 'tablaDePuntuacion'
	// siempre inician en 0 para un nuevo usuario, por lo que no se usan los parámetros para ellos aquí.
	public Usuario(String nombreDeUsuario, String nacionalidad, int edad, int contadorCarrerasGanadas, int tablaDePuntuacion) {
		this.nombreDeUsuario = nombreDeUsuario;
		this.nacionalidad = nacionalidad;
		this.edad = edad;
		this.contadorCarrerasGanadas = 0; // Siempre inicia en 0, como lo especificaste
		this.tablaDePuntuacion = 0;     // Siempre inicia en 0, como lo especificaste
	}

	/* setter & getter */

	public void setNombreDeUsuario(String nuevoNombreDeUsuario) {
		this.nombreDeUsuario = nuevoNombreDeUsuario;
	}
	public String getNombreDeUsuario() {
		return this.nombreDeUsuario;
	}


	public void setContadorCarrerasGanadas(int nuevoContadorCarrerasGanadas) {
		this.contadorCarrerasGanadas = nuevoContadorCarrerasGanadas;
	}
	public int getContadorCarrerasGanadas() {
		return this.contadorCarrerasGanadas;
	}


	public void setTablaDePuntuacion(int nuevoTablaDePuntuacion) {
		this.tablaDePuntuacion = nuevoTablaDePuntuacion;
	}
	public int getTablaDePuntuacion() {
		return this.tablaDePuntuacion;
	}

	// Agregado setter para edad y nacionalidad por si se necesitan actualizar
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


	@Override // Buena práctica para indicar que sobrescribe un método de la clase Object
	public String toString() {
		return "Resumen del jugador"
		+ "\nNombre de Usuario: " + this.nombreDeUsuario
		+ "\nEdad: " + this.edad
		+ "\nNacionalidad: " + this.nacionalidad
		+ "\nCarreras ganadas: " + this.contadorCarrerasGanadas
		+ "\nTabla de Puntuacion: " + this.tablaDePuntuacion + "pts";
	}

} // Fin clase Usuario
