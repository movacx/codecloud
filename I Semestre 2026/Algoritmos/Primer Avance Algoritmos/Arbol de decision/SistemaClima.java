public class SistemaClima {
    Nodo raiz;
	
	
	//======================================================================================================================//
    public void construirArbol() {
        Nodo hojaMontano = new Nodo("ZONA MONTANO HÚMEDO");
        Nodo hojaBosqueSeco = new Nodo("BOSQUE TROPICAL SECO");
        Nodo hojaTropicalHumedo = new Nodo("TROPICAL HÚMEDO");

        Nodo nodoHumedad = new Nodo("¿Humedad relativa > 80%?", "humedad", 80);
        nodoHumedad.nodoIzquierdo = hojaBosqueSeco;
        nodoHumedad.nodoDerecho = hojaTropicalHumedo;

        Nodo nodoLluvia = new Nodo("¿Precipitación anual > 2000 mm?", "precipitacion", 2000);
        nodoLluvia.nodoIzquierdo = nodoHumedad;
        nodoLluvia.nodoDerecho = hojaTropicalHumedo;

        Nodo nodoAltura = new Nodo("¿Altitud > 1000 msnm?", "altitud", 1000);
        nodoAltura.nodoIzquierdo = nodoLluvia;
        nodoAltura.nodoDerecho = hojaMontano;

        raiz = new Nodo("¿Temperatura promedio > 24°C?", "temperatura", 24);
        raiz.nodoIzquierdo = nodoAltura;
        raiz.nodoDerecho = nodoLluvia;
    }
    
	//======================================================================================================================//
    public void clasificarZona(ZonaClimatica zona) {
        Nodo actual = raiz;
        int paso = 1;

        System.out.println("==================================================");
        System.out.println("Clasificando zona: " + zona.nombre);
        System.out.println("==================================================");
        System.out.println("Paso\tPregunta evaluada\t\t\tRespuesta\t\tSiguiente paso");
        System.out.println("-----------------------------------------------------------------------------------------");

        while (actual.esHoja() == false) {
            double datoParaEvaluar = 0.0;

            if (actual.atributo.equals("temperatura")) { datoParaEvaluar = zona.temperatura; }
            if (actual.atributo.equals("altitud")) { datoParaEvaluar = zona.altitud; }
            if (actual.atributo.equals("precipitacion")) { datoParaEvaluar = zona.precipitacion; }
            if (actual.atributo.equals("humedad")) { datoParaEvaluar = zona.humedad; }

            String textoRespuesta = "No (" + actual.atributo + " = " + datoParaEvaluar + ")";
            String textoSiguiente = "Ir al nodo IZQUIERDO";
            Nodo proximoNodo = actual.nodoIzquierdo;

            if (datoParaEvaluar > actual.umbral) {
                textoRespuesta = "Si (" + actual.atributo + " = " + datoParaEvaluar + ")";
                textoSiguiente = "Ir al nodo DERECHO";
                proximoNodo = actual.nodoDerecho;
            }

            System.out.println(paso + "\t" + actual.pregunta + "\t" + textoRespuesta + "\t" + textoSiguiente);
            
            actual = proximoNodo;
            paso = paso + 1;
        }

        System.out.println("-----------------------------------------------------------------------------------------");
        System.out.println("RESULTADO FINAL: " + actual.clasificacionFinal + "\n");
    }
    
	//======================================================================================================================//
    public void evaluarMatriz(ZonaClimatica[] datos) {
        int aciertos = 0;
        int errores = 0;

        System.out.println("=== EVALUACION DE RENDIMIENTO ===");
        System.out.println("Zona Evaluada\t\tClase Real\t\tPredicción del Árbol\tResultado");
        System.out.println("-----------------------------------------------------------------------------------------");

        for (int i = 0; i < datos.length; i++) {
            ZonaClimatica zona = datos[i];
            
            Nodo actual = raiz;
            while (actual.esHoja() == false) {
                double dato = 0.0;
                if (actual.atributo.equals("temperatura")) { dato = zona.temperatura; }
                if (actual.atributo.equals("altitud")) { dato = zona.altitud; }
                if (actual.atributo.equals("precipitacion")) { dato = zona.precipitacion; }
                if (actual.atributo.equals("humedad")) { dato = zona.humedad; }

                if (dato > actual.umbral) {
                    actual = actual.nodoDerecho;
                } else {
                    actual = actual.nodoIzquierdo;
                }
            }
            
            String prediccion = actual.clasificacionFinal;
            String resultado = "ERROR";
            
            if (prediccion.equals(zona.claseReal)) {
                resultado = "ACIERTO";
                aciertos = aciertos + 1;
            } else {
                errores = errores + 1;
            }

            System.out.printf("%-20s\t%-20s\t%-20s\t%s\n", zona.nombre, zona.claseReal, prediccion, resultado);
        }

        System.out.println("-----------------------------------------------------------------------------------------");
        System.out.println("Total de Aciertos : " + aciertos);
        System.out.println("Total de Errores  : " + errores);
        System.out.println("Precisión Global  : " + ((aciertos * 100) / datos.length) + "%");
    }
    
	//======================================================================================================================//
    public static void main(String[] args) {
        SistemaClima clasificador = new SistemaClima();
        clasificador.construirArbol();

        ZonaClimatica[] datos = new ZonaClimatica[20];
        
        datos[0] = new ZonaClimatica("San José", "ZONA MONTANO HÚMEDO", 22, 1800, 1170, 75);
        datos[1] = new ZonaClimatica("Cartago", "ZONA MONTANO HÚMEDO", 19, 2000, 1435, 82);
        datos[2] = new ZonaClimatica("Heredia", "ZONA MONTANO HÚMEDO", 21, 1900, 1150, 78);
        datos[3] = new ZonaClimatica("Alajuela", "ZONA MONTANO HÚMEDO", 23, 1700, 952, 70);
        datos[4] = new ZonaClimatica("Moravia", "ZONA MONTANO HÚMEDO", 20, 1850, 1200, 76);
        datos[5] = new ZonaClimatica("Coronado", "ZONA MONTANO HÚMEDO", 18, 2200, 1380, 85);
        datos[6] = new ZonaClimatica("Liberia", "BOSQUE TROPICAL SECO", 28, 1500, 144, 60);
        datos[7] = new ZonaClimatica("Nicoya", "BOSQUE TROPICAL SECO", 27, 1600, 120, 65);
        datos[8] = new ZonaClimatica("Santa Cruz", "BOSQUE TROPICAL SECO", 29, 1400, 50, 58);
        datos[9] = new ZonaClimatica("Bagaces", "BOSQUE TROPICAL SECO", 28, 1300, 80, 55);
        datos[10] = new ZonaClimatica("Cañas", "BOSQUE TROPICAL SECO", 29, 1450, 90, 59);
        datos[11] = new ZonaClimatica("Puntarenas", "BOSQUE TROPICAL SECO", 28, 1700, 10, 70);
        datos[12] = new ZonaClimatica("Limón", "TROPICAL HÚMEDO", 26, 3500, 10, 88);
        datos[13] = new ZonaClimatica("Guápiles", "TROPICAL HÚMEDO", 25, 4000, 260, 85);
        datos[14] = new ZonaClimatica("Siquirres", "TROPICAL HÚMEDO", 26, 3800, 60, 87);
        datos[15] = new ZonaClimatica("Puerto Viejo", "TROPICAL HÚMEDO", 27, 3200, 5, 86);
        datos[16] = new ZonaClimatica("Turrialba", "TROPICAL HÚMEDO", 24, 2800, 646, 84);
        datos[17] = new ZonaClimatica("San Carlos", "TROPICAL HÚMEDO", 25, 3100, 250, 83);
        datos[18] = new ZonaClimatica("Sarapiquí", "TROPICAL HÚMEDO", 26, 3900, 100, 89);
        datos[19] = new ZonaClimatica("Golfito", "TROPICAL HÚMEDO", 27, 4500, 15, 90);

        clasificador.clasificarZona(datos[0]); 
        clasificador.clasificarZona(datos[6]); 
        
        clasificador.evaluarMatriz(datos);
    }
}
