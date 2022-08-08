from flask import Flask, request, jsonify, render_template
from usuarios import Usuarios


app = Flask(__name__)


@app.route("/users", methods=["GET", "POST"])
def Buscar():
    if request.method == "POST":

        req = request.form
        req2 = request.form.to_dict()
        if "edad" in req2:
            usuario = req["usuario"]
            nombre = req["nombre"]
            password = req["password"]
            edad = req["edad"]
            registro = Usuarios().agregar_nuevo(usuario, nombre, edad, password)
            if registro == False:
                return render_template(
                    "index.html", name="El usuario ya existe usar otro"
                )
            elif registro == "No":
                return render_template(
                    "index.html", name="ocurrio un error intentor de nuevo"
                )
            else:
                return f"registro exitoso tu token es {registro}"

        else:
            usuario = req["usuario"]
            password = req["password"]
            login = Usuarios().login(usuario, password)
            if login == False:
                return render_template(
                    "index.html", loginno="Usuario o contraseño erroneos"
                )
            else:
                return jsonify(login)
    return render_template("index.html", name="", loginno="")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
