from flask import render_template, jsonify
from . import home
from app.user.model import Boleto, Card
# from flask_login import login_required
from flask_cors import CORS, cross_origin

cors = CORS(home, resources={"/api/*": {"origins": "http://localhost:5000"}})


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
