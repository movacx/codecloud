# Importa las clases necesarias de Flask
from flask import Flask, render_template, request

# Crea la aplicación Flask
app = Flask(__name__)

# ---------------------------------------------------
# Ruta principal
# Muestra el formulario HTML
# ---------------------------------------------------
@app.route('/')
def inicio():

    # Muestra la vista formulario.html
    return render_template('formulario.html')


# ---------------------------------------------------
# Ruta para recibir los datos enviados
# desde JavaScript usando Fetch
# ---------------------------------------------------
@app.route('/guardar', methods=['POST'])
def guardar():

    # Obtiene los datos del formulario
    nombre = request.form['nombre']
    correo = request.form['correo']

    # Muestra los datos en consola
    print("Nombre:", nombre)
    print("Correo:", correo)

    # Respuesta del servidor
    return f'''
    <h2>Datos recibidos correctamente</h2>
    <p>Nombre: {nombre}</p>
    <p>Correo: {correo}</p>
    <a href="/">Volver</a>
    '''


# ---------------------------------------------------
# Punto de inicio de la aplicación
# ---------------------------------------------------
if __name__ == '__main__':

    # Inicia el servidor Flask
    app.run(debug=True)
