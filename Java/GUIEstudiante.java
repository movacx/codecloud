/*Herlin Fabian Chavarria Beita C5E187*/
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class GUIEstudiante extends JFrame
{
	JLabel lblCarnet, lblNombre, lblCarrera, lblPromedio;
	JTextField txtCarnet, txtNombre, txtCarrera, txtPromedio;
	JButton btnGuardar, btnBuscar, btnModificar, btnEliminar, btnLimpiar, btnSalir;
	
	ManejadorEventos manejador = new ManejadorEventos();
	Estudiante estudiantado = null;
	ManejoEstudiante vector = new ManejoEstudiante();
	
	public GUIEstudiante()
	{
		super("Ventana");
		
		lblCarnet = new JLabel("Carnet:");					
		lblNombre = new JLabel("Nombre:");					
		lblCarrera = new JLabel("Carrera:");					
		lblPromedio = new JLabel("Promedio:");				
		
		txtCarnet = new JTextField();					
		txtNombre = new JTextField();				
		txtCarrera = new JTextField();					
		txtPromedio = new JTextField();
		
		btnGuardar = new JButton("Guardar");					
		btnBuscar = new JButton("Buscar");				
		btnModificar = new JButton("Modificar");					
		btnEliminar = new JButton("Eliminar");
		btnLimpiar = new JButton("Limpiar");					
		btnSalir = new JButton("Salir");				

		setLayout(null); /* set.bounds(horizontal, vertical, alto, largo);*/
		
		lblCarnet.setBounds(30,10,150,30);					
		lblNombre.setBounds(30,50,150,30);				
		lblCarrera.setBounds(30,95,150,30);					
		lblPromedio.setBounds(30,139,150,30);	
		
		txtCarnet.setBounds(290,10,190,30);					
		txtNombre.setBounds(290,50,190,30);				
		txtCarrera.setBounds(290,95,190,30);					
		txtPromedio.setBounds(290,139,190,30);	
		
		btnGuardar.setBounds(30,200,90,30);					
		btnBuscar.setBounds(170,200,90,30);				
		btnModificar.setBounds(300,200,120,30);					
		btnEliminar.setBounds(450,200,90,30);	
		btnLimpiar.setBounds(300,250,90,30);					
		btnSalir.setBounds(450,250,90,30);
						
		add(lblCarnet);
		add(lblNombre);
		add(lblCarrera);
		add(lblPromedio);
		
		add(txtCarnet);
		add(txtNombre);
		add(txtCarrera);
		add(txtPromedio);
		
		add(btnGuardar);
		add(btnBuscar);
		add(btnModificar);
		add(btnEliminar);
		add(btnLimpiar);
		add(btnSalir);
		
		btnGuardar.addActionListener(manejador);
		btnBuscar.addActionListener(manejador);
		btnModificar.addActionListener(manejador);
		btnEliminar.addActionListener(manejador);
		btnLimpiar.addActionListener(manejador);
		btnSalir.addActionListener(manejador);
		
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setLocationRelativeTo(null);
		setSize(600,400);
		setVisible(true);
		
	}
	
	private class ManejadorEventos implements ActionListener
	{

		
		public void actionPerformed(ActionEvent evento)
		{
			/****************************************************************************************************************/
			if(evento.getActionCommand().equals("Guardar"))
			{
				if(txtCarnet.getText().isEmpty() != true && txtNombre.getText().isEmpty() != true)
				{
					String carnet = txtCarnet.getText();
					String nombreEstudiante = txtNombre.getText();
					String carrera = txtCarrera.getText();
					double promedio = Double.parseDouble(txtPromedio.getText());
					
					Estudiante estudiantado = new Estudiante(carnet, nombreEstudiante, carrera, promedio);
					vector.agregarEstudiante(estudiantado);
					vaciarCampos();
					JOptionPane.showMessageDialog(null, "Guardado con exito!");
					
					
				}else{
					JOptionPane.showMessageDialog(null, "Debe de llenar todos los cuadros antes de guardar");
				}
			}/*fin boton guardar*/
			
			
			
			
			/****************************************************************************************************************/
				if(evento.getActionCommand().equals("Buscar")) 
				{
					String carnet = txtCarnet.getText();

					if(carnet.isEmpty())
					{
						JOptionPane.showMessageDialog(null, "Debe de ingresar un numero de carnet para poder buscar");
					}
					else
					{
						Estudiante estudiantado = vector.buscarEstudiante(carnet);

						if(estudiantado != null)
						{
							cargarDatos();
							bloquearCampos(0);
						}
						else
						{
							JOptionPane.showMessageDialog(null, "No existe un estudiante con ese carnet");
						}
					}
				}//fin del boton buscar
			/****************************************************************************************************************/
			if(evento.getSource() == btnModificar)
			{
				if(txtCarnet.getText().isEmpty())
				{
					JOptionPane.showMessageDialog(null, "Debe de ingresar un numero de carnet");
				}
				else
				{
					
					// Verificar que todos los campos estén llenos
					if(!validarEspacios())
					{
						JOptionPane.showMessageDialog(null, "Carnet encontrado, se cargaran los datos antes de la modificacion, al finalizar ");
						txtCarnet.setEditable(false);
						cargarDatos();
						return;
					}
					

					
					String carnetBuscar = txtCarnet.getText();
					String modificarNombre = txtNombre.getText();
					String modificarCarrera = txtCarrera.getText();
					double modificarPromedio = Double.parseDouble(txtPromedio.getText());
					
					// Modificar directamente
					String resultado = vector.modificarDatos(carnetBuscar, modificarNombre, modificarCarrera, modificarPromedio);
					JOptionPane.showMessageDialog(null, resultado);
					
					bloquearCampos(1);
					vaciarCampos();
				}
			}
			/****************************************************************************************************************/

			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
				/****************************************************************************************************************/
				if(evento.getActionCommand().equals("Eliminar"))
				{
					
					int c = Integer.parseInt(JOptionPane.showInputDialog(null, "¿Esta seguro de eliminar el registro?\n"
					+"1. Si "
					+"\n2. No"));
					if(c == 1)
					{
						String eliminarCarnet = txtCarnet.getText();
						vector.eliminarEstudiante(eliminarCarnet);
					}else{
					}
					
					
				}//fin del boton eliminar 
				/****************************************************************************************************************/
				if(evento.getActionCommand().equals("Salir"))
				{
					System.exit(0);
				}
				/****************************************************************************************************************/
				if(evento.getActionCommand().equals("Limpiar"))
				{
					bloquearCampos(1);
					vaciarCampos();
				}
				/****************************************************************************************************************/

				
		}
		
		

		
		
		
	/***************************** Metodos propios *****************************************/
		public boolean validarEspacios()
		{
			 /*vacio es true y lleno es false;*/
			boolean validarEspacios = true;
			
			if(txtCarnet.getText().isEmpty())
			{
				validarEspacios = false;
			}
			if(txtNombre.getText().isEmpty())
			{
				validarEspacios = false;
			}
			if(txtCarrera.getText().isEmpty())
			{
				validarEspacios = false;
			}
			if(txtPromedio.getText().isEmpty())
			{
				validarEspacios = false;
			}
			return validarEspacios;
		
		}
		
		
		public void cargarDatos()
		{
			String buscarCarnet = txtCarnet.getText();
			Estudiante estudiantado = vector.buscarEstudiante(buscarCarnet);
			txtCarnet.setText(estudiantado.getCarnet());
			txtNombre.setText(estudiantado.getNombreEstudiante());
			txtCarrera.setText(estudiantado.getCarrera());
			txtPromedio.setText(String.valueOf(estudiantado.getPromedio()));
			
		}
		
		
		public void vaciarCampos()
		{
			txtCarnet.setText("");
			txtNombre.setText("");
			txtCarrera.setText("");
			txtPromedio.setText("");
		}
		
		public void bloquearCampos(int indice)
		{
			if(indice == 0 )
			{
				txtCarnet.setEditable(false);
				txtNombre.setEditable(false);
				txtCarrera.setEditable(false);
				txtPromedio.setEditable(false);
			}else 
			{
				txtCarnet.setEditable(true);
				txtNombre.setEditable(true);
				txtCarrera.setEditable(true);
				txtPromedio.setEditable(true);
			}
		}
		
		
		
		
		
	}
	
	
	public static void main(String []args)
	{
		GUIEstudiante ventana = new GUIEstudiante();
	}
	
	
}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	





























































































































	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	






































	
	
	
	
	
	
	
	
	
	
































































