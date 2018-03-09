from flask import jsonify, request, abort
from . import company
from app.user.model import Company
from flask_cors import CORS


cors = CORS(company, resources={r"*": {"origins": "http://localhost:5000"}})


@company.route('/getempresas')
def get_empresas():
    response = Company.get_companies()
    return jsonify(response)

