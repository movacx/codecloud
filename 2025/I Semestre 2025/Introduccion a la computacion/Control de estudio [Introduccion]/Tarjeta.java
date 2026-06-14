/**  clase tarjeta */

public class Tarjeta{
	private int numTarjeta;
	private int saldo;
	private String titular;
	
	/* constructor */
	public Tarjeta(String nombreCliente, int numeroTarjetaAsignar, int saldo){
		this.titular = nombreCliente;
		this.numTarjeta = numeroTarjetaAsignar;
		this.saldo = saldo;
	}
	 //metodos set=asignar  get=obtener
	public void setNumTarjeta(int nuevoNumTarjeta){
		this.numTarjeta = nuevoNumTarjeta;
	}
	
	public int getNumTarjeta(){
		return this.numTarjeta;
	}
	
	public void setSaldo(int saldo){
		this.saldo = saldo;
	}
	public int getSaldo(){
		return this.saldo;
	}
	
	public void setTitular(String nuevoTitular){
		this.titular = nuevoTitular;
	}
	
	public String getTitular(){
		return this.titular;
	}
	
	public String toString(){
		return "Titular: "+ this.getTitular() + "\nNúmero de tarjeta: "
				+ this.getNumTarjeta() +"\nSaldo: " + this.getSaldo();
	}
		
	//metodos propios 
	public void pagar(int monto){
		this.saldo = this.saldo - monto;
	}
	
}

