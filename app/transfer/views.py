from flask import jsonify, request, abort
from flask_cors import CORS
from . import transfer, Transfer


cors = CORS(transfer, resources={r"*": {"origins": "http://localhost:5000"}})


@transfer.route('/gettransfer')
def gettransfer():
    response = Transfer.get_transfers()
    return jsonify(response)


@transfer.route('/canceltransfer', methods=['POST'])
def canceltransfer():
    if not request.json:
        return abort(500)
    transfer_id = request.json.get('id')
    trans = Transfer.get_transfer(transfer_id)
    response = trans.cancel()
    return jsonify(response)


@transfer.route('/deletetransfer', methods=['POST'])
def deletetransfer():
    if not request.json:
        return abort(500)
    transfer_id = request.json.get('id')
    trans = Transfer.get_transfer(transfer_id)
    if trans:
        response = trans.delete()
    else:
        response = 500
    return jsonify(response)

@transfer.route('/updatetransfer', methods=['POST'])
def updatetransfer():
    if not request.json:
        return abort(500)
    transf_id = request.json.get('id')
    nome = request.json.get('nome')
    currency = request.json.get('currency')
    valor_compra = request.json.get('valor_compra')
    valor_deposit = request.json.get('valor_deposit')
    valor_currency = request.json.get('valor_currency')
    banco = request.json.get('banco')
    banco_name = request.json.get('banco_name')
    data = request.json.get('data')
    n_transferencia = request.json.get('n_transferencia')
    imglink = request.json.get('imglink')
    status_id = request.json.get('status_id')
    status = request.json.get('status')
    trans = Transfer.get_transfer(transf_id)
    response = trans.update(nome, currency, valor_compra, valor_deposit, valor_currency,
                            banco, banco_name, data, n_transferencia, imglink, status_id, status)
    return jsonify(response)
