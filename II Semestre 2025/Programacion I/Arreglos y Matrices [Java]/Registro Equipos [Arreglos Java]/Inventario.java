import javax.swing.JOptionPane;
public class Inventario
{
	public static void main(String args[]){
		String placa,marca,modelo,accesorios,tipo;
		int indice;
		boolean estado;
		int opcion;
		Equipo equipo=  null;
		
		RegistroEquipos registro= new RegistroEquipos();
	
	
	do{
		opcion = Integer.parseInt(JOptionPane.showInputDialog("Seleccione una opcion:\n1. Registrar equipo\n2. Consultar Equipo por indice\n3. Consultar Equipos por tipo"+
	"\n4. Ver posición que ocupa un equipo\n5. Agregar nuevo accesorio\n6. Eliminar Equipo\n7. Ver listado general de equipos\n8. Salir"));
				
		switch(opcion){
			case 1:
				placa = JOptionPane.showInputDialog("Digite la placa");
				if(registro.verificarPlaca(placa)==false)
				{
					marca = JOptionPane.showInputDialog("Digite la marca");
					modelo = JOptionPane.showInputDialog("Digite el modelo");
					accesorios = JOptionPane.showInputDialog("Digite los accesorios");
					tipo = JOptionPane.showInputDialog("Digite el tipo de equipo");
					estado= Boolean.parseBoolean(JOptionPane.showInputDialog("Didite el estado del equipo"));
					
					equipo = new Equipo(placa, marca, modelo, accesorios,tipo,estado);
					indice = Integer.parseInt(JOptionPane.showInputDialog("Digite el indice a guardar el equipo"));
					if(registro.setEquipo(indice-1,equipo))
					{
						JOptionPane.showMessageDialog(null, "El equipo se ha agregado corectamente");
					}
					else
					{
						JOptionPane.showMessageDialog(null, "El equipo no se ha agregado \nLaposicion no se encuentra ocupada");
					}
				}else
				{
					JOptionPane.showMessageDialog(null, "Ya existe un equipo en la p´laca indicada");
				}
			
			break;

			case 2:
			
				indice= Integer.parseInt(JOptionPane.showInputDialog("Ya existe un equipo con la placa indicada"));
				if((indice-1>=0)&&(indice-1<registro.length()))
				{
					if(registro.getEquipo(indice-1)!=null)
					{
						JOptionPane.showMessageDialog(null, registro.getEquipo(indice-1));
					}
					else
					{
						JOptionPane.showMessageDialog(null, "En la posicion indicada no existe ningun equipo");
					}
				}
				else
				{
					JOptionPane.showMessageDialog(null, "Posicion fuera del tamaño del arreglo");
				}
			break;

			case 3:
				tipo= JOptionPane.showInputDialog("Digite el tipo de equipo para ver la informacion");
				
				if(registro.getEquipoTipo(tipo)=="")
				{
					JOptionPane.showMessageDialog(null, "No hay ningun equipo del tipo indicado");
				}
				else
				{
					JOptionPane.showMessageDialog(null, registro.getEquipoTipo(tipo));
				}
				
			break;

			case 4:
				placa= JOptionPane.showInputDialog("Digite la placa del equipo sobre el cual quiere saber la posicion");
				
				if(registro.getPosicionEquipo(placa)==-1)
				{
					JOptionPane.showMessageDialog(null, "Nohay ningun equipo con la placa indicada");
				}
				else
				{
					JOptionPane.showMessageDialog(null, "El equipo con la placa "+placa+" esta en la posicion"+(registro.getPosicionEquipo(placa)+1));
				}
			break;

			case 5:
				placa= JOptionPane.showInputDialog("Digite la placa del equipo sobre el cual quiere saber la posicion");	
				String nuevoAccesorio= JOptionPane.showInputDialog(null, "Digite el nuevo accesorio del equipo");
				
				if(registro.setNuevoAccesorio(placa, nuevoAccesorio))
				{
					JOptionPane.showMessageDialog(null, "Accesorio agregado correctamente");
				}
				else
				{
					JOptionPane.showMessageDialog(null, "No existe un equipo con la placa indicada");
				}
			break;

			case 6:
				placa= JOptionPane.showInputDialog("Digite la placa del equipo sobre el cual quiere saber la posicion");
				
				if(registro.removerEquipo(placa))
				{
					JOptionPane.showMessageDialog(null, "Equipo eliminado correctamenre");
				}
				else
				{
					JOptionPane.showMessageDialog(null, "No existe un equipo con la placa indicada");
				}
			break;

			case 7:
				JOptionPane.showMessageDialog(null, registro.getListadoEquipo());
			break;

			case 8:
				JOptionPane.showMessageDialog(null,"Saliendo del programa");
			break;	
			default:
				JOptionPane.showMessageDialog(null,"Error, debe seleccionar una opcion valida...");
			break;
			}
		
		}while(opcion!=8);
	
	}
}
