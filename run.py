import requests
from flask import Flask, render_template, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from backend.config import Config
from werkzeug.security import generate_password_hash

app = Flask(__name__, static_folder = "./dist/static", template_folder = "./dist")
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy(app)
from backend.auth.user import Users

# db = pymysql.connect(Config.db_host, Config.db_username, Config.db_password, Config.db_name, cursorclass=pymysql.cursors.DictCursor)


# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/', defaults = {'path' : ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template('index.html')

@app.route('/user/login', methods = ['POST'])
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

@app.route('/user/register', methods = ['POST'])
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

# @app.route('/boleto', methods = ['GET'])
# def get_bol():
#     boletos = 
