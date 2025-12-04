from flask import Flask, jsonify, render_template_string, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Bienvenido a mi servidor Python con Flask"


# /suma?a=6&b=8
@app.route("/suma")
def suma():
    a = request.args.get("a", type=int, default=0)
    b = request.args.get("b", type=int, default=0)
    resultado = a + b
    return f"La suma es {resultado}"


@app.route("/saluda")
def saluda():
    return "Hola!!!!"


form_html = """
    <form action="/login" method="post">
        <input name="user" />
        <input name="pass" />
        <button>Enviar</button>
    </form>
"""


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template_string(form_html)
    elif request.method == "POST":
        user = request.form.get("user")
        password = request.form.get("pass")
        if user == "root" and password == "Ad1234":
            return "Login correcto", 200
        else:
            return "Nombre de usuario o pass incorrecto", 401
    else:
        pass


@app.route("/api/suma", methods=["POST"])
def suma_api():
    data = request.get_json()
    num1 = data.get("num1", 0)
    num2 = data.get("num2", 0)
    resultado = num1 + num2
    dict = {"resultado": resultado}
    return jsonify(dict)


# arranca el servidor (demonio / servicio)
# puerto por defecto (5000?)

if __name__ == "__main__":
    app.run()


# Para arrancar el servidor:
#  - Metodo malo python main.py