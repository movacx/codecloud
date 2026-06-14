import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class GUIGestionEstudiantes extends JFrame
{
	/***************************************************/
	JLabel lblCodigo, lblNombre, lblEdad, lblSemestre, lblCarrera, lblIngresoDatos, lblBusquedaYFiltros, lblListaEstudiantes;
	JTextField txtCodigo, txtNombre, txtEdad;
	JButton btnAgregar, btnLimpiar, btnBuscar, btnAplicar, btnEliminar, btnExportar, btnModificar;
	JRadioButton rb1, rb2, rb3, rb4,rb5,rb6,rb7,rb8;
	JCheckBox chBecado, chMonitor;
	JComboBox <String> jcCarrera;				/*"|"*/		String vector[] = {"I. Informatica", "II. Gestion Cultural", "III. Administracion de empresas"};
	JMenu jmArchivo, jmEditar, jmReportes, jmAyuda;
	JMenuItem itemNuevo, itemSalir;
	
	
	
	/***************************************************/
	ButtonGroup grupoBotones  = new ButtonGroup();
	JMenuBar barra = new JMenuBar();
	RegistroObjeto registro = null;
	VectorRegistro lista = new VectorRegistro();
	ManejoEventos manejador = new ManejoEventos();

	public GUIGestionEstudiantes()
	{
		super("Sistema Gestion Estudiantes");
		/************************************************[ Establecer parametros ]*************************************************/
		/*JMenu*/			
		jmArchivo = new JMenu("Archivo");												/*JCheckBox*/
		jmEditar = new JMenu("Editar");													chBecado = new JCheckBox("Becado");
		jmReportes = new JMenu("Reportes");												chMonitor = new JCheckBox("Monitor");
		jmAyuda = new JMenu("Ayuda");
		itemNuevo = new JMenuItem("Nuevo");
		itemSalir = new JMenuItem("Salir");
		
		/*Jlabel*/																		/*TextField*/
		lblIngresoDatos = new JLabel("INGRESO DE DATOS");								txtCodigo = new JTextField(20);
		lblCodigo = new JLabel("Codigo:");												txtNombre = new JTextField(20);
		lblNombre = new JLabel("Nombre:");												txtEdad = new JTextField(20);
		lblEdad = new JLabel("Edad:");													
		lblSemestre = new JLabel("Semestre:");
		lblCarrera = new JLabel("Carrera:");
		
		/*JButton*/																		/*RadioButton*/
		/*btnAgregar = new JButton("Agregar");*/										rb1 = new JRadioButton("1");		
		btnLimpiar = new JButton("Limpiar");											rb2 = new JRadioButton("2");		
		btnBuscar = new JButton("Buscar");  											rb3 = new JRadioButton("3");		
		btnAplicar = new JButton("Aplicar");											rb4 = new JRadioButton("4");				
		btnEliminar = new JButton("Eliminar");											rb5 = new JRadioButton("5");
		btnExportar = new JButton("Exportar");											rb6 = new JRadioButton("6");
		btnAgregar = new JButton("Agregar");											rb7 = new JRadioButton("7");
		btnModificar = new JButton("Modificar");
		/*JComboBox*/
		jcCarrera = new JComboBox<>(vector);
		
		
		JLabel lineaDos = new JLabel("_______________________________________________________________________________________________________");														
		/***********************************************[ Establecer Coordenadas ]*************************************************/
		setLayout(null);//Horizontal, vertical, largo, alto
		lblIngresoDatos.setBounds(20,0,150,30);
		
		//lineaUno.setBounds(20,140,900,30);
		/*Etiquetas*/											/*Campos de texto*/
		lblCodigo.setBounds(20,30,150,30);						txtCodigo.setBounds(100,35,150,25);
		lblNombre.setBounds(20,60,150,30);						txtNombre.setBounds(100,65,150,25);
		lblEdad.setBounds(20,90,160,30);						txtEdad.setBounds(100,95,150,25);
		lblSemestre.setBounds(20,120,150,30);					jcCarrera.setBounds(350,30,150,30);
		lblCarrera.setBounds(287,30,150,30);
		/*RadioButton*/											/*CheckBox*/
		rb1.setBounds(100,125,33,20);							chBecado.setBounds(300,90,70,20);
		rb2.setBounds(135,125,33,20);							chMonitor.setBounds(380,90,100,20);
		rb3.setBounds(167,125,33,20);										
		rb4.setBounds(197,125,33,20);
		rb5.setBounds(227,125,33,20);
		rb6.setBounds(257,125,33,20);
		rb7.setBounds(287,125,33,20);
		
		lineaDos.setBounds(20,5,900,30);
		
		/*JButton*/
		btnAgregar.setBounds(20,160,100,30);
		btnBuscar.setBounds(125,160,100,30);
		btnModificar.setBounds(230,160,100,30);
		btnLimpiar.setBounds(335,160,100,30);
		btnEliminar.setBounds(440,160,100,30);
		
		/************************************************[ Añadir a la interfaz ]*************************************************/
		/*add(JMenu)*/										/*add(JLabel)*/
		barra.add(jmArchivo);								add(lblIngresoDatos);			
		barra.add(jmEditar);								add(lblCodigo);	
		barra.add(jmReportes);								add(lblNombre);	
		barra.add(jmAyuda);									add(lblEdad);	
		jmArchivo.add(itemNuevo);							add(lblSemestre);
		jmArchivo.addSeparator();							add(lblCarrera);
		jmArchivo.add(itemSalir);							
		setJMenuBar(barra);
		
		/*add(JRadioButton)*/								/*add(JTextField)*/
		add(rb1);											add(txtEdad);
		add(rb2);											add(txtCodigo);
		add(rb3);											add(txtNombre);
		add(rb4);											
		add(rb5);
		add(rb6);											/*add(JComboBox)*/
		add(rb7);											add(jcCarrera);
		
		/*add(JCheckBox*/									/*add(Lineas);*/
		add(chBecado);										//add(lineaUno);
		add(chMonitor);										add(lineaDos);
		
		/*add(JButton)*/									/*ButtonGroup.add(JRadioButton)*/
		add(btnAgregar);									grupoBotones.add(rb1);
		add(btnModificar);									grupoBotones.add(rb2);
		add(btnBuscar);										grupoBotones.add(rb3);
		add(btnLimpiar);									grupoBotones.add(rb4);
		add(btnEliminar);									grupoBotones.add(rb5);
															grupoBotones.add(rb6);
															grupoBotones.add(rb7);
		/*variable.addActionListener(manejador);*/													
		btnAgregar.addActionListener(manejador);
		btnBuscar.addActionListener(manejador);
		btnModificar.addActionListener(manejador);
		btnLimpiar.addActionListener(manejador);
		btnEliminar.addActionListener(manejador);
		itemSalir.addActionListener(manejador);
		itemNuevo.addActionListener(manejador);
		/*************************************************[ Establecer Ventana ]*************************************************/
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setLocationRelativeTo(null);
		setSize(550,250);
		setVisible(true);

	}//Fin Constructor
	
	private class ManejoEventos implements ActionListener
	{
		public void actionPerformed(ActionEvent evento)
		{
			if(evento.getSource() == btnAgregar)
			{
				if(txtCodigo.getText().isEmpty()!=true && txtNombre.getText().isEmpty() != true && txtEdad.getText().isEmpty()!=true)
				{
					
					String codigo = txtCodigo.getText();
					String nombre = txtNombre.getText();
					int edad = Integer.parseInt(txtEdad.getText());
					String obtenerCarrera = (String) jcCarrera.getSelectedItem();
					int semestre = recorrerBotones();
					String tipoEstudiante = tipoEstudiante();
					
					RegistroObjeto registro = new RegistroObjeto(codigo, nombre, edad, obtenerCarrera, semestre, tipoEstudiante);
					
					lista.guardarObjeto(registro);
					JOptionPane.showMessageDialog(null, "Guardado con exito\n" + registro);
					vaciarCampos();
					
				}else{
					JOptionPane.showMessageDialog(null, "Debe de rellenar los campos antes de guardar");
				}
				
			}
	/*-----------------------------------------------------------------------------------------------------------------------*/
			if(evento.getSource() == btnBuscar)
			{
				if(txtCodigo.getText().isEmpty() != true)
				{
					String codigo = txtCodigo.getText(); /*Estoy haciendo un test para guardar asi no permita guardar un estudiante con el mismo codigo*/
					
					if(lista.verificarId(codigo) == false)
					{
						JOptionPane.showMessageDialog(null, "No existe un estudiante con ese mismo codigo");
					}else{
						RegistroObjeto registro = lista.buscarObjeto(txtCodigo.getText());
						JOptionPane.showMessageDialog(null, "Existe");
						/*Actualizar Campos de texto*/
						txtCodigo.setText(registro.getCodigo());
						txtNombre.setText(registro.getNombre());
						txtEdad.setText(String.valueOf(registro.getEdad()));
						/*Actualizar /*JComboBox*/
						jcCarrera.setSelectedItem(registro.getCarrera());
						/*Actualizar JCheckList*/
						String tipo = registro.getTipo();
						chBecado.setSelected(tipo.equalsIgnoreCase("Becado"));
						chMonitor.setSelected(tipo.equalsIgnoreCase("Monitor"));
						/*Actualizar RadioButton*/
						establecerBotones(registro.getSemestre());
						bloquearCampos(0);
					}
				}else{
					JOptionPane.showMessageDialog(null, "Debe de ingresar un numero de Carnet");
				}
			}
	/*-----------------------------------------------------------------------------------------------------------------------*/
			if(evento.getSource() == btnModificar)
			{
				JOptionPane.showMessageDialog(null, "modificar");
			}//Fin modificar | Es facil lo hago luego me interesa mas como agregar una segunda ventana en el itemNuevo
	/*-----------------------------------------------------------------------------------------------------------------------*/
			if(evento.getSource() == btnLimpiar)
			{
				vaciarCampos();
				bloquearCampos(1);
			}//Fin Limpiar
	/*-----------------------------------------------------------------------------------------------------------------------*/
			if(evento.getSource() == btnEliminar)
			{
				JOptionPane.showMessageDialog(null, "Eliminar");
			}
	/*-----------------------------------------------------------------------------------------------------------------------*/
			if(evento.getSource() == itemSalir)
			{
				int opcion = JOptionPane.showConfirmDialog(null, "Desea salir del programa?", "Salida", JOptionPane.YES_NO_OPTION);
				if(opcion == JOptionPane.YES_OPTION)
				{
					System.exit(0);
				}else{
					
				}
			}
	/*-----------------------------------------------------------------------------------------------------------------------*/
			if(evento.getSource() == itemNuevo)
			{
				JFrame ventanaNueva = new JFrame("Ventana Secundaria");
				JLabel obtenerNombreTest = new JLabel("Nombre");
				JTextField txtObtenerObjeto = new JTextField();
				ventanaNueva.setLayout(null);
				obtenerNombreTest.setBounds(20,30,90,30);						txtObtenerObjeto.setBounds(100,35,90,25);
				
				
				//txtObtenerObjeto.setText(registro.getNombre());
				
				ventanaNueva.setLocationRelativeTo(null);
				ventanaNueva.setSize(550,220);
				ventanaNueva.setVisible(true);
			
				ventanaNueva.add(obtenerNombreTest);
				ventanaNueva.add(txtObtenerObjeto);
			}
			
		}//Fin ActionPerformed
		
		/*************************************************[ Metodos Propios ]*************************************************/
		private void vaciarCampos()
		{
			txtCodigo.setText("");
			txtNombre.setText("");
			txtEdad.setText("");
			
			grupoBotones.clearSelection();
			
			chMonitor.setSelected(false);
			chBecado.setSelected(false);

			jcCarrera.setSelectedIndex(0);
			
		}
		/****************************************************************************************/
		private int recorrerBotones()
		{
			JRadioButton botones[] = {rb1, rb2, rb3, rb4,rb5,rb6,rb7};
			for(int indice = 0; indice < botones.length; indice++)
			{
				if(botones[indice].isSelected())
				{
					return indice + 1;
				}
			}
			rb1.setSelected(true);
			return 1;
		}
		/****************************************************************************************/
		private void bloquearBotones()
		{
			JRadioButton botones[] = {rb1, rb2, rb3, rb4, rb5, rb6, rb7};
			for(int indice = 0; indice < botones.length; indice++)
			{
					botones[indice].setEnabled(false);

			}
		}
		/****************************************************************************************/
		private void desbloquearBotones()
		{
			JRadioButton botones[] = {rb1, rb2, rb3, rb4, rb5, rb6, rb7};
			for(int indice = 0; indice < botones.length; indice++)
			{
					botones[indice].setEnabled(true);
			}
		}
		/****************************************************************************************/
		private void establecerBotones(int numeroSemestre)
		{
			JRadioButton botones[] = {rb1, rb2, rb3, rb4,rb5,rb6,rb7};
			if(numeroSemestre >= 0 && numeroSemestre <= botones.length)
			{
				grupoBotones.clearSelection();
				botones[numeroSemestre -1].setSelected(true);
			}
		}
		/****************************************************************************************/
		private String tipoEstudiante()
		{
			String mensaje = "";
			if(chBecado.isSelected())
			{
				return mensaje += "Becado";
			}
			if(chMonitor.isSelected())
			{
				return mensaje += "Monitor";
			}
			return "Estudiante";
		}
		/****************************************************************************************/
		public void bloquearCampos(int id)
		{
			if(id ==0)
			{
				/*Bloquear Campos de texto*/
				txtCodigo.setEditable(false);
				txtNombre.setEditable(false);
				txtEdad.setEditable(false);
				/*Bloquear /*JComboBox*/
				jcCarrera.setEnabled(false);
				/*Bloquear JCheckList*/
				chBecado.setEnabled(false);
				chMonitor.setEnabled(false);
				/*Bloquear RadioButton*/
				bloquearBotones();
			}else{
				/*Bloquear Campos de texto*/
				txtCodigo.setEditable(true);
				txtNombre.setEditable(true);
				txtEdad.setEditable(true);
				/*Bloquear /*JComboBox*/
				jcCarrera.setEnabled(true);
				/*Bloquear JCheckList*/
				chBecado.setEnabled(true);
				chMonitor.setEnabled(true);
				/*Bloquear RadioButton*/
				desbloquearBotones();
			}
		}
		/****************************************************************************************/
		
		
	}//Fin clase Interna
	
	

	
	


	public static void main(String []args)
	{
		GUIGestionEstudiantes ventana = new GUIGestionEstudiantes();
	}
}
