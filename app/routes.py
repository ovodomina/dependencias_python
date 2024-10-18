from flask import request, jsonify
from app import create_app

app = create_app()

@app.route('/somar', methods=['GET'])
def somar():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    resultado = a + b
    return jsonify({"resultado": resultado})

@app.route('/subtrair', methods=['GET'])
def subtrair():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    resultado = a - b
    return jsonify({"resultado": resultado})
