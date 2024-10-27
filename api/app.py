from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello, World!"})


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
