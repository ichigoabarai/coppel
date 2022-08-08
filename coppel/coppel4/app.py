from flask import Flask, request, jsonify, render_template
from apartados import Apartados


app = Flask(__name__)


@app.route("/getLayawayList", methods=["GET", "POST"])
def Buscar():
    if request.method == "POST":
        req = request.form
        token = req["token"]
        resultado = Apartados().buscar_apartados(token)
        if resultado == False:
            return "Debes estar registardo para poder ver tus spartados"
        elif resultado == None:
            return "No tienes ningun comic apartado"
        else:
            return render_template("apartados.html", resultado=resultado)
    return render_template("index.html", loginno="")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
