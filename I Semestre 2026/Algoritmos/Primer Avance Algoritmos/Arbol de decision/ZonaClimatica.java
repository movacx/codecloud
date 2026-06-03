public class ZonaClimatica {
    String nombre;
    String claseReal; 
    double temperatura;
    double precipitacion;
    double altitud;
    double humedad; 

    public ZonaClimatica(String nombre, String claseReal, double temperatura, double precipitacion, double altitud, double humedad) {
        this.nombre = nombre;
        this.claseReal = claseReal;
        this.temperatura = temperatura;
        this.precipitacion = precipitacion;
        this.altitud = altitud;
        this.humedad = humedad;
    }
}
