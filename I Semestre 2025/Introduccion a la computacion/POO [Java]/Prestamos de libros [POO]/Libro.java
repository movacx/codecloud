

public class Libro{

	private String titulo;
	private String autor;
	private int numeroPaginas;
	private boolean estaPrestado;

	//constructor
	public Libro(String titulo, String autor, int numeroPaginas){
		this.titulo = titulo;
		this.autor = autor;
		this.numeroPaginas = numeroPaginas;
		this.estaPrestado = false;
	}
	
	//set&get
	
	/*setTitulo*/
	public void setTitulo(String nuevoTitulo){
		this.titulo = nuevoTitulo;
	}
	public String getTitulo(){
		return this.titulo;
	}
	
	/* setAutor */
	public void setAutor(String nuevoAutor){
		this.autor = nuevoAutor;
	}
	public String getAutor(){
		return this.autor;
	}
	
	/* NumeroPaginas */
	public void setNumeroPaginas(int nuevoNumeroPaginas){
		this.numeroPaginas = nuevoNumeroPaginas;
	}
	public int getNumeroPaginas(){
		return this.numeroPaginas;
	}
	
	/* prestamo */
	public void setEstaPrestado(boolean estaOcupado){
		this.estaPrestado = estaOcupado;
	}
	public boolean estaPrestado(){
		return this.estaPrestado;
	}
	
	
	public void prestar(){
		if (this.estaPrestado == true){
			System.out.println("El libro \"" + this.getTitulo() +  "se encuentra en uso");
		} else{
			this.estaPrestado = true;
			System.out.println("El libro \"" + this.getTitulo() +  "ha sido prestado correctamente"); 
		}
	}
	
	public void devolver(){
		if (this.estaPrestado == true){
			this.estaPrestado = false;
			System.out.println("El libro \"" + this.getTitulo() + "Ha sido devuelto");
		} else{
			System.out.println("El libro \"" + this.getTitulo() + "No estaba prestado");
		}
	}
	
	public String toString(){
		return "titulo: " + this.titulo + "autor: " + this.autor + "numero de paginas: " + this.numeroPaginas + "estado del prestamo: " + (this.estaPrestado ? "si" : "no");		
		
	}
	


}//fin clase
