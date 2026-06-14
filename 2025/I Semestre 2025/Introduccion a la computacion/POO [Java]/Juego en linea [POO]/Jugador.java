public class Jugador {
    private String nickname;
    private int puntuacion;

    public Jugador(String nickname) {
        this.nickname = nickname;
        this.puntuacion = 0;
    }

    public String getNickname() {
        return nickname;
    }

    public void setNickname(String nickname) {
        this.nickname = nickname;
    }

    public int getPuntuacion() {
        return puntuacion;
    }

    public void aumentarPuntuacion(int puntos) {
        this.puntuacion += puntos;
    }

    @Override
    public String toString() {
        return "Jugador: " + nickname + " | Puntuación: " + puntuacion;
    }
}
