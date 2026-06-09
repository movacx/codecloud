'''
Punto de entrada para ejecutar la version web del sistema

Flujo de trabajo:
HTML > flask > service > repository > Mysql
'''
# from template import index
from service.cliente_service import ClienteService
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

app.secret_key="clave_didactica_clientes"

cliente_service = ClienteService()

@app.route("/")

def index():
    clientes = cliente_service.consultar_clientes()
    return render_template("index.html", clientes=clientes)

def consultar_estuiantes(self):
    """
    Consulta todos los estudiantes
    returns: 
        Lista de estudiantes
    """
@app.route("/clientes/nuevo", methods = ["GET", "POST"])

def nuevo_cliente():
    if request.method == "POST":
        cedula = request.form["cedula"]
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        direccion = request.form["direccion"]

        exito, mensaje = cliente_service.registrar_cliente(cedula,nombre,correo,telefono,direccion)
        flash(mensaje)

        if exito:
            return redirect(url_for("index"))
    return render_template("formulario_cliente.html")


@app.route("/clientes/editar/<int:id_clientes>", methods = ["GET","POST"])

def editar_clientes(id_cliente):
    cliente= cliente_service.buscar_cliente_por_id(id_cliente)

    if cliente is None:
        flash("Error: no existe un cliente con ese ID")
        return  redirect(url_for("index"))

    if request.method == "POST":
        cedula = request.form["cedula"]
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        direccion = request.form["direccion"]

        exito, mensaje = cliente_service.actualizar_cliente(id_cliente, cedula, nombre, correo, telefono, direccion)
        flash(mensaje)
        
        if exito:
            return  redirect(url_for("index"))
        
    return render_template("editar_cliente.html", cliente=cliente)

@app.route("/cliente/eliminar/<int:id_cliente>", methods=["GET","POST"])
def eliminar_cliente(id_cliente):
    exito, mensaje = cliente_service.eliminar_cliente(id_cliente)
    flash(mensaje)
    return redirect(url_for("index"))

if __name__ ==  "__main__":
    app.run(debug=True)
