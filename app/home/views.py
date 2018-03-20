from flask import render_template, jsonify, request, abort
from . import home
# from flask_login import login_required
from flask_cors import CORS

cors = CORS(home, resources={r"*": {"origins": "http://localhost:5000"}})


@home.route('/', defaults={'path': ''})
@home.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')


