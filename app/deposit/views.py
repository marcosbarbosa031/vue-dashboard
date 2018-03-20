from flask import jsonify, request, abort
from flask_cors import CORS
from . import deposit, Deposit
from ..company.model import Company


cors = CORS(deposit, resources={r"*": {"origins": "http://localhost:5000"}})


@deposit.route('/getdeposit')
def getdeposit():
    response = Deposit.get_depositos()
    return jsonify(response)
