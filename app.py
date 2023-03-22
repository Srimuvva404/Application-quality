from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Test!'
@app.route('/number/<int:n>')
def check_number(n):
    if n > 200:
        message = 'high'
    else:
        message = 'low'
    return jsonify({'number': n, 'message': message})
