from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])  # Define la ruta principal
def index():
    if request.method == "POST":
        data = dict()
        data["nombre"] = request.form["nombre"]  # Obtiene el valor del campo nombre
        data["edad"] = request.form["edad"] # Obtiene el valor del campo edad
        print(data)
        return redirect("/resultados", data = data) 
    else:
        return render_template("index.html")
@app.route("/resultados")
def resultados(data):
    print(data)
    return render_template("templates/index.html")
if __name__ == "__main__":
    app.run(debug=True)  # Inicia el servidor en modo de desarrollo