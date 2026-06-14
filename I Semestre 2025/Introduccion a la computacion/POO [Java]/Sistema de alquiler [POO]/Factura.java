
public class Factura {

    private Cliente cliente;
    private Casa casa;
    private double montoTotal;
    private double descuento;

    public Factura(Cliente cliente, Casa casa) {
        this.cliente = cliente;
        this.casa = casa;
        this.montoTotal = 0;
        this.descuento = 0;
    }

    public void calcularDescuento() {
        double montoInicial = this.casa.calcularMonto();

      
        if (this.casa.getDiasAlquilada() > 5) {
            this.descuento = montoInicial * 0.10;
        } else {
            this.descuento = 0; 
        }
    }



	public String generarDetalle() {
		
		this.calcularDescuento();
		double subtotal = this.casa.calcularMonto();
		this.montoTotal = subtotal - this.descuento;

		
		return "--- DETALLE DE FACTURA ---\n" + "Cliente: " + this.cliente.getNombre() + "\n" + "Casa: " + this.casa.getNombre() + "\n" + "Subtotal: " + subtotal + "\n" + "Descuento: " + this.descuento + "\n" + "TOTAL A PAGAR: " + this.montoTotal;
	}

    
    public Cliente getCliente() {
        return cliente;
    }

    public Casa getCasa() {
        return casa;
    }

    public double getMontoTotal() {
        return montoTotal;
    }

    public double getDescuento() {
        return descuento;
    }
    
    public String toString() {
        return "cliente " + this.cliente.getNombre() + " - " + "casa " + this.casa.getNombre() + " - " + "montoTotal " + this.montoTotal;
    }
}
