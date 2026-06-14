public class Equipo{
	private String placa,marca,modelo,accesorios,tipo;
	private boolean estado;

	public Equipo(String placa,String marca,String modelo,String accesorios,String tipo,boolean estado)
	{
		setPlaca(placa);
		setMarca(marca);
		setModelo(modelo);
		setAccesorios(accesorios);
		setTipo(tipo);
		setEstado(estado);
	}//Fin del constructor con parametros

	public Equipo()
	{
		setPlaca("N/A");
		setMarca("N/A");
		setModelo("N/A");
		setAccesorios("N/A");
		setTipo("N/A");
		setEstado(false);
	}	

	public void setPlaca(String placa)
	{
		this.placa = placa;
	}

	public String getPlaca()
	{
		return this.placa;
	}

	public void setMarca(String marca)
	{
		this.marca = marca;
	}

	public String getMarca()
	{
		return this.marca;
	}
	public void setModelo(String modelo)
	{
		this.modelo = modelo;
	}
	public String getModelo()
	{
		return this.modelo;
	}
	public void setAccesorios(String accesorios)
	{
		this.accesorios = accesorios;
	}
	public String getAccesorios()
	{
		return this.accesorios;
	}

	public void setTipo(String tipo)
	{
		this.tipo = tipo;
	}

	public String getTipo()
	{
		return this.tipo;
	}

	public void setEstado(boolean estado)
	{
		this.estado = estado;
	}

	public boolean getEstado()
	{
		return this.estado;
	}

	public String toString()
	{
		return "Placa: "+getPlaca()+"\nMarca: "+getMarca()+"\nModelo: "+getModelo()+
	"\nTipo: "+getTipo()+"\nAccesorios: "+getAccesorios()+"\nEstado: "+getEstado();
	}
}//fin de la clase
