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

@home.route('/updatecard', methods=['POST'])
def update_card():
    if not request.json:
        return abort(500)
    card_id = request.json.get('id')
    nome_cartao = request.json.get('nome_cartao')
    n_transacao = request.json.get('n_transacao')
    tipo_cartao = request.json.get('tipo_cartao')
    n_cartao = request.json.get('n_cartao')
    n_order = request.json.get('n_order')
    valor_brl = request.json.get('valor_brl')
    valor_usd = request.json.get('valor_usd')
    hora = request.json.get('hora')
    data = request.json.get('data')
    status_id = request.json.get('status_id')
    status = request.json.get('status')
    motivo = request.json.get('motivo')
    currency = request.json.get('currency')
    email = request.json.get('email')
    data_inicio = request.json.get('data_inicio')
    data_fim = request.json.get('data_fim')
    tipo_pag = request.json.get('tipo_pag')
    card = Card.get_cartao(card_id)
    response = card.update(nome_cartao, n_transacao, tipo_cartao, n_cartao, n_order, valor_brl, valor_usd, hora, data, status_id, status, motivo, currency, email, data_inicio, data_fim, tipo_pag)
    return jsonify(response)

@home.route('/updatetransfer', methods=['POST'])
def update_transfer():
    if not request.json:
        return abort(500)
    transf_id = request.json.get('id')