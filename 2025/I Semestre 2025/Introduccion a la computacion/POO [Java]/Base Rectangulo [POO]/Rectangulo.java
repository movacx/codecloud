/**
clase que representa al rectangulo*/


public class Rectangulo {
	private int base;
	private int altura;

	//constructor
	public Rectangulo(int base, int altura){
		this.base = base;
		this.altura = altura;
	}
	
	
	
	
	
	//setter & getters
	public void setBase (int nuevaBase){
		this.base = nuevaBase;
	}
	public int getBase(){
		return this.base;
	}
	public void setAltura (int nuevaAltura){
		this.altura = nuevaAltura;
	}
	public int getAltura(){
		return this.altura;
	}
	public String toString(){
		return "Rectangulo de base: "+this.base + "altura: "+this.altura;
	}
	
	
	
	//metodos propios
	public int calcularPerimetro(){
		int perimetro=0;
		perimetro = base*2 + altura*2;
		return perimetro;
		
		
		
	}
	
	public int calcularArea(){
		return this.getBase() * this.getAltura();
	}




}//fin clase
