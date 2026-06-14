public class RegistroEquipos
{
	private Equipo equipos[];
	
	public RegistroEquipos()
	{
		equipos= new Equipo[4];
	}
	public RegistroEquipos(int cantidadEquipos)
	{
		equipos= new Equipo[cantidadEquipos];
	} 
	public boolean setEquipo(int indice, Equipo equipo)
	{
		boolean realizado= false;
		if(equipos[indice]== null)
		{
			equipos[indice]= equipo;
			realizado= true;
		}
		return realizado;
	}
	public Equipo getEquipo(int indice)
	{
		return equipos[indice];
	}
	public int length()
	{
		return equipos.length;
	}
	

	
	public int getPosicionEquipo(String placa)
	{
		int posicion=1;
		
		for(int indice=0;indice<equipos.length;indice++)
		{
			if(equipos[indice] != null){
				
				if(equipos[indice].getPlaca().equals(placa))
				{
					posicion= indice;
					break;
				}
			}
		}
		return posicion;
	}
	
	
	
	
	
	
	
	
	
	public String getEquipoTipo(String tipo)
	{
		String informacionEquiposTipo="";
		for(int indice=0;indice<equipos.length;indice++)
		{
			if(equipos[indice].getTipo().equals(tipo))
			{
				informacionEquiposTipo+=equipos[indice]+"\n\n";
			}
		}
		return informacionEquiposTipo;
	}
	public boolean setNuevoAccesorio(String placa, String nuevoAccesorio)
	{
		boolean existe= false;
		for(int indice=0;indice<equipos.length;indice++)
		{
			if(equipos[indice]!=null)
			{
				String accesoriosActualizados = equipos[indice].getAccesorios()+"."+nuevoAccesorio;
				//equipos[indice].setAccesorios(equipos[indice].getAccesorios()+", "+nuevoAccesorio);
				equipos[indice].setAccesorios(accesoriosActualizados);
				existe= true;
				break;
			}
		}
		return existe;
	}
	
	public boolean removerEquipo(String placa)
	{
		boolean existe= false;
		for(int indice=0;indice<equipos.length;indice++)
		{
			if(equipos[indice]!=null)
			{
				if(equipos[indice].getPlaca().equals(placa))
				{
					equipos[indice]=null;
					existe= true;
				}
			}
		}
		return existe;
	}
	public String getListadoEquipo()
	{
		String listado= "Listado equipos: \n";
		for(int indice=0;indice<equipos.length;indice++)
		{
			if(equipos[indice]!=null)
			{
				listado+= equipos[indice]+"\n\n";
			}
		}
		return listado;
	}
	public boolean verificarPlaca(String placa)
	{
		boolean existe= false;
		
		for(int indice=0;indice<equipos.length;indice++)
		{
			if(equipos[indice]!=null)
			{
				if(equipos[indice].getPlaca().equals(placa))
				existe=true;
				break;
			}
		}
		return existe;
	}
}
