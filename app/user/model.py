from app import db
from werkzeug.security import generate_password_hash, check_password_hash


# from flask_login import UserMixin
def dump_date(data):
    """Deserialize datetime object into string form for JSON processing.
    :param data:
    """
    if data is None:
        return None
    return data.strftime("%Y-%m-%d")


def dump_time(data):
    """Deserialize datetime object into string form for JSON processing.
    :param data:
    """
    if data is None:
        return None
    return data.strftime("%H:%M:%S")


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
                # user = Users(username=username, password=password, email=email).insert()
                response = {
                    'err_msg': "User registered sucessully.",
                    'return': True
                }
        return response


class Company(db.Model):
    __tablename__ = 'empresas'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    id_usuario = db.Column(db.Integer, nullable=False)
    doc_empresa = db.Column(db.String(65), nullable=False)
    nome_fantasia = db.Column(db.String(65), nullable=False)
    razao_social = db.Column(db.String(65), nullable=False)
    Saldo = db.Column(db.Float, nullable=False)
    Saldo_bloqueado = db.Column(db.Float, nullable=False)
    Saldo_disponivel = db.Column(db.Float, nullable=False)
    ativa = db.Column(db.Integer, nullable=False)
    Salt = db.Column(db.String(65), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def serialize(company):
        return {
            'id': company.id,
            'Salt': company.Salt,
            'ativa': company.ativa,
            'Saldo': company.Saldo,
            'id_usuario': company.id_usuario,
            'doc_empresa': company.doc_empresa,
            'razao_social': company.razao_social,
            'nome_fantasia': company.nome_fantasia,
            'Saldo_bloqueado': company.Saldo_bloqueado,
            'Saldo_disponivel': company.Saldo_disponivel
        }

    @staticmethod
    def get_companies():
        companies = Company.query.filter_by().order_by(Company.id)

        if not companies:
            response = {
                'error_msg': "There's no card to show.",
                'return': False
            }
        else:
            resp = [Company.serialize(aux) for aux in companies]
            response = {
                'error_msg': False,
                'return': resp
            }
        return response

    @staticmethod
    def get_company(company_id):
        company = Company.query.filter_by(id=company_id).first()
        if not company:
            return None
        else:
            return company

    def update_saldo(self, valor, atualizado):
        taxa = 0.938
        self.Saldo = (float(self.Saldo) - (float(valor) * taxa)) + (float(atualizado) * taxa)
        self.Saldo_disponivel = (float(self.Saldo_disponivel) - (float(valor) * taxa)) + (float(atualizado) * taxa)
        try:
            db.session.commit()
            return 200
        except ConnectionRefusedError:
            return 500


class Boleto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empresa = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.Date, nullable=False)
    data = db.Column(db.Date, nullable=False)
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

    @staticmethod
    def get_boleto(boleto_id):
        boleto = Boleto.query.filter_by(id=boleto_id).first()
        if not boleto:
            return None
        else:
            return boleto

    def check_status(self):
        if self.status == 2:
            return True
        return False

    def update(self, nome, data, d_vencimento, documento, num_pedido, cod_barra, email, valor_brl,
               valor_moeda, moeda, hora):
        valor_anterior = float(self.valor_brl)
        self.nome = nome
        self.data = data
        self.d_vencimento = d_vencimento
        self.documento = documento
        self.num_pedido = num_pedido
        self.cod_barra = cod_barra
        self.email = email
        self.valor_brl = valor_brl
        self.valor_moeda = valor_moeda
        self.moeda = moeda
        self.hora = hora
        try:
            db.session.commit()
            if self.check_status():
                company = Company.get_company(self.empresa)
                company.update_saldo(valor_anterior, valor_brl)
            return 200

        except ConnectionRefusedError:
            return 500

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
        bol = Boleto.query.filter_by().order_by(Boleto.id.desc())

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

    def check_status(self):
        if self.status_id == 2:
            return True
        return False

    @staticmethod
    def serialize(card):
        return {
            'id': card.id,
            'empresa': card.empresa,
            'nome_cartao': card.nome_cartao,
            'n_transacao': card.n_transacao,
            'tipo_cartao': card.tipo_cartao,
            'n_cartao': card.n_cartao,
            'n_order': card.n_order,
            'valor_brl': card.valor_brl,
            'valor_usd': card.valor_usd,
            'hora': card.dump_time(card.hora),
            'data': card.dump_date(card.data),
            'status_id': card.status_id,
            'status': card.status,
            'motivo': card.motivo,
            'currency': card.currency,
            'email': card.email,
            'data_inicio': card.data_inicio,
            'data_fim': card.data_fim,
            'tipo_pag': card.tipo_pag,
            'recurrentId': card.recurrentId,
            'ip': card.ip
        }

    @staticmethod
    def get_cards():
        card = Card.query.filter_by().order_by(Card.id.desc())

        if not card:
            response = {
                'error_msg': "There's no card to show.",
                'return': False
            }
        else:
            resp = [Card.serialize(aux) for aux in card]
            response = {
                'error_msg': False,
                'return': resp
            }
        return response

    @staticmethod
    def get_cartao(card_id):
        card = Card.query.filter_by(id=card_id).first()
        if not card:
            return None
        else:
            return card

    def update(self, nome_cartao, n_transacao, tipo_cartao, n_cartao, n_order, valor_brl,
               valor_usd, hora, data, status_id, status, motivo, currency, email, data_inicio,
               data_fim, tipo_pag):
        valor_anterior = self.valor_brl
        self.nome_cartao = nome_cartao
        self.n_transacao = n_transacao
        self.tipo_cartao = tipo_cartao
        self.n_cartao = n_cartao
        self.n_order = n_order
        self.valor_brl = valor_brl
        self.valor_usd = valor_usd
        self.hora = hora
        self.data = data
        self.status_id = status_id
        self.status = status
        self.motivo = motivo
        self.currency = currency
        self.email = email
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.tipo_pag = tipo_pag
        try:
            db.session.commit()
            if self.check_status():
                company = Company.get_company(self.empresa)
                company.update_saldo(valor_anterior, valor_brl)
            return 200
        except ConnectionRefusedError:
            return 500


