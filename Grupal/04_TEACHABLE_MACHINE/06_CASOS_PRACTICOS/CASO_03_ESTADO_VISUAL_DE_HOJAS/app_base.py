# Punto de partida para el estudiante; no incluye IA todavía.
# Completa la función siguiendo los proyectos 01 a 05.
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    resultado = ""
    if request.method == "POST":
        archivo = request.files.get("foto")
        if archivo and archivo.filename:
            resultado = "Archivo recibido. Pendiente: conectar tu modelo."
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)