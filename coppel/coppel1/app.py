from flask import Flask, request, jsonify, render_template
from buscador import Buscador


app = Flask(__name__)


@app.route("/searchComics", methods=["GET", "POST"])
def Buscar():
    if request.method == "POST":
        req = request.form
        categoria = req["categoria"]
        nombre = req["nombre"]
        resultado = Buscador().run_buscador(categoria, nombre)
        return jsonify(resultado)
    return render_template("index.html")


@app.route("/searchToAdd", methods=["POST"])
def buscar_guardar():

    categoria = request.json["categoria"]
    nombre = request.json["nombre"]
    resultado = Buscador().run_buscador(categoria, nombre)
    return jsonify(resultado)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
