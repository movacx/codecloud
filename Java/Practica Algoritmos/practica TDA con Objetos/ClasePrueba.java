import javax.swing.*;

public class ClasePrueba
{
    static byte opcion;
    public static void main(String[] args)
    {
        manejo_nodo_objeto nodoObjeto = new manejo_nodo_objeto();

        do {

            opcion = Byte.parseByte(JOptionPane.showInputDialog(null, "1. Registrar" + "\n2. Validar Existencia" + "\n3. Mostrar cantidad de Personas con la misma edad."
                    + "\n4. Mostrar cantidad de personas registradas" + "\n4. Mostrar Personas registradas" + "\n5. Eliminar la lista"));

            switch(opcion)
            {
                case 1:
                    int posicion = Integer.parseInt(JOptionPane.showInputDialog(null, "En que posicion desea insertar el nuevo registro?"));
                    String ced = JOptionPane.showInputDialog(null, "Ingrese la cedula: ");
                    String nom = JOptionPane.showInputDialog(null, "Ingrese el nombre ");
                    int edad = Integer.parseInt(JOptionPane.showInputDialog(null, "Ingrese la edad: "));
                    int exito = nodoObjeto.insertar(ced,nom,edad,posicion);
                    if(exito == 1)
                    {
                        JOptionPane.showMessageDialog(null,"Exito al registrar!");
                    }else{
                        JOptionPane.showMessageDialog(null,"No se pudo agregar!");
                    }
                    break;

                    //=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

                case 2:
                    String cedula = JOptionPane.showInputDialog(null, "Ingrese la cedula: ");
                    JOptionPane.showMessageDialog(null, nodoObjeto.validarExistencia(cedula));
                    break;

                    //=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

                case 3:
                    break;

                    //=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

                case 4:
                    break;
                case 5:
                    break;
                case 0:
                    JOptionPane.showMessageDialog(null, "Saliendo del sistema");
                    break;
            }
        }while(opcion !=0);


    }
}
