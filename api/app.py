from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, Response, request
from flask_cors import CORS
from datetime import datetime
import database

import os

load_dotenv()

PORT=os.getenv('PORT')
API_URL=os.getenv('API_URL')

VALOR_VAZAMENTO = 70

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/teste', methods=['GET'])
def api_teste():
    return Response(status=200)


@app.route('/api/ultima-leitura', methods=['GET'])
def recuperar_ultima_leitura():
    row = database.get_ultima_leitura()
    
    if row is None:
        return jsonify({'data': []})
    
    data = [{'id': row['id'], 'timestamp': row['timestamp'], 'value': row['value'], 'vazamento': row['vazamento'], 'identificador': row['identificador']}]
    
    return jsonify({'data': data})


@app.route('/api/recuperar-dados', methods=['GET'])
def recuperar_dados():
    page = request.args.get('page')
    
    if page:
        rows = database.get_leituras(page=page)
    else:
        rows = database.get_leituras()
    
    data = [
        {'id': row['id'], 'timestamp': row['timestamp'], 'value': row['value'], 'vazamento': row['vazamento'], 'identificador': row['identificador']}
        for row in rows
    ]

    return jsonify({ 'data': data })


@app.route('/api/salvar-dados', methods=['GET'])
def salvar_dados():
    value = request.args.get('value')
    identificador = request.args.get('identificador')
    
    if value is None:
        return Response(status=400)
    
    timestamp = datetime.now()
    database.salvar_dados_leitura(value=value, vazamento=float(value) > VALOR_VAZAMENTO,  identificador=identificador, timestamp=timestamp)
    
    return Response(status=200)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', API_URL=API_URL)

if __name__ == '__main__':
    app.run(debug=True, port=PORT)
