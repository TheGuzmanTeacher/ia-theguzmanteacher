from flask import Flask, request, jsonify
from modelo_ia import responder_pregunta

app = Flask(__name__)

@app.route('/preguntar', methods=['POST'])
def preguntar():
    datos = request.get_json()
    pregunta = datos['pregunta']
    respuesta = responder_pregunta(pregunta)
    return jsonify({"respuesta": respuesta})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)