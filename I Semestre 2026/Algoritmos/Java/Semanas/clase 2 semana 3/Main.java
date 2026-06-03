public class Main 
{
    public static void main(String[] args) 
    {

        Lista listaEmpleados = new Lista();

        // Insertar empleados
        listaEmpleados.insertar(new Empleado("101", 25));
        listaEmpleados.insertar(new Empleado("102", 30));
        listaEmpleados.insertar(new Empleado("103", 25));

        System.out.println("----- PRUEBA INSERTAR E IMPRIMIR -----");
        listaEmpleados.imprimirEmpleados();

        // a. Buscar por cedula
        System.out.println("\n----- PRUEBA BUSCAR -----");
        System.out.println("Buscar 102 (debe ser true): " 
                + listaEmpleados.existeEmpleado("102"));
        System.out.println("Buscar 999 (debe ser false): " 
                + listaEmpleados.existeEmpleado("999"));

        // b. Contar por edad
        System.out.println("\n----- PRUEBA CONTAR POR EDAD -----");
        System.out.println("Edad 25 (debe ser 2): " 
                + listaEmpleados.contarPorEdad(25));
        System.out.println("Edad 30 (debe ser 1): " 
                + listaEmpleados.contarPorEdad(30));

        // c. Cantidad total
        System.out.println("\n----- PRUEBA CANTIDAD TOTAL -----");
        System.out.println("Total (debe ser 3): " 
                + listaEmpleados.cantidadEmpleados());

        // e. Eliminar lista
        System.out.println("\n----- PRUEBA ELIMINAR LISTA -----");
        listaEmpleados.eliminarLista();
        System.out.println("Total (despues de eliminar debe ser 0): " 
                + listaEmpleados.cantidadEmpleados());

        System.out.println("\n---------Imprimir lista----------- ");
        listaEmpleados.imprimirEmpleados();
        System.out.println("Imprimir lista (debe estar vacia):"
				+ listaEmpleados.imprimirEmpleados());
    }
}
