from flask import jsonify, request, abort
from flask_cors import CORS
from . import company, Company


cors = CORS(company, resources={r"*": {"origins": "http://localhost:5000"}})


@company.route('/getempresas')
def getempresas():
    response = Company.get_companies()
    return jsonify(response)

