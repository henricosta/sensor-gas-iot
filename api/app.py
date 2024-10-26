from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
