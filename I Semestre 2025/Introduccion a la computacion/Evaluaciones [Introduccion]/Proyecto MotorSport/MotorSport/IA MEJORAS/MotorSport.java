import javax.swing.JOptionPane;
import java.util.Random;
public class MotorSport {
    // --- Atributos de la Clase (Variables de Instancia) ---
    // Objetos principales
    private Usuario jugadorUno, jugadorDos, jugadorTres, jugadorCuatro;
    private Carro vehiculoUno, vehiculoDos, vehiculoTres, vehiculoCuatro;
    private TallerDeMejoras configCarUno, configCarDos, configCarTres, configCarCuatro;
    // Variables para datos de usuario/juego (String para inputs)
    private String ingresoPrimerJugador, ingresoSegundoJugador, ingresoTercerJugador, ingresoCuartoJugador;
    private String nombreDeUsuario; // Guarda el nombre del usuario con el que Gabriela/Cristopher interactúan
    private String nacionalidad;    // Guarda la nacionalidad del usuario actual
    private int edad;               // Guarda la edad del usuario actual
    // Variables de control de flujo y opciones de menú
    private int rentCar, modeloRentCar, menuRegistroUsuario, opcionRentCar, registrarAuto;
    private int cantidadJugadores;      // Cuántos jugadores se registraron
    private byte opcionTaller;          // Opción del menú principal del taller
    private byte opcionMenu;            // Opción del menú principal del juego
    private int subOpcion;              // Subopción dentro de los menús del taller
    private int seleccionUsuarios;      // Para seleccionar qué usuario tunear en Gabriela
    // Variables para estadísticas o cálculos (asegúrate de usarlas si las declaras)
    private double sumaVelocidad, sumaFrenado, sumaManejo, sumaAceleracion;
    // --- Método Main: Punto de entrada del programa ---
    public static void main(String[] args) {
        new MotorSport(); // Crea una instancia de MotorSport y llama a su constructor
    } // Fin main
    // --- Constructor de la Clase MotorSport ---
    // Aquí es donde se inicializan los atributos de la clase
    public MotorSport() {
        // --- 1. Inicialización de Objetos de Carro y TallerDeMejoras ---
        // ¡¡ESTO ES CLAVE PARA EVITAR EL NullPointerException!!
        // Siempre instanciá tus objetos antes de usarlos.
        this.vehiculoUno = new Carro();
        this.vehiculoDos = new Carro();
        this.vehiculoTres = new Carro();
        this.vehiculoCuatro = new Carro();
        this.configCarUno = new TallerDeMejoras();
        this.configCarDos = new TallerDeMejoras();
        this.configCarTres = new TallerDeMejoras();
        this.configCarCuatro = new TallerDeMejoras();
        // Los objetos 'Usuario' (jugadorUno, etc.) se inicializarán
        // dentro de los métodos 'usuarioUno()', etc., después de que el usuario
        // ingrese sus datos. Aquí solo se declaran como atributos de instancia.
        // --- 2. Llamada a Métodos Iniciales ---
        login();      // Primero el login para obtener datos de jugadores
        menuPrincipal(); // Luego el menú principal del juego
        // --- 3. Mensajes de Depuración/Finalización ---
        System.out.println("\nDespués de mejorar:");
        // Asegurate que los métodos toString() de Carro estén bien implementados para ver la info.
        System.out.println(vehiculoUno + "\n" + vehiculoDos + "\n" + vehiculoTres + "\n" + vehiculoCuatro);
        // Muestra la configuración del primer carro.
        // Asegurate que el método toString() de TallerDeMejoras esté bien implementado.
        JOptionPane.showMessageDialog(null, configCarUno);
    }
    // --- Métodos de la Clase ---
    public void login() {
        String inputCantidadJugadoresStr; // Declaración de variable de String para input
        int tempCantidadJugadores; // Variable temporal para la conversión
        do {
            inputCantidadJugadoresStr = JOptionPane.showInputDialog(
                null,
                "¿Cuántas personas van a ingresar al evento de Racing Sport?"
            );

            tempCantidadJugadores = Integer.parseInt(inputCantidadJugadoresStr);
            if (tempCantidadJugadores > 4 || tempCantidadJugadores < 1) {
                JOptionPane.showMessageDialog(null, "El límite de Jugadores permitidos es de 4 (mínimo 1).", "Error", JOptionPane.ERROR_MESSAGE);
                cantidadJugadores = 0; // Para que el bucle se repita
            } else {
                cantidadJugadores = tempCantidadJugadores; // Asigna el valor validado
            }
        } while (cantidadJugadores > 4 || cantidadJugadores < 1);
        JOptionPane.showMessageDialog(null, "🧑Organizador del evento: ¿Cómo están, amigos? Mi nombre es Cristopher, imagino que vienen a participar en el evento de Racing Sport."
            + "\n🧑Cristopher: Por favor, escriban su nombre en esta libreta para continuar con el evento.");
        // Lógica de registro de usuarios usando if (porque se ejecutan secuencialmente si cumplen la condición).
        if (cantidadJugadores >= 1) {
            ingresoPrimerJugador = JOptionPane.showInputDialog("🏁 Bienvenido a Racing Sport🏁 \n¿Como te llamas (Jugador 1)?: ");
            usuarioUno(); // Llama al método de registro/configuración para el Jugador 1
        }
        if (cantidadJugadores >= 2) {
            ingresoSegundoJugador = JOptionPane.showInputDialog("🏁 Bienvenido a Racing Sport🏁 \n¿Como te llamas (Jugador 2)?: ");
            usuarioDos(); // Llama al método de registro/configuración para el Jugador 2
        }
        if (cantidadJugadores >= 3) {
            ingresoTercerJugador = JOptionPane.showInputDialog("🏁 Bienvenido a Racing Sport🏁 \n¿Como te llamas (Jugador 3)?: ");
            usuarioTres(); // Llama al método de registro/configuración para el Jugador 3
        }
        if (cantidadJugadores == 4) { // Solo si son 4 jugadores, pedir el cuarto
            ingresoCuartoJugador = JOptionPane.showInputDialog("🏁 Bienvenido a Racing Sport🏁 \n¿Como te llamas (Jugador 4)?: ");
            usuarioCuatro(); // Llama al método de registro/configuración para el Jugador 4
        }
        estadisticas();
    } // Fin Login
    public void usuarioUno() {
        String inputMenuRegistroUsuarioStr;
        String inputEdadStr;
        int tempMenuRegistroUsuario; // Variable temporal para la conversión de menuRegistroUsuario
        do {
            inputMenuRegistroUsuarioStr = JOptionPane.showInputDialog(
                null,
                "Bienvenido " + (ingresoPrimerJugador != null ? ingresoPrimerJugador : "Jugador 1") + " a \"Racing Sport\""
                + "\nSeleccione una opcion: "
                + "\n 1. Registro"
                + "\n 2. Seleccion de vehiculos"
                + "\n 3. Continuar"
            );
            if (inputMenuRegistroUsuarioStr == null) {
                menuRegistroUsuario = 3; // Asumimos que si cancela, quiere continuar
                JOptionPane.showMessageDialog(null, "Operación cancelada. Continuando.");
            } else {
                tempMenuRegistroUsuario = Integer.parseInt(inputMenuRegistroUsuarioStr);
                menuRegistroUsuario = tempMenuRegistroUsuario; // Asigna el valor validado
            }
            switch (menuRegistroUsuario) {
                case 1:
                    nombreDeUsuario = JOptionPane.showInputDialog(null, "Digite su nombre:"); // Usar null para centrar
                    if (nombreDeUsuario == null) { nombreDeUsuario = ""; } // Manejar cancelación
                    inputEdadStr = JOptionPane.showInputDialog(null, "Digite su Edad:");
                    if (inputEdadStr == null) { inputEdadStr = "0"; } // Manejar cancelación
                    edad = Integer.parseInt(inputEdadStr);
                    nacionalidad = JOptionPane.showInputDialog(null, "Digite su nacionalidad:");
                    if (nacionalidad == null) { nacionalidad = ""; } // Manejar cancelación
                    // Crea la instancia de Usuario aquí, con los datos ingresados
                    // Se usa nombreDeUsuario para crear el objeto, que puede ser distinto a ingresoPrimerJugador si el usuario lo cambia.
                    jugadorUno = new Usuario(nombreDeUsuario, nacionalidad, edad, 0, 0);
                    JOptionPane.showMessageDialog(null, "¡Registro de " + jugadorUno.getNombreDeUsuario() + " completado!"); // Usar getNombreDeUsuario()
                    break;
                case 2:
                    rentCar = JOptionPane.showConfirmDialog(null, "¿Desea rentar un vehiculo?", "Racing Sport", JOptionPane.YES_NO_OPTION);
                    if (rentCar == JOptionPane.YES_OPTION) { // rentCar == 0
                        wangCars(1); // Llama el metodo de renta
                    } else if (rentCar == JOptionPane.NO_OPTION) { // rentCar == 1
                        registrarAuto = JOptionPane.showConfirmDialog(null, "🧑Christopher: Veo que tienes un auto. ¿Acaso ese es el que deseas registrar? ", "Organizador del Evento: Cristopher", JOptionPane.YES_NO_OPTION);
                        if (registrarAuto == JOptionPane.YES_OPTION) { // registrarAuto == 0
                            registrarVehiculo(1); // Llama el metodo de registrar vehiculo
                        } else if (registrarAuto == JOptionPane.NO_OPTION) { // registrarAuto == 1
                            JOptionPane.showMessageDialog(null, "Cristopher: Entonces, alquila un auto si deseas participar; te voy a presentar a Wang Jiaqi, es un asesor de WangCars; él te ayudará con el trámite."
                                + "\n 🧑Wang Jiaqi: 早上好朋友，让我自我介绍一下，我是 WangCars 顾问。");
                            JOptionPane.showMessageDialog(null, "         ......      ");
                            JOptionPane.showMessageDialog(null, "🧑Wang Jiaqi: Es broma, hablo español. \"risas\"" + "\n🧑Wang Jiaqi: Acompáñame para mostrarte los autos. ");
                            wangCars(1); // Llama el metodo de renta
                        }
                    }
                    break;
                case 3:
                    // Muestra el nombre registrado si existe, o el ingresado inicialmente
                    JOptionPane.showMessageDialog(null, "Gracias por venir, " + (jugadorUno != null ? jugadorUno.getNombreDeUsuario() : (ingresoPrimerJugador != null ? ingresoPrimerJugador : "Jugador")) + ".");
                    break;
                default:
                    JOptionPane.showMessageDialog(null, "Opción no válida. Por favor, ingrese un número del 1 al 3.", "Error", JOptionPane.ERROR_MESSAGE);
                    break;
            }
        } while (menuRegistroUsuario != 3);
    } // Fin UsuarioUno
    public void usuarioDos() {
        String inputMenuRegistroUsuarioStr;
        String inputEdadStr;
        int tempMenuRegistroUsuario;
        do {
            inputMenuRegistroUsuarioStr = JOptionPane.showInputDialog(
                null,
                "🧑Cristopher: Bienvenido " + (ingresoSegundoJugador != null ? ingresoSegundoJugador : "Jugador 2") + " a \"Racing Sport\""
                + "\nSeleccione una opcion: "
                + "\n 1. Registro"
                + "\n 2. Seleccion de vehiculos"
                + "\n 3. Continuar"
            );
            if (inputMenuRegistroUsuarioStr == null) {
                menuRegistroUsuario = 3;
                JOptionPane.showMessageDialog(null, "Operación cancelada. Continuando.");
            } else {
                tempMenuRegistroUsuario = Integer.parseInt(inputMenuRegistroUsuarioStr);
                menuRegistroUsuario = tempMenuRegistroUsuario;
            }
            switch (menuRegistroUsuario) {
                case 1:
                    nombreDeUsuario = JOptionPane.showInputDialog(null, "Digite su nombre:");
                    if (nombreDeUsuario == null) { nombreDeUsuario = ""; }
                    inputEdadStr = JOptionPane.showInputDialog(null, "Digite su Edad:");
                    if (inputEdadStr == null) { inputEdadStr = "0"; }
                    edad = Integer.parseInt(inputEdadStr);
                    nacionalidad = JOptionPane.showInputDialog(null, "Digite su nacionalidad:");
                    if (nacionalidad == null) { nacionalidad = ""; }
                    jugadorDos = new Usuario(nombreDeUsuario, nacionalidad, edad, 0, 0);
                    JOptionPane.showMessageDialog(null, "¡Registro de " + jugadorDos.getNombreDeUsuario() + " completado!");
                    break;
                case 2:
                    rentCar = JOptionPane.showConfirmDialog(null, "¿Desea rentar un vehiculo?", "Racing Sport", JOptionPane.YES_NO_OPTION);
                    if (rentCar == JOptionPane.YES_OPTION) {
                        wangCars(2);
                    } else if (rentCar == JOptionPane.NO_OPTION) {
                        registrarAuto = JOptionPane.showConfirmDialog(null, "🧑Christopher: Veo que tienes un auto. ¿Acaso ese es el que deseas registrar? ", "Organizador del Evento: Cristopher", JOptionPane.YES_NO_OPTION);
                        if (registrarAuto == JOptionPane.YES_OPTION) {
                            registrarVehiculo(2);
                        } else if (registrarAuto == JOptionPane.NO_OPTION) {
                            JOptionPane.showMessageDialog(null, "Cristopher: Entonces, alquila un auto si deseas participar; te voy a presentar a Wang Jiaqi, es un asesor de WangCars; él te ayudará con el trámite."
                                + "\n 🧑Wang Jiaqi: 早上好朋友,让我自我介绍一下,我是 WangCars 顾问。");
                            JOptionPane.showMessageDialog(null, "         ......      ");
                            JOptionPane.showMessageDialog(null, "🧑Wang Jiaqi: Es broma, hablo español. \"risas\"" + "\n🧑Wang Jiaqi: Acompáñame para mostrarte los autos. ");
                            wangCars(2);
                        }
                    }
                    break;
                case 3:
                    JOptionPane.showMessageDialog(null, "Gracias por venir, " + (jugadorDos != null ? jugadorDos.getNombreDeUsuario() : (ingresoSegundoJugador != null ? ingresoSegundoJugador : "Jugador")) + ".");
                    break;
                default:
                    JOptionPane.showMessageDialog(null, "Opción no válida. Por favor, ingrese un número del 1 al 3.", "Error", JOptionPane.ERROR_MESSAGE);
                    break;
            }
        } while (menuRegistroUsuario != 3);
    } // Fin UsuarioDos
    public void usuarioTres() {
        String inputMenuRegistroUsuarioStr; // Correcto: una sola declaración aquí
        String inputEdadStr;
        int tempMenuRegistroUsuario;
        do {
            // Correcto: solo asignación, no declaración 'String ' ni ';' aquí
            inputMenuRegistroUsuarioStr = JOptionPane.showInputDialog(
                null,
                "🧑Cristopher: Bienvenido " + (ingresoTercerJugador != null ? ingresoTercerJugador : "Jugador 3") + " a \"Racing Sport\""
                + "\nSeleccione una opcion: "
                + "\n 1. Registro"
                + "\n 2. Seleccion de vehiculos"
                + "\n 3. Continuar"
            );
            if (inputMenuRegistroUsuarioStr == null) {
                menuRegistroUsuario = 3;
                JOptionPane.showMessageDialog(null, "Operación cancelada. Continuando.");
            } else {
                tempMenuRegistroUsuario = Integer.parseInt(inputMenuRegistroUsuarioStr);
                menuRegistroUsuario = tempMenuRegistroUsuario;
            }
            switch (menuRegistroUsuario) {
                case 1:
                    nombreDeUsuario = JOptionPane.showInputDialog(null, "Digite su nombre:");
                    if (nombreDeUsuario == null) { nombreDeUsuario = ""; }
                    inputEdadStr = JOptionPane.showInputDialog(null, "Digite su Edad:");
                    if (inputEdadStr == null) { inputEdadStr = "0"; }
                    edad = Integer.parseInt(inputEdadStr);
                    nacionalidad = JOptionPane.showInputDialog(null, "Digite su nacionalidad:");
                    if (nacionalidad == null) { nacionalidad = ""; }
                    jugadorTres = new Usuario(nombreDeUsuario, nacionalidad, edad, 0, 0); // Crea el UsuarioTres
                    JOptionPane.showMessageDialog(null, "¡Registro de " + jugadorTres.getNombreDeUsuario() + " completado!");
                    break;
                case 2:
                    rentCar = JOptionPane.showConfirmDialog(null, "¿Desea rentar un vehiculo?", "Racing Sport", JOptionPane.YES_NO_OPTION);
                    if (rentCar == JOptionPane.YES_OPTION) {
                        wangCars(3);
                    } else if (rentCar == JOptionPane.NO_OPTION) {
                        registrarAuto = JOptionPane.showConfirmDialog(null, "🧑Christopher: Veo que tienes un auto. ¿Acaso ese es el que deseas registrar? ", "Organizador del Evento: Cristopher", JOptionPane.YES_NO_OPTION);
                        if (registrarAuto == JOptionPane.YES_OPTION) {
                            registrarVehiculo(3);
                        } else if (registrarAuto == JOptionPane.NO_OPTION) {
                            JOptionPane.showMessageDialog(null, "Cristopher: Entonces, alquila un auto si deseas participar; te voy a presentar a Wang Jiaqi, es un asesor de WangCars; él te ayudará con el trámite."
                                + "\n 🧑Wang Jiaqi: 早上好朋友,让我自我介绍一下,我是 WangCars 顧問。");
                            JOptionPane.showMessageDialog(null, "         ......      ");
                            JOptionPane.showMessageDialog(null, "🧑Wang Jiaqi: Es broma, hablo español. \"risas\"" + "\n🧑Wang Jiaqi: Acompáñame para mostrarte los autos. ");
                            wangCars(3);
                        }
                    }
                    break;
                case 3:
                    JOptionPane.showMessageDialog(null, "Gracias por venir, " + (jugadorTres != null ? jugadorTres.getNombreDeUsuario() : (ingresoTercerJugador != null ? ingresoTercerJugador : "Jugador")) + ".");
                    break;
                default:
                    JOptionPane.showMessageDialog(null, "Opción no válida. Por favor, ingrese un número del 1 al 3.", "Error", JOptionPane.ERROR_MESSAGE);
                    break;
            }
        } while (menuRegistroUsuario != 3);
    } // Fin UsuarioTres
    public void usuarioCuatro() {
        String inputMenuRegistroUsuarioStr;
        String inputEdadStr;
        int tempMenuRegistroUsuario;
        do {
            inputMenuRegistroUsuarioStr = JOptionPane.showInputDialog(
                null,
                "🧑Cristopher: Bienvenido " + (ingresoCuartoJugador != null ? ingresoCuartoJugador : "Jugador 4") + " a \"Racing Sport\""
                + "\nSeleccione una opcion: "
                + "\n 1. Registro"
                + "\n 2. Seleccion de vehiculos"
                + "\n 3. Continuar"
            );
            if (inputMenuRegistroUsuarioStr == null) {
                menuRegistroUsuario = 3;
                JOptionPane.showMessageDialog(null, "Operación cancelada. Continuando.");
            } else {
                tempMenuRegistroUsuario = Integer.parseInt(inputMenuRegistroUsuarioStr);
                menuRegistroUsuario = tempMenuRegistroUsuario;
            }
            switch (menuRegistroUsuario) {
                case 1:
                    nombreDeUsuario = JOptionPane.showInputDialog(null, "Digite su nombre:");
                    if (nombreDeUsuario == null) { nombreDeUsuario = ""; }
                    inputEdadStr = JOptionPane.showInputDialog(null, "Digite su Edad:");
                    if (inputEdadStr == null) { inputEdadStr = "0"; }
                    edad = Integer.parseInt(inputEdadStr);
                    nacionalidad = JOptionPane.showInputDialog(null, "Digite su nacionalidad:");
                    if (nacionalidad == null) { nacionalidad = ""; }
                    jugadorCuatro = new Usuario(nombreDeUsuario, nacionalidad, edad, 0, 0); // Crea el UsuarioCuatro
                    JOptionPane.showMessageDialog(null, "¡Registro de " + jugadorCuatro.getNombreDeUsuario() + " completado!");
                    break;
                case 2:
                    rentCar = JOptionPane.showConfirmDialog(null, "¿Desea rentar un vehiculo?", "Racing Sport", JOptionPane.YES_NO_OPTION);
                    if (rentCar == JOptionPane.YES_OPTION) {
                        wangCars(4);
                    } else if (rentCar == JOptionPane.NO_OPTION) {
                        registrarAuto = JOptionPane.showConfirmDialog(null, "🧑Christopher: Veo que tienes un auto. ¿Acaso ese es el que deseas registrar? ", "Organizador del Evento: Cristopher", JOptionPane.YES_NO_OPTION);
                        if (registrarAuto == JOptionPane.YES_OPTION) {
                            registrarVehiculo(4);
                        } else if (registrarAuto == JOptionPane.NO_OPTION) {
                            JOptionPane.showMessageDialog(null, "Cristopher: Entonces, alquila un auto si deseas participar; te voy a presentar a Wang Jiaqi, es un asesor de WangCars; él te ayudará con el trámite."
                                + "\n 🧑Wang Jiaqi: 早上好朋友,让我自我介绍一下,我是 WangCars 顾问。");
                            JOptionPane.showMessageDialog(null, "         ......      ");
                            JOptionPane.showMessageDialog(null, "🧑Wang Jiaqi: Es broma, hablo español. \"risas\"" + "\n🧑Wang Jiaqi: Acompáñame para mostrarte los autos. ");
                            wangCars(4);
                        }
                    }
                    break;
                case 3:
                    JOptionPane.showMessageDialog(null, "Gracias por venir, " + (jugadorCuatro != null ? jugadorCuatro.getNombreDeUsuario() : (ingresoCuartoJugador != null ? ingresoCuartoJugador : "Jugador")) + ".");
                    break;
                default:
                    JOptionPane.showMessageDialog(null, "Opción no válida. Por favor, ingrese un número del 1 al 3.", "Error", JOptionPane.ERROR_MESSAGE);
                    break;
            }
        } while (menuRegistroUsuario != 3);
    } // Fin usuarioCuatro
    public void wangCars(int numeroJugador) {
        String inputOpcionRentCarStr;
        String inputModeloRentCarStr;
        Carro carroRentado = null; // Inicializamos a null para evitar NPE si no se selecciona nada válido
        int tempOpcionRentCar; // Variable temporal para la conversión
        int tempModeloRentCar; // Variable temporal para la conversión
        inputOpcionRentCarStr = JOptionPane.showInputDialog(
            null,
            "\nRenta CarsWang. Seleccione una Opcion: "
            + "\n 1. Mercedes-AMG"
            + "\n 2. McLaren"
            + "\n 3. Porsche"
        );
        if (inputOpcionRentCarStr == null) {
            JOptionPane.showMessageDialog(null, "Selección de marca de carro cancelada.");
            return;
        }
        tempOpcionRentCar = Integer.parseInt(inputOpcionRentCarStr);
        opcionRentCar = tempOpcionRentCar; // Asigna el valor validado
        switch (opcionRentCar) {
            case 1:
                inputModeloRentCarStr = JOptionPane.showInputDialog(
                    null,
                    "🧑Wang Jiaqi: En CarsWang tenemos una gran variedad de modelos en nuestra disposicion."
                    + "\n🧑Wang Jiaqi: Sin embargo estos fueron algunos de los vehiculos que hemos traido al evento de Racing Sport: "
                    + "\n 1. AMG ONE 2018 - Azul"
                    + "\n 2. AMG GT3 - Amarillo"
                    + "\n 3. AMG C63 S Coupé - Blanco"
                );
                if (inputModeloRentCarStr == null) { JOptionPane.showMessageDialog(null, "Selección de modelo cancelada."); return; }
                tempModeloRentCar = Integer.parseInt(inputModeloRentCarStr); modeloRentCar = tempModeloRentCar;
                if (modeloRentCar == 1) {
                    carroRentado = new Carro("Mercedes-AMG", "AMG ONE 2018", "Azul", 6.1, 5.1, 4.9, 6.8);
                } else if (modeloRentCar == 2) {
                    carroRentado = new Carro("Mercedes-AMG", "AMG GT3", "Amarillo", 5.0, 6.4, 6.7, 6.1);
                } else if (modeloRentCar == 3) {
                    carroRentado = new Carro("Mercedes-AMG", "AMG C63 S Coupé", "Blanco", 7.4, 2.8, 2.6, 5.4);
                } else {
                    JOptionPane.showMessageDialog(null, "Modelo no válido para Mercedes-AMG.", "Error", JOptionPane.ERROR_MESSAGE);
                }
                break;
            case 2:
                inputModeloRentCarStr = JOptionPane.showInputDialog(
                    null,
                    "🧑Wang Jiaqi: En CarsWang tenemos una gran variedad de modelos en nuestra disposicion."
                    + "\n🧑Wang Jiaqi: Sin embargo estos fueron algunos de los vehiculos que hemos traido al evento de Racing Sport: "
                    + "\n 1. McLaren Senna 2018 - Azul"
                    + "\n 2. McLaren Spider 2019 - Amarillo"
                    + "\n 3. McLaren 600LT Coupé - Plateado"
                );
                if (inputModeloRentCarStr == null) { JOptionPane.showMessageDialog(null, "Selección de modelo cancelada."); return; }
                tempModeloRentCar = Integer.parseInt(inputModeloRentCarStr); modeloRentCar = tempModeloRentCar;
                if (modeloRentCar == 1) {
                    carroRentado = new Carro("McLaren", "McLaren Senna 2018", "Azul", 6.1, 5.1, 4.9, 6.8);
                } else if (modeloRentCar == 2) {
                    carroRentado = new Carro("McLaren", "McLaren Spider 2019", "Amarillo", 5.0, 6.4, 6.7, 6.1);
                } else if (modeloRentCar == 3) {
                    carroRentado = new Carro("McLaren", "McLaren 600LT Coupé", "Plateado", 7.4, 2.8, 2.6, 5.4);
                } else {
                    JOptionPane.showMessageDialog(null, "Modelo no válido para McLaren.", "Error", JOptionPane.ERROR_MESSAGE);
                }
                break;
            case 3:
                inputModeloRentCarStr = JOptionPane.showInputDialog(
                    null,
                    "🧑Wang Jiaqi: En CarsWang tenemos una gran variedad de modelos en nuestra disposicion."
                    + "\n🧑Wang Jiaqi: Sin embargo estos fueron algunos de los vehiculos que hemos traido al evento de Racing Sport: "
                    + "\n 1. 2021 Porsche 911 GT3 - Naranja"
                    + "\n 2. 2016 Porsche Cayman GT4 - Gris"
                    + "\n 3. 2017 Porsche GT Team 911 RSR - Negro"
                );
                if (inputModeloRentCarStr == null) { JOptionPane.showMessageDialog(null, "Selección de modelo cancelada."); return; }
                tempModeloRentCar = Integer.parseInt(inputModeloRentCarStr); modeloRentCar = tempModeloRentCar;
                if (modeloRentCar == 1) {
                    carroRentado = new Carro("Porsche", "2021 Porsche 911 GT3", "Naranja", 6.1, 5.1, 4.9, 6.8);
                } else if (modeloRentCar == 2) {
                    carroRentado = new Carro("Porsche", "2016 Porsche Cayman GT4", "Gris", 5.0, 6.4, 6.7, 6.1);
                } else if (modeloRentCar == 3) {
                    carroRentado = new Carro("Porsche", "2017 Porsche GT Team 911 RSR", "Negro", 7.4, 2.8, 2.6, 5.4);
                } else {
                    JOptionPane.showMessageDialog(null, "Modelo no válido para Porsche.", "Error", JOptionPane.ERROR_MESSAGE);
                }
                break;
            default:
                JOptionPane.showMessageDialog(null, "Opción de marca no válida.", "Error", JOptionPane.ERROR_MESSAGE);
                return; // Sale del método si la marca no es válida
        }
        if (carroRentado != null) { // Solo asigna si se creó un carro válido
            switch (numeroJugador) {
                case 1:
                    vehiculoUno = carroRentado;
                    break;
                case 2:
                    vehiculoDos = carroRentado;
                    break;
                case 3:
                    vehiculoTres = carroRentado;
                    break;
                case 4:
                    vehiculoCuatro = carroRentado;
                    break;
            }
            JOptionPane.showMessageDialog(null, "🧑Wang Jiaqi: ¡Genial! Fue una excelente opción, te diré las características de este vehículo:");
            JOptionPane.showMessageDialog(null, carroRentado); // Asegurate que Carro.toString() formatee bien
        } else {
            JOptionPane.showMessageDialog(null, "No se pudo rentar el vehículo. Intente de nuevo.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }
    public void registrarVehiculo(int asignarVehiculo) {
        String marca = "";
        String modelo = "";
        String color = "";
        Carro carroRegistrado = null; // Usar una variable local para el carro registrado
        JOptionPane.showMessageDialog(null, "🧑Cristopher: Bien, llena este formulario para concluir con el registro del vehículo.");
        marca = JOptionPane.showInputDialog(null, "Seleccione la marca:");
        if (marca == null) { marca = ""; } // Manejar cancelación
        modelo = JOptionPane.showInputDialog(null, "Seleccione el modelo:");
        if (modelo == null) { modelo = ""; } // Manejar cancelación
        color = JOptionPane.showInputDialog(null, "Seleccione el Color:");
        if (color == null) { color = ""; } // Manejar cancelación
        // Se asumen valores por defecto para las características si el usuario las registra manualmente
        carroRegistrado = new Carro(marca, modelo, color, 5.0, 3.1, 3.0, 4.0);
        if (carroRegistrado != null) {
            switch (asignarVehiculo) {
                case 1:
                    vehiculoUno = carroRegistrado;
                    break;
                case 2:
                    vehiculoDos = carroRegistrado;
                    break;
                case 3:
                    vehiculoTres = carroRegistrado;
                    break;
                case 4:
                    vehiculoCuatro = carroRegistrado;
                    break;
            }
            JOptionPane.showMessageDialog(null, "¡Advertencia! Las especificaciones técnicas del vehículo registrado están de Serie."
                + "\nPuedes modificar las especificaciones en el Taller de Racing Sport", "Advertencia", JOptionPane.WARNING_MESSAGE);
            JOptionPane.showMessageDialog(null, carroRegistrado); // Asegurate que Carro.toString() formatee bien
        }
    } // Fin Registro de vehiculo
    public void estadisticas() {
        // Uso de if-else if para manejar las cantidades de jugadores de forma exclusiva
        if (cantidadJugadores == 1) {
            if (jugadorUno != null) { // Asegurarse que el jugador exista
                JOptionPane.showMessageDialog(null, "🧑Cristopher: Aquí les detallo la información y especificaciones por cada uno de ustedes."
                    + "\n" + jugadorUno + "\n " + vehiculoUno); // Asumo toString() en Usuario y Carro
            } else { JOptionPane.showMessageDialog(null, "Jugador 1 no registrado."); }
        } else if (cantidadJugadores == 2) {
            if (jugadorUno != null && jugadorDos != null) {
                JOptionPane.showMessageDialog(null, "🧑Cristopher: Aquí les detallo la información y especificaciones por cada uno de ustedes."
                    + "\n" + jugadorUno + "\n " + vehiculoUno
                    + "\n" + jugadorDos + "\n " + vehiculoDos);
            } else { JOptionPane.showMessageDialog(null, "Al menos un jugador de los 2 no está registrado."); }
        } else if (cantidadJugadores == 3) {
            if (jugadorUno != null && jugadorDos != null && jugadorTres != null) {
                JOptionPane.showMessageDialog(null, "🧑Cristopher: Aquí les detallo la información y especificaciones por cada uno de ustedes."
                    + "\n" + jugadorUno + "\n " + vehiculoUno
                    + "\n" + jugadorDos + "\n " + vehiculoDos
                    + "\n" + jugadorTres + "\n " + vehiculoTres);
            } else { JOptionPane.showMessageDialog(null, "Al menos un jugador de los 3 no está registrado."); }
        } else if (cantidadJugadores == 4) {
            if (jugadorUno != null && jugadorDos != null && jugadorTres != null && jugadorCuatro != null) {
                JOptionPane.showMessageDialog(null, "🧑Cristopher: Aquí les detallo la información y especificaciones por cada uno de ustedes."
                    + "\n" + jugadorUno + "\n " + vehiculoUno
                    + "\n" + jugadorDos + "\n " + vehiculoDos
                    + "\n" + jugadorTres + "\n " + vehiculoTres
                    + "\n" + jugadorCuatro + "\n " + vehiculoCuatro);
            } else { JOptionPane.showMessageDialog(null, "Al menos un jugador de los 4 no está registrado."); }
        } else {
            // Este else debería ser casi inalcanzable si el login está bien validado
            JOptionPane.showMessageDialog(null, "No hay jugadores registrados para mostrar estadísticas.");
        }
    }
    public void menuPrincipal() {
        String inputOpcionMenuStr;
        byte tempOpcionMenu;
        do {
            inputOpcionMenuStr = JOptionPane.showInputDialog(
                null, // Para centrar la ventana
                "🧑Cristopher: ¡Antes de continuar! Racing Sport ha habilitado una sección especial donde podrán tunear sus vehículos a sus gustos."
                + "\n🧑Cristopher: Si desean hacer modificaciones, pueden seguir a Gabriela, quien los guiará en el proceso."
                + "\n🧑Cristopher: Pero si prefieren competir de una vez, pueden dirigirse directamente a la zona de competición con Lucas."
                + "\n\n¿A quien deseas seguir?"
                + "\n 1. Gabriela | Ir al Taller de Mejoras"
                + "\n 2. Lucas    | Competir "
                + "\n 3. Ver Estadisticas"
                + "\n 4. Salir"
            );
            if (inputOpcionMenuStr == null) {
                opcionMenu = 4; // Si cancela, asume que quiere salir
                JOptionPane.showMessageDialog(null, "¡Upa! Cancelaste el menú principal. ¡Hasta la próxima, che!");
            } else {
                tempOpcionMenu = Byte.parseByte(inputOpcionMenuStr);
                opcionMenu = tempOpcionMenu;
            }
            switch (opcionMenu) {
                case 1:
                    opcionGabriela();
                    break;
                case 2:
                    iniciarCarrera(); // Llamada al nuevo método para la carrera
                    break;
                case 3:
                    estadisticas();
                    break;
                case 4:
                    JOptionPane.showMessageDialog(null, "¡Tenga un buen día, regrese pronto, gurí!");
                    break;
                default:
                    if (opcionMenu != -1) {
                        JOptionPane.showMessageDialog(null, "¡Upa! Opción inválida. Intente de nuevo.");
                    }
                    break;
            }
        } while (opcionMenu != 4);
    }
    public void opcionGabriela() {
        String inputSeleccionUsuariosStr;
        int seleccionUsuariosInterna;
        StringBuilder menuUsuarios = new StringBuilder("\nSeleccione su Usuario para tunear:\n");
        boolean hayJugadoresRegistrados = false;
        if (cantidadJugadores >= 1 && jugadorUno != null) {
            menuUsuarios.append(" 1. ").append(jugadorUno.getNombreDeUsuario()).append("\n");
            hayJugadoresRegistrados = true;
        }
        if (cantidadJugadores >= 2 && jugadorDos != null) {
            menuUsuarios.append(" 2. ").append(jugadorDos.getNombreDeUsuario()).append("\n");
            hayJugadoresRegistrados = true;
        }
        if (cantidadJugadores >= 3 && jugadorTres != null) {
            menuUsuarios.append(" 3. ").append(jugadorTres.getNombreDeUsuario()).append("\n");
            hayJugadoresRegistrados = true;
        }
        if (cantidadJugadores >= 4 && jugadorCuatro != null) {
            menuUsuarios.append(" 4. ").append(jugadorCuatro.getNombreDeUsuario()).append("\n");
            hayJugadoresRegistrados = true;
        }
        menuUsuarios.append(" 0. Salir");
        if (!hayJugadoresRegistrados) {
            JOptionPane.showMessageDialog(null, "¡Upa! No hay jugadores registrados para tunear. Primero regístrelos en el login.", "Sin Jugadores", JOptionPane.INFORMATION_MESSAGE);
            return;
        }
        inputSeleccionUsuariosStr = JOptionPane.showInputDialog(null, menuUsuarios.toString());
        if (inputSeleccionUsuariosStr == null) {
            JOptionPane.showMessageDialog(null, "Selección de usuario cancelada. Volviendo al menú anterior.");
            return;
        }
        seleccionUsuariosInterna = Integer.parseInt(inputSeleccionUsuariosStr);
        switch (seleccionUsuariosInterna) {
            case 1:
                if (jugadorUno != null) {
                    nombreDeUsuario = jugadorUno.getNombreDeUsuario();
                    tallerVehiculoUno();
                } else {
                    JOptionPane.showMessageDialog(null, "El Jugador 1 no está registrado. No se puede tunear.");
                }
                break;
            case 2:
                if (jugadorDos != null) {
                    nombreDeUsuario = jugadorDos.getNombreDeUsuario();
                    tallerVehiculoDos();
                } else {
                    JOptionPane.showMessageDialog(null, "El Jugador 2 no está registrado. No se puede tunear.");
                }
                break;
            case 3:
                if (jugadorTres != null) {
                    nombreDeUsuario = jugadorTres.getNombreDeUsuario();
                    tallerVehiculoTres();
                } else {
                    JOptionPane.showMessageDialog(null, "El Jugador 3 no está registrado. No se puede tunear.");
                }
                break;
            case 4:
                if (jugadorCuatro != null) {
                    nombreDeUsuario = jugadorCuatro.getNombreDeUsuario();
                    tallerVehiculoCuatro();
                } else {
                    JOptionPane.showMessageDialog(null, "El Jugador 4 no está registrado. No se puede tunear.");
                }
                break;
            case 0:
                JOptionPane.showMessageDialog(null, "Volviendo al menú principal.");
                break;
            default:
                JOptionPane.showMessageDialog(null, "¡Upa! Opción de usuario inválida. Elegí uno de la lista, che.", "Opción Inválida", JOptionPane.ERROR_MESSAGE);
                break;
        }
    }
    public void tallerVehiculoUno() {
        String inputOpcionTallerStr;
        String inputSubOpcionStr;
        byte tempOpcionTaller;
        int tempSubOpcion;
        do {
            inputOpcionTallerStr = JOptionPane.showInputDialog(
                null,
                "🧑Gabriela: Es un placer conocerte " + nombreDeUsuario + ", si no sabes para qué sirve un componente, yo estoy aquí para ayudarte."
                + "\n\nSelecciona una opción:"
                + "\n1. Combustible y aire"
                + "\n2. Plataforma y manejo"
                + "\n3. Llantas"
                + "\n4. Tren de transmisión"
                + "\n0. Volver al menú principal"
            );
            if (inputOpcionTallerStr == null) {
                opcionTaller = 0;
                JOptionPane.showMessageDialog(null, "¡Upa! Cancelaste el menú del taller. ¡Hasta la próxima, che!");
                break;
            }
            tempOpcionTaller = Byte.parseByte(inputOpcionTallerStr);
            opcionTaller = tempOpcionTaller;
            switch (opcionTaller) {
                case 1:
                    inputSubOpcionStr = JOptionPane.showInputDialog(
                        null,
                        "🧑Gabriela: Combustible y aire"
                        + "\n1. Retirar brida de admisión"
                        + "\n0. Volver"
                    );
                    if (inputSubOpcionStr == null) { subOpcion = 0; break; }
                    tempSubOpcion = Integer.parseInt(inputSubOpcionStr); subOpcion = tempSubOpcion;
                    if (subOpcion == 1) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Brida retirada ahora el motor puede dar el mejor desempeño.");
                        configCarUno.setBridaDeAdmision(false);
                        vehiculoUno.setVelocidad(0.1);
                        vehiculoUno.setFrenado(0.6);
                        vehiculoUno.setManejo(0.2);
                        vehiculoUno.setAceleracion(0.3);
                    } else if (subOpcion != 0) {
                        JOptionPane.showMessageDialog(null, "Opción inválida.");
                    }
                    break;
                case 2:
                    inputSubOpcionStr = JOptionPane.showInputDialog(
                        null,
                        "🧑Gabriela: Plataforma y manejo"
                        + "\n1. Frenos deportivos"
                        + "\n2. Ajustar muelles y amortiguadores"
                        + "\n0. Volver"
                    );
                    if (inputSubOpcionStr == null) { subOpcion = 0; break; }
                    tempSubOpcion = Integer.parseInt(inputSubOpcionStr); subOpcion = tempSubOpcion;
                    if (subOpcion == 1) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Frenos instalados, mejor capacidad de frenado.");
                        configCarUno.setFrenos("Carreras");
                        vehiculoUno.setVelocidad(0.1);
                        vehiculoUno.setFrenado(0.6);
                        vehiculoUno.setManejo(0.2);
                        vehiculoUno.setAceleracion(0.3);
                    } else if (subOpcion == 2) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Suspensión ajustada, mejor comportamiento en curvas.");
                        configCarUno.setMuellesYAmortiguadores("Carreras");
                        vehiculoUno.setVelocidad(0.1);
                        vehiculoUno.setFrenado(0.6);
                        vehiculoUno.setManejo(0.2);
                        vehiculoUno.setAceleracion(0.3);
                    } else if (subOpcion != 0) {
                        JOptionPane.showMessageDialog(null, "Opción inválida.");
                    }
                    break;
                case 3:
                    inputSubOpcionStr = JOptionPane.showInputDialog(
                        null,
                        "🧑Gabriela: Llantas"
                        + "\n1. Cambiar compuesto de llantas"
                        + "\n2. Aumentar anchura de llantas delanteras"
                        + "\n3. Aumentar anchura de llantas traseras"
                        + "\n0. Volver"
                    );
                    if (inputSubOpcionStr == null) { subOpcion = 0; break; }
                    tempSubOpcion = Integer.parseInt(inputSubOpcionStr); subOpcion = tempSubOpcion;
                    if (subOpcion == 1) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Compuesto cambiado, mejor agarre.");
                        configCarUno.setCompuestoDeLlantas("Carreras");
                        vehiculoUno.setVelocidad(0.1);
                        vehiculoUno.setFrenado(0.6);
                        vehiculoUno.setManejo(0.2);
                        vehiculoUno.setAceleracion(0.3);
                    } else if (subOpcion == 2) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Anchura delantera aumentada, mayor estabilidad.");
                        configCarUno.setFrontTireWidth(210);
                        vehiculoUno.setVelocidad(0.1);
                        vehiculoUno.setFrenado(0.6);
                        vehiculoUno.setManejo(0.2);
                        vehiculoUno.setAceleracion(0.3);
                    } else if (subOpcion == 3) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Anchura trasera aumentada, más tracción.");
                        configCarUno.setRearTireWidth(218);
                        vehiculoUno.setVelocidad(0.1);
                        vehiculoUno.setFrenado(0.6);
                        vehiculoUno.setManejo(0.2);
                        vehiculoUno.setAceleracion(0.3);
                    } else if (subOpcion != 0) {
                        JOptionPane.showMessageDialog(null, "Opción inválida.");
                    }
                    break;
                case 4:
                    inputSubOpcionStr = JOptionPane.showInputDialog(
                        null,
                        "🧑Gabriela: Tren de transmisión"
                        + "\n1. Instalar embrague de competición"
                        + "\n2. Ajustar la transmisión"
                        + "\n3. Configurar el diferencial"
                        + "\n0. Volver"
                    );
                    if (inputSubOpcionStr == null) { subOpcion = 0; break; }
                    tempSubOpcion = Integer.parseInt(inputSubOpcionStr); subOpcion = tempSubOpcion;
                    if (subOpcion == 1) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Embrague mejorado, cambios más rápidos.");
                        configCarUno.setEmbrague("Deportivo");
                        vehiculoUno.setVelocidad(0.1);
                        vehiculoUno.setFrenado(0.6);
                        vehiculoUno.setManejo(0.2);
                        vehiculoUno.setAceleracion(0.3);
                    } else if (subOpcion == 2) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Transmisión ajustada para mejor aceleración.");
                        configCarUno.setTransmision("Carreras");
                        vehiculoUno.setVelocidad(0.1);
                        vehiculoUno.setFrenado(0.6);
                        vehiculoUno.setManejo(0.2);
                        vehiculoUno.setAceleracion(0.3);
                    } else if (subOpcion == 3) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Diferencial configurado para mejor tracción.");
                        configCarUno.setDiferencial("Carreras");
                        vehiculoUno.setVelocidad(0.1);
                        vehiculoUno.setFrenado(0.6);
                        vehiculoUno.setManejo(0.2);
                        vehiculoUno.setAceleracion(0.3);
                    } else if (subOpcion != 0) {
                        JOptionPane.showMessageDialog(null, "Opción inválida.");
                    }
                    break;
                case 0: // Volver al menú principal
                    JOptionPane.showMessageDialog(null, "🧑Gabriela: ¡Tenga un buen día! Regrese pronto.");
                    break;
                default: // Opción inválida para el menú principal del taller
                    if (opcionTaller != -1) { // Evita mensaje si ya se manejó error de formato
                        JOptionPane.showMessageDialog(null, "Opción inválida. Intente nuevamente.");
                    }
                    break;
            }
        } while (opcionTaller != 0);
    }
    public void tallerVehiculoDos() {
        String inputOpcionTallerStr;
        String inputSubOpcionStr;
        byte tempOpcionTaller;
        int tempSubOpcion;
        do {
            inputOpcionTallerStr = JOptionPane.showInputDialog(
                null,
                "🧑Gabriela: Es un placer conocerte " + nombreDeUsuario + ", si no sabes para qué sirve un componente, yo estoy aquí para ayudarte."
                + "\n\nSelecciona una opción:"
                + "\n1. Combustible y aire"
                + "\n2. Plataforma y manejo"
                + "\n3. Llantas"
                + "\n4. Tren de transmisión"
                + "\n0. Volver al menú principal"
            );
            if (inputOpcionTallerStr == null) {
                opcionTaller = 0;
                JOptionPane.showMessageDialog(null, "¡Upa! Cancelaste el menú del taller. ¡Hasta la próxima, che!");
                break;
            }
            tempOpcionTaller = Byte.parseByte(inputOpcionTallerStr);
            opcionTaller = tempOpcionTaller;
            switch (opcionTaller) {
                case 1:
                    inputSubOpcionStr = JOptionPane.showInputDialog(
                        null,
                        "🧑Gabriela: Combustible y aire"
                        + "\n1. Retirar brida de admisión"
                        + "\n0. Volver"
                    );
                    if (inputSubOpcionStr == null) { subOpcion = 0; break; }
                    tempSubOpcion = Integer.parseInt(inputSubOpcionStr); subOpcion = tempSubOpcion;
                    if (subOpcion == 1) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Brida retirada ahora el motor puede dar el mejor desempeño.");
                        configCarDos.setBridaDeAdmision(false);
                        vehiculoDos.setVelocidad(0.1);
                        vehiculoDos.setFrenado(0.6);
                        vehiculoDos.setManejo(0.2);
                        vehiculoDos.setAceleracion(0.2);
                    } else if (subOpcion != 0) {
                        JOptionPane.showMessageDialog(null, "Opción inválida.");
                    }
                    break;
                case 2:
                    inputSubOpcionStr = JOptionPane.showInputDialog(
                        null,
                        "🧑Gabriela:Plataforma y manejo"
                        + "\n1. Frenos deportivos"
                        + "\n2. Ajustar muelles y amortiguadores"
                        + "\n0. Volver"
                    );
                    if (inputSubOpcionStr == null) { subOpcion = 0; break; }
                    tempSubOpcion = Integer.parseInt(inputSubOpcionStr); subOpcion = tempSubOpcion;
                    if (subOpcion == 1) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Frenos instalados, mejor capacidad de frenado.");
                        configCarDos.setFrenos("Carreras");
                        vehiculoDos.setVelocidad(0.1);
                        vehiculoDos.setFrenado(0.6);
                        vehiculoDos.setManejo(0.2);
                        vehiculoDos.setAceleracion(0.2);
                    } else if (subOpcion == 2) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Suspensión ajustada, mejor comportamiento en curvas.");
                        configCarDos.setMuellesYAmortiguadores("Carreras");
                        vehiculoDos.setVelocidad(0.1);
                        vehiculoDos.setFrenado(0.6);
                        vehiculoDos.setManejo(0.2);
                        vehiculoDos.setAceleracion(0.2);
                    } else if (subOpcion != 0) {
                        JOptionPane.showMessageDialog(null, "Opción inválida.");
                    }
                    break;
                case 3:
                    inputSubOpcionStr = JOptionPane.showInputDialog(
                        null,
                        "🧑Gabriela: Llantas"
                        + "\n1. Cambiar compuesto de llantas"
                        + "\n2. Aumentar anchura de llantas delanteras"
                        + "\n3. Aumentar anchura de llantas traseras"
                        + "\n0. Volver"
                    );
                    if (inputSubOpcionStr == null) { subOpcion = 0; break; }
                    tempSubOpcion = Integer.parseInt(inputSubOpcionStr); subOpcion = tempSubOpcion;
                    if (subOpcion == 1) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Compuesto cambiado, mejor agarre.");
                        configCarDos.setCompuestoDeLlantas("Carreras");
                        vehiculoDos.setVelocidad(0.1);
                        vehiculoDos.setFrenado(0.6);
                        vehiculoDos.setManejo(0.2);
                        vehiculoDos.setAceleracion(0.2);
                    } else if (subOpcion == 2) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Anchura delantera aumentada, mayor estabilidad.");
                        configCarDos.setFrontTireWidth(210);
                        vehiculoDos.setVelocidad(0.1);
                        vehiculoDos.setFrenado(0.6);
                        vehiculoDos.setManejo(0.2);
                        vehiculoDos.setAceleracion(0.2);
                    } else if (subOpcion == 3) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Anchura trasera aumentada, más tracción.");
                        configCarDos.setRearTireWidth(218);
                        vehiculoDos.setVelocidad(0.1);
                        vehiculoDos.setFrenado(0.6);
                        vehiculoDos.setManejo(0.2);
                        vehiculoDos.setAceleracion(0.2);
                    } else if (subOpcion != 0) {
                        JOptionPane.showMessageDialog(null, "Opción inválida.");
                    }
                    break;
                case 4:
                    inputSubOpcionStr = JOptionPane.showInputDialog(
                        null,
                        "🧑Gabriela: Tren de transmisión"
                        + "\n1. Instalar embrague de competición"
                        + "\n2. Ajustar la transmisión"
                        + "\n3. Configurar el diferencial"
                        + "\n0. Volver"
                    );
                    if (inputSubOpcionStr == null) { subOpcion = 0; break; }
                    tempSubOpcion = Integer.parseInt(inputSubOpcionStr); subOpcion = tempSubOpcion;
                    if (subOpcion == 1) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Embrague mejorado, cambios más rápidos.");
                        configCarDos.setEmbrague("Deportivo");
                        vehiculoDos.setVelocidad(0.1);
                        vehiculoDos.setFrenado(0.6);
                        vehiculoDos.setManejo(0.2);
                        vehiculoDos.setAceleracion(0.2);
                    } else if (subOpcion == 2) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Transmisión ajustada para mejor aceleración.");
                        configCarDos.setTransmision("Carreras");
                        vehiculoDos.setVelocidad(0.1);
                        vehiculoDos.setFrenado(0.6);
                        vehiculoDos.setManejo(0.2);
                        vehiculoDos.setAceleracion(0.2);
                    } else if (subOpcion == 3) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Diferencial configurado para mejor tracción.");
                        configCarDos.setDiferencial("Carreras");
                        vehiculoDos.setVelocidad(0.1);
                        vehiculoDos.setFrenado(0.6);
                        vehiculoDos.setManejo(0.2);
                        vehiculoDos.setAceleracion(0.2);
                    } else if (subOpcion != 0) {
                        JOptionPane.showMessageDialog(null, "Opción inválida.");
                    }
                    break;
                case 0:
                    JOptionPane.showMessageDialog(null, "🧑Gabriela: ¡Tenga un buen día! Regrese pronto.");
                    break;
                default:
                    if (opcionTaller != -1) {
                        JOptionPane.showMessageDialog(null, "Opción inválida. Intente nuevamente.");
                    }
                    break;
            }
        } while (opcionTaller != 0);
    }
    public void tallerVehiculoTres() {
        String inputOpcionTallerStr;
        String inputSubOpcionStr;
        byte tempOpcionTaller;
        int tempSubOpcion;
        do {
            inputOpcionTallerStr = JOptionPane.showInputDialog(
                null,
                "🧑Gabriela: Es un placer conocerte " + nombreDeUsuario + ", si no sabes para qué sirve un componente, yo estoy aquí para ayudarte."
                + "\n\nSelecciona una opción:"
                + "\n1. Combustible y aire"
                + "\n2. Plataforma y manejo"
                + "\n3. Llantas"
                + "\n4. Tren de transmisión"
                + "\n0. Volver al menú principal"
            );
            if (inputOpcionTallerStr == null) {
                opcionTaller = 0;
                JOptionPane.showMessageDialog(null, "¡Upa! Cancelaste el menú del taller. ¡Hasta la próxima, che!");
                break;
            }
            tempOpcionTaller = Byte.parseByte(inputOpcionTallerStr);
            opcionTaller = tempOpcionTaller;
            switch (opcionTaller) {
                case 1:
                    inputSubOpcionStr = JOptionPane.showInputDialog(
                        null,
                        "🧑Gabriela: Combustible y aire"
                        + "\n1. Retirar brida de admisión"
                        + "\n0. Volver"
                    );
                    if (inputSubOpcionStr == null) { subOpcion = 0; break; }
                    tempSubOpcion = Integer.parseInt(inputSubOpcionStr); subOpcion = tempSubOpcion;
                    if (subOpcion == 1) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Brida retirada ahora el motor puede dar el mejor desempeño.");
                        configCarTres.setBridaDeAdmision(false);
                        vehiculoTres.setVelocidad(0.1);
                        vehiculoTres.setFrenado(0.6);
                        vehiculoTres.setManejo(0.2);
                        vehiculoTres.setAceleracion(0.2);
                    } else if (subOpcion != 0) {
                        JOptionPane.showMessageDialog(null, "Opción inválida.");
                    }
                    break;
                case 2:
                    inputSubOpcionStr = JOptionPane.showInputDialog(
                        null,
                        "🧑Gabriela:Plataforma y manejo"
                        + "\n1. Frenos deportivos"
                        + "\n2. Ajustar muelles y amortiguadores"
                        + "\n0. Volver"
                    );
                    if (inputSubOpcionStr == null) { subOpcion = 0; break; }
                    tempSubOpcion = Integer.parseInt(inputSubOpcionStr); subOpcion = tempSubOpcion;
                    if (subOpcion == 1) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Frenos instalados, mejor capacidad de frenado.");
                        configCarTres.setFrenos("Carreras");
                        vehiculoTres.setVelocidad(0.1);
                        vehiculoTres.setFrenado(0.6);
                        vehiculoTres.setManejo(0.2);
                        vehiculoTres.setAceleracion(0.2);
                    } else if (subOpcion == 2) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Suspensión ajustada, mejor comportamiento en curvas.");
                        configCarTres.setMuellesYAmortiguadores("Carreras");
                        vehiculoTres.setVelocidad(0.1);
                        vehiculoTres.setFrenado(0.6);
                        vehiculoTres.setManejo(0.2);
                        vehiculoTres.setAceleracion(0.2);
                    } else if (subOpcion != 0) {
                        JOptionPane.showMessageDialog(null, "Opción inválida.");
                    }
                    break;
                case 3:
                    inputSubOpcionStr = JOptionPane.showInputDialog(
                        null,
                        "🧑Gabriela: Llantas"
                        + "\n1. Cambiar compuesto de llantas"
                        + "\n2. Aumentar anchura de llantas delanteras"
                        + "\n3. Aumentar anchura de llantas traseras"
                        + "\n0. Volver"
                    );
                    if (inputSubOpcionStr == null) { subOpcion = 0; break; }
                    tempSubOpcion = Integer.parseInt(inputSubOpcionStr); subOpcion = tempSubOpcion;
                    if (subOpcion == 1) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Compuesto cambiado, mejor agarre.");
                        configCarTres.setCompuestoDeLlantas("Carreras");
                        vehiculoTres.setVelocidad(0.1);
                        vehiculoTres.setFrenado(0.6);
                        vehiculoTres.setManejo(0.2);
                        vehiculoTres.setAceleracion(0.2);
                    } else if (subOpcion == 2) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Anchura delantera aumentada, mayor estabilidad.");
                        configCarTres.setFrontTireWidth(210);
                        vehiculoTres.setVelocidad(0.1);
                        vehiculoTres.setFrenado(0.6);
                        vehiculoTres.setManejo(0.2);
                        vehiculoTres.setAceleracion(0.2);
                    } else if (subOpcion == 3) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Anchura trasera aumentada, más tracción.");
                        configCarTres.setRearTireWidth(218);
                        vehiculoTres.setVelocidad(0.1);
                        vehiculoTres.setFrenado(0.6);
                        vehiculoTres.setManejo(0.2);
                        vehiculoTres.setAceleracion(0.2);
                    } else if (subOpcion != 0) {
                        JOptionPane.showMessageDialog(null, "Opción inválida.");
                    }
                    break;
                case 4:
                    inputSubOpcionStr = JOptionPane.showInputDialog(
                        null,
                        "🧑Gabriela: Tren de transmisión"
                        + "\n1. Instalar embrague de competición"
                        + "\n2. Ajustar la transmisión"
                        + "\n3. Configurar el diferencial"
                        + "\n0. Volver"
                    );
                    if (inputSubOpcionStr == null) { subOpcion = 0; break; }
                    tempSubOpcion = Integer.parseInt(inputSubOpcionStr); subOpcion = tempSubOpcion;
                    if (subOpcion == 1) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Embrague mejorado, cambios más rápidos.");
                        configCarTres.setEmbrague("Deportivo");
                        vehiculoTres.setVelocidad(0.1);
                        vehiculoTres.setFrenado(0.6);
                        vehiculoTres.setManejo(0.2);
                        vehiculoTres.setAceleracion(0.2);
                    } else if (subOpcion == 2) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Transmisión ajustada para mejor aceleración.");
                        configCarTres.setTransmision("Carreras");
                        vehiculoTres.setVelocidad(0.1);
                        vehiculoTres.setFrenado(0.6);
                        vehiculoTres.setManejo(0.2);
                        vehiculoTres.setAceleracion(0.2);
                    } else if (subOpcion == 3) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Diferencial configurado para mejor tracción.");
                        configCarTres.setDiferencial("Carreras");
                        vehiculoTres.setVelocidad(0.1);
                        vehiculoTres.setFrenado(0.6);
                        vehiculoTres.setManejo(0.2);
                        vehiculoTres.setAceleracion(0.2);
                    } else if (subOpcion != 0) {
                        JOptionPane.showMessageDialog(null, "Opción inválida.");
                    }
                    break;
                case 0:
                    JOptionPane.showMessageDialog(null, "🧑Gabriela: ¡Tenga un buen día! Regrese pronto.");
                    break;
                default:
                    if (opcionTaller != -1) {
                        JOptionPane.showMessageDialog(null, "Opción inválida. Intente nuevamente.");
                    }
                    break;
            }
        } while (opcionTaller != 0);
    }
    public void tallerVehiculoCuatro() {
        String inputOpcionTallerStr;
        String inputSubOpcionStr;
        byte tempOpcionTaller;
        int tempSubOpcion;
        do {
            inputOpcionTallerStr = JOptionPane.showInputDialog(
                null,
                "🧑Gabriela: Es un placer conocerte " + nombreDeUsuario + ", si no sabes para qué sirve un componente, yo estoy aquí para ayudarte."
                + "\n\nSelecciona una opción:"
                + "\n1. Combustible y aire"
                + "\n2. Plataforma y manejo"
                + "\n3. Llantas"
                + "\n4. Tren de transmisión"
                + "\n0. Volver al menú principal"
            );
            if (inputOpcionTallerStr == null) {
                opcionTaller = 0;
                JOptionPane.showMessageDialog(null, "¡Upa! Cancelaste el menú del taller. ¡Hasta la próxima, che!");
                break;
            }
            tempOpcionTaller = Byte.parseByte(inputOpcionTallerStr);
            opcionTaller = tempOpcionTaller;
            switch (opcionTaller) { // CORRECCIÓN: Usar 'opcionTaller', no 'opcionTallerDos'
                case 1:
                    inputSubOpcionStr = JOptionPane.showInputDialog(
                        null,
                        "🧑Gabriela: Combustible y aire"
                        + "\n1. Retirar brida de admisión"
                        + "\n0. Volver"
                    );
                    if (inputSubOpcionStr == null) { subOpcion = 0; break; }
                    tempSubOpcion = Integer.parseInt(inputSubOpcionStr); subOpcion = tempSubOpcion;
                    if (subOpcion == 1) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Brida retirada ahora el motor puede dar el mejor desempeño.");
                        configCarCuatro.setBridaDeAdmision(false);
                        vehiculoCuatro.setVelocidad(0.1);
                        vehiculoCuatro.setFrenado(0.6);
                        vehiculoCuatro.setManejo(0.2);
                        vehiculoCuatro.setAceleracion(0.2);
                    } else if (subOpcion != 0) {
                        JOptionPane.showMessageDialog(null, "Opción inválida.");
                    }
                    break;
                case 2:
                    inputSubOpcionStr = JOptionPane.showInputDialog(
                        null,
                        "🧑Gabriela:Plataforma y manejo"
                        + "\n1. Frenos deportivos"
                        + "\n2. Ajustar muelles y amortiguadores"
                        + "\n0. Volver"
                    );
                    if (inputSubOpcionStr == null) { subOpcion = 0; break; }
                    tempSubOpcion = Integer.parseInt(inputSubOpcionStr); subOpcion = tempSubOpcion;
                    if (subOpcion == 1) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Frenos instalados, mejor capacidad de frenado.");
                        configCarCuatro.setFrenos("Carreras");
                        vehiculoCuatro.setVelocidad(0.1);
                        vehiculoCuatro.setFrenado(0.6);
                        vehiculoCuatro.setManejo(0.2);
                        vehiculoCuatro.setAceleracion(0.2);
                    } else if (subOpcion == 2) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Suspensión ajustada, mejor comportamiento en curvas.");
                        configCarCuatro.setMuellesYAmortiguadores("Carreras");
                        vehiculoCuatro.setVelocidad(0.1);
                        vehiculoCuatro.setFrenado(0.6);
                        vehiculoCuatro.setManejo(0.2);
                        vehiculoCuatro.setAceleracion(0.2);
                    } else if (subOpcion != 0) {
                        JOptionPane.showMessageDialog(null, "Opción inválida.");
                    }
                    break;
                case 3:
                    inputSubOpcionStr = JOptionPane.showInputDialog(
                        null,
                        "🧑Gabriela: Llantas"
                        + "\n1. Cambiar compuesto de llantas"
                        + "\n2. Aumentar anchura de llantas delanteras"
                        + "\n3. Aumentar anchura de llantas traseras"
                        + "\n0. Volver"
                    );
                    if (inputSubOpcionStr == null) { subOpcion = 0; break; }
                    tempSubOpcion = Integer.parseInt(inputSubOpcionStr); subOpcion = tempSubOpcion;
                    if (subOpcion == 1) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Compuesto cambiado, mejor agarre.");
                        configCarCuatro.setCompuestoDeLlantas("Carreras");
                        vehiculoCuatro.setVelocidad(0.1);
                        vehiculoCuatro.setFrenado(0.6);
                        vehiculoCuatro.setManejo(0.2);
                        vehiculoCuatro.setAceleracion(0.2);
                    } else if (subOpcion == 2) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Anchura delantera aumentada, mayor estabilidad.");
                        configCarCuatro.setFrontTireWidth(210);
                        vehiculoCuatro.setVelocidad(0.1);
                        vehiculoCuatro.setFrenado(0.6);
                        vehiculoCuatro.setManejo(0.2);
                        vehiculoCuatro.setAceleracion(0.2);
                    } else if (subOpcion == 3) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Anchura trasera aumentada, más tracción.");
                        configCarCuatro.setRearTireWidth(218);
                        vehiculoCuatro.setVelocidad(0.1);
                        vehiculoCuatro.setFrenado(0.6);
                        vehiculoCuatro.setManejo(0.2);
                        vehiculoCuatro.setAceleracion(0.2);
                    } else if (subOpcion != 0) { // Corregido: Este 'else if' ahora está correctamente indentado
                        JOptionPane.showMessageDialog(null, "Opción inválida.");
                    }
                    break;
                case 4:
                    inputSubOpcionStr = JOptionPane.showInputDialog(
                        null,
                        "🧑Gabriela: Tren de transmisión"
                        + "\n1. Instalar embrague de competición"
                        + "\n2. Ajustar la transmisión"
                        + "\n3. Configurar el diferencial"
                        + "\n0. Volver"
                    );
                    if (inputSubOpcionStr == null) { subOpcion = 0; break; }
                    tempSubOpcion = Integer.parseInt(inputSubOpcionStr); subOpcion = tempSubOpcion;
                    if (subOpcion == 1) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Embrague mejorado, cambios más rápidos.");
                        configCarCuatro.setEmbrague("Deportivo");
                        vehiculoCuatro.setVelocidad(0.1);
                        vehiculoCuatro.setFrenado(0.6);
                        vehiculoCuatro.setManejo(0.2);
                        vehiculoCuatro.setAceleracion(0.2);
                    } else if (subOpcion == 2) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Transmisión ajustada para mejor aceleración.");
                        configCarCuatro.setTransmision("Carreras");
                        vehiculoCuatro.setVelocidad(0.1);
                        vehiculoCuatro.setFrenado(0.6);
                        vehiculoCuatro.setManejo(0.2);
                        vehiculoCuatro.setAceleracion(0.2);
                    } else if (subOpcion == 3) {
                        JOptionPane.showMessageDialog(null, "🧑Gabriela: Diferencial configurado para mejor tracción.");
                        configCarCuatro.setDiferencial("Carreras");
                        vehiculoCuatro.setVelocidad(0.1);
                        vehiculoCuatro.setFrenado(0.6);
                        vehiculoCuatro.setManejo(0.2);
                        vehiculoCuatro.setAceleracion(0.2);
                    } else if (subOpcion != 0) {
                        JOptionPane.showMessageDialog(null, "Opción inválida.");
                    }
                    break;
                case 0:
                    JOptionPane.showMessageDialog(null, "🧑Gabriela: ¡Tenga un buen día! Regrese pronto.");
                    break;
                default:
                    if (opcionTaller != -1) {
                        JOptionPane.showMessageDialog(null, "Opción inválida. Intente nuevamente.");
                    }
                    break;
            }
        } while (opcionTaller != 0);
    }
    // --- Nuevo método para la lógica de la Carrera ---
    public void iniciarCarrera() {
        if (cantidadJugadores < 2) {
            JOptionPane.showMessageDialog(null, "🧑Lucas: ¡Para competir necesitamos al menos dos jugadores registrados y con vehículos asignados, che!", "Carrera Imposible", JOptionPane.INFORMATION_MESSAGE);
            return;
        }
        String opcionCarreraStr; // Declaración de variable para el input
        int opcionCarrera;       // Declaración de variable para la opción convertida
        // Mostrar opciones de carrera
        opcionCarreraStr = JOptionPane.showInputDialog(
            null,
            "🧑Lucas: ¡A la carga, gurises! ¿Cómo quieren definir esta carrera?\n"
            + "1. Carrera aleatoria (el ganador es al azar)\n"
            + "2. Carrera por tuneo (gana el de mejor rendimiento)\n"
            + "0. Volver al menú principal"
        );
        if (opcionCarreraStr == null) {
            JOptionPane.showMessageDialog(null, "Carrera cancelada. Volviendo al menú principal.");
            return;
        }
        opcionCarrera = Integer.parseInt(opcionCarreraStr);
        switch (opcionCarrera) {
            case 1:
                ejecutarCarreraAleatoria();
                break;
            case 2:
                ejecutarCarreraPorTuneo();
                break;
            case 0:
                JOptionPane.showMessageDialog(null, "Volviendo al menú principal.");
                break;
            default:
                JOptionPane.showMessageDialog(null, "Opción de carrera inválida.");
                break;
        }
    }
    private void ejecutarCarreraAleatoria() {
        Random rand = new Random();
        Usuario ganador = null;
        int numParticipantesValidos = 0;
        
        // Contar y verificar participantes válidos sin usar arrays.
        // Se crean variables temporales para almacenar los participantes si es necesario,
        // pero la selección final es sobre las variables globales jugadorX/vehiculoX.
        Usuario p1 = null, p2 = null, p3 = null, p4 = null;
        Carro v1 = null, v2 = null, v3 = null, v4 = null;
        if (jugadorUno != null && vehiculoUno != null) { p1 = jugadorUno; v1 = vehiculoUno; numParticipantesValidos++; }
        if (jugadorDos != null && vehiculoDos != null) { p2 = jugadorDos; v2 = vehiculoDos; numParticipantesValidos++; }
        if (jugadorTres != null && vehiculoTres != null) { p3 = jugadorTres; v3 = vehiculoTres; numParticipantesValidos++; }
        if (jugadorCuatro != null && vehiculoCuatro != null) { p4 = jugadorCuatro; v4 = vehiculoCuatro; numParticipantesValidos++; }
        if (numParticipantesValidos < 2) {
            JOptionPane.showMessageDialog(null, "🧑Lucas: ¡Necesitamos al menos dos jugadores con vehículos asignados para esta carrera!", "Carrera Cancelada", JOptionPane.INFORMATION_MESSAGE);
            return;
        }
        int ganadorIndex = rand.nextInt(numParticipantesValidos); // Elije un número entre 0 y (numParticipantesValidos-1)
        // Asignar el ganador basado en el índice aleatorio y los participantes válidos
        // Se recorren los jugadores en el orden de sus variables, contando solo los válidos.
        int contadorTemp = 0;
        if (p1 != null) {
            if (ganadorIndex == contadorTemp) { ganador = p1; }
            contadorTemp++;
        }
        if (p2 != null) {
            if (ganadorIndex == contadorTemp) { ganador = p2; }
            contadorTemp++;
        }
        if (p3 != null) {
            if (ganadorIndex == contadorTemp) { ganador = p3; }
            contadorTemp++;
        }
        if (p4 != null) {
            if (ganadorIndex == contadorTemp) { ganador = p4; }
            contadorTemp++;
        }
        
        if (ganador != null) {
            // Sumar punto al ganador
            ganador.setTablaDePuntuacion(ganador.getTablaDePuntuacion() + 1);
            ganador.setContadorCarrerasGanadas(ganador.getContadorCarrerasGanadas() + 1);
            JOptionPane.showMessageDialog(null, "🧑Lucas: ¡Y el ganador de esta carrera aleatoria es... " + ganador.getNombreDeUsuario() + "!\n¡Sigue sumando puntos, che!");
        } else {
            // Este else debería ser raro si numParticipantesValidos >= 2 y la lógica es correcta
            JOptionPane.showMessageDialog(null, "Error al determinar el ganador aleatorio.");
        }
    }
    private void ejecutarCarreraPorTuneo() {
        Usuario ganador = null;
        Carro carroGanador = null;
        double maxRendimiento = -1.0;
        
        // Primero, verificar que haya suficientes participantes válidos antes de empezar a calcular
        int numParticipantesValidos = 0;
        if (jugadorUno != null && vehiculoUno != null) numParticipantesValidos++;
        if (jugadorDos != null && vehiculoDos != null) numParticipantesValidos++;
        if (jugadorTres != null && vehiculoTres != null) numParticipantesValidos++;
        if (jugadorCuatro != null && vehiculoCuatro != null) numParticipantesValidos++;
        if (numParticipantesValidos < 2) {
            JOptionPane.showMessageDialog(null, "🧑Lucas: ¡Necesitamos al menos dos jugadores con vehículos asignados para esta carrera!", "Carrera Cancelada", JOptionPane.INFORMATION_MESSAGE);
            return;
        }
        // Evaluar Jugador 1
        if (jugadorUno != null && vehiculoUno != null) {
            double rendimientoActual = (vehiculoUno.getVelocidad() + vehiculoUno.getAceleracion())
                                     * vehiculoUno.getManejo()
                                     / (vehiculoUno.getFrenado() == 0 ? 0.01 : vehiculoUno.getFrenado()); // Evitar división por cero
            if (rendimientoActual > maxRendimiento) {
                maxRendimiento = rendimientoActual;
                ganador = jugadorUno;
                carroGanador = vehiculoUno;
            }
        }
        // Evaluar Jugador 2
        if (jugadorDos != null && vehiculoDos != null) {
            double rendimientoActual = (vehiculoDos.getVelocidad() + vehiculoDos.getAceleracion())
                                     * vehiculoDos.getManejo()
                                     / (vehiculoDos.getFrenado() == 0 ? 0.01 : vehiculoDos.getFrenado());
            if (rendimientoActual > maxRendimiento) {
                maxRendimiento = rendimientoActual;
                ganador = jugadorDos;
                carroGanador = vehiculoDos;
            }
        }
        // Evaluar Jugador 3
        if (jugadorTres != null && vehiculoTres != null) {
            double rendimientoActual = (vehiculoTres.getVelocidad() + vehiculoTres.getAceleracion())
                                     * vehiculoTres.getManejo()
                                     / (vehiculoTres.getFrenado() == 0 ? 0.01 : vehiculoTres.getFrenado());
            if (rendimientoActual > maxRendimiento) {
                maxRendimiento = rendimientoActual;
                ganador = jugadorTres;
                carroGanador = vehiculoTres;
            }
        }
        // Evaluar Jugador 4
        if (jugadorCuatro != null && vehiculoCuatro != null) {
            double rendimientoActual = (vehiculoCuatro.getVelocidad() + vehiculoCuatro.getAceleracion())
                                     * vehiculoCuatro.getManejo()
                                     / (vehiculoCuatro.getFrenado() == 0 ? 0.01 : vehiculoCuatro.getFrenado());
            if (rendimientoActual > maxRendimiento) {
                maxRendimiento = rendimientoActual;
                ganador = jugadorCuatro;
                carroGanador = vehiculoCuatro;
            }
        }
        
        if (ganador != null) {
            // Sumar punto al ganador
            ganador.setTablaDePuntuacion(ganador.getTablaDePuntuacion() + 1);
            ganador.setContadorCarrerasGanadas(ganador.getContadorCarrerasGanadas() + 1);
            JOptionPane.showMessageDialog(null, "🧑Lucas: ¡En una demostración de pura ingeniería, el ganador por mejor tuneo es... " + ganador.getNombreDeUsuario() + "!\n¡Su rendimiento fue de: " + String.format("%.2f", maxRendimiento) + "!");
        } else {
            // Este else debería ser raro si numParticipantesValidos >= 2 y la lógica es correcta
            JOptionPane.showMessageDialog(null, "🧑Lucas: Hubo un problema al determinar el ganador de la carrera por tuneo. ¿Están todos los vehículos con atributos válidos?");
        }
    }
} // Fin Clase MotorSport
