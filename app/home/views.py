from flask import render_template, jsonify, request, abort
from . import home
from app.user.model import Boleto, Card, Transfer
# from flask_login import login_required
from flask_cors import CORS

cors = CORS(home, resources={r"*": {"origins": "http://localhost:5000"}})


@home.route('/', defaults={'path': ''})
@home.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')


@home.route('/getboleto')
# @login_required
def boleto():
    response = Boleto.get_boletos()
    return jsonify(response)

@home.route('/getcard')
# @login_required
def card():
    response = Card.get_cards()
    return jsonify(response)

@home.route('/gettransfer')
def transfer():
    response = Transfer.get_transfers()
    return jsonify(response)

@home.route('/updateboleto', methods=['POST'])
def update_boleto():
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



