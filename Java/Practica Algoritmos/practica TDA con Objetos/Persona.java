public class Persona
{
    private String nombre;
    private int edad;
    private String cedula;

    public Persona(String cedula, String nombre, int edad)
    {
        this.cedula = cedula;
        this.nombre = nombre;
        this.edad = edad;
    }

    public String getCedula()
    {
        return this.cedula;
    }

    public String getNombre()
    {
        return this.nombre;
    }

    public int getEdad()
    {
        return this.edad;
    }

    @Override
    public String toString()
    {
        return "DNI: " + this.cedula + "Nombre: " + this.nombre + "Edad: " +this.edad;
    }

}