class Transfer(db.Model):
    __tablename__ = 'transferencia'
    id = db.Column(db.Integer, primary_key=True)
    empresa = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(65), nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    valor_compra = db.Column(db.Float, nullable=False)
    valor_deposit = db.Column(db.Float, nullable=False)
    valor_currency = db.Column(db.Float, nullable=False)
    banco = db.Column(db.Integer, nullable=False)
    banco_name = db.Column(db.String(30), nullable=False)
    banco_img = db.Column(db.String(60), nullable=False)
    data = db.Column(db.String(65), nullable=False)
    n_transferencia = db.Column(db.Integer, nullable=False)
    imglink = db.Column(db.String(60), nullable=False)
    status_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    ip = db.Column(db.String(45), nullable=True, default=None)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def check_status(self):
        if self.status_id == 2:
            return True
        return False

    @staticmethod
    def serialize(transfer):
        return {
            'id': transfer.id,
            'empresa': transfer.empresa,
            'nome': transfer.nome,
            'currency': transfer.currency,
            'valor_compra': transfer.valor_compra,
            'valor_deposit': transfer.valor_deposit,
            'valor_currency': transfer.valor_currency,
            'banco': transfer.banco,
            'banco_name': transfer.banco_name,
            'banco_img': transfer.banco_img,
            'data': transfer.dump_date(transfer.data),
            'n_transferencia': transfer.n_transferencia,
            'imglink': transfer.imglink,
            'status_id': transfer.status_id,
            'status': transfer.status,
            'ip': transfer.ip
        }

    @staticmethod
    def get_transfers():
        transfer = Transfer.query.filter_by().order_by(Transfer.id.desc())

        if not transfer:
            response = {
                'error_msg': "There's no card to show.",
                'return': False
            }
        else:
            resp = [Transfer.serialize(aux) for aux in transfer]
            response = {
                'error_msg': False,
                'return': resp
            }
        return response

    @staticmethod
    def get_transfer(transfer_id):
        trans = Transfer.query.filter_by(id=transfer_id).first()
        if not trans:
            return None
        else:
            return trans

    def update(self, nome, currency, valor_compra, valor_deposit, valor_currency, banco, banco_name,
               data, n_transferencia, imglink, status_id, status):
        valor_anterior = float(self.valor_deposit)
        self.nome = nome
        self.currency = currency
        self.valor_compra = valor_compra
        self.valor_deposit = valor_deposit
        self.valor_currency = valor_currency
        self.banco = banco
        self.banco_name = banco_name
        self.data = data
        self.n_transferencia = n_transferencia
        self.imglink = imglink
        self.status_id = status_id
        self.status = status
        try:
            db.session.commit()
            if self.check_status():
                company = Company.get_company(self.empresa)
                company.update_saldo(valor_anterior, valor_deposit)
            return 200

        except ConnectionRefusedError:
            return 500


class Deposit(db.Model):
    __tablename__ = 'deposito'

    id = db.Column(db.Integer, primary_key=True)
    empresa = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(65), nullable=False)
    valor_brl = db.Column(db.Float, nullable=False)
    valor_usd = db.Column(db.Float, nullable=False)
    moeda = db.Column(db.String(5), nullable=True, default='USD')
    data = db.Column(db.String(65), nullable=False)
    n_deposito = db.Column(db.Integer, nullable=False)
    imglink = db.Column(db.String(60), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    ip = db.Column(db.String(45), nullable=True)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def check_status(self):
        if self.status == 2:
            return True
        return False

    def update(self, dep_id, empresa, nome, valor_brl, valor_usd, moeda, data, n_deposito, imglink,
               status, ip):
        valor_anterior = float(self.valor_brl)
        self.id = dep_id
        self.empresa = empresa
        self.nome = nome
        self.valor_brl = valor_brl
        self.valor_usd = valor_usd
        self.moeda = moeda
        self.data = data
        self.n_deposito = n_deposito
        self.imglink = imglink
        self.status = status
        self.ip = ip
        try:
            db.session.commit()
            if self.check_status():
                company = Company.get_company(self.empresa)
                company.update_saldo(valor_anterior, valor_brl)
            return 200

        except ConnectionRefusedError:
            return 500

    @staticmethod
    def get_deposito(deposito_id):
        deposito = Deposit.query.filter_by(id=deposito_id).first()
        if not deposito:
            return None
        else:
            return deposito

    @staticmethod
    def serialize(deposit):
        return {
            'id': deposit.id,
            'empresa': deposit.empresa,
            'nome': deposit.nome,
            'valor_brl': deposit.valor_brl,
            'valor_usd': deposit.valor_usd,
            'moeda': deposit.moeda,
            'data': deposit.dump_date(deposit.data),
            'n_deposito': deposit.n_deposito,
            'imglink': deposit.imglink,
            'status': deposit.status,
            'ip': deposit.ip
        }

    @staticmethod
    def get_depositos():
        dep = Deposit.query.filter_by().order_by(Deposit.id.desc())

        if not dep:
            response = {
                'error_msg': "There's no Boleto to show.",
                'return': False
            }
        else:
            resp = [Deposit.serialize(aux) for aux in dep]
            response = {
                'error_msg': False,
                'return': resp
            }
        return response
