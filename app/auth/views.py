from flask import render_template, jsonify, request, abort
# from flask_login import login_user
from werkzeug.security import generate_password_hash
from . import auth
from app.user.model import Users
from flask_cors import CORS, cross_origin

cors = CORS(auth, resources={r"/api/*": {"origins": "http://localhost:5000"}})


@auth.route('/user/login', methods=['POST'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def user_login():
    if not request.json:
        return abort(500)
    username = request.json.get('user')
    password = request.json.get('pass')
    response = Users.login(username, password)
    return jsonify(response)


@auth.route('/user/register', methods=['POST'])
def user_register():
    if not request.json:
        return abort(500)
    username = request.json.get('user')
    password = request.json.get('pass')
    repassword = request.json.get('repass')
    email = request.json.get('email')
    response = Users.register(username, password, repassword, email)
    return jsonify(response)
