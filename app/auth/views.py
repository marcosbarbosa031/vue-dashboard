from flask import render_template, jsonify, request, abort
from werkzeug.security import generate_password_hash
from . import auth
from app.user.model import Users
from flask_cors import CORS, cross_origin

cors = CORS(auth, resources={r"/api/*": {"origins": "http://localhost:5000"}})

@auth.route('/user/login', methods=['POST'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def login_user():
    if not request.json:
        return abort(500)
    username = request.json.get('user')
    password = request.json.get('pass')
    user = Users.query.filter_by(username=username).first()
    if not user:
        response = {
            'err_msg' : "Invalid Username",
            'return': False
        }
    else:
        if not user.check_password(password):
            response = {
                'err_msg' : "Invalid Password",
                'return': False
            }
        else:
            response = {
                'err_msg' : False,
                'return': True
            }
    return jsonify(response)


@auth.route('/user/register', methods=['POST'])
def register_user():
    if not request.json:
        return abort(500)
    username = request.json.get('user')
    password = request.json.get('pass')
    repassword = request.json.get('repass')
    email = request.json.get('email')
    if password != repassword:
        response = {
            'err_msg' : "Passwords are different.",
            'return': False
        }
    else:
        user = Users.query.filter_by(username=username).first()
        e = Users.query.filter_by(email=email).first()
        if user:
            response = {
                'err_msg' : "Username unavailable.",
                'return': False
            }
        elif e:
            response = {
                'err_msg' : "Email address unavailable.",
                'return': False
            }
        else:
            user = Users(username=username, password=password, email=email).insert()
            response = {
                'err_msg' : "User registered sucessully.",
                'return' : True
            }
    return jsonify(response)
