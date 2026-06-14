import javax.swing.JOptionPane; // ¡Siempre necesitamos importar JOptionPane!

public class GestionLibrosApp {

    public static void main(String[] args) {

        // --- Paso 1: Crear un objeto Libro ---
        // Vamos a crear un libro de ejemplo directamente para empezar.
        // Después, podrías pedirle los datos al usuario si quieres.
        Libro miLibro = new Libro("El Principito", "Antoine de Saint-Exupéry", 96);
        Libro miLibro2 = new Libro("El movacxvives", "fabian beita", 23);

        JOptionPane.showMessageDialog(null, "¡Bienvenido a la gestión de un libro!", "Inicio", JOptionPane.INFORMATION_MESSAGE);

        // --- Paso 2: Mostrar el estado inicial del libro ---
        JOptionPane.showMessageDialog(null, "Información del libro actual:\n" + miLibro.toString(), "Estado del Libro", JOptionPane.INFORMATION_MESSAGE);
        JOptionPane.showMessageDialog(null, "Información del libro actual:\n" + miLibro2.toString(), "Estado del Libro", JOptionPane.INFORMATION_MESSAGE);

        // --- Paso 3: Preguntarle al usuario qué quiere hacer con el libro ---
        String opcionElegida = "";
        do {
            opcionElegida = JOptionPane.showInputDialog(null,
                                            "¿Qué desea hacer con el libro \"" + miLibro.getTitulo() + "\"?\n" +
                                            "1. Prestar\n" +
                                            "2. Devolver\n" +
                                            "3. Ver estado\n" +
                                            "4. Salir",
                                            "Menú de Opciones",
                                            JOptionPane.QUESTION_MESSAGE);

            // Manejamos lo que el usuario ingresó
            if (opcionElegida == null) { // Si el usuario presiona Cancelar o cierra la ventana
                opcionElegida = "4"; // Tratamos como si quisiera salir
            }

            switch (opcionElegida) {
                case "1":
                    // Llama al método prestar() de tu objeto miLibro
                    miLibro.prestar();
                    // Después de la acción, volvemos a mostrar el estado actualizado
                    JOptionPane.showMessageDialog(null, "El libro ha intentado ser prestado. Estado actual:\n" + miLibro.toString(), "Resultado Prestar", JOptionPane.INFORMATION_MESSAGE);
                    break;
                case "2":
                    // Llama al método devolver() de tu objeto miLibro
                    miLibro.devolver();
                    // Después de la acción, volvemos a mostrar el estado actualizado
                    JOptionPane.showMessageDialog(null, "El libro ha intentado ser devuelto. Estado actual:\n" + miLibro.toString(), "Resultado Devolver", JOptionPane.INFORMATION_MESSAGE);
                    break;
                case "3":
                    // Solo muestra el estado actual del libro
                    JOptionPane.showMessageDialog(null, "Información actual del libro:\n" + miLibro.toString(), "Estado del Libro", JOptionPane.INFORMATION_MESSAGE);
                    break;
                case "4":
                    JOptionPane.showMessageDialog(null, "¡Gracias por usar la aplicación de gestión de libros! ¡Hasta pronto!", "Adiós", JOptionPane.INFORMATION_MESSAGE);
                    break;
                default:
                    // Si el usuario ingresa algo diferente a 1, 2, 3 o 4
                    JOptionPane.showMessageDialog(null, "Opción no válida. Por favor, ingrese 1, 2, 3 o 4.", "Error", JOptionPane.ERROR_MESSAGE);
                    break;
            }

        } while (!opcionElegida.equals("4")); // El bucle continúa mientras la opción no sea "4" (Salir)

    } // fin main

} // fin clase GestionLibrosApp
