/*Herlin Fabian Chavarria Beita C5E187*/
public class RegistroObjeto
{
	private String codigo;
	private String nombre;
	private int edad;
	private String carrera;
	private int semestre; 
	private String tipo;
	
	public RegistroObjeto(String codigo, String nombre,  int edad, String carrera, int semestre, String tipo)
	{
		this.codigo  = codigo;
		this.nombre = nombre;
		this.edad = edad;
		this.carrera = carrera;
		this.semestre = semestre;
		this.tipo = tipo;
	}
	
	public void setTipo(String tipo)
	{
		this.tipo = tipo;
	}
	public String getTipo()
	{
		return tipo;
	}
	
	public void setCodigo(String codigo)
	{
		this.codigo = codigo;
	}
	public String getCodigo()
	{
		return codigo;
	}
	
	public void setNombre(String nombre)
	{
		this.nombre = nombre;
	}
	public String getNombre()
	{
		return nombre;
	}
	
	public void setEdad(int edad)
	{
		this.edad = edad;
	}
	public int getEdad()
	{
		return edad;
	}
	
	public void setCarrera(String carrera)
	{
		this.carrera = carrera;
	}
	public String getCarrera()
	{
		return carrera;
	}
	
	public void setSemestre(int semestre)
	{
		this.semestre = semestre;
	}
	public int getSemestre()
	{
		return semestre;
	}
	
    public String toString()
    {
        return "codigo: " + codigo + 
               "\nnombre: " + nombre + 
               "\nedad: " + edad + 
               "\ncarrera: " + carrera +
               "\nTipo: " + tipo +
               "\nsemestre: " + semestre;
    }
	
	
	
}


