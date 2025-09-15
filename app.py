from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Función para cargar las sesiones desde el archivo
def cargar_sesiones():
    try:
        with open('sesiones.txt', 'r') as file:
            return [json.loads(line) for line in file]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Función para guardar una nueva sesión
def guardar_sesion(sesion):
    with open('sesiones.txt', 'a') as file:
        json.dump(sesion, file)
        file.write('\n')

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Recoge los datos del formulario
        nueva_sesion = {
            "fecha": request.form["fecha"],
            "duracion": request.form["duracion"],
            "musculos": request.form["musculos"]
        }
        guardar_sesion(nueva_sesion)
        return redirect(url_for('index'))
    
    sesiones = cargar_sesiones()
    return render_template("index.html", sesiones=sesiones)

if __name__ == "__main__":
    app.run(debug=True)