from flask import render_template
# from flask_login import login_required
from . import home


@home.route('/', defaults={'path': ''})
@home.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')


@home.route('/boleto')
# @login_required
def boleto():
    pass


@home.route('/card')
# @login_required
def card():
    pass
