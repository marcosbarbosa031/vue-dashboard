from app import db
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(65), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(128))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>\n<email {}>'.format(self.username, self.email)

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def login(username, password):
        user = Users.query.filter_by(username=username).first()
        if not user:
            response = {
                'err_msg': "Invalid Username",
                'return': False
            }
        else:
            if not user.check_password(password):
                response = {
                    'err_msg': "Invalid Password",
                    'return': False
                }
            else:
                response = {
                    'err_msg': False,
                    'return': True
                }
        return response
    
    @staticmethod
    def register(username, password, repassword, email):
        if password != repassword:
            response = {
                'err_msg': "Passwords are different.",
                'return': False
            }
        else:
            user = Users.query.filter_by(username=username).first()
            e = Users.query.filter_by(email=email).first()
            if user:
                response = {
                    'err_msg': "Username unavailable.",
                    'return': False
                }
            elif e:
                response = {
                    'err_msg': "Email address unavailable.",
                    'return': False
                }
            else:
                user = Users(username=username, password=password, email=email).insert()
                response = {
                    'err_msg': "User registered sucessully.",
                    'return': True
                }
        return response
    
class Boleto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empresa = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(65), nullable=False)
    data = db.Column(db.Date, nullable=False)
    d_vencimento = db.Column(db.Date, nullable=False)
    documento = db.Column(db.String(65), nullable=False)
    num_pedido = db.Column(db.Integer, nullable=False)
    cod_barra = db.Column(db.String(65), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False)
    valor_brl = db.Column(db.Float, nullable=False)
    valor_moeda = db.Column(db.Float, nullable=False)
    moeda = db.Column(db.String(65), nullable=False)
    status = db.Column(db.String(30), default='1')
    verify = db.Column(db.String(70), nullable=True)
    hora = db.Column(db.Time, nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_boletos():
        bol = Boleto.query.filter_by()
        if not bol:
            response = {
                'error_msg' : "There's no Boleto to show.",
                'return' : False
            }
        else:
            resp = jsonify(bol)
            response = {
                'error_msg' : False,
                'return' : resp
            }
        return response
    

