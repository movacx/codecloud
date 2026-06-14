import javax.swing.JOptionPane;

public class Juego {
    private Jugador jugador1;
    private Jugador jugador2;

    public static void main(String args[]) {
        new Juego();
    }

    /* constructor construlle el juego */
    public Juego() {
        String nick1 = JOptionPane.showInputDialog("Ingrese el nickname del Jugador 1:");
        String nick2 = JOptionPane.showInputDialog("Ingrese el nickname del Jugador 2:");

        jugador1 = new Jugador(nick1);
        jugador2 = new Jugador(nick2);

        menu();
    }

    public void menu() {
        int opcion;
        do {
            opcion = Integer.parseInt(JOptionPane.showInputDialog(
                "🎮 MENÚ DEL JUEGO MULTIJUGADOR 🎮\n" +
                "1. Jugar\n" +
                "2. Ver puntajes\n" +
                "3. Cambiar nickname\n" +
                "4. Salir"));

            switch (opcion) {
                case 1:
                    jugar();
                    break;
                case 2:
                    verPuntajes();
                    break;
                case 3:
                    cambiarNickname();
                    break;
                case 4:
                    JOptionPane.showMessageDialog(null, "Gracias por jugar. ¡Hasta pronto!");
                    break;
                default:
                    JOptionPane.showMessageDialog(null, "Opción no válida.");
            }
        } while (opcion != 4);
    }

    public void jugar() {
        int puntos1 = (int)(Math.random() * 10 + 1);
        int puntos2 = (int)(Math.random() * 10 + 1);

        jugador1.aumentarPuntuacion(puntos1);
        jugador2.aumentarPuntuacion(puntos2);

        String mensaje = jugador1.getNickname() + " gana " + puntos1 + " puntos.\n" +
                         jugador2.getNickname() + " gana " + puntos2 + " puntos.";

        JOptionPane.showMessageDialog(null, mensaje);
    }

    public void verPuntajes() {
        JOptionPane.showMessageDialog(null,
            "📊 Puntajes actuales 📊\n" +
            jugador1.toString() + "\n" +
            jugador2.toString());
    }

    public void cambiarNickname() {
        String nuevoNickJugador1 = JOptionPane.showInputDialog("Nuevo nickname para " + jugador1.getNickname() + ":");
        jugador1.setNickname(nuevoNickJugador1);

        String nuevoNickJugador2 = JOptionPane.showInputDialog("Nuevo nickname para " + jugador2.getNickname() + ":");
        jugador2.setNickname(nuevoNickJugador2);

        JOptionPane.showMessageDialog(null, "Nicknames actualizados.");
    }
}
