from flask import jsonify, request, abort
from flask_cors import CORS
from . import card, Card
from ..company.model import Company


cors = CORS(card, resources={r"*": {"origins": "http://localhost:5000"}})


@card.route('/getcard')
def getcard():
    response = Card.get_cards()
    return jsonify(response)

@card.route('/cancelcard', methods=['POST'])
def cancelcard():
    if not request.json:
        return abort(500)
    card_id = request.json.get('id')
    c = Card.get_cartao(card_id)
    response = c.cancel()
    return jsonify(response)


@card.route('/deletecard', methods=['POST'])
def deletecard():
    if not request.json:
        return abort(500)
    card_id = request.json.get('id')
    c = Card.get_cartao(card_id)
    if c:
        response = c.delete()
    else:
        response = 500
    return jsonify(response)

@card.route('/updatecard', methods=['POST'])
def updatecard():
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
    response = card.update(nome_cartao, n_transacao, tipo_cartao, n_cartao, n_order, valor_brl, valor_usd,
                           hora, data, status_id, status, motivo, currency, email, data_inicio, data_fim, tipo_pag)
    return jsonify(response)
