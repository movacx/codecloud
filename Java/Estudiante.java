/*Herlin Fabian Chavarria Beita C5E187*/
public class Estudiante
{
	private String carnet;
	private String nombreEstudiante;
	private String carrera;
	private double promedio;
	
	public Estudiante(String carnet, String nombreEstudiante, String carrera, double promedio)
	{
		this.carnet  = carnet;
		this.nombreEstudiante = nombreEstudiante;
		this.carrera = carrera;
		this.promedio = promedio;
	}
	
	public void setCarnet(String carnet)
	{
		this.carnet = carnet;
	}
	public String getCarnet()
	{
		return carnet;
	}
	
	public void setNombreEstudiante(String nombreEstudiante)
	{
		this.nombreEstudiante = nombreEstudiante;
	}
	public String getNombreEstudiante()
	{
		return nombreEstudiante;
	}
	
	public void setCarrera(String carrera)
	{
		this.carrera = carrera;
	}
	public String getCarrera()
	{
		return carrera;
	}
	
	public void setPromedio(double promedio)
	{
		this.promedio = promedio;
	}
	public double getPromedio()
	{
		return promedio;
	}
	
	public String toString()
	{
		return "Carnet: " + getCarnet() + "\nNombre estudiante: " + getNombreEstudiante() + "\nCarrera: " + getCarrera() + "\nPromedio: " + getPromedio();

	}
	
	
	
}









