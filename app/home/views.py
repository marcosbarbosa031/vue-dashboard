from flask import render_template, jsonify
from . import home
from app.user.model import Boleto
# from flask_login import login_required


@home.route('/', defaults={'path': ''})
@home.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')


@home.route('/boleto')
# @login_required
def boleto():
    response = Boleto.get_boletos()
    return jsonify(response)


@home.route('/card')
# @login_required
def card():
    pass
