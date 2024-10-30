from flask import Flask, jsonify, render_template, Response

import database

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api_teste():
    return Response(status=200)


@app.route('/api/recuperar-dados', methods=['GET'])
def recuperar_dados():
    rows = database.get_all_leituras()
    
    data = [
        { 'id': row[0], 'timestamp': row[1], 'value': row[2] }
        for row in rows
    ]

    return jsonify({ 'data': data })


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
