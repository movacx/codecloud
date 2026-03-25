//++======================================================================================================================++
public class Empleado 
{
    private String cedula;
    private int edad;

    public Empleado(String cedula, int edad) 
    {
        this.cedula = cedula;
        this.edad = edad;
    }

    public String getCedula()
    { 
		return cedula; 
	}
    public int getEdad()
    { 
		return edad; 
	}

    public String mostrarDatos()
    {
        String mensaje;
        mensaje = "- Cedula: " + cedula + " Edad: " + edad;
        return mensaje;
    }
}//fin clase
