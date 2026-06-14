public class Casa {
    
    private String nombre;
    private String ubicacion;
    private int precioPorNoche;
    private boolean estaOcupada;
    private int diasAlquilada;

    // Constructor
    public Casa(String nombre, String ubicacion, int precioPorNoche) {
        this.nombre = nombre;
        this.ubicacion = ubicacion;
        this.precioPorNoche = precioPorNoche;
        this.estaOcupada = false; 
        this.diasAlquilada = 0;
    }

    // Métodos
    public void alquilar(int dias) {
        if (dias > 0) {
            this.estaOcupada = true;
            this.diasAlquilada = dias;
        }
    }

    public void devolver() {
        this.estaOcupada = false;
        this.diasAlquilada = 0;
    }

    public int calcularMonto() {
        return this.precioPorNoche * this.diasAlquilada;
    }

    // getyset
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

	//ubicacion
    public String getUbicacion() {
        return ubicacion;
    }
    public void setUbicacion(String ubicacion) {
        this.ubicacion = ubicacion;
    }

	//preciopornoche
    public int getPrecioPorNoche() {
        return precioPorNoche;
    }
    public void setPrecioPorNoche(int precioPorNoche) {
        this.precioPorNoche = precioPorNoche;
    }

	//estaocupada
	public boolean getEstaOcupada() {
		return estaOcupada;
	}
	public void setEstaOcupada(boolean estaOcupada) {
		this.estaOcupada = estaOcupada;
	}
    
	//diasalquiler
    public int getDiasAlquilada() {
        return diasAlquilada;
    }
    public void setDiasAlquilada(int diasAlquilada) {
        this.diasAlquilada = diasAlquilada;
    }


    //  Método toString
    
	public String toString() {
        return "nombre " + this.nombre + " - " + "ubicacion " + this.ubicacion + " - " + "precioPorNoche " + this.precioPorNoche + " - " + "estaOcupada " + this.estaOcupada + " - " + "diasAlquilada " + this.diasAlquilada;
    }
}
