from flask import Flask, request, redirect, url_for, send_from_directory
from correo import Correo

import os
import time

UPLOAD_FOLDER = os.path.abspath("./perfil/")

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def index():
    return "Hola mundo"

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if "ourfile" not in request.files:
            return "El campo esta vacio"

        f = request.files["ourfile"]

        if f.filename == "":
            return "Ningun archivo seleccionado"

        extencion = f.filename.split(".")
        filename = "/perfil/time_" + time.strftime("%b") + time.strftime("%d") + time.strftime("%Y") + "_" + time.strftime("%H") + "_" + time.strftime("%M") + "_" + time.strftime("%S") + "." + extencion[1]

        f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        return filename

@app.route("/enviarcorreo", methods=["POST"])
def send():
    print(request.form['correo'])
    correo = Correo(request.form['correo'])
    return correo.enviar()

@app.route("/uploads/<filename>")
def get_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)