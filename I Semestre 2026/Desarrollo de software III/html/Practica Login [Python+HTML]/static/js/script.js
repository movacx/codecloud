// ---------------------------------------------------
// Obtiene el formulario por ID
// ---------------------------------------------------
const formulario = document.getElementById("formulario");


// ---------------------------------------------------
// Evento submit
// Se ejecuta cuando el usuario presiona Enviar
// ---------------------------------------------------
formulario.addEventListener("submit", function(event) {

    // Muestra mensaje en consola
    console.log("Formulario enviado");

    // Obtiene valores de los campos
    const nombre = document.getElementById("nombre").value;

    const correo = document.getElementById("correo").value;

    // Validación básica
    if(nombre === "" || correo === "") {

        alert("Todos los campos son obligatorios");

        // Cancela envío
        event.preventDefault();
    }
});
