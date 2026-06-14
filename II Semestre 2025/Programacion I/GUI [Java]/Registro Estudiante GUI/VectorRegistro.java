import javax.swing.JOptionPane; 
import java.util.ArrayList;
public class VectorRegistro
{
   private ArrayList<RegistroObjeto> lista;

    public VectorRegistro()
    {
        lista = new ArrayList<RegistroObjeto>();
    }
    
	//-------------------------------------------------------------------------------------
	//Metodo guardar
	public void guardarObjeto(RegistroObjeto registro)
	{
		if(registro != null)
		{
			lista.add(registro);
			JOptionPane.showMessageDialog(null, "guardada correctamente");	
		}
		else
		{
			JOptionPane.showMessageDialog(null, "Error: Es nula");
		}
	}		
	//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	// Metodo buscar
	public RegistroObjeto buscarObjeto(String buscarPorId)
	{
		RegistroObjeto registro = null;

		for(int indice = 0; indice < lista.size(); indice++)
		{
			if(lista.get(indice).getCodigo().equals(buscarPorId))
			{
				registro = lista.get(indice);
				break;
			}
		}
		
		// Mensaje
		if(registro == null)
		{
			JOptionPane.showMessageDialog(null, "No existe ese Id");
		}

		return registro;
	}
	//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	public int validarExistencia(String buscarPorId)
	{
		int validarExistencia=0;

		for(int indice = 0; indice < lista.size(); indice++)
		{
			if(lista.get(indice).getCodigo().equals(buscarPorId))
			{
				validarExistencia = 1; 
				break;
			}
		}
		return validarExistencia;
	}
	//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	
	//Verificar numero de factura 
	public boolean verificarId(String buscarPorId)
	{
		boolean existe= false;
		for(int indice=0; indice<lista.size();indice++)
		{
			if(lista.get(indice).getCodigo().equals(buscarPorId))
			{
				existe = true;
				break;  
			}
		}
		return existe;
	}//Fin del verificar 
	//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	
	//Metodo elimina
	public String eliminarObjeto(String buscarPorId)
	{
		boolean eliminado = false;
		
		if(verificarId(buscarPorId) == true)
		{
			for(int indice=0; indice<lista.size();indice++)
			{
				if(lista.get(indice).getCodigo().equals(buscarPorId))
				{
					lista.remove(indice);
					eliminado = true;
					break;
				}
			}
		}
		
		if(eliminado)
			return "Eliminado con exito";
		else
			return "No se encontró";
	}
	//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	//Modificar datos 
	public String modificarDatos(String buscarPorId, String dato2, String dato3)
	{
		for(int indice=0; indice<lista.size();indice++)
		{
			if(lista.get(indice).getCodigo().equals(buscarPorId))
			{
				// SOLO CAMBIA nombre y cantidad, NO el numero de factura
				lista.get(indice).setCodigo(dato2);
				lista.get(indice).setNombre(dato2);
				return "Modificacion realizada exitosamente"; 
			}
		}
		return "No se encontro ninguna objeto con ese identificador"; 
	}
	//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	// Extra
	public String mostrarTodo()
	{
		String resultado = "";
		for(int indice=0; indice<lista.size();indice++)
		{
			RegistroObjeto registro = lista.get(indice);
			resultado += "Codigo: " + registro.getCodigo() + 
						" Nombre: " + registro.getNombre() + 
						" Carrera: " + registro.getCarrera() + "\n";
		}
		return resultado;
	}
}//Fin de la clase 
