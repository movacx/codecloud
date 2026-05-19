// obtiene el formulario por id

const formulario = document.getElementById('formulario');

// Evento submit
// se ejecuta cuando el usuario presiona enviar

formulario.addEventListener('submit', function(event){

    // muestra mensaje en la consola
    console.log('Formulario enviado');

    // obtiene los valores de los campos

    const nombre = document.getElementById('nombre').value;
    const correo = document.getElementById('correo').value;

    // validacion basica
    if(nombre === "" || correo === ""){

        alert('Todos los campos son obligatorios');

        // cancelar el envio
        event.preventDefault();
    }

});