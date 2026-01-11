import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class listas extends JFrame
{
    JLabel campoDeTexto;
    public listas()
    {
        campoDeTexto = new JLabel("Malparido");
        setLayout(null);

        campoDeTexto.setBounds(100,10,100,100);
        add(campoDeTexto);
        setLocationRelativeTo(null);
        setVisible(true);
        setSize(300, 300);

    }
    public static void main(String []args)
    {
       listas miVentana = new listas();
       
    }
}