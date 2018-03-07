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
    data = db.Column(db.String(65), nullable=False)
    d_vencimento = db.Column(db.String(65), nullable=False)
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

    
    def dump_date(value, data):
        """Deserialize datetime object into string form for JSON processing.
        :param vencimento:
        """
        if value is None:
            return None
        return data.strftime("%Y-%m-%d")

    def dump_time(value, data):
        """Deserialize datetime object into string form for JSON processing.
        :param vencimento:
        """
        if value is None:
            return None
        return data.strftime("%H:%M:%S")

    @staticmethod
    def serialize(boleto):
        return {
            'id': boleto.id,
            'empresa': boleto.empresa,
            'nome': boleto.nome,
            'data': boleto.dump_date(boleto.data),
            'd_vencimento': boleto.dump_date(boleto.d_vencimento),
            'documento': boleto.documento,
            'num_pedido': boleto.num_pedido,
            'cod_barra': boleto.cod_barra,
            'email': boleto.email,
            'valor_brl': boleto.valor_brl,
            'valor_moeda': boleto.valor_moeda,
            'moeda': boleto.moeda,
            'status': boleto.status,
            'verify': boleto.verify,
            'hora': boleto.dump_time(boleto.hora)
        }

    @staticmethod
    def get_boletos():
        bol = Boleto.query.filter_by()

        if not bol:
            response = {
                'error_msg': "There's no Boleto to show.",
                'return': False
            }
        else:
            resp = [Boleto.serialize(aux) for aux in bol]
            response = {
                'error_msg': False,
                'return': resp
            }
        return response

class Card(db.Model):
    __tablename__ = 'credit_card'

    id = db.Column(db.Integer, primary_key=True)
    empresa = db.Column(db.Integer, nullable=False)
    nome_cartao = db.Column(db.String(65), nullable=False)
    n_transacao = db.Column(db.String(65), nullable=True, default=None)
    tipo_cartao = db.Column(db.String(65), nullable=False)
    n_cartao = db.Column(db.String(65), nullable=False)
    n_order = db.Column(db.String(65), nullable=False)
    valor_brl = db.Column(db.Float, nullable=False)
    valor_usd = db.Column(db.Float, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    data = db.Column(db.String(65), nullable=False)
    status_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(30), nullable=False)
    motivo = db.Column(db.String(65), nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(65), nullable=False)
    data_inicio = db.Column(db.String(65), nullable=True, default=None)
    data_fim = db.Column(db.String(65), nullable=True, default=None)
    tipo_pag = db.Column(db.String(20), nullable=True, default='a vista')
    recurrentId = db.Column(db.String(60), nullable=True, default=None)
    ip = db.Column(db.String(45), nullable=True, default=None)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def dump_date(data):
        """Deserialize datetime object into string form for JSON processing.
        :param vencimento:
        """
        if data is None:
            return None
        return data.strftime("%Y-%m-%d")

    @staticmethod
    def dump_time(data):
        """Deserialize datetime object into string form for JSON processing.
        :param vencimento:
        """
        if data is None:
            return None
        return data.strftime("%H:%M:%S")

    @staticmethod
    def serialize(card):
        return {
            'id': card.id,
            'empresa' : card.empresa,
            'nome_cartao' : card.nome_cartao,
            'n_transacao' : card.n_transacao,
            'tipo_cartao' : card.tipo_cartao,
            'n_cartao' : card.n_cartao,
            'n_order' : card.n_order,
            'valor_brl' : card.valor_brl,
            'valor_usd': card.valor_usd,
            'hora' : card.dump_time(card.hora),
            'data' : card.dump_date(card.data),
            'status_id' : card.status_id,
            'status' : card.status,
            'motivo' : card.motivo,
            'currency' : card.currency,
            'email' : card.email,
            'data_inicio' : card.data_inicio,
            'data_fim' : card.data_fim,
            'tipo_pag' : card.tipo_pag,
            'recurrentId' : card.recurrentId,
            'ip' : card.ip
        }
    
    @staticmethod
    def get_cards():
        card = Card.query.filter_by()

        if not card:
            response = {
                'error_msg' : "There's no card to show.",
                'return' : False
            }
        else:
            resp = [Card.serialize(aux) for aux in card]
            response = {
                'error_msg' : False,
                'return' : resp
            }
        return response
    
