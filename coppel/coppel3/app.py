from flask import Flask, request, jsonify, render_template, redirect
from comics import Comics


app = Flask(__name__)


@app.route("/addToLayaway", methods=["GET", "POST"])
def Buscar():
    if request.method == "POST":
        req = request.form
        categoria = "comic"
        nombre = req["nombre"]
        token = req["token"]
        resultado = Comics().run_buscador(categoria, nombre, token)
        if resultado == False:
            return (
                "El Token es Incorrecto debe estar resgitrado para poder añadir comics"
            )

        elif resultado[0]["id"] == False:
            return jsonify(resultado)

        else:
            resultado[0]["token"] = token
            return render_template("busqueda.html", resultado=resultado)
    return render_template("index.html", loginno="")


@app.route("/busqueda", methods=["POST"])
def guardar():

    req = request.form
    idd = req["id"]
    title = req["title"]
    image = req["image"]
    onsaleDate = req["onsaleDate"]
    token = req["token"]
    resultado = Comics().agregar_comics(idd, title, image, onsaleDate, token)
    if resultado == False:
        return {"data": "no se pudo añadir intente de nuevo mas tarde"}
    return render_template("index.html", loginno="Se añadio satisfactoriamente")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
