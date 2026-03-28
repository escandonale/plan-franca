from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/datos')
def enviar_datos():
    return jsonify({"mensaje":"Conexión exitosa."})

if __name__ == '__main__':
    app.run(host='192.168.1.136', port=5000)