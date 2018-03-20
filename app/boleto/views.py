from flask import jsonify, request, abort
from flask_cors import CORS
from . import boleto, Boleto
from ..company.model import Company


cors = CORS(boleto, resources={r"*": {"origins": "http://localhost:5000"}})


@boleto.route('/getboleto')
def getboleto():
    response = Boleto.get_boletos()
    return jsonify(response)


@boleto.route('/cancelboleto', methods=['POST'])
def cancelboleto():
    if not request.json:
        return abort(500)
    boleto_id = request.json.get('id')
    bol = Boleto.get_boleto(boleto_id)
    response = bol.cancel()
    return jsonify(response)


@boleto.route('/deleteboleto', methods=['POST'])
def deleteboleto():
    if not request.json:
        return abort(500)
    boleto_id = request.json.get('id')
    bol = Boleto.get_boleto(boleto_id)
    if bol:
        response = bol.delete()
    else:
        response = 500
    return jsonify(response)

@boleto.route('/updateboleto', methods=['POST'])
def updateboleto():
    if not request.json:
        return abort(500)
    boleto_id = request.json.get('id')
    nome = request.json.get('nome')
    data = request.json.get('data')
    d_vencimento = request.json.get('d_vencimento')
    documento = request.json.get('documento')
    num_pedido = request.json.get('num_pedido')
    cod_barra = request.json.get('cod_barra')
    email = request.json.get('email')
    valor_brl = request.json.get('valor_brl')
    valor_moeda = request.json.get('valor_moeda')
    moeda = request.json.get('moeda')
    hora = request.json.get('hora')
    bol = Boleto.get_boleto(boleto_id)
    response = bol.update(nome, data, d_vencimento, documento, num_pedido, cod_barra, email,
                          valor_brl, valor_moeda, moeda, hora)
    return jsonify(response)
