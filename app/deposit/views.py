from flask import jsonify, request, abort
from flask_cors import CORS
from . import deposit, Deposit
from ..company.model import Company


cors = CORS(deposit, resources={r"*": {"origins": "http://localhost:5000"}})


@deposit.route('/getdeposit')
def getdeposit():
    response = Deposit.get_depositos()
    return jsonify(response)

@deposit.route('/canceldeposit', methods=['POST'])
def canceldeposit():
    if not request.json:
        return abort(500)
    deposit_id = request.json.get('id')
    dep = Deposit.getdeposit(deposit_id)
    response = dep.cancel()
    return jsonify(response)

@deposit.route('/deletedeposit', methods=['POST'])
def deletedeposit():
    if not request.json:
        return abort(500)
    depoist_id = request.json.get('id')
    dep = Deposit.get_deposito(depoist_id)
    if dep:
        response = dep.delete()
    else:
        response = 500
    return jsonify(response)

@deposit.route('/updatedeposit', methods=['POST'])
def updatedeposit():
    if not request.json:
        return abort(500)
    deposit_id = request.json.get('id')
    empresa = request.json.get('empresa')
    valor_brl = request.json.get('valor_brl')
    valor_usd = request.json.get('davalor_usdta')
    moeda = request.json.get('moeda')
    data = request.json.get('data')
    n_deposito = request.json.get('n_deposito')
    imglink = request.json.get('imglink')
    status = request.json.get('status')
    dep = Deposit.getdeposit(deposit_id)
    response = dep.update(empresa, valor_brl, valor_usd, moeda, data, n_deposito, imglink, status)
    return jsonify(response)