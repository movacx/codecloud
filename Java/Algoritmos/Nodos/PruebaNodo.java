import javax.swing.JOptionPane;
public class PruebaNodo {
    
    

    
    public static void main(String args[]) {
        int v1 = 1, v2 = 2, v3 = 3, v4 = 4;
        int v100 = 100;

        Nodo n1 = new Nodo(v1);
        Nodo n2 = new Nodo(v2);
        Nodo n3 = new Nodo(v3);
        Nodo n4 = new Nodo(v4);


        n1.setSiguiente(n2);
        n2.setSiguiente(n3); 
        n3.setSiguiente(n4); 

        Nodo aux = n1;
       

        while (aux != null) {
            String carga = String.valueOf(aux.getDato());
            System.out.println(carga);
            aux = aux.getSiguiente();
        }
    }
      
}
