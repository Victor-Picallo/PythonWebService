from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido a mi servidor Python con Flask!"

@app.route('/saluda')
def saluda():
    return "¡Hola!"

# /suma?a=6&b=8
@app.route('/suma')
def suma(a, b):
    a = request.args.get('a')
    b = request.args.get('b')
    resultado = a + b
    return f'La suma es: {resultado}'

# Arranca el servido (Demonio/Servicio) en el puerto por defecto 5000
if __name__ == "__main__":
    app.run()